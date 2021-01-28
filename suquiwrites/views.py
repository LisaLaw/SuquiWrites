from django.shortcuts import render, get_object_or_404
from .models import Entry
from django.utils import timezone


def home(request):
    entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "suquiwrites/home.html", {"entries": entries})


def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, "suquiwrites/entry_detail.html", {"entry": entry})
