from django.contrib import admin
from django.contrib.admin import register

from .models import Cart, Favorite, Ingredient, Recipe, Tag, IngredientAmount, TagRecipe


class IngredientAmountAdminInLine(admin.TabularInline):
    model = IngredientAmount
    extra = 2


class TagRecipeAdminInLine(admin.TabularInline):
    model = TagRecipe
    extra = 2


@register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    """Настройки админ панели для модели рецептов"""

    list_display = ('id', 'name', 'author', 'cooking_time')
    search_fields = ('name',)
    list_filter = ('tags', 'name', 'author')
    inlines = (IngredientAmountAdminInLine, TagRecipeAdminInLine)

    fieldsets = (
        ('Основные данные', {
            'fields': ('name', 'author', 'image')
        }),
        ('Приготовление', {
            'fields': ('text', 'cooking_time')
        }),
        ('Счётчики', {
            'fields': ('in_favorite_count', 'in_cart_count')
        })
    )
    readonly_fields = ('in_favorite_count', 'in_cart_count')

    def in_favorite_count(self, obj):
        return obj.favorites.count()

    def in_cart_count(self, obj):
        return obj.cart.count()

    in_favorite_count.short_description = 'Пользователей, добавили в избранное:'
    in_cart_count.short_description = 'Пользователей, добавили в корзину:'


@register(Ingredient)
class IngredientsAdmin(admin.ModelAdmin):
    """Настройки админ панели для модели ингредиентов"""

    list_display = ('id', 'name', 'measurement_unit')
    search_fields = ('name',)


@register(IngredientAmount)
class IngredientRecipeAdmin(admin.ModelAdmin):
    """Настройки админ панели для модели ингредиенты-Рецепт"""

    list_display = ('id', 'recipe', 'ingredient', 'amount')
    search_fields = ('recipe',)


admin.site.register(Tag)
admin.site.register(TagRecipe)
admin.site.register(Cart)
admin.site.register(Favorite)
