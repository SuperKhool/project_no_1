from django.db import models 
from django.contrib.auth.models import User

# Create your models here.

class catagory(models.Model):
    name =models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class products(models.Model):
    prod_name=models.CharField( max_length=50)
    prod_img=models.ImageField(upload_to='product_image')
    old_price=models.PositiveIntegerField()
    new_price=models.PositiveIntegerField()
    catagoty=models.ForeignKey(catagory,on_delete=models.CASCADE)
    description=models.TextField(max_length=9000)
    def __str__(self):
        return self.prod_name
    

class cart(models.Model):

    user=models.ForeignKey(User, on_delete=models.CASCADE)
    prod=models.ForeignKey(products, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user.username