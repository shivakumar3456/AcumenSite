from django.contrib import admin
from .models import Profile,Event,EventDetails,Organizer,Team
admin.site.register(Profile)
admin.site.register(Organizer)
admin.site.register(Event)
admin.site.register(EventDetails)
# Register your models here.
