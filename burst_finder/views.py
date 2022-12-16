from django.forms import ValidationError
from django.shortcuts import render, redirect
from .models import XRayDataModel, BurstModel
import random
import json
# Create your views here.
def get_plot_data():
    data = ""
    for _ in range(100):
        data+=str(round(random.random()*100 , 3))+"/"
    data = data.rstrip(data[-1])
    return data
def get_bursts(x_ray_file):
    no_of_bursts = (int)(random.random()*10 )+1
    print(no_of_bursts)
    for i in range(no_of_bursts):
        start_time = round(random.random()*1,3)
        end_time = round(random.random()*1,3)
        time_of_occurence = round(random.random()*100 , 3)
        type_of_burst = random.choice(["Type 1", "Type 2", "Type 3"])
        burst = BurstModel.objects.create(
            rise_time = start_time,
            decay_time = end_time, 
            time_of_occurence = time_of_occurence, 
            type_of_burst = type_of_burst)
        x_ray_file.bursts.add(burst)

def home_view(request):
    
    return render(request, 'home.html')
def file_details_view(request, id):
    print(id)
    x_ray_file = XRayDataModel.objects.get(pk = id)
    plot_data = x_ray_file.plot_data.split('/')
    print(x_ray_file.bursts)
    plot_numbers = [float(st) for st in plot_data]
    burst_list = x_ray_file.bursts.all()
    plot_numbers_array = json.dumps(plot_numbers)
    
   # print(burst_list[0])
    return render(request,'details.html' , context={
        "plot_data" : plot_numbers_array,
        "file": x_ray_file,
        "bursts" : burst_list
    })
def file_add_view(request):
    if(request.method == 'POST'):
        form_data = request.POST
        #print(form_data["x-ray-data"].split('.'))
        
        if(form_data["x-ray-data"].split('.')[-1] == "fits" or form_data["x-ray-data"].split('.')[-1] == "ascii"):
            x_ray_file = XRayDataModel.objects.create(
            file_name  = form_data["x-ray-data"],
            plot_data = get_plot_data(),
        )
            get_bursts(x_ray_file=x_ray_file)

            return redirect('file_details' , id = x_ray_file.id)
        else:
            raise(ValidationError("incorrect file"))
            
    return render(request, "add_file.html")
def dashboard_view(request):
    files = XRayDataModel.objects.all()

    return render(request, 'dashboard.html', context = {'files' : files})
    
