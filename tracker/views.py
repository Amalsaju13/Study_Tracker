import calendar
from datetime import date
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import StudyEntry, StudyImage
from .forms import StudyEntryForm, SignupForm


# -------------------------
# SIGNUP
# -------------------------

def signup_view(request):

    if request.method == "POST":

        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('calendar')

    else:
        form = SignupForm()

    return render(request, "tracker/signup.html", {"form": form})


# -------------------------
# LOGIN
# -------------------------

def login_view(request):

    error = None

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            next_url = request.GET.get('next', 'calendar')
            return redirect(next_url)

        else:
            error = "Invalid username or password"

    return render(request, "tracker/login.html", {"error": error})



# -------------------------
# LOGOUT
# -------------------------

def logout_view(request):

    logout(request)

    return redirect("login")


# -------------------------
# ADD STUDY ENTRY
# -------------------------

@login_required
def add_study(request):

    if request.method == "POST":

        form = StudyEntryForm(request.POST)
        files = request.FILES.getlist('images')

        if form.is_valid():


            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()

            for f in files:
                StudyImage.objects.create(entry=entry, image=f)

            return redirect('calendar')

    else:
        form = StudyEntryForm()

    return render(request, "tracker/add_study.html", {"form": form})


# -------------------------
# CALENDAR VIEW
# -------------------------

@login_required
def calendar_view(request):

    month = request.GET.get('month')
    year = request.GET.get('year')

    today = date.today()

    month = int(month) if month else today.month
    year = int(year) if year else today.year

    cal = calendar.monthcalendar(year, month)

    entries = StudyEntry.objects.filter(
        user=request.user,
        study_date__year=year,
        study_date__month=month
    )

    
    from collections import defaultdict

    entry_dict = {}

    for e in entries:
        entry_dict[e.study_date.day] = e

    prev_month = month - 1
    prev_year = year

    if prev_month == 0:
        prev_month = 12
        prev_year -= 1

    next_month = month + 1
    next_year = year

    if next_month == 13:
        next_month = 1
        next_year += 1

    return render(request, 'tracker/calendar.html', {
        'calendar': cal,
        'entries': entries,
        'month': month,
        'year': year,
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year
    })


# -------------------------
# STUDY DETAIL
# -------------------------

@login_required
def study_detail(request, id):

    entry = get_object_or_404(
        StudyEntry,
        id=id,
        user=request.user
    )

    return render(request, 'tracker/detail.html', {'entry': entry})



# -------------------------
# ADD IMAGES
# -------------------------

@login_required
def add_images(request, id):

    entry = get_object_or_404(
        StudyEntry,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        images = request.FILES.getlist("images")

        for img in images:
            StudyImage.objects.create(
                entry=entry,
                image=img
            )

    return redirect("detail", id=entry.id)


# -------------------------
# DELETE IMAGE
# -------------------------

@login_required
def delete_image(request, id):

    image = get_object_or_404(
        StudyImage,
        id=id,
        entry__user=request.user
    )

    entry_id = image.entry.id

    image.delete()

    return redirect('detail', id=entry_id)


# -------------------------
# EDIT STUDY
# -------------------------

@login_required
def edit_study(request, id):

    entry = get_object_or_404(
        StudyEntry,
        id=id,
        user=request.user
    )

    if request.method == "POST":

        form = StudyEntryForm(request.POST, instance=entry)

        if form.is_valid():
            form.save()
            return redirect('detail', id=entry.id)

    else:
        form = StudyEntryForm(instance=entry)

    return render(request, "tracker/edit_study.html", {
        "form": form,
        "entry": entry
    })


# -------------------------
# DELETE STUDY
# -------------------------

@login_required
def delete_study(request, id):

    entry = get_object_or_404(
        StudyEntry,
        id=id,
        user=request.user
    )

    if request.method == "POST":
        entry.delete()
        return redirect('calendar')

    return render(request, "tracker/delete_confirm.html", {"entry": entry})


# -------------------------
# DASHBOARD
# -------------------------

@login_required
def dashboard(request):

    entries = StudyEntry.objects.filter(user=request.user)

    total = sum(e.progress for e in entries)
    count = entries.count()

    overall = total // count if count > 0 else 0

    return render(request, 'tracker/dashboard.html', {
        'entries': entries,
        'overall': overall
    })