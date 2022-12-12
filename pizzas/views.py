from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')



def pizzas(request): # two types of requests 'Get' and 'Post'
    
    pizzas = Pizza.objects.all()
    
    context = {'available_pizzas': pizzas}  # (1) KEY IS THE VARIABLE NAME YOU WILL USE IN THE HTML FILE 
                                            # (2) VALUE IS THE VARIABLE NAME THAT YOU'RE USING IN YOUR VIEW  
    
    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    p = Pizza.objects.get(id=pizza_id)
    
    comments = Comment.objects.filter(pizza=p)

    toppings = Topping.objects.filter(pizza=p) #'topic=' because of the foreign key in the entry model

    id=pizza_id

    if (id==1):
        var_url = 'Buffalo-Chicken-2.jpg'
    if (id==2):
        var_url = 'Zealot.jpg'
    if (id==3):
        var_url = 'PMC2.jpg'
    if (id==4):
        var_url = 'SweetRevenge.jpg'
    if (id==5):
        var_url = 'Loaded-Notato-2.jpg'
    if (id==6):
        var_url = 'Pineapple-Express.jpg'

    new_url= "https://zalatpizza.com/wp-content/uploads/2022/06/" + var_url


    context = {'pizza': p, 'toppings': toppings, 'url':new_url, 'comment':comments}

    return render(request, 'pizzas/pizza.html', context)
    

def customer_comment(request, pizza_id):    
    pizza = Pizza.objects.get(id=pizza_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            customer_comment = form.save(commit=False)
            customer_comment.pizza = pizza
            customer_comment.save()

            return redirect('pizzas:pizza', pizza_id=pizza_id)

    context = {'form':form, 'pizza':pizza}

    return render(request, 'pizzas/customer_comment.html', context)


