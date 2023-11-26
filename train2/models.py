from django.db import models
from datetime import datetime

# Create your models here.

class User(models.Model):
    user_id = models.IntegerField(primary_key= True)
    password = models.CharField(max_length= 10)
    fname = models.CharField(max_length=10)
    lname = models.CharField(max_length = 10)
    gender = models.CharField(max_length = 10)
    age = models.IntegerField()
    email = models.EmailField(max_length = 34)
    adhaar = models.IntegerField()
    mobile = models.IntegerField()
    city =  models.CharField(max_length = 11)
    state = models.CharField(max_length = 15)
    pincode = models.IntegerField()
    def __str__(self):
        return self.user_id

# class Passenger(models.Model):
#     name = models.CharField(max_length = 20)
#     gender = models.CharField(max_length = 10)
#     age = models.IntegerField(max_length = 2)
#     pnr =  models.IntegerField(max_length = 10)
#     seat = models.IntegerField(max_length = 2)
#     booked_by = models.CharField(max_length = 11)
#     reservation_atatus = models.CharField(max_length = 11)

class Train(models.Model):
    train_no = models.IntegerField(primary_key = True)
    tname = models.CharField(max_length= 20)
    source = models.CharField(max_length= 20)
    destination = models.CharField(max_length= 20)
    arrival_time = models.TimeField()
    dep_time = models.TimeField()
    avail_seats = models.CharField(max_length = 10)
    date =  models.DateField()
    def __str__(self):
        return self.tname

class Station(models.Model):
    station_code = models.CharField(primary_key = True, max_length= 10)
    name = models.CharField(max_length = 20)
    hault = models.IntegerField()
    train_no = models.ForeignKey(Train, on_delete= models.SET_NULL, null=True)
    distance = models.IntegerField()
    def __str__(self):
        return self.name

class Train_status(models.Model):
    train_no = models.ForeignKey(Train, primary_key = True, on_delete= models.CASCADE)
    a_seats1 = models.IntegerField()
    a_seats2 = models.IntegerField()
    a_seats3 = models.IntegerField()
    b_seats1 = models.IntegerField()
    b_seats2 = models.IntegerField()
    b_seats3 = models.IntegerField()
    w_seats1 = models.IntegerField()
    w_seats2 = models.IntegerField()
    w_seats3 = models.IntegerField()
    flare1 = models.FloatField(max_length = 11)
    flare2 = models.FloatField(max_length = 11)
    def __str__(self):
        return self.train_no

class Ticket(models.Model):
    ticket_id = models.IntegerField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    status = models.CharField(max_length = 11)
    no_of_passenger = models.IntegerField()
    train_no = models.ForeignKey(Train, on_delete= models.SET_NULL, null=True)
    def __str__(self):
        return self.ticket_id

class Passenger(models.Model):
    passenger_id = models.IntegerField(primary_key = True)
    pnr = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length = 11)
    user_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    reservation_status = models.CharField(max_length = 20)
    seat_no = models.IntegerField()
    name = models.CharField(max_length = 20)
    ticket_id = models.ForeignKey(Train, on_delete= models.SET_NULL, null=True)
    def __str__(self):
        return self.passenger_id

class Starts(models.Model):
    train_no = models.ForeignKey(Train, primary_key= True, on_delete= models.CASCADE)
    station_code = models.ForeignKey(Station, on_delete= models.SET_NULL, null=True)
    def __str__(self):
        return self.station_code

class Stops_at(models.Model):
    train_no = models.ForeignKey(Train, on_delete= models.SET_NULL, null=True)
    station_code = models.ForeignKey(Station, on_delete= models.SET_NULL, null=True)
    def __str__(self):
        return self.station_code

class Reaches(models.Model):
    train_no = models.ForeignKey(Train, on_delete= models.SET_NULL, null=True)
    station_code = models.ForeignKey(Station, on_delete= models.SET_NULL, null=True)
    arrival_time = models.TimeField(null=True,blank=True)
    dep_time = models.TimeField(null= True, blank= True)
    time = models.DurationField()


class Books(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    ticket_id = models.ForeignKey(Ticket, on_delete= models.SET_NULL, null=True)
    def __str__(self):
        return self.ticket_id

class Cancel(models.Model):
    user_id = models.ForeignKey(User, on_delete= models.SET_NULL, null=True)
    ticket_id = models.ForeignKey(Ticket, on_delete= models.SET_NULL, null=True)
    passenger_id = models.ForeignKey(Passenger, on_delete= models.SET_NULL, null=True)
    def __str__(self):
        return self.passenger_id
class Contact(models.Model):
    name = models.CharField(max_length = 25)
    email = models.EmailField(max_length = 25)
    number = models.CharField(max_length = 10)
    desc = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name