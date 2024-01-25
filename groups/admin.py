from django.contrib import admin
from .import models

# Register your models here.
class GroupForm(admin.ModelForm):
    class Meta:
        model = Group
        exclude = ['description']

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember

admin.site.register(models.Group)
