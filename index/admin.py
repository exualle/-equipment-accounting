from django.contrib import admin
from .models import ItemModel, ItemRelationModel

# Register your models here.
admin.site.register(ItemModel)
admin.site.register(ItemRelationModel)
