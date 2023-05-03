"""ParkTicketManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from park.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('admin_home',admin_home,name='admin_home'),
    path('add_tickettype',add_tickettype,name='add_tickettype'),
    path('manage_tickettype', manage_tickettype, name='manage_tickettype'),
    path('delete_tickettype/<int:pid>',delete_tickettype,name='delete_tickettype'),
path('edit_tickettype/<int:pid>',edit_tickettype,name='edit_tickettype'),
    path('add_ticket',add_ticket,name='add_ticket'),
    path('manage_ticket', manage_ticket, name='manage_ticket'),
    path('view_ticketdetail/<int:pid>',view_ticketdetail,name='view_ticketdetail'),
    path('betweendate_report',betweendate_report,name='betweendate_report'),
    path('betweendate_reportdetails',betweendate_reportdetails,name='betweendate_reportdetails'),
    path('search', search, name='search'),
    path('changepassword',changepassword, name='changepassword'),
    path('logout/', Logout, name='logout'),
]
