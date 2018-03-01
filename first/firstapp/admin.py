from django.contrib import admin
from .models import Topic, Webpage, AccessRecord,Userprofile

admin.site.register(Userprofile)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
