from django.db import models

# Create your models here.
class product(models.Model):
    ProductId = models.AutoField
    Product_name = models.CharField(max_length=20)
    product_desc = models.CharField(max_length=300)
    product_price = models.IntegerField()
    launch_date = models.DateField()
    product_image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.Product_name
    
