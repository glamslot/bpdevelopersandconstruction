from django.contrib import admin
from .models import Property,Agent,pub_mail
# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('name', 'prop_type', 'image_tag','price')
    # list_display_links = ('id', 'title')
    list_filter = ('name',)
    # list_editable = ('is_published',)
    # list_per_page = 25
    # search_fields = ('title', 'description_1', 'description_2', 'description_3', 'list_date')

class AgentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone_no', 'image_tag')
    list_filter = ('name',)
class Pub_mailAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','subject')
    list_filter = ('name','email','subject')

admin.site.register(Property,PropertyAdmin)
admin.site.register(Agent,AgentAdmin)
admin.site.register(pub_mail,Pub_mailAdmin)
