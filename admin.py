from django.contrib import admin
from .models import Record, CD, Cassette, Equipment

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'format', 'availability_status')
    list_filter = ('format', 'availability_status')
    search_fields = ('title', 'artist')
    fieldsets = (
        ('Record Information', {
            'fields': ('title', 'artist', 'description', 'format')
        }),
        ('Availability', {
            'fields': ('availability_status', 'due_back')
        }),
    )

@admin.register(CD)
class CDAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'format', 'availability_status')
    list_filter = ('format', 'availability_status')
    search_fields = ('title', 'artist')
    fieldsets = (
        ('CD Information', {
            'fields': ('title', 'artist', 'description', 'format')
        }),
        ('Availability', {
            'fields': ('availability_status', 'due_back')
        }),
    )

@admin.register(Cassette)
class CassetteAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'format', 'availability_status')
    list_filter = ('format', 'availability_status')
    search_fields = ('title', 'artist')
    fieldsets = (
        ('Cassette Information', {
            'fields': ('title', 'artist', 'description', 'format')
        }),
        ('Availability', {
            'fields': ('availability_status', 'due_back')
        }),
    )

@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'availability_status')
    list_filter = ('type', 'availability_status')
    search_fields = ('name', 'type')
    fieldsets = (
        ('Equipment Information', {
            'fields': ('name', 'type', 'description')
        }),
        ('Availability', {
            'fields': ('availability_status', 'due_back')
        }),
    )
