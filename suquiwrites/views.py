from django.shortcuts import render, get_object_or_404
from .models import Entry
from .forms import EntryForm
from django.utils import timezone
from django.shortcuts import redirect


def home(request):
    entries = Entry.objects.filter(published_date__lte=timezone.now()).order_by(
        "published_date"
    )
    return render(request, "suquiwrites/home.html", {"entries": entries})


def entry_detail(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, "suquiwrites/entry_detail.html", {"entry": entry})


def entry_new(request):
    if request.method == "POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.published_date = timezone.now()
            entry.save()
            return redirect("entry_detail", pk=entry.pk)
    else:
        form = EntryForm()
    return render(request, "suquiwrites/entry_edit.html", {"form": form})


def entry_edit(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "POST":
        form = EntryForm(request.POST, instance=post)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.author = request.user
            entry.published_date = timezone.now()
            entry.save()
            return redirect("entry_detail", pk=entry.pk)
    else:
        form = EntryForm(instance=post)
    return render(request, "suquiwrites/entry_edit.html", {"form": form})
