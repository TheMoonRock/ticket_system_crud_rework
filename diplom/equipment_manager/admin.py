from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.urls import path
from .models import OfficeEquipment, LicenseTimer

class CategoryFilter(admin.SimpleListFilter):
    title = 'Категория'
    parameter_name = 'category'

    def lookups(self, request, model_admin):
        return [(category, category) for category in OfficeEquipment.objects.values_list('category', flat=True).distinct()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(category=self.value())
        return queryset

class StatusFilter(admin.SimpleListFilter):
    title = 'Статус'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return OfficeEquipment.STATUS_CHOICES

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(status=self.value())
        return queryset

class UserFilter(admin.SimpleListFilter):
    title = 'Пользователь'
    parameter_name = 'user'

    def lookups(self, request, model_admin):
        return [(user.id, user.username) for user in User.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(user__id=self.value())
        return queryset

class GroupFilter(admin.SimpleListFilter):
    title = 'Группа'
    parameter_name = 'group'

    def lookups(self, request, model_admin):
        return [(group.id, group.name) for group in Group.objects.all()]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(group__id=self.value())
        return queryset

class OfficeEquipmentAdmin(admin.ModelAdmin):
    list_display = ('id_device', 'name', 'description', 'category', 'status', 'user', 'group', 'delivery_date')
    list_per_page = 25
    ordering = ('name',)
    list_filter = (CategoryFilter, StatusFilter, UserFilter, GroupFilter)

    actions = ['print_selected']

    def print_selected(self, request, queryset):
        context = {
            'objects': queryset,
            'title': 'Печать выбранных объектов',
        }
        return render(request, 'admin/print.html', context)

    print_selected.short_description = "Распечатать выбранные объекты"

admin.site.register(OfficeEquipment, OfficeEquipmentAdmin)

@admin.register(LicenseTimer)
class LicenseTimerAdmin(admin.ModelAdmin):
    list_display = ('os_timer', 'antivirus_timer', 'office_timer')
    fields = ('os_timer', 'antivirus_timer', 'office_timer')
