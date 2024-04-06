# urls.py
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, ProductViewSet, CustomerViewSet
from .views import TopSellingProducts, TopPerformingEmployees


router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('analytics/top-selling-products/', TopSellingProducts.as_view(), name='top_selling_products'),
    path('analytics/top-performing-employees/', TopPerformingEmployees.as_view(), name='top_performing_employees'),
  
]
