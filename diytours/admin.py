from django.contrib import admin
from diytours.models import *
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

class LocationAdmin(admin.ModelAdmin):
    pass

class FeatureAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class ActivityAdmin(admin.ModelAdmin):
    pass

class PlaceAdmin(admin.ModelAdmin):
    pass

class TourAdmin(admin.ModelAdmin):
    pass

class DateAdmin(admin.ModelAdmin):
    pass

class PromoAdmin(admin.ModelAdmin):
    pass

class FAQAdmin(admin.ModelAdmin):
    pass

class MediaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Tour, TourAdmin)
admin.site.register(Date, DateAdmin)
admin.site.register(Promo, PromoAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Media, MediaAdmin)