from django.contrib import admin
from member.models import Member

@admin.register(Member)
class Member(admin.ModelAdmin):
    list_display = ['M_id', 'M_pw']