from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Expense_track(models.Model):
    description = models.CharField(max_length=300)
    date = models.DateTimeField(auto_now_add=True)
    debit = models.IntegerField(blank=True, null=True)
    credit = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)



