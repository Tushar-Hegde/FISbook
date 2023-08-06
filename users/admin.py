from django.contrib import admin
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = get_user_model()
    list_display = [model.USERNAME_FIELD,'first_name',]
    ordering = (model.USERNAME_FIELD,)
    fieldsets = (
            (("Basic Info"), {"fields": (model.USERNAME_FIELD, "password")}),
            (("Personal info"), {"fields": ("first_name",)}),
            (
                ("Permissions"),
                {
                    "fields": (
                        "is_active",
                        "is_staff",
                        "is_superuser",
                        "groups",
                        "user_permissions",
                    ),
                },
            ),
            (("Important dates"), {"fields": ("last_login",)}),
        )
    
admin.site.register(get_user_model(),CustomUserAdmin)