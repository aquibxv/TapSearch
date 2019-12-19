from django.db import models

# Create your models here.
class PDF(models.Model):
    name = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='pdf')


    def _str_(self):
        return self.name