from django.shortcuts import render
from . import facebookGraph

from access_dict_by_dot import AccessDictByDot
# Create your views here.

from django.views.generic import View
from django.http import JsonResponse
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

class AjaxHandlerView(View):
    def get(self, request, pk):
        text = request.GET.get("text")
        print(text)
        if is_ajax(request):
            if text == "comments":
                comments = facebookGraph.cleanComments(pk)
                return JsonResponse({"comments":comments})
            text = "I have to do it"
            return JsonResponse({"text":text})
        context = {
        "user" : facebookGraph.getUser(),
        "groups" : facebookGraph.getGroups(),
        # "comments" : facebookGraph.getComments(),
        }
        return render(request, "landing/index.html", context)







def home(request):
    try:
        user = facebookGraph.getData("/me?fields=name")
        userE =str(user)[:5]
        if userE == "Error":
            context = {"error": user}
            return render(request, "landing/home.html", context)
    except Exception as e:
        context = {"error":e}
        return render(request, "landing/home.html", context)

    context = {
    "user" : facebookGraph.getUser(),
    "groups" : facebookGraph.getGroups(),
    # "comments" : facebookGraph.getComments(),
    }
    # print(context)
    # context = {'groups': [{'name': 'TAITA TAVETA UNIVERSITY:OUR ISSUES', 'privacy': 'CLOSED', 'id': '469107796433221'}, {'name': 'TAITA TAVETA UNIVERSITY - VOI', 'id': '1416553615229929'}, {'name': 'Taita Taveta University Voi', 'id': '1387991968282905'}, {'name': 'TSC TEACHERS OF KENYA', 'id': '1778669782297839'}, {'name': 'Google Workspace', 'id': '1182334638549024'}, {'name': 'KENYA DEFENCE FORCE (KDF)', 'id': '228885705319400'}]}
    return render(request, "landing/home.html", context)


def group(request, pk):
    comments = facebookGraph.getComments(pk),
    if "error" in comments[0]:
        print("===")
        print(comments[0]["error"])
        print("===")
        error =comments[0]["error"]
        comments = []
    else:
        error =""
        comments = comments[0]
    context = {
    "user" : facebookGraph.getUser(),
    "groups" : facebookGraph.getGroups(),
    "comments" : comments,
    "pk":str(pk),
    "error" : error
    }
    print(context)
    return render(request, "landing/group.html", context)


def ajaxHandler(request, pk):
    context = {
    "user" : facebookGraph.getUser(),
    "groups" : facebookGraph.getGroups(),
    "pk":str(pk),
    "comments_length" : len(facebookGraph.getComments(pk)),
    }
    print(context)
    return render(request, "landing/group_query.html", context)
