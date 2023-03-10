from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# import random
# import numpy as np

def index(request):
    print('Request for index page received')
    return render(request, 'hello_azure/index.html')

@csrf_exempt
def hello(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        
        if name is None or name == '':
            print("Request for hello page received with no name or blank name -- redirecting")
            return redirect('index')
        else:
            print("Request for hello page received with name=%s" % name)
            context = {
                'name': name,
                # 'random' : random.randint(1,100),
                # 'seed' : np.random.default_rng(2021).random(4)[1]
                }
            return render(request, 'hello_azure/hello.html', context)
    else:
        return redirect('index')