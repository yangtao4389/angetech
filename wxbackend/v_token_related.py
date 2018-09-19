import hashlib
from tools.common import client
from django.shortcuts import HttpResponse


def verifyToken(request):
    token = "HELLOWORLD"
    signature = request.GET.get("signature")
    timestamp = request.GET.get("timestamp")
    nonce = request.GET.get("nonce")
    echostr = request.GET.get("echostr")
    list = [token, timestamp, nonce]
    print(list)
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update,list)
    hashcode = sha1.hexdigest()
    if hashcode == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("非法请求")


