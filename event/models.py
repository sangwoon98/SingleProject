from datetime import datetime
from django.db import models


class E_board(models.Model):
    E_no=models.AutoField(primary_key=True)
    E_event_no=models.IntegerField(blank=True)
    E_progress=models.CharField(max_length=20)
    E_title=models.CharField(max_length=100)
    E_content=models.CharField(max_length=2000)
    E_start_day=models.CharField(max_length=50)
    E_end_day=models.CharField(max_length=50)
    E_image=models.ImageField(upload_to='images/',blank=True, null=True)
    E_image02=models.ImageField(upload_to='images/',blank=True, null=True)

    
    def __str__(self):
        return self.E_title
    

class R_board(models.Model):
    R_no=models.AutoField(primary_key=True)
    R_e_no=models.IntegerField()
    R_writer=models.CharField(max_length=100)
    R_content=models.CharField(max_length=1000)
    R_createdate =models.DateTimeField(default=datetime.now(),blank=True)
    
    def __str__(self):
        return self.R_writer
