from django.shortcuts import render, redirect
from django.contrib import messages
from train2.models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as dj_user
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .helpers import send_otp
# Create your views here.

def home(request):
    return render(request,"home.html")





def status(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "status.html")


def search_by_name(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "search_by_name.html")


def search_by_station(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "search_by_station.html")


def booking(request):

    return render(request, "booking.html")
        

def search_booking(request):
    if request.method == "GET":
        start =  request.GET.get('from')
        end = request.GET.get('to')
        params = []
        params2 = []
        params3 = []
        params4 = []
        params5 = []
        dict1 = {}
        dict2 = {}
        # search_train = Train.objects.filter(train_no = number)
        station = Station.objects.all().values().order_by('distance')
        # reaches = Reaches.objects.filter(train_no = number).values()

        station2 = Station.objects.filter(name = start).values()
        station3 = Station.objects.filter(name = end).values()
        station4 = []
        station5 = []
        all_stops = []
        for i in station2:
            station4.append(list(i.values())[0])
        for i in station3:
            station5.append(list(i.values())[0])
        string = "".join([str(item) for item in station4])
        string2 = "".join([str(item) for item in station5])
            
        print(string, string2)
        for stop in station:
            all_stops.append(stop)
        for stop in station:
            if list(stop.values())[0] == string:
                global req1
                dict1.update(stop)
                for stop in station:
                    if list(stop.values())[0] == string2:
                        dict2.update(stop)
                        reaches = Reaches.objects.filter(station_code = string).values()
                        reaches2 = Reaches.objects.filter(station_code = string2).values()
                        for reach in reaches:
                            params2.append(list(reach.values())[1])
                            params3.append(list(reach.values())[3])
                        for reach in reaches2:
                            params4.append(list(reach.values())[3])
                            tr_name = Train.objects.filter(train_no = list(reach.values())[1]).values()
                            for name in tr_name:
                                params5.append(list(name.values())[1])

                # map(lambda x: dict2.update(x) if string2 == x else ... , list(stop.values())[0])
        print(dict1, dict2)
    return render(request, "search_booking.html", {"start": start,"end": end, "train_no": params2, "start_arrival": params3,"end_arrival": params4, "train_name": params5})




def search_status(request):
    if request.user.is_anonymous:
        return redirect("/login")
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
    if request.user.is_anonymous:
        return redirect("/login")
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
    if request.user.is_anonymous:
        return redirect("/login")
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


def contact_us(request):

    if request.method == "POST":
        name =  request.POST.get('name')
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        contact = Contact(name = name, email = email, desc = desc, number = phone, date = datetime.today())
        contact.save()
        messages.success(request, "Profile details updated.")

    return render(request, "contact_us.html")


def loginUser(request):

    if request.method == "POST":
        name =  request.POST.get('name')
        password = request.POST.get("password")
        user = authenticate(username="john", password="secret")
        if user is not None:
        # A backend authenticated the credentials
            login(request, user)
            return redirect("/")
        else:
        # No backend authenticated the credentials
            return render(request, "registration/login.html")
    return render(request, "registration/login.html")


def signupUser(request):
    if request.method == "POST":
        name =  request.POST.get('name')
        password = request.POST.get("password")
        user = dj_user.objects.create_user(username = name, password = password)
        user.save()
    return render(request, "registration/signup.html")


def logoutUser(request):
    logout(request)
    return render(request, "registration/login.html")


def forgot_password(request):
    return render(request, "registration/forgot_password.html")


@api_view(['POST'])
def send_otp(request):
    if request.method == "POST":
        name =  request.POST.get('name')
        number = request.POST.get('phone_number')
        password = request.POST.get("password")
        global otp
        # data = request.data
        # if data.get('phone_number') is None:
        #     return Response({'status': 400,"message": "key phone_number is required"})
        # if data.get('password') is None:
        #     return Response({'status': 400,"message": "key password is required"})
        otp = send_otp(number)

        return Response({
            'status': 200,"message": "otp sent"
        })


@api_view(['POST'])
def verify_otp(request):
    data = request.data
    user = dj_user.objects.get(username= data.get('username'))

    if data.get('phone_number') is None:
        return Response({'status': 400,"message": "key phone_number is required"})
    if data.get('otp') is None:
        return Response({'status': 400,"message": "key otp is required"})
    try:
        user_name = dj_user.objects.get(username = data.request.get('user_name'))
    except Exception as e:
        return Response({'status': 400,"message":'invalid username'})
    if otp == data.get('otp'):
        user.set_password(data.get('set_password'))

        return Response({'status': 200,"message":'otp matched'})
    
    else:
        return Response({'status': 200,"message":'invalid otp'})

