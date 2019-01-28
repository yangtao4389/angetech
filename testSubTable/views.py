from django.shortcuts import render,HttpResponse

# Create your views here.
from testSubTable.models import User
def index(request):
    a = User.shard().objects.create(id=1,name="yy",age=10)
    print(a)
    return HttpResponse("ok")

def index2(request):
    a = User.shard().objects.get(id=1)
    a.age = 20
    a.save()
    print(a)
    print(dir(a))

    # newClass = getModel('29345794_table')
    # MyModel._meta.db_table = '10293847_table'
    # MyModel.objects.all()

    return HttpResponse("ok")