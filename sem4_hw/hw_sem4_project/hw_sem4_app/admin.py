from django.contrib import admin
from .models import Good, Order, Client
from .admin_mixins import ExportAsCSVMixin

# Register your models here.


@admin.action(description="Cделать подарок (бесплатный заказ) покупателю")
def make_present_to_customer(modeladmin, request, queryset):
    queryset.update(order_total=0)



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    list_display = ('id', 'order_client', 'order_date', 'order_total', 'get_order_items')
    ordering = ['order_client', '-id']
    list_filter = ['order_date', 'order_total']
    search_fields = ['order_items__good_name']
    actions = [make_present_to_customer, 'export_manytomany_as_csv']
    readonly_fields = ['order_total']
    search_help_text = 'Поиск по полю Наимование товара (order_items__good_name)'
    fieldsets = (
        (None,
         {'fields': ('order_client', 'order_date', 'order_items', 'order_total')}
         ),
    )
    filter_horizontal = ('order_items',)

def get_order_items(self, obj):
    return "\n".join([str(x) for x in list(obj.order_items.all())])



@admin.action(description="Добавить НОВИНКА к имени")
def add_NEW_to_name(modeladmin, request, queryset):
    names = queryset.values_list('good_name', flat=True)
    for name in names:
        queryset.update(good_name=f'НОВИНКА_{name}')

@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
   list_display = ('id', 'good_name', 'description', 'price','quantity')
   ordering = ['-quantity','id']
   list_filter = ['price','add_date']
   search_fields = ['description']
   actions = [add_NEW_to_name]

