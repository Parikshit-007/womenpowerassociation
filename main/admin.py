from django.contrib import admin
from .models import Profile, Professional, VerifiedProfessionalAdmin, NonVerifiedProfessionalAdmin

class CombinedProfessionalAdmin(VerifiedProfessionalAdmin, NonVerifiedProfessionalAdmin):
        pass


#admin.site.register(Profile)
admin.site.register(Professional, CombinedProfessionalAdmin)
