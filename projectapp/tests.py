from django.test import TestCase
from projectapp.views import *
# Create your tests here.
class OrganizationTest(TestCase):
    def setUp(self):
        Oraganization_Model.objects.create(Organization_Id=60,Organization_Name= "foyer",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
        Oraganization_Model.objects.create(Organization_Id=56,Organization_Name= "foyer",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
        Oraganization_Model.objects.create(Organization_Id=58,Organization_Name= "foyer",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
        Oraganization_Model.objects.create(Organization_Id=1,Organization_Name= "foyer",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
        Oraganization_Model.objects.create(Organization_Id=303,Organization_Name= "foyer",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= False)
    # Creating Organization Test Cases for post method
    def test_organiztion_post_status_200(self):
        org = Organization.post(self, request={"Organization_Id":308,"Organization_Name": "foyer","Organization_Location": "chennai","Organization_Address": {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},"Organization_No_Of_Employee": 13,"Organization_Turnover": 100000,"Organization_Capitalamount": 50000,"Is_Delete": True})
        self.assertEqual(org.status_code,200)
    def test_organization_post_status1_400(self):
        org=Organization.post(self,request={"Organization_Id": 54,"Organization_Name": "f","Organization_Location": "chennai","Organization_Address": {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},"Organization_No_Of_Employee": 13,"Organization_Turnover": 100000,"Organization_Capitalamount": 50000,"Is_Delete": True})
        self.assertEqual(org.status_code,400)
    def test_organization_post_status2_400(self):
        org=Organization.post(self,request='')
        self.assertEqual(org.status_code,400)
    # # Creating Organization Test cases for Get method
    def test_organization_get_status_400(self):
        org=Organization.get(self,request={})
        self.assertEqual(org.status_code,400)
    def test_organization_get_status_200(self):
        org=Organization.get(self,request=56)
        self.assertEqual(org.status_code,200)
    # Creating Organization Test cases for Put Method
    def test_organization_put_status_400(self):
        org=Organization.put(self,request={"Organization_Id":60,"Organization_Location": "chennai","Organization_Address": {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},"Organization_No_Of_Employee": 13,"Organization_Turnover": 100000,"Organization_Capitalamount": 50000,"Is_Delete": True})
        self.assertEqual(org.status_code,400)
    def test_organization_put_status_200(self):
        org=Organization.put(self,request={"Organization_Id":58,"Organization_Name": "fjhfhdsfb","Organization_Location": "chennai","Organization_Address": {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},"Organization_No_Of_Employee": 13,"Organization_Turnover": 100000,"Organization_Capitalamount": 50000,"Is_Delete": True})
        self.assertEqual(org.status_code,200)
    def test_organization_put_status1_400(self):
        org=Organization.put(self,request={"Organization_Name": "fjhfhdsfb","Organization_Location": "chennai","Organization_Address": {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},"Organization_No_Of_Employee": 13,"Organization_Turnover": 100000,"Organization_Capitalamount": 50000,"Is_Delete": True})
        self.assertEqual(org.status_code,400)
# creating organization test cases for the partial method
    def test_organization_partial_status_400(self):
         org=Organization.patch(self,request={"Organization_Id":1,"Is_Delete":''})
         self.assertEqual(org.status_code,400)
    def test_organization_partial_status_200(self):
         org=Organization.patch(self,request={"Organization_Id":1,"Organization_Name": "fjhfhdsfb","Organization_Location": "chennai","Organization_No_Of_Employee": 13,"Organization_Turnover": 100000,"Is_Delete": True})
         self.assertEqual(org.status_code,200)
    def test_organization_partial_status1_400(self):
         org=Organization.patch(self,request="")
         self.assertEqual(org.status_code,400)
 # creating the organization test cases for the delete method
    def test_organization_delete_400(self):
         org=Organization.delete(self,request=45)
         self.assertEqual(org.status_code,400)
    def test_organization_delete_200(self):
         org=Organization.delete(self,request={"Organization_Id":303})
         self.assertEqual(org.status_code,200)
class EmployeeTest(TestCase):
    def setUp(self):
       Oraganization_Model.objects.create(Organization_Id=58,Organization_Name= "foyer",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
       Oraganization_Model.objects.create(Organization_Id=56,Organization_Name= "foyer",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
       Oraganization_Model.objects.create(Organization_Id=57,Organization_Name= "foyer",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
       Employee_Model.objects.create(Employee_Id=12,Employee_Name= "kumar",Employee_Salary= 15000.0,Employee_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Employee_Designation= 'Trainee',Is_Delete= False,Organization_Id=Oraganization_Model.objects.get(Organization_Id=58))
       Employee_Model.objects.create(Employee_Id=11,Employee_Name= "kumar",Employee_Salary= 15000.0,Employee_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Employee_Designation= 'Trainee',Is_Delete= False,Organization_Id=Oraganization_Model.objects.get(Organization_Id=57))
       Employee_Model.objects.create(Employee_Id=10,Employee_Name= "kumar",Employee_Salary= 15000.0,Employee_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Employee_Designation= 'Trainee',Is_Delete= False,Organization_Id=Oraganization_Model.objects.get(Organization_Id=56))
    #creating employee test cases for  get method  
    def test_employee_get_status_400(self):
            Q=Employee.get(self,request={})
            self.assertEqual(Q.status_code,400)
    def test_employee_get_status_200(self):
            Q=Employee.get(self,request=10)
            self.assertEqual(Q.status_code,200)
    #creating employee test cases for post method
    def test_employee_post_status_400(self):
            Q=Employee.post(self,request=" ")
            self.assertEqual(Q.status_code,400)
    def test_employee_post_status_200(self):
            Q=Employee.post(self,request={ "Employee_Id": 56,"Employee_Name": "malliga","Employee_Salary": 15000.0,"Employee_Address": {"DoorNO": "01","street": "vellarivelli","country": "India","state": "Tamilnadu"},"Employee_Designation": "Trainee","Is_Delete": False,"Organization_Id": 56})
            self.assertEqual(Q.status_code,200)
    def test_employee_post_status1_400(self):
            Q=Employee.post(self,request={})
            self.assertEqual(Q.status_code,400)
    # creating test cases for the put method
    def test_employee_put_status_400(self):
             Q=Employee.put(self,request={"Employee_Id": 10})
             self.assertEqual(Q.status_code,400)
    def test_employee_put_status_200(self):
             Q=Employee.put(self,request={"Employee_Id": 10,"Employee_Name": "mall","Employee_Salary": 15000.0,"Employee_Address": {"DoorNO": "01","street": "vellarivelli","country": "India","state": "Tamilnadu"},"Employee_Designation": "Trainee","Is_Delete": False,"Organization_Id": 56})
             self.assertEqual(Q.status_code,200)
    def test_employee_put_status1_400(self):
             Q=Employee.put(self,request=" ")
             self.assertEqual(Q.status_code,400)
    #creating test cases for the patch method
    def test_employee_patch_status_400(self):
             Q=Employee.patch(self,request={"Employee_Id": 11,"Is_Delete":''})
             self.assertEqual(Q.status_code,400)
    def test_employee_patch_status_200(self):
             Q=Employee.patch(self,request={"Employee_Id": 11,"Employee_Name": "mall","Employee_Salary": 15000.0,"Employee_Address": {"DoorNO": "01","street": "vellarivelli","country": "India","state": "Tamilnadu"},"Employee_Designation": "Trainee"})
             self.assertEqual(Q.status_code,200)
    def test_employee_patch_status1_400(self):
             Q=Employee.patch(self,request=' ')
             self.assertEqual(Q.status_code,400)
    # # creating test cases for the delete method
    def test_employee_delete_status_400(self):
             Q=Employee.delete(self,request={})
             self.assertEqual(Q.status_code,400)
    def test_employee_delete_status_200(self):
             Q=Employee.delete(self,request={"Employee_Id":12})
             self.assertEqual(Q.status_code,200)
#creating test cases for Organizational additional operations
class organizationaladditionalTest(TestCase):
    def setUp(self):
        Oraganization_Model.objects.create(Organization_Id=59,Organization_Name= "foyer",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= False)
        Oraganization_Model.objects.create(Organization_Id=60,Organization_Name= "foyer",Organization_Location= "salem",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= False)
        Oraganization_Model.objects.create(Organization_Id=61,Organization_Name= "yoonwoo",Organization_Location= "pune",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
        Oraganization_Model.objects.create(Organization_Id=62,Organization_Name= "ub",Organization_Location= "nashik",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
    # create test cases for list
    def test_organizationaddition_list_400(self):
        org=class_For_Organization.get(self,request={"Organization_Id":59})
        self.assertEqual(org.status_code,400)
    def test_organizationaddition_get_200(self):
        org=class_For_Organization.get(self,request=False)
        self.assertEqual(org.status_code,200)
    #create test cases for filter
    def test_organizationaddition_filter_status_400(self):
        org=class_For_Organization.post(self,request={})
        self.assertEqual(org.status_code,400)
    def test_organizationaddition_filter_status_200(self):
        org=class_For_Organization.post(self,request={"Organization_Name":"foyer","Organization_Location":"chennai"})
        self.assertEqual(org.status_code,200)
    # creating test cases for the serach
    def test_organizationaddition_search_status_400(self):
        org=class_For_Organization.put(self,request={})
        self.assertEqual(org.status_code,400)
    def test_organizationaddition_search_status_200(self):
        org=class_For_Organization.put(self,request={"Organization_Name":"yoonwoo","search":"nashik"})
        self.assertEqual(org.status_code,200)
#create test cases for the Employeeadditional operations
class EmployeeadditionalTest(TestCase):
    def setUp(self):
       Oraganization_Model.objects.create(Organization_Id=58,Organization_Name= "foyer",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
       Oraganization_Model.objects.create(Organization_Id=56,Organization_Name= "ub",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
       Oraganization_Model.objects.create(Organization_Id=57,Organization_Name= "yoonwoo",Organization_Location= "chennai",Organization_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Organization_No_Of_Employee= 13,Organization_Turnover= 100000,Organization_Capitalamount= 50000,Is_Delete= True)
       Employee_Model.objects.create(Employee_Id=12,Employee_Name= "kumar",Employee_Salary= 15000.0,Employee_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Employee_Designation= 'Trainee',Is_Delete= False,Organization_Id=Oraganization_Model.objects.get(Organization_Id=58))
       Employee_Model.objects.create(Employee_Id=11,Employee_Name= "kumar",Employee_Salary= 12000.0,Employee_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Employee_Designation= 'Trainee',Is_Delete= True,Organization_Id=Oraganization_Model.objects.get(Organization_Id=57))
       Employee_Model.objects.create(Employee_Id=10,Employee_Name= "kumar",Employee_Salary= 10000.0,Employee_Address= {"No": "23","street": "perundgudi","country": "india","state": "Tamilnadu"},Employee_Designation= 'Trainee',Is_Delete= True,Organization_Id=Oraganization_Model.objects.get(Organization_Id=56))
    # Creating test cases for list api
    def test_employeeadditional_status_list_400(self):
        emp=class_For_Employee.get(self,request={})
        self.assertEqual(emp.status_code,400)
    def test_employeeadditional__list_status_200(self):
        data=False
        emp=class_For_Employee.get(self,request=data)
        self.assertEqual(emp.status_code,200)
    # Creating test cases for the Fiter api
    def test_employeeadditional_Filter_status_400(self):
        emp=class_For_Employee.post(self,request={})
        self.assertEqual(emp.status_code,400)
    def test_employeeadditional_Filter_status_200(self):
        emp=class_For_Employee.post(self,request={"Organization_Name":"foyer","Employee_Salary":[0,15000]})
        self.assertEqual(emp.status_code,200)
    # Creating test cases for the search api
    def test_employeeadditional_search_status_200(self):
        emp=class_For_Employee.put(self,request={"Employee_Name":"Ravikumar","search":"pune"})
        self.assertEqual(emp.status_code,200)
    def test_employeeadditional_search_status_400(self):
        emp=class_For_Employee.put(self,request={})
        self.assertEqual(emp.status_code,400)

    


    
    
        




    
    




    
    



    

    

    
