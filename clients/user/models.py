from django.db import models
#from clients.user.models import User
#from clients.designation.models import Designation
#from clients.department.models import Department
class User(models.Model):
    user_name = models.CharField(max_length=255)
    created_by = models.CharField(max_length=100)
    client_id =  models.ForeignKey('clients.User',null = True,on_delete= models.SET_NULL,blank=True)
    #department_id = models.ForeignKey(Department,null = True,on_delete= models.SET_NULL,blank=True)
    #designation_id = models.ForeignKey(Designation,null = True,on_delete= models.SET_NULL,blank=True)
    department_id = models.ForeignKey('clients.Department', null=True, on_delete=models.SET_NULL, blank=True)
    designation_id = models.ForeignKey('clients.Designation', null=True, on_delete=models.SET_NULL, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user_name