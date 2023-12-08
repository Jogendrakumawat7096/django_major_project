from django.db import models

class Signup(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    mobile = models.PositiveBigIntegerField()
    address =models.TextField()
    password = models.CharField(max_length=150)
    image = models.ImageField(upload_to='profile_image/')
    user_type=models.CharField(max_length=100,default="buyer")

    
    def __str__(self):
        return self.name

class Product(models.Model):
    Category=(
        ("Men","Men"),
        ("Women","Women"),
        ("kids","kids"),
    )
    Brand=(
        ("luvis","luvis"),
        ("Diesel","Diesel"),
        ("polo","polo"),
    )
    Size=(
        ("s","s"),
        ("l","l"),
        ("xl","xl"),
        ("xxl","xxl"),
    )
    seller=models.ForeignKey(Signup,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=150)
    product_price=models.PositiveIntegerField()
    product_category=models.CharField(max_length=100,choices=Category)
    product_brand=models.CharField(max_length=100,choices=Brand)
    product_size=models.CharField(max_length=100,choices=Size)
    product_desc=models.TextField()
    product_fimage=models.ImageField(upload_to="product_image/")
    product_bimage=models.ImageField(upload_to="product_image/")
    
    def __str__(self):
        return self.seller.name+"-"+self.product_name
    