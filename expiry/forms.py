from django import forms

from .models import Medicine

class DateInput(forms.DateInput):
    input_type = 'date'

class NewMedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['medicine_name', 'expiry_date', 'medicine_per_strip', 'medicine_mrp', 'medicine_quantity']
        widgets = {
            'expiry_date': DateInput()
            }