from django.contrib import admin
from .models import M_USER, M_USER_FRIENDS

# Register your models here.
admin.site.register(M_USER)
admin.site.register(M_USER_FRIENDS)
