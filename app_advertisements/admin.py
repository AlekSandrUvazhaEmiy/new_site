from django.contrib import admin
from .models import Advertisements

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'created_date', 'updatet_at', 'auction']

    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_True']

    fieldsets = (
        (
            'общее',
            (
                {
                    'fields': ('title', 'description')
                }
            )
        ),
        (
            "финансыф",
            (
                {
                    'fields': ('auction', 'price'),
                    'classes': ['collapse']
                }
            )
        ),
    )

    @admin.action(description='убрать торг')
    def make_auction_as_false(self, requests, queryset):
        queryset.update(auction = False)

    @admin.action(description='сделать торг')
    def make_auction_as_True(self, requests, queryset):
        queryset.update(auction = True)

admin.site.register(Advertisements, AdvertisementsAdmin)