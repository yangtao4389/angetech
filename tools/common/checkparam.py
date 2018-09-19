import time,hashlib
def isVaildDate(date):
    '''
    判断日期格式是否符合标准
    :param self:
    :param date:
    :return:
    '''
    try:
        if ":" in date:
            time.strptime(date, "%Y-%m-%d %H:%M:%S")
        else:
            time.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False

def isVaildInt(data):
    try:
        int(data)
        return True
    except:
        return False


def get_md5(string):
    hash_md5 = hashlib.md5(string.encode("utf-8"))
    md5_string = hash_md5.hexdigest()
    return md5_string