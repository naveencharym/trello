from django.contrib import admin
from .models import Board
from .models import task,card
admin.site.register(Board);
admin.site.register(task)
admin.site.register(card)
# Register your models here.
