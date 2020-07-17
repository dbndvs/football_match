from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(REG)
admin.site.register(fixture)
admin.site.site_url="/adm"