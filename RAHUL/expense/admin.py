from django.contrib import admin
from .models import Expense_track


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('date','description','debit','credit','total')

# Register the admin class with the associated model
admin.site.register(Expense_track, AuthorAdmin)