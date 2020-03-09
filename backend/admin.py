from django.contrib import admin
from .models import Address, Founder, Mesh, Price
from .models import Param, Office, Factory, Storage
from .models import Founders
from .models import Factories, Offices, Storages, Firm, FoundersCompanyOrganization
from .models import Item, Items, ItemsInStorage, ItemsSupplier, Employee, OrderTable, DeliveryTransport, DeliveryInAWay, SupplierInfo, Supplier
from .models import Ready, Orderes
from .models import RoleNow, TotalRole, UserCustom
from django.contrib.auth.admin import UserAdmin





admin.site.site_header = 'ERP SYSTEM'


# Register your models here.


class AddressAdmin(admin.ModelAdmin):
    list_display = ('country','city','street', 'bilding', 'flat', 'type_org', 'user')
    list_display_links = ('country',)
    search_fields = ('country','city','street', 'bilding', 'flat', 'type_org', 'user' )
    fields = ('country','city', ('street', 'bilding', 'flat'), 'type_org', 'user')
    list_editable = ('city','street', 'bilding', 'flat', 'type_org', 'user')

class MeshAdmin(admin.ModelAdmin):
    list_display = ('mesh','info_mesh','additional_mesh', 'user')
    list_display_links = ('info_mesh',)
    list_editable = ('mesh','additional_mesh', 'user')
    fields = (( 'mesh', 'additional_mesh',), 'info_mesh', 'user')
    search_fields = ('mesh','info_mesh','additional_mesh', 'user')

class PriceAdmin(admin.ModelAdmin):
    list_display = ('price','sale_price', 'user')
    list_display_links = ('sale_price',)
    list_editable = ('price', 'user')
    fields = (('price','sale_price'), 'user')
    search_fields = ('price','sale_price', 'user' )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(is_hidden=False) 

class RoleNowAdmin(admin.ModelAdmin):
    list_display = ('name','countpeople','needHE', 'user')
    list_display_links = ('name', 'user')
    list_editable = ('countpeople','needHE', 'user')
    search_fields = ('name','user')


class ParamAdmin(admin.ModelAdmin):
    list_display = ('height','width','thickness', 'diagonal','weight', 'get_mesh', 'user')
    list_editable = ('height', 'width','thickness', 'diagonal','weight', 'user')
    list_display_links = ( 'get_mesh',)
    search_fields = ('height','width','thickness', 'diagonal','weight', 'get_mesh', 'user')
    
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','mail', 'this_company_office', 'address', 'state_or_private', 'user')
    list_editable = ('mobile','mail', 'this_company_office', 'address', 'state_or_private', 'user')
    fields = ('name','mobile','mail', 'address',  ('this_company_office',  'state_or_private'), 'user')
    search_fields = ('name','mobile','mail', 'this_company_office', 'address', 'state_or_private', 'user' )

class FactoryAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','mail', 'count_empl', 'this_company_factory', 'address', 'state_or_private', 'user')
    list_editable = ('mobile','mail', 'count_empl', 'this_company_factory', 'address', 'state_or_private', 'user')
    fields = (('name', 'count_empl'), ('mobile','mail'), 'address',  ('this_company_factory',  'state_or_private'), 'user')
    list_display_links = ('name',)
    search_fields = ('name','mobile','mail', 'count_empl', 'this_company_factory', 'address', 'state_or_private', 'user')

class StorageAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','mail', 'full_content', 'content', 'this_company_storage', 'address', 'state_or_private', 'user')
    list_editable = ('mobile','mail', 'full_content', 'content', 'this_company_storage', 'address', 'state_or_private', 'user')
    list_display_links = ('name',)
    fields = ('name', ('mobile','mail'), 'address', ('full_content', 'content'),  ('this_company_storage',  'state_or_private'), 'user')
    search_fields = ('name','mobile','mail', 'full_content', 'content', 'this_company_storage', 'address', 'state_or_private', 'user' )

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'firm', 'param', 'price', 'create_date' )
    fields = ('name', ('param', 'price'), 'firm', 'create_date' )
    list_editable = ('firm', 'param', 'price', 'create_date' )
    list_display_links = ('name',)
    search_fields = ('name', 'firm', 'param', 'price', 'create_date' )

class ItemsAdmin(admin.ModelAdmin):
    list_display = ('name_group', 'item', 'count')
    fields = ('name_group', ('item', 'count'))
    list_editable = ('item', 'count')
    list_display_links = ('name_group',)
    search_fields = ('name_group', 'item', 'count')

class ItemsInStorageAdmin(admin.ModelAdmin):
    list_display = ('storage', 'get_items')
    list_display_links = ('storage', 'get_items')
    search_fields = ('storage', 'get_items')

class ItemsSupplierAdmin(admin.ModelAdmin):
    list_display = ('name_group', 'get_items')
    list_display_links = ('name_group', 'get_items')
    search_fields = ('name_group', 'get_items')

class FounderAdmin(admin.ModelAdmin):
    list_display = ('second_name', 'first_name', 'age', 'namber', 'mail', 'info' )
    list_editable = ('first_name', 'age', 'namber', 'mail', 'info' )
    fields = (('second_name', 'first_name'), 'age', ('namber', 'mail'), 'info' )
    list_display_links = ('second_name',)
    search_fields = ('first_name', 'second_name', 'age', 'namber', 'mail', 'info')

class FirmAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'director', 'mail', 'info' , 'firm_is_supplier', 'connect_date_firm', 'create_date_firm', 'get_founders_company')
    list_editable = ('mobile', 'director', 'mail', 'info' , 'firm_is_supplier', 'connect_date_firm', 'create_date_firm',)
    list_display_links = ('name', 'get_founders_company')
    search_fields = ('name', 'mobile', 'director', 'mail', 'info' , 'firm_is_supplier', 'connect_date_firm', 'create_date_firm', 'get_founders_company')
    fields = (('name','director',), ('mobile',  'mail'), 'info' , 'firm_is_supplier', ('connect_date_firm', 'create_date_firm'), 'founderscompanyorganization')

class FoundersCompanyOrganizationAdmin(admin.ModelAdmin):
    list_display = ('companyname', 'get_founders', 'get_storages', 'get_factories', 'get_offices')
    fieldsets = (
        ('Информация о компании', {
            'fields': ('companyname', 'founders')
        }),
        ('Недвижимость', {
            'fields': (('factories', 'storages', 'offices'))
        }),
    )
    list_display_links = ('companyname', 'get_founders', 'get_storages', 'get_factories', 'get_offices',)
    search_fields = ('companyname', 'get_founders', 'get_storages', 'get_factories', 'get_offices',)


class DeliveryTransportAdmin(admin.ModelAdmin):
    list_display = ('model_name', 'type_of_transport', 'year_constructed', 'order_coast', 'ready', 'time_delivery', 'done_order' )
    list_editable = ('model_name', 'year_constructed', 'order_coast', 'ready', 'time_delivery', 'done_order',)
    fields = (('model_name', 'type_of_transport', 'year_constructed', 'done_order'),  'ready', 'order_coast', 'time_delivery' )
    list_display_links = ('type_of_transport',)
    search_fields = ('model_name', 'type_of_transport', 'year_constructed', 'order_coast', 'ready', 'time_delivery', 'done_order')

class DeliveryInAWayAdmin(admin.ModelAdmin):
    list_display = ('transport', 'get_items')
    list_display_links = ('transport', 'get_items',)
    search_fields = ('transport', 'get_items',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'experience',  'trole',  'mail', 'mobile', 'salary', 'info', 'create_date', 'address', 'get_orderes', )
    list_editable = ('first_name', 'second_name', 'experience',   'mail', 'mobile', 'salary', 'info',  'create_date', 'address' )
    list_display_links = ('trole',  'get_orderes',)
    search_fields = ('first_name', 'second_name', 'experience', 'trole', 'mail', 'mobile', 'salary', 'info',  'create_date', 'address', 'get_orderes',)

class OrderTableAdmin(admin.ModelAdmin):
    list_display = ('address', 'get_items', 'create_date', 'get_date')
    list_editable = ('create_date', 'get_date',)
    list_display_links = ('address', 'get_items',)
    search_fields = ('address', 'get_items', 'create_date', 'get_date',)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','mail', 'director', 'get_founders_company', 'supplier_info', 'get_issup', 'create_date', 'connect_date')
    list_editable = ('name','mobile','mail', 'director',  'create_date', 'connect_date')
    list_display_links = ('get_founders_company', 'supplier_info', 'get_issup',)
    search_fields = ('name','mobile','mail', 'director', 'get_founders_company', 'supplier_info', 'get_issup', 'create_date', 'connect_date', )

class SupplierInfoAdmin(admin.ModelAdmin):
    list_display = ('count_storages','average_time_delivery','get_offices', 'get_storages', 'get_factories', 'get_delivery_variant', 'text')
    list_display_links = ('get_offices', 'get_storages', 'get_factories', 'get_delivery_variant',)
    list_editable = ('count_storages','average_time_delivery','text',)
    search_fields = ('count_storages','average_time_delivery','get_offices', 'get_storages', 'get_factories', 'get_delivery_variant', 'text', )

class ReadyAdmin(admin.ModelAdmin):
    list_display = ('order_status','employee','address', 'items', 'total_price')
    list_editable = ('order_status','employee','address', 'items')
    list_display_links = ('total_price',)
    search_fields = ('order_status','employee','address', 'items', 'total_price', )

class OrderesAdmin(admin.ModelAdmin):
    list_display = ('get_orders','total_price','supplier', 'storage', 'send', 'received', 'pos_one_get', 'date_send', 'date_get')
    list_display_links = ('get_orders','total_price','supplier', 'storage', 'send', 'received', 'pos_one_get', 'date_send', 'date_get')
    search_fields = ('get_orders','total_price','supplier', 'storage', 'send', 'received', 'pos_one_get', 'date_send', 'date_get', )

class FoundersAdmin(admin.ModelAdmin):
    list_display = ('founders','get_founder')
    list_editable = ('founders',)
    list_display_links = ('get_founder',)
    search_fields = ('founders','get_founder')

class OficesAdmin(admin.ModelAdmin):
    list_display = ('holding','get_office')
    list_editable = ('holding',)
    list_display_links = ('get_office',)
    search_fields = ('holding','get_office')

class FactoriesAdmin(admin.ModelAdmin):
    list_display = ('holding','get_factory')
    list_editable = ('holding',)
    list_display_links = ('get_factory',)
    search_fields = ('holding','get_factory')

class StoragesAdmin(admin.ModelAdmin):
    list_display = ('holding','get_storage')
    list_editable = ('holding',)
    list_display_links = ('get_storage',)
    search_fields = ('holding','get_storage')

class TotalRoleAdmin(admin.ModelAdmin):
    list_display = ('name','get_role_now')
    list_display_links = ('name','get_role_now')
    search_fields = ('name','get_role_now')

    



# Re-register UserAdmin

admin.site.register(Address, AddressAdmin)
admin.site.register(Founder, FounderAdmin)
admin.site.register(Mesh, MeshAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Param, ParamAdmin)
admin.site.register(Office, OfficeAdmin)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(Storage, StorageAdmin)
admin.site.register(Founders, FoundersAdmin)
admin.site.register(FoundersCompanyOrganization, FoundersCompanyOrganizationAdmin)
admin.site.register(Offices, OficesAdmin)
admin.site.register(Factories, FactoriesAdmin)
admin.site.register(Firm, FirmAdmin)
admin.site.register(Storages, StoragesAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(ItemsInStorage, ItemsInStorageAdmin)
admin.site.register(ItemsSupplier, ItemsSupplierAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(OrderTable, OrderTableAdmin)
admin.site.register(DeliveryTransport, DeliveryTransportAdmin)
admin.site.register(DeliveryInAWay, DeliveryInAWayAdmin)
admin.site.register(SupplierInfo, SupplierInfoAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Ready, ReadyAdmin)
admin.site.register(Orderes, OrderesAdmin)
admin.site.register(RoleNow, RoleNowAdmin)
admin.site.register(TotalRole, TotalRoleAdmin)
admin.site.register(UserCustom)