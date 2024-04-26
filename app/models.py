
from django.db import models

# Create your models here.
class topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    email=models.EmailField(default='mini@gmail.com')
    



    def __str__(self):
        return self.topic_name    

class webpage(models.Model):
    topic_name=models.ForeignKey(topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    creater=models.CharField(default='mini',max_length=11)

    def __str__(self):
        return self.name    


class AccessRecords(models.Model):
    name=models.ForeignKey(webpage,on_delete=models.CASCADE)
    date=models.DateField()
    author=models.CharField(max_length=100)
    type=models.CharField(default='a', max_length=50)

    def __str__(self):
        return self.author 

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    dloc=models.CharField(max_length=100,default='marathali')  

    def __str__(self):
        return str(self.deptno)

class Emp(models.Model):
    empno=models.IntegerField()
    ename=models.CharField(max_length=100,unique=True)
    job=models.CharField( max_length=50)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True,blank=True)#SET_NULL is used for setting the value null as when we delete mgr empno data should not be deleted
    hiredate=models.DateField()
    sal=models.DecimalField(max_digits=10,decimal_places=2)
    comm=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
        return self.ename
    
class Salgrade(models.Model):
    grade=models.IntegerField(primary_key=True)
    losal=models.DecimalField(max_digits=10,decimal_places=2)
    hisal=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return str(self.grade)





    
   


    
