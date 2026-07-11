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


def testing1(request):
    template = loader.get_template("template.html")
    context = {
        "fruits": ["ABE", "AA", "NAA"],
    }
    return HttpResponse(template.render(context, request))


from django.http import HttpResponse
from django.template import loader


def testing2(request):
    template = loader.get_template("template.html")
    context = {
        "firstname": "Linus",
    }
    return HttpResponse(template.render(context, request))


from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member


def testing3(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("template.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))


def testing4(request):
    mydata = Member.objects.all()
    template = loader.get_template("template.html")
    context = {"mymembers": mydata}
    return HttpResponse(template.render(context, request))


def testing5(request):
    mydata = Member.objects.values_list("firstname")
    template = loader.get_template("template.html")
    context = {"mymembers": mydata}
    return HttpResponse(template.render(context, request))


def testing6(request):
    mydata = Member.objects.filter(firstname="Emile").values()
    template = loader.get_template("template.html")
    context = {"mymembers": mydata}
    return HttpResponse(template.render(context, request))
