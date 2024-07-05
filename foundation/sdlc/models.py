from django.db import models

class SDLC(models.Model):
    SDLC_name = models.CharField(max_length=400)
    client = models.ForeignKey('clients.Client',on_delete=models.CASCADE)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.SDLC_name