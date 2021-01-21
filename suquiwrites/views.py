from django.shortcuts import render
from .models import Entry


def home(request):
    entries = Entry.objects.filter(
        published_date__lte=timezone.now().order_by("published_date")
    )
    return render(request, "suquiwrites/home.hmtl", {"entries": entries})
