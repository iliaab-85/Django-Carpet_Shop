from rest_framework import routers
from .views import ProductViewSet,ProductSearchView
from django.urls import path,include
from . import views

router = routers.DefaultRouter()
router.register(r"read_product",ProductViewSet)
router.register(r"Search_product",ProductSearchView, basename='search')

urlpatterns = [
    path('',include(router.urls)),
    #path('search/',views.ProductSearchView.as_view()),
]