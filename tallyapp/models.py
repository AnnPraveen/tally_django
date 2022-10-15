from pickle import TRUE
from tkinter import FALSE
from django.db import models

class Countries(models.Model):
    name=models.CharField(max_length=225)
    

    
class States(models.Model):
    name=models.CharField(max_length=225)
    country=models.ForeignKey(Countries,on_delete=models.CASCADE,blank=True,null=True)
    
class Companies(models.Model):#ann(for my display)
    d_path=models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=240, null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20,null=True)
    formal_name = models.CharField(max_length=20,null=True)
    fin_begin = models.DateField(null=True)
    books_begin = models.DateField(null=True)
    fin_end = models.DateField(null=True)
    status=models.BooleanField(default=True)
   
class Months(models.Model):
    month_name = models.CharField(max_length=255)  
     
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
      group=models.ForeignKey(Group,on_delete=models.CASCADE,blank=True,null=True)
      
class ledgers_vouchers(models.Model):
    Voucher=models.ForeignKey(Voucher,on_delete=models.CASCADE,blank=True,null=True)
    Group =models.ForeignKey(Group ,on_delete=models.CASCADE,blank=True,null=True)
    SubGroup =models.ForeignKey(SubGroup ,on_delete=models.CASCADE,blank=True,null=True)
    ledgers =models.ForeignKey(ledgers ,on_delete=models.CASCADE,blank=True,null=True)
    ledgervoucher_date=models.DateField(null=True)
    credit= models.IntegerField(default=0)#ledger credit
    debit= models.IntegerField(default=0)#ledger debit
    closingbalance=models.IntegerField(default=0)#closing balance
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)    

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
     particularsto = models.CharField(max_length=225,null=True)
     total=models.IntegerField(default=0)
     credit = models.IntegerField(default=0,null=True)#current balance of party
     debit = models.IntegerField(null=True,default=0)#balance of corresponding sales ledger   
     

class Particular(models.Model):#ann Particular table
    particularsby = models.CharField(max_length=225,null=True)
    particularsto = models.CharField(max_length=225,null=True)
    credit = models.IntegerField(default=0,null=True)#current balance of party
    debit = models.IntegerField(null=True,default=0)#balance of corresponding sales ledger
    journal=models.ForeignKey(Journal,on_delete=models.CASCADE,blank=True,null=True)  
######NITHYA
class tally_group(models.Model):
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    group_name = models.CharField(max_length=255)
    group_alias = models.CharField(max_length=255)
    group_under = models.CharField(max_length=255)
    nature = models.CharField(max_length=255,null=True)
    gross_profit = models.CharField(max_length=255 ,null=True)
    sub_ledger = models.CharField(max_length=255)
    debit_credit = models.CharField(max_length=255)
    calculation = models.CharField(max_length=255)
    invoice = models.CharField(max_length=255)

class tally_ledger(models.Model):
    c_balance = models.IntegerField(null = True,blank = True)
    c_type = models.CharField(max_length=100,null=True,blank = True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255,null=True)
    under = models.CharField(max_length=255)
    grp = models.ForeignKey(tally_group,on_delete = models.CASCADE,null = True)
    mname = models.CharField(max_length=255,null=True)
    address = models.CharField(max_length=255,null=True)
    state = models.CharField(max_length=255,null=True)
    country = models.CharField(max_length=255,null=True)
    pincode = models.CharField(max_length=6,null=True)
    bank_details = models.CharField(max_length=20,null=True)
    pan_no = models.CharField(max_length=100,null=True)
    registration_type = models.CharField(max_length=100,null=True)
    gst_uin = models.CharField(max_length=100,null=True)
    set_alter_gstdetails = models.CharField(max_length=100,null=True)
    opening_blnc = models.IntegerField(null=True)

    set_odl = models.CharField(max_length=255,null=True)
    ac_holder_nm = models.CharField(max_length=255,null=True)
    acc_no = models.CharField(max_length=255,null=True)
    ifsc_code = models.CharField(max_length=255,null=True)
    swift_code = models.CharField(max_length=255,null=True)
    bank_name = models.CharField(max_length=255,null=True)
    branch = models.CharField(max_length=255,null=True)
    SA_cheque_bk = models.CharField(max_length=20,null=True)
    Echeque_p = models.CharField(max_length=20,null=True)
    SA_chequeP_con = models.CharField(max_length=20,null=True)
    
    type_of_ledger = models.CharField(max_length=100,null=True)
    rounding_method = models.CharField(max_length=100,null=True)
    rounding_limit = models.IntegerField(blank=True, null=True, default=None)

    type_duty_tax = models.CharField(max_length=100,null=True)
    tax_type = models.CharField(max_length=100,null=True)
    valuation_type = models.CharField(max_length=100,null=True)
    rate_per_unit = models.IntegerField(blank=True, null=True, default=None)
    percentage_of_calcution = models.CharField(max_length=100,null=True)
    rond_method = models.CharField(max_length=100,null=True)
    rond_limit = models.IntegerField(blank=True, null=True, default=None)

    gst_applicable = models.CharField(max_length=100,null=True)
    setalter_gstdetails = models.CharField(max_length=20,null=True)
    type_of_supply = models.CharField(max_length=100,null=True)
    assessable_value = models.CharField(max_length=100,null=True)
    appropriate_to = models.CharField(max_length=100,null=True)
    method_of_calculation = models.CharField(max_length=100,null=True)

    balance_billbybill = models.CharField(max_length=100,null=True)
    credit_period = models.CharField(max_length=100,null=True)
    creditdays_voucher = models.CharField(max_length=100,null=True)
    c_balance = models.IntegerField(null = True,blank = True)
    closing_balance=models.FloatField(default=0)

class Ledger_vouchers_new(models.Model):
    
    ledger = models.ForeignKey(tally_ledger, on_delete=models.CASCADE, blank=True,null=True)
    group = models.ForeignKey(tally_group, on_delete=models.CASCADE, blank=True,null=True)

    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    date=models.DateField()
    particulars=models.CharField(max_length=225)
    account=models.CharField(max_length=225,null=True)
    voucher_type=models.CharField(max_length=225,null=True)
    voucher_no=models.CharField(max_length=225)
    debit=models.IntegerField(null=True)
    credit=models.IntegerField(null = True)

class total_balance(models.Model):
    company = models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)

    group = models.ForeignKey(tally_group, on_delete=models.CASCADE, blank=True,null=True)

    total_debit = models.IntegerField(null=True)
    total_credit = models.IntegerField(null = True)
    total= models.IntegerField(null = True) 


################profit and lose

  
class stock_item_crt(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)
    units=models.CharField(max_length=100,null=True)
    batches=models.CharField(max_length=100,null=True)
    manufacturing_date=models.CharField(max_length=100,null=True)
    expiry_dates=models.CharField(max_length=100,null=True)
    rate_of_duty=models.CharField(max_length=100,null=True)
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)
    additional=models.CharField(max_length=100,null=True)
    
    
    
    
class CreateStockGrp(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)
    quantities=models.CharField(max_length=50)


class group_summary(models.Model):
    CreateStockGrp=models.ForeignKey(CreateStockGrp, on_delete=models.CASCADE)
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=100,null=True)
    units=models.CharField(max_length=100,null=True)
    batches=models.CharField(max_length=100,null=True)
    manufacturing_date=models.CharField(max_length=100,null=True)
    expiry_dates=models.CharField(max_length=100,null=True)
    rate_of_duty=models.CharField(max_length=100,null=True)
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)
    additional=models.CharField(max_length=100,null=True)
    
    
    
class payhead_crt(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    payhead_type=models.CharField(max_length=100,null=True)
    income_type=models.CharField(max_length=100,null=True)
    under_name=models.CharField(max_length=100,null=True)
    net_salary=models.CharField(max_length=100,null=True)
    pay_slip_name=models.CharField(max_length=100,null=True)
    currency_ledger=models.CharField(max_length=100,null=True)
    calculation_type=models.CharField(max_length=100,null=True)
    attendance_type=models.CharField(max_length=100,null=True)
    production_type=models.CharField(max_length=100,null=True)   
    
    
    
    

class create_payhead(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    income_type=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    affect_net=models.CharField(max_length=225)
    payslip=models.CharField(max_length=225)
    calculation_of_gratuity=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)
    calculation_period=models.CharField(max_length=225)
    leave_withpay=models.CharField(max_length=225)
    leave_with_out_pay=models.CharField(max_length=225)
    production_type=models.CharField(max_length=225)
    opening_balance=models.CharField(max_length=225)
    compute=models.CharField(max_length=225,default="Null")
    effective_from=models.CharField(max_length=225,default="NULL")
    amount_greater=models.CharField(max_length=225,default="NULL")
    amount_upto=models.CharField(max_length=225,default="NULL")
    slab_type=models.CharField(max_length=225,default="NULL")
    value=models.CharField(max_length=225,default="NULL")
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)
    days_of_months=models.CharField(max_length=225)
    number_of_months_from=models.CharField(max_length=225)
    to=models.CharField(max_length=225)
    calculation_per_year=models.CharField(max_length=225)
    
    
    
    
        
class Ledger(models.Model):
    ledger_name = models.CharField(max_length=225,default="Null",blank=True)
    ledger_alias = models.CharField(max_length=225,default="Null",blank=True)
    group_under =  models.CharField(max_length=225,default="Null",blank=True)
    ledger_opening_bal = models.CharField(max_length=225,default="Null",blank=True)
    ledger_cr_db=models.CharField(max_length=225,default="Null",blank=True)
    ledger_type = models.CharField(max_length=225,default="Null",blank=True)
    provide_banking_details =  models.CharField(max_length=225,default="Null",blank=True)

    def __str__(self):
        return self.ledger_name


class Ledger_Banking_Details(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    od_limit = models.CharField(max_length=225,default="Null",blank=True)
    holder_name =models.CharField(max_length=225,default="Null",blank=True)
    ac_number =models.CharField(max_length=225,default="Null",blank=True)
    ifsc =models.CharField(max_length=225,default="Null",blank=True)
    swift_code =models.CharField(max_length=225,default="Null",blank=True)
    bank_name = models.CharField(max_length=225,default="Null",blank=True)
    branch_name = models.CharField(max_length=225,default="Null",blank=True)
    alter_chk_bks =  models.CharField(max_length=225,default="Null",blank=True)
    enbl_chk_printing =  models.CharField(max_length=225,default="Null",blank=True)
    chqconfg= models.CharField(max_length=225,default="Null",blank=True)

class Ledger_Mailing_Address(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=225,default="Null",blank=True)
    address = models.CharField(max_length=225,default="Null",blank=True)
    state = models.CharField(max_length=225,default="Null",blank=True)
    country =models.CharField(max_length=225,default="Null",blank=True)
    pincode =models.CharField(max_length=225,default="Null",blank=True)


class Ledger_Tax_Register(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    gst_uin = models.CharField(max_length=225,default="Null",blank=True)
    register_type =models.CharField(max_length=225,default="Null",blank=True)
    pan_no = models.CharField(max_length=225,default="Null",blank=True)
    alter_gst_details = models.CharField(max_length=225,default="Null",blank=True)


class Ledger_Satutory(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    assessable_calculation = models.CharField(max_length=225,default="Null",blank=True)
    Appropriate_to =models.CharField(max_length=225,default="Null",blank=True)
    gst_applicable = models.CharField(max_length=225,default="Null",blank=True)
    Set_alter_GST =models.CharField(max_length=225,default="Null",blank=True)
    type_of_supply = models.CharField(max_length=225,default="Null",blank=True)
    Method_of_calc=models.CharField(max_length=225,default="Null",blank=True)

class Ledger_Rounding(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)

class ledger_tax(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    type_of_duty_or_tax =models.CharField(max_length=225,default="Null",blank=True)
    type_of_tax =models.CharField(max_length=225,default="Null",blank=True)
    valuation_type=models.CharField(max_length=225,default="Null",blank=True)
    rate_per_unit =models.CharField(max_length=225,default="Null",blank=True)
    Persentage_of_calculation=models.CharField(max_length=225,default="Null",blank=True)
   

class Ledger_sundry(models.Model):
    ledger_id = models.ForeignKey(Ledger, on_delete=models.CASCADE, null=True, blank=True)
    maintain_balance_bill_by_bill =models.CharField(max_length=225,default="Null",blank=True)
    Default_credit_period=models.CharField(max_length=225,default="Null",blank=True)
    Check_for_credit_days=models.CharField(max_length=225,default="Null",blank=True)    
    
class add_voucher(models.Model):
    date=models.CharField(max_length=225)
    particular=models.CharField(max_length=225)
    voucher_type=models.CharField(max_length=225)
    voucher_number=models.CharField(max_length=225)
    quntity=models.CharField(max_length=225)
    value=models.CharField(max_length=225)   
        
    def __str__(self):
        return self.particular    
    
    

class add_voucher2(models.Model):
    date=models.CharField(max_length=225,default="Null",blank=True)
    particular=models.CharField(max_length=225,default="Null",blank=True)
    voucher_type=models.CharField(max_length=225,default="Null",blank=True)
    voucher_number=models.CharField(max_length=225,default="Null",blank=True)
    debit=models.CharField(max_length=225,default="Null",blank=True)
    credit=models.CharField(max_length=225,default="Null",blank=True)

    def _str_(self):
        return self.particular    
    
    
    

class add_voucher3(models.Model):
    date=models.CharField(max_length=225,default="Null",blank=True)
    particular=models.CharField(max_length=225,default="Null",blank=True)
    voucher_type=models.CharField(max_length=225,default="Null",blank=True)
    voucher_number=models.CharField(max_length=225,default="Null",blank=True)
    debit=models.CharField(max_length=225,default="Null",blank=True)
    credit=models.CharField(max_length=225,default="Null",blank=True)

    def _str_(self):
        return self.particular    
        
###############Neethu
class Stock_closingbalance(models.Model):
    stock_group=models.IntegerField(null=True)
    stock_item=models.IntegerField(null=True)
    closing_balance=models.FloatField()
class Ledger_vouchers(models.Model):
    ledger = models.ForeignKey(tally_ledger, on_delete=models.CASCADE, blank=True,null=True)
    company=models.ForeignKey(Companies,on_delete=models.CASCADE,blank=True,null=True)
    date=models.DateField()
    particulars=models.CharField(max_length=225)
    account=models.CharField(max_length=225,null=True)
    voucher_type=models.CharField(max_length=225,null=True)
    voucher_no=models.CharField(max_length=225)
    debit=models.IntegerField()
    credit=models.IntegerField()    



     


