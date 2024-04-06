from rest_framework import viewsets
from .models import Employee, Product, Customer, Sale
from .serializers import EmployeeSerializer, ProductSerializer, CustomerSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Count

# employee view
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = []  # Remove all permission classes

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []  # Remove all permission classes

class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = []  # Remove all permission classes

class TopSellingProducts(APIView):
    serializer_class = ProductSerializer  # Define serializer_class
    def get(self, request):
        top_products = Sale.objects.values('product__name').annotate(total_sales=Count('product')).order_by('-total_sales')[:10]
        return Response({'top_selling_products': top_products})

class TopPerformingEmployees(APIView):
    serializer_class = EmployeeSerializer  # Define serializer_class
    def get(self, request):
        top_employees = Sale.objects.values('employee__username').annotate(total_sales=Count('employee')).order_by('-total_sales')[:10]
        return Response({'top_performing_employees': top_employees})
