from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Event)
admin.site.register(Body)
admin.site.register(BodyCategory)
