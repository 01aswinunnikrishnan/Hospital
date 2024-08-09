from django.contrib import admin
from.models import userreg,doctorreg,Category,Blogs,Appointment,DoctorOAuthToken

admin.site.register(userreg)
admin.site.register(doctorreg)
admin.site.register(Category)
admin.site.register(Blogs)
admin.site.register(Appointment)
admin.site.register(DoctorOAuthToken)


# Register your models here.
