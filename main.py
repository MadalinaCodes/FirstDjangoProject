"""
https://docs.djangoproject.com/en/4.2/topics/install/
https://docs.djangoproject.com/en/4.2/intro/tutorial01/
https://docs.djangoproject.com/en/4.2/intro/tutorial02/
https://docs.djangoproject.com/en/4.2/intro/tutorial03/
"""

"""
Tu10:42
care e ordinea comenzilor in terminal?
Corneliu Mihai Gherman10:48
abia acum am vazut Madalina
:)
python manage.py makemigrations backend
python manage.py sqlmigrate backend 0002
python manage.py migrate
Bogdan s10:51
class Order(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    products = models.ManyToManyField(Product, through='OrderItem')
    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default
"""