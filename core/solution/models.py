from django.db import models

class solution(models.Model):
    solution_name = models.CharField(max_length=200)
    client = models.ForeignKey('clients.Client',on_delete=models.CASCADE)
    project_id = models.ForeignKey('core.Project',on_delete=models.CASCADE)
    solution_description = models.CharField(max_length=500)
    created_by = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.solution_name