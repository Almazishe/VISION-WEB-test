from django.contrib import admin

from .models import Goal, Advantage, Ad

admin.site.register(Ad)
admin.site.register(Goal)

@admin.register(Advantage)
class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'img_place')