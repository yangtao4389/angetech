import hashlib
from tools.common import client
from django.shortcuts import HttpResponse


def verifyToken(request):
    token = "HELLOWORLD"
    signature = request.GET.get("signature")
    timestamp = request.GET.get("timestamp")
    nonce = request.GET.get("nonce")
    echostr = request.GET.get("echostr")
    if not signature or not timestamp or not nonce or not echostr:
        return HttpResponse("非法请求")
    list = [token, timestamp, nonce]
    print(list)
    list.sort()
    print(list,'list222')
    sha1 = hashlib.sha1()
    map(sha1.update,list)
    hashcode = sha1.hexdigest()
    print(hashcode,'hashcode')
    print(signature,'signature')
    if hashcode == signature:
        return HttpResponse(echostr)
    else:
        return HttpResponse("验证失效")


