from django.db import models


# Models for Organization
class Oraganization_Model(models.Model):

    Organization_Id=models.IntegerField(primary_key=True)
    Organization_Name=models.CharField(max_length=30)
    Organization_Location=models.CharField(max_length=30)
    Organization_Address=models.JSONField()
    Organization_No_Of_Employee=models.IntegerField()
    Organization_Turnover=models.BigIntegerField()
    Organization_Capitalamount=models.BigIntegerField()
    Is_Delete=models.BooleanField(default=False)

# Models for Employees

class Employee_Model(models.Model):
    Employee_Id=models.IntegerField(primary_key=True)
    Organization_Id=models.ForeignKey(Oraganization_Model, on_delete=models.CASCADE)  #doubt about models.CASCADE
    Employee_Name=models.CharField(max_length=20)     
    Employee_Salary=models.FloatField()
    Employee_Address=models.JSONField()
    Employee_Designation=models.CharField(max_length=30)
    Is_Delete=models.BooleanField(default=False)






