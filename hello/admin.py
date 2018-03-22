from django.contrib import admin
from hello.models import *
# Register your models here.
@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name','city','state_province','country')
    search_fields = ('name',)
    list_filter = ('state_province',)
    fields = ('name', "address")
    # exclude = ('name', 'address')


admin.site.register(Author)
admin.site.register(AuthorDetail)
# admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Book)
