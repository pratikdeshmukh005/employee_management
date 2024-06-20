from rest_framework import viewsets
from .models import Department, Employee, Role, EmployeeRole, Project, WorksOn, Leave, PerformanceReport
from .serializers import DepartmentSerializer, EmployeeSerializer, RoleSerializer, EmployeeRoleSerializer, ProjectSerializer, WorksOnSerializer, LeaveSerializer, PerformanceReportSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class EmployeeRoleViewSet(viewsets.ModelViewSet):
    queryset = EmployeeRole.objects.all()
    serializer_class = EmployeeRoleSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class WorksOnViewSet(viewsets.ModelViewSet):
    queryset = WorksOn.objects.all()
    serializer_class = WorksOnSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class PerformanceReportViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReport.objects.all()
    serializer_class = PerformanceReportSerializer

