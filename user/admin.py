from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.
from .models import Course,Profile

# admin.site.register(Student)
# admin.site.register(Tutor)
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = True
    verbose_name_plural = Profile

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline, )

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Course)
