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

def search(request):
    def reach(**reaches):
        return render(request, "search.html",reaches)
    if request.method == "GET":
        number =  request.GET.get('search_tr_no')
        params = {"searched": number}
        params2 = {}
        search_train = Train.objects.filter(train_no = number)
        reaches = Reaches.objects.filter(train_no = number)

        # for srch in search_train:
        #     train_no = srch.train_no
        #     tname = srch.tname
        #     source = srch.source
        #     destination = srch.destination
        #     arrival_time = srch.arrival_time
        #     dep_time = srch.dep_time
            # avail_seats = srch.avail_seats
            # date =  srch.date
            # params.update({"train_no": train_no, "tname": tname, "source": source, "destination": destination, "arrival_time": arrival_time, "dep_time": dep_time, "avail_seats": avail_seats, "date": date})
        train_no = search_train[0].train_no
        tname = search_train[0].tname
        source = search_train[0].source
        destination = search_train[0].destination
        arrival_time = search_train[0].arrival_time
        dep_time = search_train[0].dep_time
        params.update({"train_no": train_no, "tname": tname, "source": source, "destination": destination, "arrival_time": arrival_time, "dep_time": dep_time})
        for reache in reaches:

            params2.update({"station_code": reache.station_code})
            reach(station_code = reache.station_code)
        return render(request, "search.html", {"params":params,"params2": params2})
