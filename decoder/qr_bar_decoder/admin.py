from django.contrib import admin

from .models import Product, Item, List, Section

class ItemInline(admin.TabularInline):
	model = Item
	extra = 3

class ListAdmin(admin.ModelAdmin):
	readonly_fields = ["completed"]
	list_display = ["name", "published_date", "was_published_recently"]
	list_filter = ["published_date"]
	search_fields = ["name", "publisded_date", "was_published_recently", "completed"]
	inlines = [ItemInline]

class SectionAdmin(admin.ModelAdmin):
	readonly_fields = ["id"]
	list_display = ["id", "list", "published_date", "was_published_recently"]
	list_filter = ["published_date"]
	search_fields = ["id", "list", "published_date", "was_published_recently"]


admin.site.register(Section, SectionAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Product)
