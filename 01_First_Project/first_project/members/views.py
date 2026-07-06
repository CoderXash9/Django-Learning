from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    mymebers = Member.objects.all().values()
    template = loader.get_template("allmembers.html")
    context = {
        "mymembers": mymebers,
    }

    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def testing(request):
    template = loader.get_template("template.html")
    context = {
        "fruits": ["ABE", "AA", "NAA"],
    }
    return HttpResponse(template.render(context, request))


from django.http import HttpResponse
from django.template import loader


def testing(request):
    template = loader.get_template("template.html")
    context = {
        "firstname": "Linus",
    }
    return HttpResponse(template.render(context, request))
