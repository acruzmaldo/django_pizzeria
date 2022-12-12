from django.db import models

'''
To save changes to database you have to
  (1) Save the file (usually models.py and settings.py)
  (2) Type 'py manage.py makemigrations' in the terminal
  (3) Type 'py manage.py migrate' in the terminal
'''


# Create your models here.
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=50)

    def __str__(self):
        return self.pizza_name


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.topping_name


class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
    
    def __str__(self):
        return self.comment

