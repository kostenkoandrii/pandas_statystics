from rest_framework.permissions import AllowAny
from rest_framework import status, views
from rest_framework.response import Response
from django.db.models import Q
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

        df = df1 = pd.DataFrame(list(queryset.values('total_price', 'qty', 'shop', 'product')))

        df['profit'] = df['total_price'] * df['qty']
        df['profit'] = df['profit'].apply(pd.to_numeric)
        df = df.groupby('shop').agg(avg_profit=('profit', 'mean'), total_sales=('shop', 'count'))

        def agg_f(agg_df):
            products_categories = {
                'A': {'max_val': 80, 'min_val': 0, 'name': 'A'},
                'B': {'max_val': 95, 'min_val': 80, 'name': 'B'},
                'C': {'max_val': 100,  'min_val': 95, 'name': 'C'},
            }

            agg_df['percent'] = agg_df.product_profit_sum * 100 / agg_df.product_profit_sum.sum()
            agg_df = agg_df.sort_values(by=['percent'], ascending=False)

            category_count = 0
            abc = {}

            for i, row_value in agg_df['percent'].iteritems():
                category_count += row_value

                if products_categories['A']['min_val'] <= category_count <= products_categories['A']['max_val']:
                    abc[i[0]] = products_categories['A']['name']
                elif products_categories['B']['min_val'] < category_count <= products_categories['B']['max_val']:
                    abc[i[0]] = products_categories['B']['name']
                elif products_categories['C']['min_val'] < category_count <= products_categories['C']['max_val']:
                    abc[i[0]] = products_categories['C']['name']

            return json.dumps(abc)

        df1 = df1.groupby(['product', 'shop']).agg(product_profit_sum=('profit', 'sum'))
        df1 = df1.groupby('shop').agg(agg_f)
        df1 = df1.rename(columns={'product_profit_sum': 'abc'})

        res_data = df.join(df1).to_json(orient="index")
        return Response(json.loads(res_data), status=status.HTTP_200_OK)
