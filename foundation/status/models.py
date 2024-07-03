from django.db import models

class statuss(models.Model):
    status_name = models.CharField(max_length=200)
    client = models.ForeignKey('clients.Client',null = True,on_delete= models.SET_NULL,blank=True)
    progress = models.CharField(max_length=200)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status_name