from django.contrib import admin

from . import models

admin.site.register(models.Category)
admin.site.register(models.Tag)


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    fields = [
        models.Item.is_published.field.name,
        models.Item.name.field.name,
        models.Item.category.field.name,
        models.Item.tags.field.name,
        models.Item.text.field.name,
    ]
    list_display = (
        models.Item.name.field.name,
        models.Item.is_published.field.name,
    )
    list_editable = (models.Item.is_published.field.name,)
    list_display_links = (models.Item.name.field.name,)
    filter_horizontal = (models.Item.tags.field.name,)
