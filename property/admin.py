from django.contrib import admin

from .models import Flat, Claim, Owner


class MembershipInline(admin.TabularInline):
    model = Flat.flat_owners.through
    raw_id_fields = ['owner', 'flat']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address',)
    readonly_fields = ['created_at']
    list_display = (
        'address',
        'price',
        'new_building',
        'construction_year'
    )
    list_editable = ['new_building']
    list_filter = ['new_building']
    raw_id_fields = ['liked_by']
    inlines = [
        MembershipInline,
    ]


class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('name', 'address')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['own_flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Claim, ClaimAdmin)
admin.site.register(Owner, OwnerAdmin)
