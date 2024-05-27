from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models import *

# Create your views here.
def insert_topic(request):
    n=input()
    to=topic.objects.get_or_create(topic_name=n)[0]
    to.save()
    return HttpResponse ('topic is created')

def insert_webpage(request):
    tn=input()
    n=input()
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    wo=webpage.objects.get_or_create(topic_name=to,name=n)[0]
    wo.save()
    return HttpResponse ('webpage is created')
def insert_AccessRecords(request):
    tn=input('topic name is:')
    to=topic.objects.get_or_create(topic_name=tn)[0]
    to.save()
    n=input('name is:')
    wo=webpage.objects.get_or_create(topic_name=to,name=n)[0]
    wo.save()
    d=input('date is:')
    au=input('author is:')
    ao=AccessRecords.objects.get_or_create(name=wo,date=d,author=au)[0]
    ao.save()
    return HttpResponse ('accsess record is created')

def insert_Dept(request):
    do=Dept.objects.get_or_create(deptno=30,dname='sales',dloc='blr')[0]
    do.save()
    dob=Dept.objects.get_or_create(deptno=40,dname='accounts',dloc='mumbai')[0]
    dob.save()
    doc=Dept.objects.get_or_create(deptno=20,dname='accounts',dloc='mumbai')[0]
    doc.save()
    dod=Dept.objects.get_or_create(deptno=10,dname='cook',dloc='delhi')[0]
    dod.save()
    return HttpResponse ('dept is created')

    

def insert_Emp(request):
    eo=Dept.objects.all()
    en=Emp.objects.get_or_create(empno=1111,ename='scott',job='analyst',hiredate='1999-01-02',sal=6000,deptno=eo[0])[0]
    en.save()
    sn=Emp.objects.get_or_create(empno=2222,ename='mini',job='manager',mgr=en,hiredate='1989-01-02',sal=6000,deptno=eo[1])[0]
    sn.save()
    tn=Emp.objects.get_or_create(empno=3333,ename='neha',job='analyst',mgr=sn,hiredate='1979-01-02',sal=3000,deptno=eo[2])[0]
    tn.save()
    rn=Emp.objects.get_or_create(empno=4444,ename='bibhu',job='cook',mgr=tn,hiredate='1969-01-02',sal=5000,deptno=eo[2])[0]
    rn.save()
    vn=Emp.objects.get_or_create(empno=5555,ename='mama',job='it',mgr=sn,hiredate='1959-01-02',sal=50000,deptno=eo[3])[0]
    vn.save()
    return HttpResponse ('emp is created')

def selfjoins(request):
    EMJD=Emp.objects.select_related('mgr').all()
    EMJD=Emp.objects.select_related('mgr').filter(mgr__isnull=True)
    EMJD=Emp.objects.select_related('mgr').filter(ename__contains='K')
    EMJD=Emp.objects.select_related('mgr').filter(ename__contains='A')
    EMJD=Emp.objects.select_related('mgr').filter(mgr__sal__gt=10)
    EMJD=Emp.objects.select_related('mgr').filter(empno=1111)
    EMJD=Emp.objects.select_related('mgr').filter(mgr__ename='mini')



    d={'EMJD':EMJD}
    return render(request,"selfjoins.html",d)
def innerequijoins(request):
    EMJD=Emp.objects.select_related('deptno').filter(job='cook')
    EMJD=Emp.objects.select_related('deptno').filter(job='analyst')
    EMJD=Emp.objects.select_related('deptno').filter(ename__endswith='a')
    EMJD=Emp.objects.select_related('deptno').filter(ename__contains='i')
    EMJD=Emp.objects.select_related('deptno').filter(mgr__ename='neha')
    EMJD=Emp.objects.select_related('deptno').filter(sal__gt=50000)
    EMJD=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    AEAS=Emp.objects.aggregate(AEA=Avg('sal'))['AEA']
    DAS=Emp.objects.values('deptno').annotate(gas=Avg('sal')).filter(gas__gte=AEAS)
    IDAS=Emp.objects.values('deptno').annotate(gas=Avg('sal')).filter(deptno=30)[0]['gas']
    print(IDAS)

    




    #EMJD=Emp.objects.all()
    d={'EMJD':EMJD}
    return render(request,'innerequijoins.html',d)


'''def update(request):
    #Emp.objects.filter(ename='neha').update(sal=60000)
    #Emp.objects.filter(ename='bibhu').update(deptno=10)
    Emp.objects.update_or_create(job='cook',defaults=('sal':222))
    EMU=Emp.objects.all()
    d={'EMU':EMU}
    return render(request,"update.html",d)'''




