from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from .models import UserProfile, SubcriptionInfo


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)

class SubcriptionInfoAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'payment_id', 'paid', 'subscription_type', 'activation_date', 'expiry_date', 'amount')
    search_fields= ['order_id', 'payment_id', 'user__username']


admin.site.register(UserProfile)
admin.site.register(SubcriptionInfo, SubcriptionInfoAdmin)