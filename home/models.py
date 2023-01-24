from django.db import models

class TopImages(models.Model):
    
    T_no=models.IntegerField(blank=True)
    T_title=models.CharField(max_length=100)
    # M_=models.CharField(max_length=100) 상품페이지 연결 db
    T_image=models.ImageField(upload_to='images/',blank=True, null=True)
    
    def __str__(self):
        return self.T_title

