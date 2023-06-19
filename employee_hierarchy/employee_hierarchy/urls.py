from django.contrib import admin
from django.urls import path
from employees.views import employee_hierarchy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', employee_hierarchy, name='employee_hierarchy'),
]
