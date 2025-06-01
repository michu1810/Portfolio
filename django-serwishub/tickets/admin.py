from django.contrib import admin
from tickets.models import Ticket
from users.models import CustomUser


admin.site.register(Ticket)
admin.site.register(CustomUser)