from rest_framework import viewsets,generics
from rest_framework.views import APIView
from Store.models import Add_Product
from .serialize import ProductSerializers
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Add_Product.objects.all()
    serializer_class = ProductSerializers

class ProductSearchView(viewsets.ModelViewSet):
        queryset = Add_Product.objects.all()
        serializer_class = ProductSerializers
        filter_backends = [DjangoFilterBackend]
        filterset_fields = {
            'Product_Title':['icontains']
        }
        def get_queryset(self):
            queryset = super().get_queryset()
            q = self.request.GET.get('q')
            if q:
                queryset = queryset.filter(Product_Title__icontains=q)
                return queryset