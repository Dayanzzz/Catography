from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
# render can replace rendertostring and send a response
# below is a dictionary with months and response text as values
monthly_challenges = {
    "january": "This works!",
    "february": "Walk Goku",
    "march": "walk lil b",
    "april": "walk daisy",
    "may": "walk katsu",
    "june": "wash goku",
    "july": "wash lil b",
    "october": "wash daisy",
    "november": "wash katsu",
    "december": "love"
}

# Create your views here.


def index(request):
    # list_items = ""
    months = list(monthly_challenges.keys())
    return render(request, "catography/index.html", {
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     # reverse allows to build url dynamically instead of hard code
    #     list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)

# request and any dynamic segment aka month


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    # keys returns a list in an array and ordered
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    # this equals to challenge/january
    return HttpResponseRedirect(redirect_path)
    # return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # dict w key value pairs
        return render(request, "catography/challenge.html", {
            "text": challenge_text,
            "month_name": month
        })
    # render needs request to extract data,need to pass request as arg
        # response_data = render_to_string("catography/challenge.html")
        # response_data = f"<h1>{challenge_text}</h1>"
        # f in front for string interpolation
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month not supported</h1>")
# how to send back html file to client?

# def monthly_challenge(request, month):
#     challenge_text = None
#     if month == 'january':
#         challenge_text = "This works!"
#     elif month == 'february':
#         challenge_text = "Walk Goku"
#     else:
#         return HttpResponseNotFound("This month is not supported")
#     return HttpResponse(challenge_text)
