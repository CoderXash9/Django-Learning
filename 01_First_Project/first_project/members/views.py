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
