from employees.data.repositories import EmployeeRepository

class EmployeeUsecase:
    def __init__(self):
        self.repo = EmployeeRepository()

    def create_employee(self, data):
        return self.repo.create_employee(data)

    def list_employees(self):
        return self.repo.get_all_employees()

    def update_employee(self, pk, data):
        return self.repo.update_employee(pk, data)

    def delete_employee(self, pk):
        self.repo.delete_employee(pk)
