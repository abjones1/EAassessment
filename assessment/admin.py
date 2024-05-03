from django.contrib import admin
from .models import User, Recipient, Response, Assessment, Question

# Register your models here.
admin.site.register(User)
admin.site.register(Recipient)
admin.site.register(Response)
admin.site.register(Assessment)
admin.site.register(Question)