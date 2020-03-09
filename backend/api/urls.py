from .views import *
from backend.api import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib.auth import authenticate



addressList = AddressViewSet.as_view({'get': 'list', 'post': 'create',})
addressDetails = AddressViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
userList = UserCustomViewSet.as_view({'get': 'list', 'post': 'create',})
userDetails = UserCustomViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
paramList = ParamViewSet.as_view({'get': 'list', 'post': 'create',})
paramDetails = ParamViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
priceList = PriceViewSet.as_view({'get': 'list', 'post': 'create',})
priceDetails = PriceViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
meshList = MeshViewSet.as_view({'get': 'list', 'post': 'create',})
meshDetails = MeshViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
founderList = FounderViewSet.as_view({'get': 'list', 'post': 'create',})
founderDetails = FounderViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
foundersList = FoundersViewSet.as_view({'get': 'list', 'post': 'create',})
foundersDetails = FoundersViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
officeList = OfficeViewSet.as_view({'get': 'list', 'post': 'create',})
officeDetails = OfficeViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
factoryList = AddressViewSet.as_view({'get': 'list', 'post': 'create',})
factoryDetails = AddressViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
storagesList = StoragesViewSet.as_view({'get': 'list', 'post': 'create',})
storagesDetails = StoragesViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
officesList = OfficesViewSet.as_view({'get': 'list', 'post': 'create',})
officesDetails = OfficesViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
factoriesList = FactoriesViewSet.as_view({'get': 'list', 'post': 'create',})
factoriesDetails = FactoriesViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
storageList = StorageViewSet.as_view({'get': 'list', 'post': 'create',})
storageDetails = StorageViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
founderscompanyorganizationList = FoundersCompanyOrganizationViewSet.as_view({'get': 'list', 'post': 'create',})
founderscompanyorganizationDetails = FoundersCompanyOrganizationViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
firmList = FirmViewSet.as_view({'get': 'list', 'post': 'create',})
firmDetails = FirmViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
itemList = ItemViewSet.as_view({'get': 'list', 'post': 'create',})
itemDetails = ItemViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
itemsList = ItemsViewSet.as_view({'get': 'list', 'post': 'create',})
itemsDetails = ItemsViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
itemssupplierList = ItemsSupplierViewSet.as_view({'get': 'list', 'post': 'create',})
itemssupplierDetails = ItemsSupplierViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
itemsinstorageList = ItemsInStorageViewSet.as_view({'get': 'list', 'post': 'create',})
itemsinstorageDetails = ItemsInStorageViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
deliverytransportList = DeliveryTransportViewSet.as_view({'get': 'list', 'post': 'create',})
deliverytransportDetails = DeliveryTransportViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
deliveryinawayList = DeliveryInAWayViewSet.as_view({'get': 'list', 'post': 'create',})
deliveryinawayDetails = DeliveryInAWayViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
supplierinfoList = SupplierInfoViewSet.as_view({'get': 'list', 'post': 'create',})
supplierinfoDetails = SupplierInfoViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
supplierList = SupplierViewSet.as_view({'get': 'list', 'post': 'create',})
supplierDetails = SupplierViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
ordertableList = OrderTableViewSet.as_view({'get': 'list', 'post': 'create',})
ordertableDetails = OrderTableViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
rolenowList = RoleNowViewSet.as_view({'get': 'list', 'post': 'create',})
rolenowDetails = RoleNowViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })
totalroleList = TotalRoleViewSet.as_view({'get': 'list', 'post': 'create',})
totalroleDetails = TotalRoleViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })

employeeList = EmployeeViewSet.as_view({'get': 'list', 'post': 'create',})
employeeDetails = EmployeeViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })

readyList = ReadyViewSet.as_view({'get': 'list', 'post': 'create',})
readyDetails = ReadyViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })

orderesList = OrderesViewSet.as_view({'get': 'list', 'post': 'create',})
orderesDetails = OrderesViewSet.as_view({
      'get': 'retrieve',
      'put': 'update',
      'patch': 'partial_update',
      'delete': 'destroy'
  })

from .permissions import CustomDjangoModelPermissions

"""
Provides a set of pluggable permission policies.
"""
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    perm = request.POST['perm']
    user = authenticate(username=username, password=password, perm = perm)
    return (user.perm)

router = DefaultRouter(CustomDjangoModelPermissions)

router.register(r'address', views.AddressViewSet)
router.register(r'users', views.UserCustomViewSet)
router.register(r'param', views.ParamViewSet)
router.register(r'price', views.PriceViewSet)
router.register(r'mesh', views.MeshViewSet)
router.register(r'founder', views.FounderViewSet)
router.register(r'founders', views.FoundersViewSet)
router.register(r'office', views.OfficeViewSet)
router.register(r'factory', views.FactoryViewSet)
router.register(r'storages', views.StoragesViewSet)
router.register(r'offices', views.OfficesViewSet)
router.register(r'factories', views.FactoriesViewSet)
router.register(r'storage', views.StorageViewSet)
router.register(r'founderscompanyorganization', views.FoundersCompanyOrganizationViewSet)
router.register(r'firm', views.FirmViewSet)
router.register(r'item', views.ItemViewSet)
router.register(r'items', views.ItemsViewSet)
router.register(r'itemssupplier', views.ItemsSupplierViewSet)
router.register(r'itemsinstorage', views.ItemsInStorageViewSet)
router.register(r'deliverytransport', views.DeliveryTransportViewSet)
router.register(r'deliveryinaway', views.DeliveryInAWayViewSet)
router.register(r'supplierinfo', views.SupplierInfoViewSet)
router.register(r'supplier', views.SupplierViewSet)
router.register(r'ordertable', views.OrderTableViewSet)
router.register(r'rolenow', views.RoleNowViewSet)
router.register(r'totalrole', views.TotalRoleViewSet)
router.register(r'employee', views.EmployeeViewSet)
router.register(r'ready', views.ReadyViewSet)
router.register(r'orderes', views.OrderesViewSet)
router.register(r'deliveryinaway', views.DeliveryInAWayViewSet)
router.register(r'orderes', views.OrderesViewSet)
  




urlpatterns = [
  path('', include(router.urls)),
  path(r'logout/', LogoutAPIView.as_view(), name='logout'),
]