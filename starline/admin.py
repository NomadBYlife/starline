from django.contrib import admin

from starline.models import Comment, Contacts, Category, Product, Feedback, Action, OurWork, Security, Characteristic, \
    Company


class SecurityAdmin(admin.ModelAdmin):
    list_display = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'published')
    exclude = ('slug',)
    list_display_links = ('title',)
    list_editable = ('published',)


class CharecteristicAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class ProductAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = (
        'title',
        'price',
        'price_install',
        'image',
        'presence',
        'description',
        'instruction',
        'published',
        'popular',
        'novelties'
    )
    list_display_links = ('title',)
    list_editable = ('price', 'price_install', 'published')


class ActionAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'published')
    list_display_links = ('title',)
    list_editable = ('published',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('title', 'name', 'numbers_phone', 'body', 'published')
    list_filter = ('title', 'name', 'numbers_phone')
    search_fields = ('title', 'name', 'numbers_phone', 'pub_data', 'body')


class OurWorkAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'installation_time',
        'installation_price',
        'description_video',
        'url',
        'description_image',
        'image',
        'published',
    )
    list_filter = ('title',)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'message', 'published')
    list_filter = ('published',)
    list_editable = ('published',)


class ContactsAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'logo1',
        'phone1',
        'logo2',
        'phone2',
        'email',
        'social_info1',
        'social_info2',
        'social_info3',
        'time_work1',
        'time_work2',
        'maps',
    )
    list_display_links = ('address',)
    list_editable = ('time_work1', 'time_work2')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('image', 'description')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Action, ActionAdmin)
admin.site.register(OurWork, OurWorkAdmin)
admin.site.register(Security, SecurityAdmin)
admin.site.register(Characteristic, CharecteristicAdmin)
