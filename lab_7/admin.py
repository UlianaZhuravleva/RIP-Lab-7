from django.contrib import admin
from .models import GroupModel, MemberModel, User


class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'genre', 'base_date')
    search_fields = ('group_name', 'genre')


admin.site.register(GroupModel, GroupAdmin)


class MemberAdmin(admin.ModelAdmin):
    def item_amount(self, obj):
        data = GroupModel.objects.filter(ord_num=obj.id).all()
        i = len(data)
        return i
    list_display = ('member_name', 'member_surname', 'member_thirdname', 'member_bdate')
    list_filter = ['member_name']

admin.site.register(MemberModel, MemberAdmin)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')

admin.site.register(User, UserAdmin)
# Register your models here.