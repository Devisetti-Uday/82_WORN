from django.contrib import admin
from home.models import Sell,Order

# Register your models here.
admin.site.register(Sell)
admin.site.register(Order)
admin.site.site_header="82_WORN"
admin.site.site_title="82_WORN portal"
admin.site.index_title="welcome Admin"