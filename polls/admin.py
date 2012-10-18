from django.contrib import admin
from polls.models import Poll

# admin.site.register(Poll) #Replaced by below code
class PollAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question']

admin.site.register(Poll, PollAdmin)