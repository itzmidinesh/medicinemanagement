from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Medicine

# Register your models here.
class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False
	verbose_name_plural = 'Profile'
	fk_name = 'user'

class CustomUserAdmin(UserAdmin):
	inlines = (ProfileInline, )
	list_display = ('username', 'first_name', 'last_name', 'shop_name', 'mobile', 'license1', 'license2', 'email', 'is_staff')
	list_select_related = ('profile', )

	def shop_name(self, instance):
		return instance.profile.shop_name
		get_shop_name.short_description = 'Shop Name'

	def mobile(self, instance):
		return instance.profile.mobile_number
		get_mobile.short_description = 'Mobile Number'

	def license1(self, instance):
		return instance.profile.license1
		get_license1.short_description = 'License 1'

	def license2(self, instance):
		return instance.profile.license2
		get_license2.short_description = 'License 2'

	def get_inline_instances(self, request, obj=None):
		if not obj:
			return list()
		return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Medicine)