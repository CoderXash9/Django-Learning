from django.shortcuts import render
from .models import Member


def main(request):
    return render(request, "main.html")


def members(request):
    mymembers = Member.objects.all()
    return render(
        request,
        "allmembers.html",
        {
            "mymembers": mymembers,
        },
    )


def details(request, slug):
    mymember = Member.objects.get(slug=slug)
    return render(
        request,
        "details.html",
        {
            "mymember": mymember,
        },
    )


def testing10(request):
    mymembers = Member.objects.all().order_by("lastname", "-id")
    return render(
        request,
        "template.html",
        {
            "mymembers": mymembers,
            "fruits": ["Apple", "Banana", "Mango"],
            "greeting": 1,
        },
    )
