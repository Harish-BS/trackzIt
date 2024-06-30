from django.db import models
#from clients.user.models import User
class Department(models.Model):
    department_name = models.CharField(max_length=255)
    client_id = models.ForeignKey('clients.User', null=True, on_delete=models.SET_NULL, blank=True)
    #client_id =  models.ForeignKey(User,null = True,on_delete= models.SET_NULL,blank=True)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.department_name