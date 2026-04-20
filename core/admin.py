from django.contrib import admin
from .models import Artist, Track, Repository

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'artist', 'popularity', 'source')
    search_fields = ('name', 'artist__name')
    list_filter = ('source',)

admin.site.register(Artist)
admin.site.register(Repository)

