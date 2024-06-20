from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from records import views

router = DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'roles', views.RoleViewSet)
router.register(r'employee_roles', views.EmployeeRoleViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'works_on', views.WorksOnViewSet)
router.register(r'leaves', views.LeaveViewSet)
router.register(r'performance_reports', views.PerformanceReportViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

