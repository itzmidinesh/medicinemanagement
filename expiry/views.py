from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Medicine
from django.contrib.auth.models import User
from .forms import NewMedicineForm

# Create your views here.
def index_view(request):
	return render(request, 'index.html')

@login_required
def medicine_list(request):
	medicines=Medicine.objects.all()
	return render(request, 'medicine_list.html', {'medicines': medicines})

@login_required
def my_medicine(request):
	medicines=Medicine.objects.filter(medicine_added_by=request.user)
	return render(request, 'my_medicine.html', {'medicines': medicines})

@login_required
def medicine_new(request):
	if request.method == 'POST':
		form = NewMedicineForm(request.POST)
		if form.is_valid():
			medicine = form.save(commit=False)
			medicine.medicine_added_by=request.user
			medicine.save()
			return redirect('medicine_list')
	else:
		form = NewMedicineForm()
	return render(request, 'medicine_new.html',{'form': form})

class MedicineDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicine
    success_url = reverse_lazy('my_medicine')

class MedicineUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Medicine
    fields = ['medicine_name', 'expiry_date', 'medicine_per_strip', 'medicine_mrp', 'medicine_quantity']
    success_message = "Record successfully updated."
    success_url = reverse_lazy('my_medicine')

@login_required
def get_user_profile(request, username):
	userprofile = User.objects.get(username=username)
	return render(request, 'user_profile.html',{'userprofile':userprofile})