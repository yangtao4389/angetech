import urllib.parse
def get_client_ip(request):
    """
    :param request:
    :return: 访问用户的ip
    """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def get_client_previous_url(request):
    """
    :param request:
    :return:访问用户的前一个地址
    """
    try:
        url = request.META.get('HTTP_REFERER')
    except:
        url = None
    return url

def get_client_current_path(request):
    """
    :param request:
    :return: 不带参数的地址
    """
    return request.path

def get_client_current_full_path(request):
    """
    :param request:
    :return: 带参数的完整地址
    """
    return request.get_full_path()

def url_query_replace(url, name, value):
    """
        url参数替换
    """
    parse_obj = urllib.parse.urlparse(url)
    parse_query = parse_obj.query
    parse_query_dict = dict(urllib.parse.parse_qsl(parse_query))
    if name in parse_query_dict.keys():
        # 找到后需要将所有同名的参数全部删除，然后替换成新的
        del parse_query_dict[name]
    parse_query_dict[name] = value
    pure_url = url.replace('?'+parse_query, '')
    ret = pure_url + "?" + urllib.parse.urlencode(parse_query_dict)
    print(ret)
    return ret

