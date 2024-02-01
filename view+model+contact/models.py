from django.db import models

# Create your models here.
class contact_file(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email = models.EmailField(max_length=60, unique=True)
    subject=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    country=models.CharField(max_length=20)
    message=models.TextField()
    
    def __str__(self):
        return str(self.id)+"-"+self.name+self.lastname+"-"+self.phone+"-"+self.country
    