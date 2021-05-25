from django.contrib import admin

from pizza import models


class PizzaInline(admin.TabularInline):
    model = models.Pizza
    extra = 0


@admin.register(models.Pizzeria)
class PizzeriaAdmin(admin.ModelAdmin):
    ordering = ['owner']
    list_display =  ['owner', 'name', 'phone',
                     'registration_date', 'update_date']
    inlines = [PizzaInline,]


class LikesInline(admin.TabularInline):
    model = models.Likes
    extra = 0

@admin.register(models.Pizza)
class PizzaAdmin(admin.ModelAdmin):
    ordering = ['creator']
    list_display =  ['creator', 'title', 'approved',
                     'registration_date', 'update_date']
    inlines = [LikesInline,]


@admin.register(models.Likes)
class LikesAdmin(admin.ModelAdmin):
    ordering = ['user']
    list_display =  ['user', 'pizza']

