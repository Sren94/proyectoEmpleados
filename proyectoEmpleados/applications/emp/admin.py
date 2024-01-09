from django.contrib import admin
from .models import employee,skills
# Register your models here.


class employeeAdmin(admin.ModelAdmin):
    list_display = (
        'firstName',
        'lastName',
        'email',
        'job',
        'dep',
        'fullName',)
    def fullName(self,obj):
        print(obj)
        return obj.firstName
    search_fields=('lastName',)
    list_filter=('dep','job')
    filter_horizontal=('skill',)
class skillAdmin(admin.ModelAdmin):
    list_display = ('skill',)
admin.site.register(employee,employeeAdmin)
admin.site.register(skills,skillAdmin)