# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthBotToken(models.Model):
    token = models.CharField(unique=True, max_length=255)
    chat_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_bot_token'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DataAssortmentDate(models.Model):
    dt = models.DateField()
    client_id = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'data_assortment_date'


class DataAssortmentInfo(models.Model):
    client_id = models.IntegerField()
    product_cid = models.CharField(max_length=255)
    shop_cid = models.CharField(max_length=255)
    assortment_type = models.ForeignKey('DataAssortmentType', models.DO_NOTHING)
    product = models.ForeignKey('DataProduct', models.DO_NOTHING)
    shop = models.ForeignKey('DataShop', models.DO_NOTHING)
    dt = models.DateField()
    active = models.BooleanField(blank=True, null=True)
    changed = models.BooleanField()
    assortment_type_cid = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    system_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'data_assortment_info'


class DataAssortmentInfoAssortmentDt(models.Model):
    assortmentinfo = models.ForeignKey(DataAssortmentInfo, models.DO_NOTHING)
    assortmentdate = models.ForeignKey(DataAssortmentDate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_assortment_info_assortment_dt'
        unique_together = (('assortmentinfo', 'assortmentdate'),)


class DataAssortmentType(models.Model):
    cid = models.CharField(max_length=255)
    active = models.BooleanField()
    client_id = models.IntegerField()
    name = models.CharField(max_length=256)
    changed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'data_assortment_type'
        unique_together = (('cid', 'client_id'),)


class DataAttribute(models.Model):
    cid = models.CharField(unique=True, max_length=100)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'data_attribute'


class DataBrand(models.Model):
    cid = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    update_date = models.DateTimeField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    changed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'data_brand'
        unique_together = (('client', 'cid'),)


class DataCategory(models.Model):
    cid = models.CharField(max_length=100)
    parent_cid = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255)
    update_date = models.DateTimeField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    changed = models.BooleanField()
    l = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    r = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_category'
        unique_together = (('client', 'cid'),)


class DataDataloadlog(models.Model):
    task_id = models.CharField(max_length=150)
    task_type = models.CharField(max_length=150)
    event_type = models.CharField(max_length=150)
    date = models.DateTimeField()
    message = models.TextField()  # This field type is a guess.
    status = models.CharField(max_length=50)
    meta = models.TextField(blank=True, null=True)  # This field type is a guess.
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    event_id = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'data_dataloadlog'


class DataMarker(models.Model):
    cid = models.CharField(max_length=100)
    parent_cid = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    l = models.IntegerField(blank=True, null=True)
    r = models.IntegerField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    client_id = models.IntegerField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_marker'
        unique_together = (('client_id', 'cid'),)


class DataMarkerproducts(models.Model):
    client_id = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('DataProduct', models.DO_NOTHING, blank=True, null=True)
    marker = models.ForeignKey(DataMarker, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_markerproducts'


class DataProduct(models.Model):
    cid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    update_date = models.DateTimeField()
    brand = models.ForeignKey(DataBrand, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(DataCategory, models.DO_NOTHING, blank=True, null=True)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    article = models.CharField(max_length=100, blank=True, null=True)
    barcode = models.TextField(blank=True, null=True)
    depth = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    height = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    photo = models.CharField(max_length=100, blank=True, null=True)
    width = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    changed = models.BooleanField()
    sync = models.BooleanField()
    create_dt = models.DateField(blank=True, null=True)
    is_weight = models.BooleanField()
    compression = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    compression_height = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    compression_width = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    compression_depth = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_product'
        unique_together = (('client', 'cid'),)


class DataProductAttribute(models.Model):
    value = models.CharField(max_length=500)
    value_type = models.CharField(max_length=255)
    attribute = models.ForeignKey(DataAttribute, models.DO_NOTHING)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_product_attribute'
        unique_together = (('client', 'product', 'attribute'),)


class DataProductImage(models.Model):
    photo = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_product_image'
        unique_together = (('client', 'product', 'type'),)


class DataProductInventory(models.Model):
    dt = models.DateField()
    qty = models.DecimalField(max_digits=20, decimal_places=4)
    original_price = models.DecimalField(max_digits=20, decimal_places=4)
    stock_total_price = models.DecimalField(max_digits=20, decimal_places=4)
    changed = models.BooleanField()
    update_date = models.DateTimeField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)
    shop = models.ForeignKey('DataShop', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_product_inventory'
        unique_together = (('client', 'shop', 'product', 'dt'),)


class DataProductMessage(models.Model):
    client_id = models.IntegerField()
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)
    user_id = models.IntegerField(blank=True, null=True)
    conf = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    body = models.CharField(max_length=1000)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data_product_message'


class DataProductPack(models.Model):
    name = models.CharField(max_length=100)
    qty = models.DecimalField(max_digits=14, decimal_places=4)
    height = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    depth = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    width = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)
    compression = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_product_pack'
        unique_together = (('client', 'product', 'name', 'qty'),)


class DataProductsale(models.Model):
    receipt_id = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField()
    original_price = models.DecimalField(max_digits=20, decimal_places=4)
    price = models.DecimalField(max_digits=20, decimal_places=4)
    qty = models.DecimalField(max_digits=20, decimal_places=4)
    discount = models.DecimalField(max_digits=20, decimal_places=4)
    margin_price_total = models.DecimalField(max_digits=20, decimal_places=4)
    total_price = models.DecimalField(max_digits=20, decimal_places=4)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)
    shop = models.ForeignKey('DataShop', models.DO_NOTHING, blank=True, null=True)
    terminal = models.ForeignKey('DataTerminal', models.DO_NOTHING)
    week_day = models.IntegerField(blank=True, null=True)
    dt = models.DateField(blank=True, null=True)
    refund = models.BooleanField(blank=True, null=True)
    bulk = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_productsale'


class DataPromotion(models.Model):
    cid = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500, blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    changed = models.BooleanField()
    update_date = models.DateTimeField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_promotion'
        unique_together = (('client', 'cid'),)


class DataPromotionAccess(models.Model):
    changed = models.BooleanField()
    update_date = models.DateTimeField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)
    promotion = models.ForeignKey(DataPromotion, models.DO_NOTHING)
    shop = models.ForeignKey('DataShop', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_promotion_access'
        unique_together = (('client', 'promotion', 'shop', 'product'),)


class DataPurchaseProduct(models.Model):
    cid = models.CharField(max_length=100)
    document_id = models.CharField(max_length=100)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    shop = models.ForeignKey('DataShop', models.DO_NOTHING)
    supplier = models.ForeignKey('DataSupplier', models.DO_NOTHING)
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)
    order_date = models.DateTimeField()
    receive_date = models.DateTimeField()
    price = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    price_total = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    changed = models.BooleanField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data_purchase_product'
        unique_together = (('client', 'cid'),)


class DataReceiveProduct(models.Model):
    cid = models.CharField(max_length=100)
    document_id = models.CharField(max_length=100)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    shop = models.ForeignKey('DataShop', models.DO_NOTHING)
    supplier = models.ForeignKey('DataSupplier', models.DO_NOTHING)
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)
    document_date = models.DateTimeField()
    price = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    qty = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    price_total = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    changed = models.BooleanField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data_receive_product'
        unique_together = (('client', 'cid'),)


class DataShop(models.Model):
    cid = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    update_date = models.DateTimeField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    changed = models.BooleanField()
    format = models.ForeignKey('DataShopformat', models.DO_NOTHING, blank=True, null=True)
    group_id = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_shop'
        unique_together = (('client', 'cid'),)


class DataShopAccess(models.Model):
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    shop = models.ForeignKey(DataShop, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'data_shop_access'
        unique_together = (('client', 'shop', 'user'),)


class DataShopGroups(models.Model):
    group_id = models.CharField(primary_key=True, max_length=1000)
    parent_id = models.CharField(max_length=1000, blank=True, null=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_shop_groups'
        unique_together = (('client_id', 'group_id'),)


class DataShopformat(models.Model):
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    cid = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    changed = models.BooleanField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data_shopformat'
        unique_together = (('client', 'cid'),)


class DataSupplier(models.Model):
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    cid = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    changed = models.BooleanField()
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'data_supplier'
        unique_together = (('client', 'cid'),)


class DataTerminal(models.Model):
    cid = models.CharField(max_length=100)
    name = models.CharField(max_length=200)
    update_date = models.DateTimeField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    shop = models.ForeignKey(DataShop, models.DO_NOTHING)
    changed = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'data_terminal'
        unique_together = (('client', 'shop', 'cid'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryResultsTaskresult(models.Model):
    task_id = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=50)
    content_type = models.CharField(max_length=128)
    content_encoding = models.CharField(max_length=64)
    result = models.TextField(blank=True, null=True)
    date_done = models.DateTimeField()
    traceback = models.TextField(blank=True, null=True)
    hidden = models.BooleanField()
    meta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_results_taskresult'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class LayoutBlocks(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    conf = models.TextField(blank=True, null=True)  # This field type is a guess.
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING, blank=True, null=True)
    supplier = models.ForeignKey(DataSupplier, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(DataCategory, models.DO_NOTHING, blank=True, null=True)
    brand = models.ForeignKey(DataBrand, models.DO_NOTHING, blank=True, null=True)
    stand = models.ForeignKey('LayoutStand', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_blocks'


class LayoutDevice(models.Model):
    device_type = models.CharField(max_length=15)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    planogram = models.ForeignKey('LayoutPlanogram', models.DO_NOTHING)
    terminal = models.ForeignKey(DataTerminal, models.DO_NOTHING, blank=True, null=True)
    depth = models.DecimalField(max_digits=14, decimal_places=4)
    position_x = models.DecimalField(max_digits=14, decimal_places=4)
    position_y = models.DecimalField(max_digits=14, decimal_places=4)
    rotation = models.DecimalField(max_digits=14, decimal_places=4)
    width = models.DecimalField(max_digits=14, decimal_places=4)
    name = models.CharField(max_length=100)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'layout_device'


class LayoutDevicehistory(models.Model):
    date = models.DateTimeField()
    device_type = models.CharField(max_length=15)
    name = models.CharField(max_length=100)
    rotation = models.DecimalField(max_digits=14, decimal_places=4)
    position_x = models.DecimalField(max_digits=14, decimal_places=4)
    position_y = models.DecimalField(max_digits=14, decimal_places=4)
    width = models.DecimalField(max_digits=14, decimal_places=4)
    depth = models.DecimalField(max_digits=14, decimal_places=4)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    device = models.ForeignKey(LayoutDevice, models.DO_NOTHING)
    planogram = models.ForeignKey('LayoutPlanogram', models.DO_NOTHING)
    terminal = models.ForeignKey(DataTerminal, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_devicehistory'


class LayoutGroup(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'layout_group'


class LayoutInstrument(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    producer = models.CharField(max_length=200)
    description = models.CharField(max_length=512)
    image = models.CharField(max_length=100)
    conf = models.TextField()  # This field type is a guess.
    linear_conf = models.TextField()  # This field type is a guess.
    equipment_conf = models.TextField()  # This field type is a guess.
    empty = models.BooleanField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    type = models.ForeignKey('LayoutInstrumentType', models.DO_NOTHING, blank=True, null=True)
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'layout_instrument'
        unique_together = (('client', 'name'),)


class LayoutInstrumentHistory(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    producer = models.CharField(max_length=200)
    description = models.CharField(max_length=512)
    image = models.CharField(max_length=100)
    conf = models.TextField()  # This field type is a guess.
    linear_conf = models.TextField()  # This field type is a guess.
    equipment_conf = models.TextField()  # This field type is a guess.
    empty = models.BooleanField()
    date = models.DateTimeField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    instrument = models.ForeignKey(LayoutInstrument, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'layout_instrument_history'


class LayoutInstrumentType(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=16)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'layout_instrument_type'
        unique_together = (('client', 'name'),)


class LayoutPlanogram(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    conf = models.TextField()  # This field type is a guess.
    update_date = models.DateTimeField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    active = models.BooleanField()
    trade_area = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_planogram'


class LayoutPlanogramHistory(models.Model):
    conf = models.TextField()  # This field type is a guess.
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    planogram = models.ForeignKey(LayoutPlanogram, models.DO_NOTHING)
    image = models.CharField(max_length=100)
    active = models.BooleanField()
    name = models.CharField(max_length=100)
    update_date = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    trade_area = models.DecimalField(max_digits=14, decimal_places=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_planogram_history'


class LayoutPlanogramShop(models.Model):
    planogram = models.ForeignKey(LayoutPlanogram, models.DO_NOTHING)
    shop = models.ForeignKey(DataShop, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'layout_planogram_shop'


class LayoutPlanogramUserAccess(models.Model):
    status = models.CharField(max_length=32)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    planogram = models.ForeignKey(LayoutPlanogram, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'layout_planogram_user_access'
        unique_together = (('client', 'planogram', 'user'), ('planogram', 'user'),)


class LayoutPlanogramstandlife(models.Model):
    planogram = models.ForeignKey(LayoutPlanogram, models.DO_NOTHING)
    stand = models.ForeignKey('LayoutStand', models.DO_NOTHING)
    main_stand = models.ForeignKey('LayoutStand', models.DO_NOTHING, related_name='Layout')
    date_from = models.DateTimeField()
    date_to = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField()
    was_changing = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_planogramstandlife'
        unique_together = (('planogram', 'stand'),)


class LayoutStand(models.Model):
    image = models.CharField(max_length=100)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    date = models.DateTimeField()
    conf = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=100)
    style_conf = models.TextField()  # This field type is a guess.
    instrument = models.ForeignKey(LayoutInstrument, models.DO_NOTHING)
    stand_no = models.CharField(max_length=100)
    main_stand_id = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=32, blank=True, null=True)
    alignment = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_stand'


class LayoutStandGroup(models.Model):
    order_no = models.IntegerField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    group = models.ForeignKey(LayoutGroup, models.DO_NOTHING)
    planogram = models.ForeignKey(LayoutPlanogram, models.DO_NOTHING)
    stand = models.ForeignKey(LayoutStand, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'layout_stand_group'
        unique_together = (('client', 'planogram', 'group', 'stand', 'order_no'),)


class LayoutStandHistory(models.Model):
    date = models.DateTimeField()
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    image = models.CharField(max_length=100)
    conf = models.TextField()  # This field type is a guess.
    name = models.CharField(max_length=100, blank=True, null=True)
    stand = models.ForeignKey(LayoutStand, models.DO_NOTHING)
    style_conf = models.TextField()  # This field type is a guess.
    instrument = models.ForeignKey(LayoutInstrument, models.DO_NOTHING)
    stand_no = models.CharField(max_length=100)
    type = models.CharField(max_length=32, blank=True, null=True)
    alignment = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_stand_history'


class LayoutStandPlanogram(models.Model):
    planogram = models.ForeignKey(LayoutPlanogram, models.DO_NOTHING)
    stand = models.ForeignKey(LayoutStand, models.DO_NOTHING, blank=True, null=True)
    position_x = models.DecimalField(max_digits=14, decimal_places=4)
    position_y = models.DecimalField(max_digits=14, decimal_places=4)
    rotation = models.DecimalField(max_digits=14, decimal_places=4)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'layout_stand_planogram'
        unique_together = (('planogram', 'stand'),)


class LayoutStandPlanogramHistory(models.Model):
    position_x = models.DecimalField(max_digits=14, decimal_places=4)
    position_y = models.DecimalField(max_digits=14, decimal_places=4)
    rotation = models.DecimalField(max_digits=14, decimal_places=4)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    date = models.DateTimeField()
    planogram = models.ForeignKey(LayoutPlanogram, models.DO_NOTHING)
    stand = models.ForeignKey(LayoutStand, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'layout_stand_planogram_history'


class LayoutStandProduct(models.Model):
    shelf_no = models.IntegerField()
    qty = models.DecimalField(max_digits=14, decimal_places=4)
    date = models.DateTimeField()
    rotation = models.CharField(max_length=30)
    position_x = models.DecimalField(max_digits=14, decimal_places=4)
    position_y = models.DecimalField(max_digits=14, decimal_places=4)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)
    stand = models.ForeignKey(LayoutStand, models.DO_NOTHING)
    placement_depth = models.IntegerField()
    placement_height = models.IntegerField()
    position_z = models.DecimalField(max_digits=14, decimal_places=4)
    packing = models.ForeignKey(DataProductPack, models.DO_NOTHING, blank=True, null=True)
    block = models.ForeignKey(LayoutBlocks, models.DO_NOTHING, blank=True, null=True)
    compression_type = models.CharField(max_length=30, blank=True, null=True)
    depend_product = models.IntegerField(blank=True, null=True)
    apply_compression = models.BooleanField(blank=True, null=True)
    compression_types = models.TextField(blank=True, null=True)  # This field type is a guess.
    error_product = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_stand_product'


class LayoutStandProductHistory(models.Model):
    shelf_no = models.IntegerField()
    qty = models.DecimalField(max_digits=14, decimal_places=4)
    date = models.DateTimeField()
    rotation = models.CharField(max_length=30)
    position_x = models.DecimalField(max_digits=14, decimal_places=4)
    position_y = models.DecimalField(max_digits=14, decimal_places=4)
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    product = models.ForeignKey(DataProduct, models.DO_NOTHING)
    stand = models.ForeignKey(LayoutStand, models.DO_NOTHING)
    placement_depth = models.IntegerField()
    placement_height = models.IntegerField()
    position_z = models.DecimalField(max_digits=14, decimal_places=4)
    packing = models.ForeignKey(DataProductPack, models.DO_NOTHING, blank=True, null=True)
    block = models.ForeignKey(LayoutBlocks, models.DO_NOTHING, blank=True, null=True)
    compression_type = models.CharField(max_length=30, blank=True, null=True)
    depend_product = models.IntegerField(blank=True, null=True)
    compression_types = models.TextField(blank=True, null=True)  # This field type is a guess.
    apply_compression = models.BooleanField(blank=True, null=True)
    error_product = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layout_stand_product_history'


class LayoutStandconversation(models.Model):
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    stand = models.ForeignKey(LayoutStand, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    users = models.TextField(blank=True, null=True)  # This field type is a guess.
    conf = models.TextField(blank=True, null=True)  # This field type is a guess.
    type = models.CharField(max_length=100)
    read = models.BooleanField()
    title = models.CharField(max_length=300)
    body = models.CharField(max_length=1000)
    done = models.BooleanField()
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'layout_standconversation'


class LayoutStandconversationFiles(models.Model):
    storage = models.ForeignKey('LayoutStorage', models.DO_NOTHING)
    standconversation = models.ForeignKey(LayoutStandconversation, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'layout_standconversation_files'
        unique_together = (('storage', 'standconversation'),)


class LayoutStandexecution(models.Model):
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    planogram = models.ForeignKey(LayoutPlanogram, models.DO_NOTHING)
    stand = models.ForeignKey(LayoutStand, models.DO_NOTHING)
    from_user = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='Layout', blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='Layout_user', blank=True, null=True)
    comment = models.CharField(max_length=500)
    done = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    was_show = models.BooleanField()
    main_stand_id = models.IntegerField(blank=True, null=True)
    is_clone = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'layout_standexecution'


class LayoutStandphotoreport(models.Model):
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    planogram = models.ForeignKey(LayoutPlanogram, models.DO_NOTHING)
    stand = models.ForeignKey(LayoutStand, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    comment = models.CharField(max_length=500)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'layout_standphotoreport'


class LayoutStandphotoreportPhotos(models.Model):
    storage = models.ForeignKey('LayoutStorage', models.DO_NOTHING)
    standphotoreport = models.ForeignKey(LayoutStandphotoreport, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'layout_standphotoreport_photos'
        unique_together = (('storage', 'standphotoreport'),)


class LayoutStorage(models.Model):
    client = models.ForeignKey('ProfileClient', models.DO_NOTHING)
    name = models.CharField(max_length=500, blank=True, null=True)
    file = models.CharField(max_length=1000)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'layout_storage'


class ProductCategoriesArrays(models.Model):
    id = models.AutoField(primary_key=True)
    object = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    level = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    client = models.IntegerField(blank=True, null=True)
    array_field_1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    array_field_2 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'product_categories_arrays'


class ProfileAccountAction(models.Model):
    hash = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    email = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'profile_account_action'
        unique_together = (('user', 'type'),)


class ProfileClient(models.Model):
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100)
    receive_conf = models.TextField()  # This field type is a guess.
    first_load = models.BooleanField()
    connector = models.CharField(max_length=30, blank=True, null=True)
    db_name = models.CharField(max_length=100)
    connector_config = models.TextField()
    db_encoding = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_client'


class ProfileEmailVerification(models.Model):
    verification_hash = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    verified = models.BooleanField()
    email = models.CharField(max_length=200)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_email_verification'


class ProfileNotification(models.Model):
    client = models.ForeignKey(ProfileClient, models.DO_NOTHING)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=100)
    link = models.CharField(max_length=1000, blank=True, null=True)
    from_user = models.ForeignKey(AuthUser, models.DO_NOTHING, related_name='profile_notification', blank=True,
                                  null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    read = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uniq_key = models.CharField(max_length=100)
    conf = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'profile_notification'


class ProfileProfile(models.Model):
    phone = models.CharField(max_length=25)
    client = models.ForeignKey(ProfileClient, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    company = models.CharField(max_length=200, blank=True, null=True)
    full_name = models.CharField(max_length=200)
    plain_password = models.CharField(max_length=100)
    language = models.CharField(max_length=10)
    settings = models.TextField()  # This field type is a guess.
    image = models.CharField(max_length=100)
    is_admin = models.BooleanField()
    original_image = models.CharField(max_length=100)
    permission = models.TextField(blank=True, null=True)  # This field type is a guess.
    telegram_id = models.IntegerField(blank=True, null=True)
    is_shop = models.BooleanField(blank=True, null=True)
    telegram_config = models.TextField(blank=True, null=True)  # This field type is a guess.
    telegram_markup = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profile_profile'
        unique_together = (('client', 'user'),)


class RestorePassword(models.Model):
    token = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, blank=True, null=True)
    done = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'restore_password'
