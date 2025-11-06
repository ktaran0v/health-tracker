from django.contrib import admin
from .models import HealthRecord

@admin.register(HealthRecord)
class HealthRecordAdmin(admin.ModelAdmin):
    list_display = ("patient_name", "date", "weight", "blood_pressure", "pulse")
    search_fields = ("patient_name",)
    list_filter = ("date",)
