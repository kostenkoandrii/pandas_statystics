from rest_framework.permissions import AllowAny
from rest_framework import status, views
from rest_framework.response import Response
from django.db.models import Q, Sum, Count, Avg, F, ExpressionWrapper, fields
from .models import DataProductsale
import pandas as pd
import json


class ShopAnalytics(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        q = Q()

        if request.query_params.get('date_from'):
            q &= Q(date__gte=request.query_params.get('date_from'))
        if request.query_params.get('date_to'):
            q &= Q(date__lte=request.query_params.get('date_to'))
        if request.query_params.get('shop_ids'):
            q &= Q(shop__in=request.query_params.get('shop_ids').split(','))

        queryset = DataProductsale.objects.filter(q)

        if not queryset.exists():
            return Response({'message': 'records not found'}, status=status.HTTP_200_OK)
        df = queryset.values('shop').annotate(
            avg_price=Avg('margin_price_total'),
            count=Count('id')
        )
        df1 = queryset.values('shop', 'product') \
            .annotate(total=Sum('margin_price_total'))

        df = pd.DataFrame(list(df))
        df1 = pd.DataFrame(list(df1))

        def abc_stat(agg_df):
            agg_df['percent'] = agg_df.total * 100 / agg_df.total.sum()
            agg_df = agg_df.sort_values(by=['percent'], ascending=False, ignore_index=True)

            for i, _ in agg_df.iterrows():
                try:
                    agg_df.loc[i, 'percent'] += agg_df.loc[i-1, 'percent']
                except KeyError:
                    continue

            agg_df.loc[agg_df['percent'] <= 80, 'Category'] = "A"
            agg_df.loc[(80 < agg_df['percent']) & (95 >= agg_df['percent']), 'Category'] = "B"
            agg_df.loc[(95 < agg_df['percent']), 'Category'] = "C"

            m = agg_df[['product', 'Category']].to_json(orient="index")
            parsed = json.loads(m)
            return json.dumps(parsed)

        df1 = df1.groupby('shop').agg(abc_stat)
        df1['shop'] = df1.index
        df1 = df1.drop(columns=['product'])
        df1 = df1.rename(columns={'total': 'abc'})
        df1.reset_index(drop=True, inplace=True)

        res_data = df.merge(df1, how='left', on='shop').drop_duplicates(['shop'], keep='first').to_json(orient="index")

        return Response(json.loads(res_data), status=status.HTTP_200_OK)
