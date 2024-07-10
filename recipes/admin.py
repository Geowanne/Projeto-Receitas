from django.contrib import admin
from.models import Category, Recipe

# Classe para Categooria
class CategoryAdmin(admin.ModelAdmin):
    ...

# Classe para receitas e registrando com decorators
@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

#Registrando a categoria 
admin.site.register(Category, CategoryAdmin)