from django.db import models

class Task(models.Model):
    task_name = models.CharField(max_length=255)
    task_description = models.CharField(max_length=1000)
    client_id =  models.ForeignKey('clients.Client',null = True,on_delete= models.SET_NULL,blank=True)
    project_id = models.ForeignKey('core.Project',null = True,on_delete= models.SET_NULL,blank=True)
    solution_id = models.ForeignKey('core.Solution',null = True,on_delete= models.SET_NULL,blank=True)
    feature_id = models.ForeignKey('core.Feature',null = True,on_delete= models.SET_NULL,blank=True)
    usecase_id = models.ForeignKey('core.Usecase',null = True,on_delete= models.SET_NULL,blank=True)
    priority_id = models.ForeignKey('foundation.Priority',null = True,on_delete= models.SET_NULL,blank=True)
    user_id = models.ForeignKey('clients.User',null = True,on_delete= models.SET_NULL,blank=True)
    department_id = models.ForeignKey('clients.Department', null=True, on_delete=models.SET_NULL, blank=True)
    issue_stage_id = models.ForeignKey('foundation.Issue_stage',null = True,on_delete= models.SET_NULL,blank=True)
    issue_source_id = models.ForeignKey('foundation.Issue_source',null = True,on_delete= models.SET_NULL,blank=True)
    issue_type_id = models.ForeignKey('foundation.Issue_type',null = True,on_delete= models.SET_NULL,blank=True)
    complexity_id = models.ForeignKey('foundation.Complexity',null = True,on_delete= models.SET_NULL,blank=True)
    sdlc_id = models.ForeignKey('foundation.SDLC',null = True,on_delete= models.SET_NULL,blank=True)
    status_id = models.ForeignKey('foundation.Statuss',null = True,on_delete= models.SET_NULL,blank=True)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    estd_hrs = models.CharField(max_length=255)
    actual_hrs = models.CharField(max_length=255)
    actual_end_date = models.CharField(max_length=255)
    #designation_id = models.ForeignKey('clients.Designation', null=True, on_delete=models.SET_NULL, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.task_name