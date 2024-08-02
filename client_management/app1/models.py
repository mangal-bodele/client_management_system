from django.db import models

class Employee(models.Model):
    PROJECTDOMAIN = [ 'SAAS','Ecommerce', 'CRM', 'ERP', 'Finance']
    STATUS = ['Onboarded' , 'Not Onboarded']
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=50)
    email_id = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=50)
    dateOfJoining = models.DateField()
    status = models.CharField(max_length=50,choices=STATUS)
    projectDomain = models.CharField(max_length=50,choices=PROJECTDOMAIN)

    def __str__(self):
        return self.name
