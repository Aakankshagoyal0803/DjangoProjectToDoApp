from django.contrib import admin
from .models import todo,done
class doneadmin(admin.ModelAdmin):
    list_dispaly=['title']
class todoadmin(admin.ModelAdmin):
    list_display=['title','due_date','done']
    list_display_links=['title']
    list_editable=['done']
admin.site.register(todo,todoadmin)
# Register your models here.
