from django.db import models

# Create your models here.
class product(models.Model):
    id = models.AutoField
    Product_name = models.CharField(max_length=20)
    Product_desc = models.CharField(max_length=300)
    Product_category= models.CharField(max_length=20,default="")
    Product_price = models.IntegerField(default=0)
    Launch_date = models.DateField()
    Product_image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.Product_name
    
