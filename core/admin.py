from django.contrib import admin
from . models import *

@admin.register(produto)
class produtoadmin(admin.ModelAdmin):
    list_display=('nome','preço','estoque','slug','criado','modificado','ativo')

