from pickle import TRUE
from tkinter import FALSE
from django.db import models

class Countries(models.Model):
    name=models.CharField(max_length=225)
    

    
class States(models.Model):
    name=models.CharField(max_length=225)
    country=models.ForeignKey(Countries,on_delete=models.CASCADE,blank=True,null=True)
    
class Companies(models.Model):#ann(for my display)
    name=models.CharField(max_length=225)
    mailing_name=models.CharField(max_length=225)
    
    
    
class Group(models.Model):#ann(for my display)
    name = models.CharField(max_length=225)
    
    
class SubGroup(models.Model):#ann(for my display)
    name = models.CharField(max_length=225)
    group=models.ForeignKey(Group,on_delete=models.CASCADE,blank=True,null=True)
    # company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True) 
          
class Voucher(models.Model):#ann(for my display)
    name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    under =  models.CharField(max_length=225)
    #company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    

#  class stock_item(models.Model):#ajmay

#     rateper=models.CharField(max_length=100,null=True)
#     value=models.CharField(max_length=100,null=True)    
# #     group = models.ForeignKey(StockGroup,on_delete=models.SET_NULL, null=True)
#     # bn  opening_balance=models.IntegerField(null=True)    

class Features(models.Model):
    maintain_accounts = models.BooleanField(default=True)
    bill_wise_entry = models.BooleanField(default=True)
    cost_centres = models.BooleanField(default=False)
    interest_calc = models.BooleanField(default=True)
    maintain_inventory = models.BooleanField(default=True)
    integrate_accounts = models.BooleanField(default=True)
    multiple_price_level = models.BooleanField(default=True)
    batches = models.BooleanField(default=True)
    expirydate_batches = models.BooleanField(default=True)
    joborder_processing = models.BooleanField(default=True)
    sub_ledger = models.BooleanField(default=True)
    cost_tracking= models.BooleanField(default=True)
    job_costing = models.BooleanField(default=True)
    discount_invoices = models.BooleanField(default=True)
    Billed_Quantity = models.BooleanField(default=True)
    gst = models.BooleanField(default=False)
    tds = models.BooleanField(default=False)
    tcs = models.BooleanField(default=False)
    vat = models.BooleanField(default=False)
    excise = models.BooleanField(default=True)
    servicetax = models.BooleanField(default=True)
    payroll = models.BooleanField(default=False)
    multiple_addrss = models.BooleanField(default=True)
    vouchers = models.BooleanField(default=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class Costcentre(models.Model):
    cname = models.CharField(max_length=225)
    alias = models.CharField(max_length=225,null=True)
    under = models.CharField(max_length=225)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

  
class ledgers(models.Model):
      ledger=models.CharField(max_length=225,null=True) 
      SubGroup =models.ForeignKey(SubGroup ,on_delete=models.CASCADE,blank=True,null=True)
      
class ledgers_vouchers(models.Model):
    Voucher=models.ForeignKey(Voucher,on_delete=models.CASCADE,blank=True,null=True)
    SubGroup =models.ForeignKey(SubGroup ,on_delete=models.CASCADE,blank=True,null=True)
    ledgers =models.ForeignKey(ledgers ,on_delete=models.CASCADE,blank=True,null=True)
    ledgervoucher_date=models.DateField(null=True)
    credit= models.IntegerField(default=0)#ledger credit
    debit= models.IntegerField(default=0)#ledger debit
     


    #company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)    

class Sales(models.Model):#ann sales table
    partyAccntname = models.CharField(max_length=225)
    currentbalancep = models.CharField(max_length=225,null=True)#current balance of party
    salesledger = models.CharField(max_length=225)
    currentbalancesl = models.IntegerField(null=True)#balance of corresponding sales ledger
    nameofitem=models.CharField(max_length=225,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(default=0)
    sales_date=models.DateField(null=True)
    total=models.IntegerField(default=0)
   # voucher=models.ForeignKey(Voucher,on_delete=models.CASCADE,blank=True,null=True)

class Purchase(models.Model):#ann purchase tabel
    supplierinvoiceno= models.CharField(max_length=225,default=True)
    partyAccntname = models.CharField(max_length=225,default=True)
    currentbalancep = models.CharField(max_length=225,null=True)
    currentbalancepl = models.CharField(max_length=225,null=True)
    purchaseledger = models.CharField(max_length=225,default=True)
    nameofitem=models.CharField(max_length=225,null=True)
    quantity=models.IntegerField(null=True)
    price=models.IntegerField(default=0)
    total=models.IntegerField(default=0)
    purchase_date=models.DateField(null=True) 
    #voucher=models.ForeignKey(Voucher,on_delete=models.CASCADE,blank=True,null=True)

# class Dispatchdetails(models.Model):#ann dispatch  tabel
#     supplierinvoiceno= models.CharField(max_length=225,default=True)
#     partyAccntname = models.CharField(max_length=225,default=True)
#     currentbalancep = models.CharField(max_length=225,null=True)
#     currentbalancepl = models.CharField(max_length=225,null=True)
#     purchaseledger = models.CharField(max_length=225,default=True)
#     nameofitem=models.CharField(max_length=225,null=True)
#     quantity=models.IntegerField(null=True)
#     price=models.IntegerField(default=0)
#     total=models.IntegerField(default=0)
#     purchase_date=models.DateField(null=True) 
#     #voucher=models.ForeignKey(Voucher,on_delete=models.CASCADE,blank=True,null=True)

class Currency(models.Model):
    symbol = models.CharField(max_length=225)
    formal_name = models.CharField(max_length=225)
    currency_code = models.CharField(max_length=225)
    decimal_places = models.CharField(max_length=225)
    show_in_millions = models.BooleanField(default=False)
    suffix_symbol = models.BooleanField(default=False)
    symbol_and_amount = models.BooleanField(default=False)
    after_decimal = models.CharField(max_length=225)
    amount_in_words = models.CharField(max_length=225)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

class Journal(models.Model):#ann journal table
     journalledger = models.CharField(max_length=225,null=True)
     journal_date=models.DateField(null=True)  

class Particular(models.Model):#ann Particular table
    particularsby = models.CharField(max_length=225,null=True)
    particularsto = models.CharField(max_length=225,null=True)
    credit = models.IntegerField(default=0,null=True)#current balance of party
    debit = models.IntegerField(null=True,default=0)#balance of corresponding sales ledger
    journal=models.ForeignKey(Journal,on_delete=models.CASCADE,blank=True,null=True)  
