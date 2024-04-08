from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer

class CompanyList(APIView):
    def get(self, request, format=None):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

class CompanyDetail(APIView):
    def get_object(self, id):
        try:
            return Company.objects.get(pk=id)
        except Company.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id, format=None):
        company = self.get_object(id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)

class CompanyVacancies(APIView):
    def get(self, request, id, format=None):
        vacancies = Vacancy.objects.filter(company_id=id)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

class VacancyList(APIView):
    def get(self, request, format=None):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

class VacancyDetail(APIView):
    def get_object(self, id):
        try:
            return Vacancy.objects.get(pk=id)
        except Vacancy.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id, format=None):
        vacancy = self.get_object(id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

class TopTenVacancies(APIView):
    def get(self, request, format=None):
        vacancies = Vacancy.objects.order_by('-salary')[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
