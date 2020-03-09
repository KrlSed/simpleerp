from rest_framework import generics, mixins
from backend.models import *
from .serializers import  *
from rest_framework import authentication, permissions
from rest_framework.authentication import SessionAuthentication
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from .permissions import IsAuthenticated, CustomDjangoModelPermissions
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import renderers

from django.http import Http404


from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class LogoutAPIView(APIView):

    def get_queryset(self):
        return (UserCustom.objects.all())


    def get(self, request):
        logout(request)
        return HttpResponseRedirect(redirect_to='/accounts/login')


@action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])


class AddressViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated &
        CustomDjangoModelPermissions
    ]
    authentication_classes = [
        SessionAuthentication,
    ]


    serializer_class = AddressSerializer

    queryset = Address.objects.all()



class UserCustomViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = UserCustom.objects.all()
    serializer_class = UserCustomSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class FounderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Founder.objects.all()
    serializer_class = FounderSerializer
    authentication_classes = [
        SessionAuthentication,
    ]



class MeshViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Mesh.objects.all()
    serializer_class = MeshSerializer
    authentication_classes = [
        SessionAuthentication,
    ]

class PriceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Price.objects.all()
    serializer_class = PriceSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class ParamViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Param.objects.all()
    serializer_class = ParamSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class FoundersViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Founders.objects.all()
    serializer_class = FoundersSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class OfficeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Office.objects.all()
    serializer_class = OfficeSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class FactoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Factory.objects.all()
    serializer_class = FactorySerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class StorageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class OfficesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Offices.objects.all()
    serializer_class = OfficesSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class FactoriesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Factories.objects.all()
    serializer_class = FactoriesSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class StoragesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Storages.objects.all()
    serializer_class = StoragesSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class FoundersCompanyOrganizationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = FoundersCompanyOrganization.objects.all()
    serializer_class = FoundersCompanyOrganizationSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class FirmViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class ItemsViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class ItemsSupplierViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = ItemsSupplier.objects.all()
    serializer_class = ItemsSupplierSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class ItemsInStorageViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = ItemsInStorage.objects.all()
    serializer_class = ItemsInStorageSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class DeliveryTransportViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = DeliveryTransport.objects.all()
    serializer_class = DeliveryTransportSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class DeliveryInAWayViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = DeliveryInAWay.objects.all()
    serializer_class = DeliveryInAWaySerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class SupplierInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = SupplierInfo.objects.all()
    serializer_class = SupplierInfoSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class SupplierViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class OrderTableViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = OrderTable.objects.all()
    serializer_class = OrderTableSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class RoleNowViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = RoleNow.objects.all()
    serializer_class = RoleNowSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class TotalRoleViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = TotalRole.objects.all()
    serializer_class = TotalRoleSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class ReadyViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Ready.objects.all()
    serializer_class = ReadySerializer
    authentication_classes = [
        SessionAuthentication,
    ]


class OrderesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated & CustomDjangoModelPermissions]
    queryset = Orderes.objects.all()
    serializer_class = OrderesSerializer
    
