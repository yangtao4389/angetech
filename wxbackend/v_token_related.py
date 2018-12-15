import hashlib
from tools.common import client
from django.shortcuts import HttpResponse
import requests
import json
from logging import getLogger
logger = getLogger("default")

def verifyToken(request):
    token = "HELLOWORLD"
    signature = request.GET.get("signature")
    timestamp = request.GET.get("timestamp")
    nonce = request.GET.get("nonce")
    echostr = request.GET.get("echostr")
    list = [token, timestamp, nonce]
    list.sort()
    temp = ''.join(list)
    sha1 = hashlib.sha1(temp.encode('utf-8'))

    hashcode = sha1.hexdigest()
    if hashcode == signature:

        return HttpResponse(echostr)
    else:
        return HttpResponse("非法请求")


def getToken():
    APPID = "wxd2ee708e2f14a707"
    APPSECRET = "7ea2c0df5e192baa3565bb0b6bed4cc7"
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s" % (APPID,APPSECRET)
    try:
        responseJson = requests.get(url).text
        responseDict = json.loads(responseJson)
        #{"access_token":"ACCESS_TOKEN","expires_in":7200}
        # {"errcode": 40013, "errmsg": "invalid appid"}
        logger.info(responseDict)
        access_token = responseDict.get("access_token")
        expires_in = responseJson.get("expires_in")
        if access_token and expires_in:
            return access_token,expires_in
        else:
            raise Exception
    except:
        logger.exception("获取token出错")
        return False

