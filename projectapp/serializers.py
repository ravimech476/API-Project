from projectapp.models import Employee_Model
from projectapp.models import Oraganization_Model
from rest_framework import serializers
from rest_framework.response import Response

# serializers for Organization model

class Serializers_For_Organization(serializers.ModelSerializer):
    class Meta:
        model=Oraganization_Model
        fields="__all__"
# Validation for field level validation  the organization name
    def validate_Organization_Name(self,value):
        if len(value)<2:
           raise serializers.ValidationError('Name is too short')
        return value
# # Validation for object level validation for the model
#     def validate(self,data): 
#         if data['Organization_Capitalamount']==data['Organization_Turnover']:
#             Response({'Errors':(serializers.ValidationError('the fields too short'))})
#         else:
#             return data
# serializers for Employee model
class Serializers_For_Employee(serializers.ModelSerializer):
    class Meta:
        model=Employee_Model
        fields="__all__"


