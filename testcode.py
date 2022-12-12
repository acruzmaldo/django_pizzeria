import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Pizzeria.settings")

import django 
django.setup()


from pizzas.models import *

pizzas = Pizza.objects.all() # SQL equivalent: topics = select * from Topic

print(pizzas)

for p in pizzas:
    print(p)

'''
https://zalatpizza.com/wp-content/uploads/2022/06/Zealot.jpg
https://zalatpizza.com/wp-content/uploads/2022/06/PMC2.jpg
https://zalatpizza.com/wp-content/uploads/2022/06/SweetRevenge.jpg
https://zalatpizza.com/wp-content/uploads/2022/06/Loaded-Notato-2.jpg
https://zalatpizza.com/wp-content/uploads/2022/06/Pineapple-Express.jpg
https://zalatpizza.com/wp-content/uploads/2022/06/Buffalo-Chicken-2.jpg
'''