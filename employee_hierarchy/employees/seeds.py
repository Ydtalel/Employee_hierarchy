from django_seed import Seed
from employees.models import Employee
import random
from datetime import date, timedelta

seeder = Seed.seeder()

# Определите количество сотрудников, которые вы хотите создать
num_employees = 100

# Добавьте генератор данных для модели Employee
seeder.add_entity(Employee, num_employees, {
    'name': lambda x: seeder.faker.name(),
    'position': lambda x: seeder.faker.job(),
    'hire_date': lambda x: date.today() - timedelta(days=random.randint(1, 365)),
    'salary': lambda x: random.randint(30000, 100000),
    'manager': lambda x: random.choice(Employee.objects.all()) if Employee.objects.exists() else None,
})


# Выполните заполнение базы данных
inserted_pks = seeder.execute()

# Выведите информацию о заполненных записях
print(f"{len(inserted_pks[Employee])} employees created.")

