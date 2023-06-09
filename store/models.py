from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class CustomerModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)   #a user can only have a customer and a customer canonly have a user
    name = models.CharField(max_length=50, null=True)
    surname = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)

    def __str__(self):
        return self.name


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class ProductModel(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    numberOfLikes = models.IntegerField(default=0)



    def __str__(self):
        return self.name

    @property
    def imageURL(self):   #senza questa funzione se ci fosse un prodotto senza immagine darebbe errore a tutta la pagina
        try:
            url = self.image.url
        except:
            url = ''
        return url


class OrderModel(models.Model):
    customer = models.ForeignKey(CustomerModel, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=5, null=True)


    def __str__(self):
        return str(self.id)

    def calculate_cart_total(self):
        orderitems = self.orderitemmodel_set.all()
        total = sum([item.calculate_total for item in orderitems])
        return total

    def calculate_cart_items(self):
        orderitems = self.orderitemmodel_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

    def get_ordered_products(self):
        order_items = self.orderitemmodel_set.all()
        products = [item.product for item in order_items]
        return products


class OrderItemModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(OrderModel, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def calculate_total(self):
        total = self.product.price * self.quantity
        return total


class CheckOutModel(models.Model):
    name = models.CharField(max_length=20, default='')
    #name = models.ForeignKey(CustomerModel, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(OrderModel, on_delete=models.SET_NULL, null=True, blank=True)
    surname = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    postalCode = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class LikedProducts(models.Model):
    productId = models.CharField(max_length=50)
    username = models.CharField(max_length=300)

    def __str__(self):
        return self.username


class Review(models.Model):
    CHOICES = [
        ('0', 'Zero stelle'),
        ('1', 'Una stella'),
        ('2', 'Due stelle'),
        ('3', 'Tre stelle'),
        ('4', 'Quattro stelle'),
        ('5', 'Cinque stelle'),
    ]
    customer = models.ForeignKey(CustomerModel, on_delete=models.CASCADE)
    date_added = models.DateField(auto_now_add=True)
    product = models.ForeignKey(ProductModel, related_name="reviews", on_delete=models.CASCADE)
    content = models.TextField(max_length=300)
    rating = models.CharField(max_length= 20, choices=CHOICES, default= 'star0')

    def __str__(self):
        return '%s - %s' % (self.product.name, self.customer.name)

