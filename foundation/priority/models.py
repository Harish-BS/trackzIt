from django.db import models

class priority(models.Model):
    priority_name = models.CharField(max_length=400)
    designation_id = models.ForeignKey('clients.Designation', on_delete=models.CASCADE)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.priority_name