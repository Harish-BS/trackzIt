from django.db import models

class feature(models.Model):
    feature_name = models.CharField(max_length=300)
    client = models.ForeignKey('clients.Client',on_delete=models.CASCADE)
    project_id = models.ForeignKey('core.Project',on_delete=models.CASCADE)
    solution_id = models.ForeignKey('core.Solution',on_delete=models.CASCADE)
    feature_description = models.CharField(max_length=300)
    created_by = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=300)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feature_name