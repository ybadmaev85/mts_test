from django.contrib import admin

from new_app.models import ModelA, ModelB, ModelC


@admin.register(ModelA)
class ModelAAdmin(admin.ModelAdmin):
    list_display = ('pk', 'a_one', 'a_two', 'a_three', )


@admin.register(ModelB)
class ModelDAdmin(admin.ModelAdmin):
    list_display = ('a_one', 'a_two', 'a_three', )


@admin.register(ModelC)
class ModelCAdmin(admin.ModelAdmin):
    list_display = ('a_one', 'a_two', 'a_three', )
