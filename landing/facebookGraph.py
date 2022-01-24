import facebook
from access_dict_by_dot import AccessDictByDot

from .models import Token



# token = "EAAGxFiSPvZAsBAGW9bgJ8fTjiDUhRCcyIj5kwOP8mIKBrg1s7fZADI5oB0WFEJCaxe3vQTC2xcrOVrGKeV9FofSQvQJaR38VsgoHajMuwVZBdlyOxtBs3YXZCeprfRZC8lDg5X4XgnQZCW2ZBti90bLxs6rY36ZCF4p6lpTzmQmY3DPjPrOYUns3mZCsRHhmZAjTNYjslNnnpZAa3Iz8ljIXs546Cu80B9GL4JdPT2LPkDNi3u7kAtWAiW2"

def getData(req):
    try:
        token = Token.objects.get(id=1)
        token = (token.value)
    except Exception as e:
        token = ""
        print(e)
    try:
        graph = facebook.GraphAPI(access_token=token, version=3.1)
        resp = graph.request(f"{req}")
        return resp
    except Exception as error:
        return error


def getUser():
    req = "/me?fields=name"
    data = getData(req)
    data = AccessDictByDot.load(data)
    return data


def getGroups():
    data = getUser()
    req = f"/{data.id}/groups"
    data = getData(req)
    data = AccessDictByDot.load(data)
    return data.data

# 469107796433221
def cleanComments(id):
    req = f"/{id}/feed"
    data = getData(req)
    return data

def getComments(id):
    try:
        req = f"/{id}/feed"
        data = getData(req)
        sdata = (str(data))[2:5]
        if sdata == "200":
            return {"error" : "You are not an admin on this group. Hence cant see Posts"}
        else:
            data = AccessDictByDot.load(data)
            return data.data
    except Exception as e:
        print(e)
        return e



# print(getComments())