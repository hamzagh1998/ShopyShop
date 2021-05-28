from django.db import models

def uploadLocation(instance, filename):
    return f"product/{instance.name}/{filename}"

categories = (
                ("technologies", "technologies"), ("clothes", "clothes"),
                ("books", "books"), ("accessoires", "accessoires"),
                ("other", "other"),
             )

class Product(models.Model):
    owner = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    category = models.CharField(max_length=100, choices=categories)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(default="media/default.jpg", upload_to=uploadLocation, blank=True, null=True)
    price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def summary(self):
        return self.description[:50]

    @property
    def imageURL(self):
        try:
            path = self.image.url
        except:
            try:
                path = "media/default.jpg"
            except:
                path = ""
        return path

    def __str__(self):
        return f"{self.name} - ${self.price}"

class ShippingAddress(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    phone = models.CharField(max_length=8, blank=False, null=False)
    address = models.CharField(max_length=250, blank=False, null=False)
    city = models.CharField(max_length=250, blank=False, null=False)
    state = models.CharField(max_length=250, blank=False, null=False)
    zipcode = models.IntegerField(blank=True, null=True)
    shipped = models.BooleanField(default=False)
    date_submit = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.address} - {self.phone}"

class OrderItem(models.Model):
    shippingaddress = models.ForeignKey(ShippingAddress, blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    date_orderd = models.DateTimeField(auto_now_add=True)

    @property
    def getTotal(self):
        return round(self.product.price * self.quantity, 2)

    def __str__(self):
        return f"Product: {self.product.name} - Quantity: {self.quantity} - Total: ${self.getTotal}"
