from django.db import models

class Member(models.Model):
    M_name=models.CharField(max_length=100)
    M_id=models.CharField(primary_key=True,max_length=100)
    M_pw=models.CharField(max_length=100)
    M_email=models.EmailField(max_length=128)
    M_email_check=models.BooleanField()
    M_address=models.CharField(max_length=100)
    M_sms=models.CharField(max_length=100)
    M_sms_check=models.BooleanField()
    M_date_of_birth=models.CharField(max_length=10)
    
    
    def __str__(self):
        return self.M_id