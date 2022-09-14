from sys import api_version, modules
from django.shortcuts import render
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from projectapp.models import Oraganization_Model, Employee_Model
from projectapp.serializers import Serializers_For_Organization, Serializers_For_Employee
import json
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from django.db.models import Q, Max

# Class for Organization model
class Organization(APIView):
    def get(self,request):
        try:
            #data=request.GET.get("Organization_Id")
            data = request
            Org_Query=Oraganization_Model.objects.get(Organization_Id=data)
            seri=Serializers_For_Organization(Org_Query,partial=True)
            return Response((seri.data),status=200)
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)
    def post(self,request):
        try:
            # data=request.data
            data = request
            if data == '':
                raise TypeError("Please send vaild payload")
            seri=Serializers_For_Organization(data=data)
            if seri.is_valid(): 
                seri.save()
                return Response((seri.data),status=200)
            return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)    
    def put(self,request):
        try:
            #data=request.data
            data=request
            
            Org_Query=Oraganization_Model.objects.get(Organization_Id=data['Organization_Id'])
            seri=Serializers_For_Organization(Org_Query,data=data)
            print(seri)
            if seri.is_valid():
                seri.save()
                return Response((seri.data),status=200)
            return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)    
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request):
        try:
            #data=request.data
            data=request
            if data=="":
                raise TypeError('raise Exception')
            Org_Query=Oraganization_Model.objects.get(Organization_Id=data['Organization_Id'])
            seri=Serializers_For_Organization(Org_Query,data=data,partial=True)
            if seri.is_valid():
                seri.save()
                return Response((seri.data),status=200)   
            return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)    
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request):
        #data=request.data
        data=request
        try:
            Org_Query= Oraganization_Model.objects.filter(Organization_Id= data['Organization_Id']).update(Is_Delete=True)
            return Response("sucessfully Deleted")  
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)

# View  Class for Employee model
class Employee(APIView):
    def get(self,request):
        try:
            #emp=Employee_Model.objects.filter(Employee_Org_Id__Organization_Name='foyer')
            #data = request.GET.get('Employee_Id')
            data=request
            Emp_Query=Employee_Model.objects.get(Employee_Id=data)
            seri=Serializers_For_Employee(Emp_Query,partial=True)
            return Response((seri.data),status=200)
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)

    def post(self,request):
        try:
            data=request
            if data==" ":
                raise TypeError('plz enter the valid reason')
            seri=Serializers_For_Employee(data=data)
            if seri.is_valid():
                seri.save()
                return Response((seri.data),status=200)
            return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST) 
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)

    def put(self,request):
        try:
            #data=request.data
            data=request
            if data==" ":
                raise TypeError('plz enter the crt value')
            Emp_Query=Employee_Model.objects.get(Employee_Id=data['Employee_Id'])
            print(Emp_Query)
            seri=Serializers_For_Employee(Emp_Query,data=data)
            if seri.is_valid():
                seri.save()
                return Response((seri.data),status=200)  
            return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)   
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)
    def patch(self,request):
        try:
            #data=request.data
            data=request
            if data==" ":
                raise TypeError('is not valid')
            emp=Employee_Model.objects.get(Employee_Id=data['Employee_Id'])
            seri=Serializers_For_Employee(emp,data=data,partial=True)
            if seri.is_valid():
                seri.save()
                return Response((seri.data),status=200)
            return Response(seri.errors,status=status.HTTP_400_BAD_REQUEST)   
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request):
        #data=request.data
        data=request
        try:
            Emp_Query = Employee_Model.objects.filter(Employee_Id = data['Employee_Id']).update(Is_Delete=True)
            print(Emp_Query)
            return Response("sucessfully deleted",content_type='appilcation/json',status=200) 
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)


#Class for list,search,filter operation  in Organization Model

class class_For_Organization(APIView):
    def get(self,request):    #List API for the Organization
        #data=request.GET.get("Is_Delete")
        data=request
        print(data)
        try:
            Org_Query=Oraganization_Model.objects.filter(Is_Delete=data).order_by('-Organization_Id')
            print(Org_Query)
            seri=Serializers_For_Organization(Org_Query,many=True)
            return Response((seri.data),status=200)
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)

    def post(self,request): # Filter API
        try:
            #data=request.data
        
            data=request
        
            Org_Query=Oraganization_Model.objects.filter(Organization_Name__icontains=data["Organization_Name"],
                                              Organization_Location__icontains=data["Organization_Location"])
            print(Org_Query)

            seri=Serializers_For_Organization(Org_Query,many=True)
            return Response((seri.data),status=200)
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)
    def put(self,request): #search API
        try:
            #data=request.data
            data=request
            print(data)
            Org_Query=Oraganization_Model.objects.filter(Q(Organization_Name__icontains=data["Organization_Name"])|
                                              Q(Organization_Location__icontains=data["search"]))
            print(Org_Query)

            seri=Serializers_For_Organization(Org_Query,many=True)
        
          
            return Response((seri.data),status=200)
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)
    

#Class for list,search,filter operation  in Employee model

class class_For_Employee(APIView):
    def get(self,request):    #List API for the Employee
        #data=request.GET.get("Is_Delete")
        data=request
        try:
            Org_Query=Employee_Model.objects.filter(Is_Delete=data).order_by('-Employee_Id')
            print(Org_Query)
            seri=Serializers_For_Employee(Org_Query,many=True)
            return Response((seri.data),status=200)
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)
    
    def post(self,request):    #filter API for the Employee
        #data=request.data
        data=request
        try:
            Org_Query=Employee_Model.objects.filter(Organization_Id__Organization_Name__icontains=data["Organization_Name"],
                                                    Employee_Salary__range=data["Employee_Salary"])
            print(Employee_Model.objects.aggregate(Max('Employee_Salary'))['Employee_Salary__max'])
            seri=Serializers_For_Employee(Org_Query,many=True)
            return Response((seri.data),status=200)
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)

    def put(self,request): #search API
        try:
            #data=request.data    
            data=request             
        
            Query=Employee_Model.objects.filter(Q(Employee_Name__icontains=data["Employee_Name"])|
                                              Q(Employee_Address__country__icontains=data["search"]))
            print(Query.values_list)

            
            seri=Serializers_For_Employee(Query,many=True)
            return Response((seri.data),status=200)
        except Exception as e:
            return Response(({'Errors':str(e)}),status=status.HTTP_400_BAD_REQUEST)
    






    





