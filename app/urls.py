from django.urls import path
from .views import DepartmentDetailView, DepartmentListCreateView, EmpListView, EmpListViewBySalary, EmpListViewByloc, EmployeeDetailView, EmployeeListCreateView, EmployeesDetailView, EmployeesListView, LocationDetailView, LocationListCreateView
from app import views

urlpatterns = [
    path('location/', LocationListCreateView.as_view(), name='student-list-create'),
    path('location/<int:pk>/', LocationDetailView.as_view(), name='student-detail'),
    path('employee/', EmployeeListCreateView.as_view(), name='student-list-create'),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name='student-detail'),
    path('department/', DepartmentListCreateView.as_view(), name='student-list-create'),
    path('department/<int:pk>/', DepartmentDetailView.as_view(), name='student-detail'),
    path('employees/',EmployeesListView.as_view(),name='employee-list'),
    path('employees/<int:pk>/',EmployeesDetailView.as_view(),name='employee-detail'),
    
    path('emp/',EmpListView.as_view(),name='employee-list'),
    path('emplo/',EmpListViewByloc.as_view(),name='employee-list'),
    path('empsalary/',EmpListViewBySalary.as_view(),name='employee-salary'),

]

