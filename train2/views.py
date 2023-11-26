from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.contrib import messages
from train2.models import *

# Create your views here.

def home(request):
    return render(request,"home.html")
def booking(request):
    return render(request, "booking.html")
def status(request):
    return render(request, "status.html")

def search_by_name(request):
    return render(request, "search_by_name.html")

def search_by_station(request):
    return render(request, "search_by_station.html")

def search_status(request):
    def reach(**reaches):
        return render(request, "search.html",reaches)
    if request.method == "GET":
        number =  request.GET.get('search_tr_no')
        params = {"searched": number}
        params2 = []
        params3 = []
        params4 = []

        search_train = Train.objects.filter(train_no = number)
        station = Station.objects.filter(train_no = number).values().order_by('distance')
        reaches = Reaches.objects.filter(train_no = number).values()
        for station in station:
            for reache in reaches:
                if list(station.values())[0] == list(reache.values())[2]:

                    li = Station.objects.filter(station_code = list(reache.values())[2]).order_by('distance')
                    for x in li:
                        params2.append(x.name)
                    li2 = list(reache.values())[3]
                    li3 = list(reache.values())[4]
                    params3.append(li2)
                    params4.append(li3)

        train_no = search_train[0].train_no
        tname = search_train[0].tname
        source = search_train[0].source
        destination = search_train[0].destination
        arrival_time = search_train[0].arrival_time
        dep_time = search_train[0].dep_time

        params.update({"train_no": train_no, "tname": tname, "source": source, "destination": destination, "arrival_time": arrival_time, "dep_time": dep_time})


        return render(request, "search_status.html", {"params":params, "params2": params2, "params3": params3, "params4": params4})
def search_train(request):
    number =  request.GET.get('search_tr_no')
    params = {"searched": number}
    params2 = []
    params3 = []
    params4 = []
    params5 = []
    params6 = []

    search_train = Train.objects.filter(train_no = number)
    reaches = Reaches.objects.filter(train_no = number).values().order_by('arrival_time')
    station = Station.objects.filter(train_no = number).values().order_by('distance')
    for station in station:
        params5.append(list(station.values())[0])
        params6.append(list(station.values())[4])
        for reache in reaches:
            if list(station.values())[0] == list(reache.values())[2]:
                li = Station.objects.filter(station_code = list(reache.values())[2]).order_by('distance')
                for x in li:
                    params2.append(x.name)
                li2 = list(reache.values())[3]
                li3 = list(reache.values())[4]
                params3.append(li2)
                params4.append(li3)

    train_no = search_train[0].train_no
    tname = search_train[0].tname
    source = search_train[0].source
    destination = search_train[0].destination
    arrival_time = search_train[0].arrival_time
    dep_time = search_train[0].dep_time
    station = Station.objects.filter(name = source).order_by('distance').values()
    for source_code in station:
            source_code = list(source_code.values())[0]
    station = Station.objects.filter(name = destination).order_by('distance').values()
    for destination_code in station:
            destination_code = list(destination_code.values())[0]
    params.update({"train_no": train_no, "tname": tname, "source": source, "destination": destination, "arrival_time": arrival_time, "dep_time": dep_time, "source_code": source_code, "destination_code": destination_code})

    return render(request, "search_train.html", {"params":params, "params2": params2, "params3": params3, "params4": params4,"station_code": params5, "distance": params6})

def search_station(request):
    code =  request.GET.get('search_station')
    reaches = Reaches.objects.filter(station_code = code).values()
    train_num = []
    train_name = []
    arrival_time = []
    dep_time = []
    source = []
    destination = []
    for details in reaches:
        li = list(details.values())[1]
        train = Train.objects.filter(train_no = list(details.values())[1]).values()
        for det in train:
            li2 = list(det.values())[1]
            li5 = list(det.values())[2]
            li6 = list(det.values())[3]
        li3 = list(details.values())[3]
        li4 = list(details.values())[4]
        train_num.append(li)
        train_name.append(li2)
        arrival_time.append(li3)
        dep_time.append(li4)
        source.append(li5)
        destination.append(li6)
    return render(request, "search_station.html", {"train_number": train_num, "train_name": train_name, "arrival_time": arrival_time, "dep_time": dep_time, "searched": code, "source": source, "destination": destination})
def contact(request):
    if request.method == "POST":
        name =  request.POST.get('name')
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name = name, email = email, desc = desc, number = phone, date = datetime.today())
        contact.save()
        # messages.success(request, "Profile details updated.")

    return render(request, "contact.html")