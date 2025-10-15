from employees.presentation.views import EmployeeListCreateView, EmployeeRetrieveUpdateDeleteView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/employees/', EmployeeListCreateView.as_view(), name='employees'),
    path('api/employees/<int:pk>/', EmployeeRetrieveUpdateDeleteView.as_view(), name='employee_detail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
]
