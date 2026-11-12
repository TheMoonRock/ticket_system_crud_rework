from django import forms
from .models import OfficeEquipment, LicenseTimer

class OfficeEquipmentForm(forms.ModelForm):
    class Meta:
        model = OfficeEquipment
        fields = ('name', 'description', 'category', 'status', 'user', 'department', 'delivery_date')
