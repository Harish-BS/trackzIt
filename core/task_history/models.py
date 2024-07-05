from django.db import models

class task_history(models.Model):
    task_id =  models.ForeignKey('core.Task',on_delete=models.CASCADE)
    client_id =  models.ForeignKey('clients.Client',on_delete=models.CASCADE)
    project_id = models.ForeignKey('core.Project',on_delete=models.CASCADE)
    solution_id = models.ForeignKey('core.Solution',on_delete=models.CASCADE)
    feature_id = models.ForeignKey('core.Feature',on_delete=models.CASCADE)
    usecase_id = models.ForeignKey('core.Usecase',on_delete=models.CASCADE)
    priority_id = models.ForeignKey('foundation.Priority',on_delete=models.CASCADE)
    user_id = models.ForeignKey('clients.User',on_delete=models.CASCADE)
    department_id = models.ForeignKey('clients.Department', null=True, on_delete=models.SET_NULL, blank=True)
    issue_stage_id = models.ForeignKey('foundation.Issue_stage',on_delete=models.CASCADE)
    issue_source_id = models.ForeignKey('foundation.Issue_source',on_delete=models.CASCADE)
    issue_type_id = models.ForeignKey('foundation.Issue_type',on_delete=models.CASCADE)
    complexity_id = models.ForeignKey('foundation.Complexity',on_delete=models.CASCADE)
    sdlc_id = models.ForeignKey('foundation.SDLC',on_delete=models.CASCADE)
    status_id = models.ForeignKey('foundation.Statuss',on_delete=models.CASCADE)
    start_date = models.CharField(max_length=255)
    end_date = models.CharField(max_length=255)
    estd_hrs = models.CharField(max_length=255)
    actual_hrs = models.CharField(max_length=255)
    actual_end_date = models.CharField(max_length=255)
    #designation_id = models.ForeignKey('clients.Designation', null=True, on_delete=models.SET_NULL, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.task_id