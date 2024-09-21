from django.contrib import admin
from .models import ToDo

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_completed', 'created_at')
    list_filter = ('is_completed', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)


admin.site.register(ToDo, ToDoAdmin)
