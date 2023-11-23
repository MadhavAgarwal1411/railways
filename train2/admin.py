from django.contrib import admin
import train2.models as md
# Register your models here.

admin.site.register(md.User)
admin.site.register(md.Train)
admin.site.register(md.Station)
admin.site.register(md.Train_status)
admin.site.register(md.Ticket)
admin.site.register(md.Passenger)
admin.site.register(md.Starts)
admin.site.register(md.Stops_at)
admin.site.register(md.Reaches)
admin.site.register(md.Books)
admin.site.register(md.Cancel)