from django.contrib import admin
from .models import Booking


# Register your models here.
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "kind",
        "user",
        "guests",
        "room",
        "check_in",
        "check_out",
        "experience",
        "experience_time",
    )

    list_filter = ("kind",)
