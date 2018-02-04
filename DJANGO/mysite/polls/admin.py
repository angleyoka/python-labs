from django.contrib import admin
from .models import Question
# Register your models here.
admin.site.register(Question)

class MyModelAdmin(admin.ModelAdmin):
    

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions
