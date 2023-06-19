from django.shortcuts import render
from .models import Employee

# для удаления данных в бд python manage.py flush
# для заполнения тестовыми данными бд python manage.py shell затем exec(open('employees/seeds.py').read())


def employee_hierarchy(request):
    employees = Employee.objects.select_related('manager').all()
    return render(request, 'employees/employee_hierarchy.html', {'employees': employees})



# def generate_hierarchy(employee, visited=None, depth=0, max_depth=5):
#     if visited is None:
#         visited = set()
#
#     if employee in visited or depth >= max_depth:
#         return None
#
#     visited.add(employee)
#
#     hierarchy = {
#         'name': employee.name,
#         'position': employee.position,
#         'manager': None,
#         'subordinates': []
#     }
#
#     if employee.manager:
#         hierarchy['manager'] = generate_hierarchy(employee.manager, visited, depth=depth + 1, max_depth=max_depth)
#
#     hierarchy['subordinates'] = [
#         generate_hierarchy(subordinate, visited, depth=depth + 1, max_depth=max_depth)
#         for subordinate in employee.subordinates.all()
#     ]
#
#     return hierarchy
#
#
# def employee_hierarchy(request):
#     employees = Employee.objects.select_related('manager').all()
#     hierarchy = [generate_hierarchy(employee) for employee in employees]
#     return render(request, 'employees/employee_hierarchy.html', {'hierarchy': hierarchy})






# def employee_hierarchy(request):
#     employees = Employee.objects.select_related('manager').all()[:50]
#     return render(request, 'employees/employee_hierarchy.html', {'employees': employees})

