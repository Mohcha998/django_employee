from employees.domain.models import Employee
from employees.data.serializers import EmployeeSerializer
from employees.presentation.models_django import EmployeeModel

class EmployeeRepository:
    def create_employee(self, data) -> Employee:
        serializer = EmployeeSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Employee(id=obj.id, name=obj.name, email=obj.email, position=obj.position, salary=obj.salary)

    def get_all_employees(self):
        objs = EmployeeModel.objects.all()
        return [Employee(id=o.id, name=o.name, email=o.email, position=o.position, salary=o.salary) for o in objs]

    def update_employee(self, pk, data) -> Employee:
        try:
            obj = EmployeeModel.objects.get(pk=pk)
        except EmployeeModel.DoesNotExist:
            raise Exception("Employee not found")
        serializer = EmployeeSerializer(obj, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        obj = serializer.save()
        return Employee(id=obj.id, name=obj.name, email=obj.email, position=obj.position, salary=obj.salary)

    def delete_employee(self, pk):
        try:
            obj = EmployeeModel.objects.get(pk=pk)
        except EmployeeModel.DoesNotExist:
            raise Exception("Employee not found")
        obj.delete()
