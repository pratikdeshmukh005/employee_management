from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    hire_date = models.DateField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

class Role(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)

class EmployeeRole(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('emp', 'role')

class Project(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class WorksOn(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    proj = models.ForeignKey(Project, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('emp', 'proj')

class Leave(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()

class PerformanceReport(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    proj = models.ForeignKey(Project, on_delete=models.CASCADE)
    eval_date = models.DateField()
    performance_score = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()
from django.db import models

# Create your models here.
