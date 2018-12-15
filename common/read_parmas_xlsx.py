"""
从file/params1.xlsx读取数据，手动写入到keywords.py里面的Series_KEY_MAP  Series_property_api
关于params1.xlsx 数据来源于接口文档

"""

from openpyxl import load_workbook
wb = load_workbook(filename='鉴权.xlsx', read_only=True)
ws = wb['Sheet10']

li = []
key = []
key_value = []
item = {}
for num_row,row in enumerate(ws.rows):
    if num_row < 1 :
        continue
    for index,cell in enumerate(row):
        # item = {}
        if index == 0:
            a = cell.value
            key.append(a)
            item[a] = None
        if index == 1:
            b = cell.value
            li.append(cell.value)
            item[a] = b

            # key_value.append(item)
print(key_value)
print(key)
print(item)
# for value in Series_list_property:
#     if value.lower() in li:



