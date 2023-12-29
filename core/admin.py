from django.contrib import admin
from .models import UserModel, Links


admin.site.register([UserModel, Links])