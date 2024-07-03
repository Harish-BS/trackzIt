from django.db import models

class feature(models.Model):
    feature_name = models.CharField(max_length=300)
    client = models.ForeignKey('clients.Client',null = True,on_delete= models.SET_NULL,blank=True)
    project_id = models.ForeignKey('core.Project',null = True,on_delete= models.SET_NULL,blank=True)
    solution_id = models.ForeignKey('core.Solution',null = True,on_delete= models.SET_NULL,blank=True)
    feature_description = models.CharField(max_length=300)
    created_by = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feature_name