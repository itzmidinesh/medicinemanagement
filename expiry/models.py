from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
import decimal

User._meta.get_field('email')._unique=True

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	shop_name = models.CharField(max_length=100, unique=True)
	shop_address = models.CharField(max_length=500)
	shop_area = models.CharField(max_length=30)
	shop_locality = models.CharField(max_length=30)
	mobile_num_regex = RegexValidator(regex="^[0-9]{10}$", message="Entered mobile number isn't in a right format!")
	mobile_number = models.CharField(validators=[mobile_num_regex], max_length=10, unique=True, blank=True)
	license_regex = RegexValidator(regex="^[A-Z]{3}\/[\d]{4}\/[\d]{2}$", message="Entered license number isn't in a right format!")
	license1 = models.CharField(validators=[license_regex], max_length=11, unique=True)
	license2 = models.CharField(validators=[license_regex], max_length=11, unique=True)
	def __str__(self):
		return self.user.username

class Medicine(models.Model):
	medicine_name=models.CharField(max_length=50)
	expiry_date=models.DateField(validators=[MinValueValidator(limit_value=date.today)])
	medicine_per_strip=models.DecimalField(max_digits=5, decimal_places=0,validators=[MinValueValidator(1)])
	medicine_mrp=models.DecimalField(max_digits=5, decimal_places=2,validators=[MinValueValidator(0.01)])
	medicine_quantity=models.IntegerField(validators=[MaxValueValidator(100),MinValueValidator(1)], default=1)
	medicine_added_by=models.ForeignKey(User, related_name='medicines', on_delete=models.CASCADE)
	
	def medicine_price(self):
		price= (self.medicine_mrp/self.medicine_per_strip)*self.medicine_quantity
		return round(price, 2)

	def clean(self):
		today=date.today()
		if self.expiry_date < today:
			raise ValidationError('Expiry date cannot be in the past.')
		elif self.medicine_per_strip < 1:
			raise ValidationError('Medicine per strip cannot be less than 1.')
		elif self.medicine_mrp <=0:
			raise ValidationError('MRP for medicine cannot be less than or equal to 0.')
		elif self.medicine_quantity < 1:
			raise ValidationError('Medicine quantity cannot be less than 1.')
	def __str__(self):
		return self.medicine_name