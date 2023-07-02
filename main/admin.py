from django.contrib import admin
from .models import Profile, Professional, VerifiedProfessionalAdmin, NonVerifiedProfessionalAdmin, Contact

class CombinedProfessionalAdmin(VerifiedProfessionalAdmin, NonVerifiedProfessionalAdmin):
        pass


admin.site.register(Contact)
admin.site.register(Professional, CombinedProfessionalAdmin)
