from django.db import models
from django.utils import timezone

class Document(models.Model):
    filename = models.CharField(max_length=255, default=timezone.now())
    document = models.FileField(upload_to='g4emma_admin_documents/')
    desc = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    last_mod_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.filename
