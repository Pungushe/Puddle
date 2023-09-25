from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from item.models import Item


@login_required
def dashboard(request):
    items=Item.objects.filter(created_by=request.user)
    context={
        'items': items
    }
    return render(request, 'dashboard/dashboard.html', context)
