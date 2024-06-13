from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
	category = models.CharField(max_length=7, choices=[('INGRESO', 'Ingreso'), ('GASTO', 'Gasto')], default = 'INGRESO')
	value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	date = models.DateTimeField(auto_now_add=True)
	description = models.CharField(max_length=100)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.description + " - por " + self.user.username
		
class Saving(models.Model):
	current_value = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	goal = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
	percentage = models.DecimalField(max_digits=5, decimal_places=2, default = 0.00)
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return f'Ahorro de {self.user.username}'