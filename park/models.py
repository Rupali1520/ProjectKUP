from django.db import models

# Create your models here.

class tblTicketType(models.Model):
    tickettype = models.CharField(max_length=70)
    price = models.CharField(max_length=10)
    def __str__(self):
        return self.tickettype



class tblTicket(models.Model):
    ticketid = models.CharField(max_length=20)
    noofadult = models.CharField(max_length=20)
    noofchild = models.CharField(max_length=20)
    adultunitprice = models.CharField(max_length=10)
    childunitprice = models.CharField(max_length=10)
    postingdate = models.DateField(auto_now=True)
    def __str__(self):
        return self.ticketid