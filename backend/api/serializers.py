from rest_framework import serializers

from backend.models import Address, Founder, Mesh, Price#, Role
from backend.models import Param, Office, Factory, Storage
from backend.models import Founders
from backend.models import Factories, Offices, Storages, Firm, FoundersCompanyOrganization
from backend.models import Item, Items, ItemsInStorage, ItemsSupplier, Employee, OrderTable, DeliveryTransport, DeliveryInAWay, SupplierInfo, Supplier
from backend.models import Ready, Orderes
from backend.models import RoleNow, TotalRole
from backend.models import UserCustom
from rest_framework.authtoken.models import Token


class UserCustomSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCustom
        fields = ('email',
                  'perm',
                  'name',
                  'is_staff'
                  )
        read_only_fields = ('email',
                            'perm',
                            'name',
                            'is_staff'
                            )
        

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            'id',
            'country',
            'city',
            'street',
            'bilding',
            'flat',
            'type_org',
            'user'
    )

class FounderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Founder
        fields = (
            'id',
            'second_name',
            'first_name',
            'age',
            'namber',
            'mail',
            'info',
            'user'
    )

class MeshSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesh
        fields = (
            'id',
            'mesh',
            'info_mesh',
            'additional_mesh',
            'info_additional_mesh',
            'user'
    )

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = (
            'id',
            'price',
            'sale_price',
            'user'
    )

class ParamSerializer(serializers.ModelSerializer):
    mesh = serializers.PrimaryKeyRelatedField(
        many=False,
        read_only=False,
        queryset = Mesh.objects.all()
     )
    class Meta:
        model = Param
        fields = (
            'id',
            'height',
            'width',
            'thickness',
            'weight',
            'diagonal',
            'mesh',
            'user'
    )

class FoundersSerializer(serializers.ModelSerializer):
    founder = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Founder.objects.all()
     )

    class Meta:
        model = Founders
        fields = (
            'id'
            'founders',
            'founder',
            'user'
        )

class OfficeSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Address.objects.all()
     )

    class Meta:
        model = Office
        fields = (
            'id',
            'name',
            'mobile',
            'mail',
            'info',
            'this_company_office',
            'state_or_private',
            'address',
            'user'
        )

class FactorySerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Address.objects.all()
     )

    class Meta:
        model = Factory
        fields = (
            'id',
            'name',
            'mobile',
            'mail',
            'info',
            'this_company_factory',
            'state_or_private',
            'address',
            'user'
        )

class StorageSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Address.objects.all()
     )

    class Meta:
        model = Storage
        fields = (
            'id',
            'name',
            'mobile',
            'mail',
            'info',
            'full_content',
            'content',
            'this_company_storage',
            'state_or_private',
            'address',
            'user'
        )

class OfficesSerializer(serializers.ModelSerializer):
    office = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Office.objects.all()
     )

    class Meta:
        model = Offices
        fields = (
            'id',
            'holding',
            'office',
            'user'
        )

class FactoriesSerializer(serializers.ModelSerializer):
    factory = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Factory.objects.all()
     )

    class Meta:
        model = Factories
        fields = (
            'id',
            'holding',
            'factory',
            'user'
        )

class StoragesSerializer(serializers.ModelSerializer):
    storage = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Storage.objects.all()
     )

    class Meta:
        model = Storages
        fields = (
            'id',
            'holding',
            'factory',
            'user'
        )

class FoundersCompanyOrganizationSerializer(serializers.ModelSerializer):
    storages = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Storages.objects.all()
     )
    founders = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Founders.objects.all()
     )
    factories = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Factories.objects.all()
     )
    offices = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Offices.objects.all()
     )

    class Meta:
        model = FoundersCompanyOrganization
        fields = (
            'id',
            'companyname',
            'factories',
            'storages',
            'founders',
            'offices',
            'user'
        )


class FirmSerializer(serializers.ModelSerializer):
    founderscompanyorganization = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = FoundersCompanyOrganization.objects.all()
     )

    class Meta:
        model = Firm
        fields = (
            'id',
            'name',
            'mobile',
            'directer',
            'mail',
            'info',
            'connect_date_firm',
            'create_date_firm',
            'firm_is_supplier',
            'founderscompanyorganization',
            'user'
        )

class ItemSerializer(serializers.ModelSerializer):
    firm = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Firm.objects.all()
     )

    param = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Param.objects.all()
     )
    
    price = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Price.objects.all()
     )

    class Meta:
        model = Item
        fields = (
            'id',
            'name',
            'firm',
            'param',
            'price',
            'create_date',
            'user'
        )

class ItemsSerializer(serializers.ModelSerializer):
    item = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Item.objects.all()
     )

    class Meta:
        model = Items
        fields = (
            'id',
            'name_group',
            'item',
            'count',
            'user'
        )

class ItemsSupplierSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Items.objects.all()
     )

    class Meta:
        model = ItemsSupplier
        fields = (
            'id',
            'name_group',
            'items',
            'user'
        )

class ItemsInStorageSerializer(serializers.ModelSerializer):
    storage = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Storage.objects.all()
     )

    items = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Items.objects.all()
     )

    class Meta:
        model = ItemsInStorage
        fields = (
            'id',
            'storage',
            'items',
            'user'
        )

class DeliveryTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryTransport
        fields = (
            'id',
            'model_name',
            'type_of_transport',
            'year_constructed',
            'order_coast',
            'ready',
            'time_delivery',
            'done_order',
            'user'
        )

class DeliveryInAWaySerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Items.objects.all()
     )

    transport = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Items.objects.all()
     )
    class Meta:
        model = DeliveryInAWay
        fields = (
            'id',
            'transport',
            'items',
            'user'
        )

class SupplierInfoSerializer(serializers.ModelSerializer):
    storages = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Storages.objects.all()
     )
    delivery_transport = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = DeliveryTransport.objects.all()
     )
    factories = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Factories.objects.all()
     )
    offices = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Offices.objects.all()
     )

    class Meta:
        model = SupplierInfo
        fields = (
            'id',
            'count_storages',
            'average_time_delivery',
            'storages',
            'factories',
            'offices',
            'delivery_transport',
            'text',
            'user'
        )

class SupplierSerializer(serializers.ModelSerializer):
    items_supplier = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = ItemsSupplier.objects.all()
     )
    supplier_info = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = SupplierInfo.objects.all()
     )

    founderscompanyorganization = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = FoundersCompanyOrganization.objects.all()
     )

    class Meta:
        model = Supplier
        fields = (
            'id',
            'name',
            'mobile',
            'director',
            'founderscompanyorganization',
            'mail',
            'supplier_info',
            'items_supplier',
            'create_date',
            'connect_date',
            'user'
        )

class OrderTableSerializer(serializers.ModelSerializer):
    address = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Address.objects.all()
     )

    items = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Items.objects.all()
     )

    class Meta:
        model = OrderTable
        fields = (
            'id',
            'name',
            'wornot',
            'address',
            'items',
            'create_date',
            'get_date',
            'user'
        )

class RoleNowSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoleNow
        fields = (
            'id',
            'name',
            'countpeople',
            'needHE',
            'user'
        )

class TotalRoleSerializer(serializers.ModelSerializer):

    role_now = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = RoleNow.objects.all()
     )

    class Meta:
        model = TotalRole
        fields = (
            'id',
            'name',
            'role_now',
            'user'
        )

class EmployeeSerializer(serializers.ModelSerializer):

    address = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Address.objects.all()
     )

    trole = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = TotalRole.objects.all()
     )

    user = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = UserCustom.objects.all()
     )

    orderes = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = OrderTable.objects.all()
     )

    class Meta:
        model = Employee
        fields = (
            'id',
            'first_name',
            'second_name',
            'photo',
            'mobile',
            'mail',
            'info',
            'he',
            'salary',
            'create_date',
            'experience',
            'trole',
            'address',
            'user',
            'orderes',
            'adduser'
        )

class ReadySerializer(serializers.ModelSerializer):

    employee = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Employee.objects.all()
     )

    address = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Address.objects.all()
     )

    items = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Items.objects.all()
     )


    class Meta:
        model = Ready
        fields = (
            'id',
            'order_status',
            'employee',
            'address',
            'items',
            'total_price',
            'user'
        )

class OrderesSerializer(serializers.ModelSerializer):

    orderes = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=True,
        queryset = Orderes.objects.all()
     )

    supplier = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Supplier.objects.all()
     )

    storage = serializers.PrimaryKeyRelatedField(
        read_only=False,
        many=False,
        queryset = Storage.objects.all()
     )


    class Meta:
        model = Orderes
        fields = (
            'id',
            'orderes',
            'total_price',
            'storage',
            'supplier',
            'send',
            'received',
            'pos_one_get',
            'date_send',
            'date_get',
            'user'
        )