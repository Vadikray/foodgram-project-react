from django.contrib import admin
from django.contrib.admin import register

from .models import User
from users.models import Follow


admin.site.unregister(User)


@register(User)
class UserAdmin(admin.ModelAdmin):
    """Настройки админ панели для модели Пользователей"""

    list_display = ('id', 'first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser')


admin.site.register(Follow)
