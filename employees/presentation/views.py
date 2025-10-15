from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from employees.usecases.employee_usecases import EmployeeUsecase
from rest_framework_simplejwt.tokens import RefreshToken

class EmployeeListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    usecase = EmployeeUsecase()

    def get(self, request):
        employees = self.usecase.list_employees()
        return Response([e.__dict__ for e in employees])

    def post(self, request):
        employee = self.usecase.create_employee(request.data)
        return Response(employee.__dict__, status=status.HTTP_201_CREATED)


class EmployeeRetrieveUpdateDeleteView(APIView):
    permission_classes = [IsAuthenticated]
    usecase = EmployeeUsecase()

    def get(self, request, pk):
        employees = self.usecase.list_employees()
        employee = next((e for e in employees if e.id == int(pk)), None)
        if not employee:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(employee.__dict__)

    def put(self, request, pk):
        employees = self.usecase.list_employees()
        employee = next((e for e in employees if e.id == int(pk)), None)
        if not employee:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        updated_employee = self.usecase.update_employee(pk, request.data)
        return Response(updated_employee.__dict__)

    def delete(self, request, pk):
        employees = self.usecase.list_employees()
        employee = next((e for e in employees if e.id == int(pk)), None)
        if not employee:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        self.usecase.delete_employee(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful"}, status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response({"detail": "Refresh token required"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
