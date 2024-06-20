from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees.views import DepartmentViewSet, EmployeeViewSet, RoleViewSet, EmployeeRoleViewSet, ProjectViewSet, WorksOnViewSet, LeaveViewSet, PerformanceReportViewSet

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'employee-roles', EmployeeRoleViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'works-on', WorksOnViewSet)
router.register(r'leaves', LeaveViewSet)
router.register(r'performance-reports', PerformanceReportViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

