from django.shortcuts import render
from .models import LicenseTimer, OfficeEquipment
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user
    license_timer = LicenseTimer.objects.first()
    user_equipment = OfficeEquipment.objects.filter(user=user)

    context = {
        'license_timer': license_timer,
        'user_equipment': user_equipment,
    }
    return render(request, 'dashboard.html', context)

