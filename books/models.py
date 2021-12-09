from django.db import models
from uuid import uuid4

# Create your models here.
class Books(models.Model):
    id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=255, null=False)    
    author = models.char_field(max_length=255, null=False)
    release_year = models.IntegerField()
    stete = models.CharField(max_length=50)
    pages = models.IntegerField()
    publishing_company = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)    
