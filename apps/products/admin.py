from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    model = Item

    fieldsets = (
        ('Information', {
            'fields': (
                'name',
                'description',
                'price',
                'img',
            )
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': (
                'wide',
            ),
            'fields': (
                'name',
                'price',
            ),
        }),
    )

    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
        'price',
        'img',
    )
    ordering = (
        'name',
    )


admin.site.register(Item, ItemAdmin)

