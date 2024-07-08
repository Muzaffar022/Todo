from django.contrib import admin

from django.contrib import admin
from to_do.models import ToDo
import requests


def send_tasks_to_telegram(self, request, queryset):
    for todo in queryset:
        text = f'{todo.id}. {todo.name}\n'
        text += f'Description: {todo.description}\n'
        text += f"Status: {todo.status}"
        TOKEN = "7309689830:AAHj71Z6-FgsdjJxJVWdiXYCgOKokyaUUso"
        CHAT_ID = 996198101

        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={text}"

        requests.get(url)


send_tasks_to_telegram.short_description = "Telegramga yuborish"


@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')
    search_fields = ("name",)
    list_filter = ("status",)

    actions = (send_tasks_to_telegram,)
