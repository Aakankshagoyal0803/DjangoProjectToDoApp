from django.shortcuts import render,get_object_or_404,redirect
from .forms import delaform,todoform
from .models import todo,done
from django.utils import timezone
from django.http import HttpResponseRedirect
def todoview(request):
    obj=todo.objects.all()
    count=todo.objects.count()
    d=todo.objects.filter(done='no')
    return render(request,'base.html',{'object':obj,'not_done': d,'count':count})


# Create your views here.
def addentry(request):
    form=todoform(request.POST or None)
    if form.is_valid():
        instance=form.save()
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context={'form':form}
    return render(request,'base1.html',context)


def delentry(request,i):
        instance=get_object_or_404(todo,pk=i)
        instance.delete()
        return redirect('show')
        #return render(request,'base1.html')

def doneview(request,i=None):
    instance=get_object_or_404(todo,id=i)
    form=todoform(request.POST or None,instance=instance)
    if form.is_valid():
      instance=form.save(commit=False)
      instance.save()
      return HttpResponseRedirect(instance.get_absolute_url())
    context={'form':form}
    return render(request,'base1.html',context)

def finview(request,i=None):
    instance=get_object_or_404(todo,id=i)
    title=instance.title
    new=done.objects.create(title=title)
    instance.delete()
    return redirect('showdone')

def showdonee(request):
    obj=done.objects.all()
    c=done.objects.count()
    return render(request,'base.html',{'doneobj':obj,'count':c})

def accdelete(request,i):
    instance=get_object_or_404(done,pk=i)
    instance.delete()
    return redirect('showdone')
