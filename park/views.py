from django.db.models import Q
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from datetime import date
from datetime import datetime, timedelta, time
import random
from django.db.models import Sum
# Create your views here.

def Index(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request,user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d = {'error': error}
    return render(request, 'index.html', d)


def Logout(request):
    logout(request)
    return redirect('index')


def admin_home(request):
    if not request.user.is_authenticated:
        return redirect('index')
    today = datetime.now().date()
    yesterday = today - timedelta(1)
    print(today)

    ta = tblTicket.objects.filter(postingdate=today).aggregate(Sum('noofadult'))
    ya = tblTicket.objects.filter(postingdate=yesterday).aggregate(Sum('noofadult'))
    tc = tblTicket.objects.filter(postingdate=today).aggregate(Sum('noofchild'))
    yc = tblTicket.objects.filter(postingdate=yesterday).aggregate(Sum('noofchild'))


    d = {'ta':ta,'ya':ya,'tc':tc,'yc':yc}
    return render(request,'admin_home.html',d)







def add_tickettype(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""

    if request.method=="POST":

        tt = request.POST['tickettype']
        p = request.POST['price']

        try:
            tblTicketType.objects.create(tickettype=tt,price=p)
            error = "no"
        except:
            error = "yes"
    d = {'error':error}
    return render(request, 'add_tickettype.html',d)


def manage_tickettype(request):
    if not request.user.is_authenticated:
        return redirect('index')
    ttype = tblTicketType.objects.all()
    d = {'ttype':ttype}
    return render(request, 'manage_tickettype.html', d)


def delete_tickettype(request,pid):
    if not request.user.is_authenticated:
        return redirect('index')
    ttype = tblTicketType.objects.get(id=pid)
    ttype.delete()
    return redirect('manage_tickettype')


def edit_tickettype(request,pid):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    ttype=tblTicketType.objects.get(id=pid)
    if request.method == 'POST':
        tp = request.POST['tprice']

        ttype.price=tp

        try:
            ttype.save()
            error = "no"
        except:
            error="yes"
    d = {'error':error,'ttype':ttype}
    return render(request, 'edit_tickettype.html',d)




def add_ticket(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    aprice = tblTicketType.objects.get(tickettype="Adult")
    cprice = tblTicketType.objects.get(tickettype="Child")
    if request.method=="POST":
        ti = str(random.randint(10000000, 99999999))
        na = request.POST['noadult']
        nc = request.POST['nochildren']
        ap = request.POST['aprice']
        cp = request.POST['cprice']

        try:
            tblTicket.objects.create(ticketid=ti,noofadult=na,noofchild=nc,adultunitprice=ap,childunitprice=cp)
            error = "no"
        except:
            error = "yes"
    d = {'error':error,'aprice':aprice,'cprice':cprice}
    return render(request, 'add_ticket.html', d)


def manage_ticket(request):
    if not request.user.is_authenticated:
        return redirect('index')
    ticket = tblTicket.objects.all()
    d = {'ticket':ticket}
    return render(request, 'manage_ticket.html', d)



def view_ticketdetail(request,pid):
    if not request.user.is_authenticated:
        return redirect('index')
    ticket = tblTicket.objects.get(id=pid)
    totalcostadult = int(ticket.noofadult) * int(ticket.adultunitprice)
    totalcostchild = int(ticket.noofchild) * int(ticket.childunitprice)
    total = totalcostadult + totalcostchild
    d = {'ticket': ticket,'totalcostadult':totalcostadult,'totalcostchild':totalcostchild,'total':total}
    return render(request, 'view_ticketdetail.html', d)


def betweendate_reportdetails(request):
    if not request.user.is_authenticated:
        return redirect('index')
    return render(request, 'betweendate_reportdetails.html')



def betweendate_report(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        fd = request.POST['fromdate']
        td = request.POST['todate']
        ticket = tblTicket.objects.filter(Q(postingdate__gte=fd) & Q(postingdate__lte=td))
        ticketcount = tblTicket.objects.filter(Q(postingdate__gte=fd) & Q(postingdate__lte=td)).count()
        d = {'ticket': ticket,'fd':fd,'td':td,'ticketcount':ticketcount}
        return render(request, 'betweendate_reportdetails.html', d)
    return render(request, 'betweendate_report.html')


def search(request):
    q = request.POST.get('searchdata')

    try:
        ticket = tblTicket.objects.filter(Q(ticketid=q))
        ticketcount = tblTicket.objects.filter(Q(ticketid=q)).count()
    except:
        ticket = ""
    d = {'ticket': ticket,'q':q,'ticketcount':ticketcount}
    return render(request, 'search.html',d)


def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('index')
    error = ""
    if request.method=="POST":
        o = request.POST['currentpassword']
        n = request.POST['newpassword']
        c = request.POST['confirmpassword']
        if c == n:
            u = User.objects.get(username__exact=request.user.username)
            u.set_password(n)
            u.save()
            error = "yes"
        else:
            error = "not"
    d = {'error':error}
    return render(request,'changepassword.html',d)