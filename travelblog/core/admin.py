from django.contrib import admin
from core.models import BlogPosts,Contacts,User

#For configuration of Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display =('id','title','created_at')
    search_fields =('title',)
    list_filter =('category',)
    list_per_page = 10



class ContactAdmin(admin.ModelAdmin):
    list_display =('id','name','created_on')
    search_fields =('subject',)
    list_per_page = 10
# Register your models here.


admin.site.register(BlogPosts,CategoryAdmin)
admin.site.register(Contacts,ContactAdmin)
admin.site.register(User)
