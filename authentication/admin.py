from django.contrib import admin
from .models import *

# Register your models here.
UserModels = [UserInformation] # User,
admin.site.register(UserModels)
RoleModels = [PermissionInRole, Permission] # Role,
admin.site.register(RoleModels)

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_name','id']

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','role',]


# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
    # list_display = ['title','status', 'approved', 'author','publish','slug']
    # ordering = ['approved', 'title']
    # list_filter = ['status','publish' ,'author']
    # search_fields = ['title']
    # raw_id_fields = ['author']
    # date_hierarchy = 'publish'
    # prepopulated_fields = {'slug':('title',)}
    # list_editable = ['status']
    # list_display_links = ['author','title']