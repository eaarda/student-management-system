from django.db import models


class BaseModel(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False, unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)