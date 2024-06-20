from django.contrib import admin
from .models import CoinFlip, Article, Author
from .admin_mixins import ExportAsCSVMixin

# Register your models here.






@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    list_display = ['first_name', 'last_name', 'email', 'bio', 'birthday']
    actions = ['export_as_csv']

@admin.action(description="Сделать по 5 просмотров")
def reset_quantity_to_five(modeladmin, request, queryset):
    queryset.update(views=5)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'category','text', 'views']
    ordering = ['title', '-category']
    list_filter = ['author']
    search_fields = ['text']
    search_help_text = 'Поиск по полю Текст (text)'
    actions = [reset_quantity_to_five]
    readonly_fields = ['publication_date']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['author','title'],
            },
        ),
        (
            'Текст статьи',
            {
                'classes': ['collapse'],
                'description': 'Текст',
                'fields':['text'],
            },
        ),
        (
            'Даты',
            {
                'fields': ['publication_date'],
            }
        ),
        (
            'Рейтинг и прочее',
            {
                'description': 'Просмотры и категория',
                'fields': ['category', 'views'],
            }
        ),
    ]



admin.site.register(CoinFlip)
admin.site.register(Article, ArticleAdmin)
# admin.site.register(Author, AuthorAdmin)
