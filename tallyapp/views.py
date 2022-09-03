from calendar import month
from datetime import date

from re import A, S
from this import s
from xml.etree.ElementTree import tostring
from django.db.models import Sum
from django.db.models.functions import TruncDay
from django.db.models.functions import TruncMonth
from django.db.models.functions import TruncDate
from django.db.models.functions import Extract
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count
from datetime import datetime
#from tallyapp.models import Sales, Purchase,Companies
def index(request):
    comp=Companies.objects.all()
    return render(request,'index.html',{'comp':comp})

def company(request):
    com=Companies.objects.all()
    return render(request,'company.html',{'com':com})
# Reports sales ,purchase and journal
 
     
def disp_more_reports(request):#ann
    com=Companies.objects.all()
    return render(request,'dispmorereprt.html')    

def salesregister(request):#ann
    credit=Sales.objects.all().annotate(month=TruncMonth('sales_date')).values('month').annotate(total=Sum('total')).order_by('month').values("month", "total")                 # Select the count of the grouping       
    sales=Sales.objects.all()
    print("hai")
    vol=[];
    s= credit[0]
    for s in  credit:
        # truncate_date = datetime(s["month"])
      print(s['total'])
    vol.append(s["total"])
    for x in vol:
      print(x)            
    total1 = sum(sales.values_list('total', flat=True)) 
    return render(request,'salesregister.html',{'sales':sales,'total1':total1,'credit':credit})   

def purchaseregister(request):#ann
    p=Purchase.objects.all()
    credit=Purchase.objects.all().annotate(month=TruncMonth('purchase_date')).values('month').annotate(total=Sum('total')).order_by('month').values("month", "total")                 # Select the count of the grouping       
    total1 = sum(p.values_list('total', flat=True))  
    return render(request,'purchaseregister.html',{'total1':total1,'credit':credit})   

def journalregister(request):#ann
    p=Particular.objects.all()
    s=Journal.objects.all()
    items=Journal.objects.all().annotate(month=TruncMonth('journal_date')).values('month').annotate(journal_count = Count('id')).values('month','journal_count').order_by('month')
    print(items)
    return render(request,'journal_report.html',{'items':items})
def ledgersummary(request):#ann
    l=ledgers_vouchers.objects.all()
    credit=ledgers_vouchers.objects.all().annotate(month=TruncMonth('ledgervoucher_date')).values('month').annotate(credit=Sum('credit')).order_by('month').values("month", "credit")                 # Select the count of the grouping       
    total1 = sum(l.values_list('credit', flat=True))  
    return render(request,'ledgersummary.html',{'total1':total1,'credit':credit}) 
  
def listofledgers(request,pk):#ann
   # s=ledgers_vouchers.objects.all()
    m=pk
    l= ledgers_vouchers.objects.filter(ledgervoucher_date='2022', 
                     sales_date__month=m)
 
    total1 = sum(l.values_list('credit', flat=True))               
       
    if m==1:
            msg1="1-Jan-22  to 31-jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
        
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 31-May-22"
    elif m ==7:
            msg1="1-july-22  to 31-july-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 30-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 31-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"     
    else:
        msg1="July 01 to 31" 
    return render(request,'currentliablities.html',{'ledgers':l,'msg1':msg1,'total1':total1})     

def listofpurchasevoucher(request,pk):#ann
    m=pk
    p= Purchase.objects.filter(purchase_date__year='2022', 
                     purchase_date__month=m)   
    total1 = sum(p.values_list('total', flat=True))                             
    if m==1:
            msg1="1-Jan-22  to 31-jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 31-May-22"
    elif m ==7:
            msg1="1-july-22  to 31-july-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 30-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 31-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"      
    else:
        msg1="July 01 to 31"               
    return render(request,'listofpurchasevouchers.html',{'purchase':p,'msg1':msg1,'total1':total1})
    
def listofsalesvoucher(request,pk):#ann
   # s=Sales.objects.all()
    m=pk
    s= Sales.objects.filter(sales_date__year='2022', 
                     sales_date__month=m)
 
    total1 = sum(s.values_list('total', flat=True))               
       
    if m==1:
            msg1="1-Jan-22  to 31-jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
        
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 31-May-22"
    elif m ==7:
            msg1="1-july-22  to 31-july-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 30-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 31-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"     
    else:
        msg1="July 01 to 31" 
    return render(request,'listofsalesvouchers.html',{'sales':s,'msg1':msg1,'total1':total1})     

def listofpurchasevoucher(request,pk):#ann
    m=pk
    p= Purchase.objects.filter(purchase_date__year='2022', 
                     purchase_date__month=m)   
    total1 = sum(p.values_list('total', flat=True))                             
    if m==1:
            msg1="1-Jan-22  to 31-jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 31-May-22"
    elif m ==7:
            msg1="1-july-22  to 31-july-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 30-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 31-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"      
    else:
        msg1="July 01 to 31"               
    return render(request,'listofpurchasevouchers.html',{'purchase':p,'msg1':msg1,'total1':total1})
    
def listjournalvouchers(request,pk):#ann 
    m=pk
    j= Journal.objects.filter(journal_date__year='2022', 
                     journal_date__month=m)   
                          
    if m==1:
            msg1="1-Jan-22  to 31-jan-22"
    elif m==2:
            msg1="1-Feb-22  to 28-feb-22"
    elif m ==3:
            msg1="1-March-22  to 31-March-22"
    elif m ==4:
             msg1="1-April-22 to 30-April-22"
    elif m ==5:
             msg1="1-May-22  to 31-May-22"
    elif m ==6:
            msg1="1-June-22 to 31-May-22"
    elif m ==7:
            msg1="1-july-22  to 31-july-22"
    elif m ==8:
             msg1="1-Aug-22  to 31-Aug-22"  
    elif m==9:
            msg1="1-Sep-22  to 30-Sep-22"
    elif m ==10:
             msg1="1-Oct-22 to 30-Oct-22"
    elif m ==11:
            msg1="1-Nov-22 to 31-Nov-22" 
    elif m ==12:
             msg1="1-Dec-22 to 31-Dec-22"      
    else:
        msg1="July 01 to 31"                        
    return render(request,'listjournalvouchers.html',{'journal':j,'msg1':msg1})

def index1(request):
    return render(request,'basepage.html')

def voucher1(request):
    return render(request,'vouchertype.html')  
def sales(request):#ann
    sal=Sales.objects.all
    return render(request,'sales.html',{'sale':sal})      
def saleview(request,pk):#ann
    sal=Sales.objects.get(id=pk)
    print(sal)
    return render(request,'saleview.html',{'sale':sal}) 

def purchaseview(request,pk):#ann
    p=Purchase.objects.get(id=pk)
    print(p)
    return render(request,'purchaseview.html',{'purchase':p})       

def purchase(request):#ann
    return render(request,'purchase.html')    

def journal(request):#ann
    return render(request,'journal.html')

def sales_add (request):#ann
 if request.method=="POST":
    partyAc=request.POST.get('Party_name') 
    sales_date=request.POST.get('Date')
    currentp=request.POST.get('current_ac_balancep')
    currentbl=request.POST.get('current_ac_balancesl')
    Item_name=request.POST.get('Item_name')
    quantity1=request.POST.get('quantity')
    price1=request.POST.get('rate')
    salesle=request.POST.get('salesledger')
    total1=request.POST.get('amount')
    sales=Sales(partyAccntname=partyAc,sales_date=sales_date,salesledger=salesle,currentbalancesl=currentbl,currentbalancep=currentp,nameofitem=Item_name,quantity=quantity1,price=price1,total=total1)
    sales.save()
    messages.info(request,'Sale entered successfully')
    #return redirect('/')  
    return render(request,'sales.html')     


def purchase_add(request):#ann
 if request.method=="POST":
    supplierinvoiceno=request.POST.get('Suppliernumber') 
    partyAc=request.POST.get('Party_name') 
    purchase_date=request.POST.get('Date')
    currentbalancep =request.POST.get('current_ac_balancep')
    currentbalancepl =request.POST.get('current_ac_balancel')
    quantity1=request.POST.get('quantity')
    price1=request.POST.get('rate')
    total1=request.POST.get('amount')
    nameofitem=request.POST.get('Item_name')
    purchasele=request.POST.get('purchaseledger')
    purchase=Purchase(supplierinvoiceno=supplierinvoiceno,partyAccntname=partyAc,purchase_date=purchase_date,purchaseledger=purchasele,currentbalancepl =currentbalancepl ,currentbalancep=currentbalancep,nameofitem=nameofitem,quantity=quantity1,price=price1,total=total1)
    purchase.save()
    print("purchase")
    messages.info(request,'Purchase entered successfully')
    return render(request,'purchase.html',)    
    #return redirect('/')      

def showvouchers(request):
    return render(request,'listofvouchertypes.html')    
      
def getStates(request):
    return States.objects.all()

def createcompany(request):
    com=States.objects.all()
    country=Countries.objects.all()
    return render(request,'createcompany.html',{'com':com,'country':country})

def companycreate(request):
    
    if request.method=='POST':
            name=request.POST['name']
            mailing_name=request.POST['mailing_name']
            address1=request.POST['address1']
            address2=request.POST['address2']
            address3=request.POST['address3']
            address4=request.POST['address4']
            state=request.POST['state']
            country=request.POST['country']
            #stateId= request.POST['statehidden']
            #print('fghj')
            
            state=States.objects.get(name=state) 
            country=Countries.objects.get(name=country) 
            pincode=request.POST['pincode']
            telephone=request.POST['telephone']
            mobile=request.POST['mobile']
            fax=request.POST['fax']
            email=request.POST['email']
            website=request.POST['website']
            fin_begin=request.POST['fin_begin']
            books_begin=request.POST['books_begin']
            currency_symbol=request.POST['currency_symbol']
            formal_name=request.POST['formal_name']
            cmp=Companies.objects.filter(name=name)
            if cmp:
                messages.info(request,'Company name already exists!!')
                return redirect('createcompany')
            else:
                ctg=Companies(name=name,mailing_name=mailing_name,address1=address1,address2=address2,address3=address3,
                    address4=address4,
                    state=state,country=country,
                    pincode=pincode,
                    telephone=telephone,mobile=mobile,fax=fax,email=email,website=website,fin_begin=fin_begin,
                    books_begin=books_begin,currency_symbol=currency_symbol,formal_name=formal_name)
                ctg.save()
            
            
             
            
            
            demo1(request, ctg.id)
            
            # return redirect('companycreated')
            return render(request,'features.html',{'ctg':ctg})
    return render(request,'createcompany.html')

def groupsummary(request):#ann
    pk=1
    subg=SubGroup.objects.filter(group_id=pk)
    return render(request,'groupsummary.html',{'subgrp':subg})
    
def ledgergroupsummary(request,pk):#ann
    m=pk  
    ledg=ledgers.objects.filter(SubGroup_id=m)
    return render(request,'ledgergroupsummary.html',{'ledg':ledg})  
def ledgersummary(request,lk):#ann
   # ledgname=ledgers.objects.filter(id=lk)
    ledgname =ledgers.objects.get(id=lk)
    #v=ledgers_vouchers.objects.filter(ledgers_id=lk)
    v=ledgers_vouchers.objects.filter(ledgers_id=lk).annotate(month=TruncMonth('ledgervoucher_date')).values('month').annotate(credit=Sum('credit')).order_by('month').values("month", "credit").annotate(debit=Sum('debit')).order_by('month').values("month", "debit")                                  # Select the count of the grouping       qa23
    #ledgname=ledgers.objects.values_list('id', 'ledger')
    print(v)
    return render(request,'ledgersummary.html',{'name':ledgname,'v':v})       

   
def ledger(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        #ledger
        name = request.POST['name']
        alias = request.POST['alias']
        under = request.POST['under']
        provide_banking_details = request.POST['provide_banking_details']
        pan_no = request.POST['pan_no']
        
        #mailing_details
        mailingname = request.POST['mailingname']
        address = request.POST['address']
        state = request.POST['state']
        country = request.POST['country']
        pincode = request.POST['pincode']
        
        #banking_details
        od_limit= request.POST['od_limit']
        holder_name = request.POST['holder_name']
        acc_no = request.POST['acc_no']
        ifsc = request.POST['ifsc']
        swift_code = request.POST['swift_code']
        bank_name = request.POST['bank_name']
        branch = request.POST['branch']
        set_cheque = request.POST['set_cheque']
        ch_printing = request.POST['ch_printing']
        ch_config = request.POST['ch_config']
        
        #Asset_rounding
        rounding_method=request.POST['rounding_method']
        round_limit=request.POST['round_limit']
        
        #Asset_statutory
        assessable_calculation=request.POST['assessable_calculation']
        appropriate_to=request.POST['appropriate_to']
        gst_applicable=request.POST['gst_applicable']
        set_alter_GST=request.POST['set_alter_GST']
        type_of_supply=request.POST['type_of_supply']
        method_of_calc=request.POST['method_of_calc']
        
        
        led=Ledger.objects.filter(name=name)
        if led:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            data = Ledger(name=name,alias=alias,under=under,provide_banking_details=provide_banking_details,
                            pan_no=pan_no,company=cmp)
            data.save()
            
            #mailing_details
            data1=Ledger_Mailing_Details(mailingname=mailingname,address=address,state=state,country=country,pincode=pincode,
                                        company=cmp,ledger=data)
            data1.save()
            
            #banking_details
            data2=Ledger_Banking_Details(od_limit=od_limit,holder_name=holder_name,acc_no=acc_no,ifsc=ifsc,swift_code=swift_code,bank_name=bank_name,
                                        branch=branch,set_cheque=set_cheque,ch_printing=ch_printing,ch_config=ch_config,
                                        company=cmp,ledger=data)
            data2.save()
            
            #Asset_rounding
            data3=Ledger_Asset_Rounding(rounding_method=rounding_method,round_limit=round_limit,
                                        company=cmp,ledger=data)
            data3.save()
            
            #Asset_statutory
            data4=Ledger_Asset_Statutory(assessable_calculation=assessable_calculation,appropriate_to=appropriate_to,
                                         gst_applicable=gst_applicable,set_alter_GST=set_alter_GST,type_of_supply=type_of_supply,
                                         method_of_calc=method_of_calc,company=cmp,ledger=data)
            data4.save()
            
            
    grup=Group.objects.filter(company_id=cmp)
    return render(request,'ledger.html',{'cmp':cmp,'grup':grup})

def costcentre(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        cname = request.POST['cname']
        alia = request.POST['alia']
        under = request.POST['under']
        costc=Costcentre.objects.filter(cname=cname)
        if costc:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            
            data = Costcentre(cname=cname,alias=alia,under=under,company=cmp)
            data.save()
        # return redirect('costcentre')
    ccentre=Costcentre.objects.filter(company_id=cmp)
    return render(request,'costcentre.html',{'cmp':cmp,'ccentre':ccentre})


def ratesofexchange(request,pk):
    cmp=Companies.objects.get(id=pk)
    cur=Currency.objects.filter(company_id=cmp)
    return render(request,'ratesofexchange.html',{'cmp':cmp,'cur':cur})

def voucher(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        Vname = request.POST['nam']
        alias = request.POST['alias']
        vtype = request.POST['vtype']
        abbre = request.POST['abbre']
        activ_vou_typ = request.POST['avtyp']  # bool
        meth_vou_num = request.POST['meth_vou_num']
        useadv = request.POST.get('useadvc', False)
        prvtdp = request.POST.get('prvtdp', False)
        use_effct_date = request.POST['uefftdate']  # bool
        allow_zero_trans = request.POST['allow_zero_trans']  # bool
        allow_naration_in_vou = request.POST['allow_naration_in_vou']  # bool
        optional = request.POST['optional'] 
        provide_narr = request.POST['providenr']  # bool
        print = request.POST['print']  # bool

        if Voucher.objects.filter(voucher_name=Vname).exists():
               pass
        
        mdl = Voucher(

            voucher_name=Vname,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_effective_date=use_effct_date,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            allow_naration_in_voucher=allow_naration_in_vou,
            make_optional=optional,
            provide_naration=provide_narr,
            print_voucher=print,
            company=cmp

        )
        mdl.save()
    return render(request,'voucher.html',{'cmp':cmp})

def currency(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        symbol = request.POST['symbol']
        formal_name = request.POST['formal_name']
        currency_code = request.POST['currency_code']
        decimal_places = request.POST['decimal_places']
        show_in_millions = request.POST['show_in_millions']
        suffix_symbol = request.POST['suffix_symbol']
        symbol_and_amount = request.POST['symbol_and_amount']
        after_decimal = request.POST['after_decimal']
        amount_in_words = request.POST['amount_in_words']
        data = Currency(symbol=symbol,formal_name=formal_name,currency_code=currency_code,
                        decimal_places=decimal_places,show_in_millions=show_in_millions,
                        suffix_symbol=suffix_symbol,symbol_and_amount=symbol_and_amount,
                        after_decimal=after_decimal,amount_in_words=amount_in_words,company=cmp)
        data.save()
        # return redirect('costcentre')
    return render(request,'currency.html',{'cmp':cmp})




def creategroup(request,pk):
    cmp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        cmp=Companies.objects.get(id=pk)
        gname = request.POST['gname']
        alia = request.POST['alia']
        under = request.POST['under']
        sub_ledger = request.POST['sub_ledger']
        nett = request.POST['nee']
        calc = request.POST['cal']
        meth = request.POST['meth']
        grp=Group.objects.filter(name=gname)
        if grp:
            # messages.info(request,'Company name already exists!!')
            pass
        else:
            mdl = Group(
                name=gname,
                alias=alia,
                under=under,
                sub_ledger=sub_ledger,
                debit_credit=nett,
                calculation=calc,
                used_purchase=meth,
                company=cmp
            )
            mdl.save()
        # return redirect('index')
    grup=Group.objects.filter(company_id=cmp)
    return render(request,'group.html',{'cmp':cmp,'grup':grup})
    
def altercompanyview(request):
    com=Companies.objects.all()
    return render(request,'altercompanyview.html' ,{'com':com})


def altercompany(request,pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        comp.name=request.POST['name']
        comp.mailing_name=request.POST['mailing_name']
        comp.address1=request.POST['address1']
        comp.address2=request.POST['address2']
        comp.address3=request.POST['address3']
        comp.address4=request.POST['address4']
            # state=request.POST['state']
            # country=request.POST['country']
        comp.pincode=request.POST['pincode']
        comp.telephone=request.POST['telephone']
        comp.mobile=request.POST['mobile']
        comp.fax=request.POST['fax']
        comp.email=request.POST['email']
        comp.website=request.POST['website']
        comp.fin_begin=request.POST['fin_begin']
        comp.books_begin=request.POST['books_begin']
            # currency_symbol=request.POST['currency_symbol']
            # formal_name=request.POST['formal_name']
        comp.save()
        return redirect('altercompanyview', {'comp':comp})
    return render(request,'editcompany.html',{'comp':comp})

def selectcompany(request):
    com=Companies.objects.all()
    return render(request,'selectcompany.html',{'com':com})

def addstate(request):
    if request.method=='POST':
        name=request.POST['name']
        st=States.objects.filter(name=name)
        if st:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            data=States(name=name)
            data.save()
            return redirect('createcompany')
    return render(request,'createcompany.html')
def addcountry(request):
    if request.method=='POST':
        name=request.POST['name']
        con=Countries.objects.filter(name=name)
        if con:
            # messages.info(request,'Company name already exists!!')
            return redirect('createcompany')
        else:
            data=Countries(name=name)
            data.save()
        return redirect('createcompany')
    return render(request,'createcompany.html')

def featurecompany(request,pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        maintain_accounts=request.POST['maintain_accounts']
        ctg=features(maintain_accounts=maintain_accounts, company= comp)
        ctg.save()
    return render(request,'company.html')
def democreate(request):
    return render(request,'democreate.html')

def demo1(request, pk):
    comp=Companies.objects.get(id=pk)
    if request.method == 'POST':
        #maintain_accounts=request.POST['maintain_accounts']
        ctg=Features(company= comp)
        ctg.save()
    return render(request,'company.html')

def features(request, pk):
    feature=Features.objects.get(company_id=pk)
    c=Companies.objects.get(id=pk)
    if request.method == 'POST':
        if request.POST['maintain_accounts'] == 'Yes':
            feature.maintain_accounts= 'True'
        else:
            feature.maintain_accounts= 'False'
        if request.POST['bill_wise_entry'] == 'Yes':
            feature.bill_wise_entry= 'True'
        else:
            feature.bill_wise_entry= 'False'
        feature.save()
    return render(request,'features.html',{'ctg':c, 'ft':feature})


def shutcompany(request):
    com=Companies.objects.all()
    return render(request,'shutcompany.html',{'com':com})

def disable(request,pk):
    c=Companies.objects.get(id=pk)
    c.active=False
    c.save()
    return redirect('shutcompany')


def enable(request,pk):
    c=Companies.objects.get(id=pk)
    c.active=True
    c.save()
    return redirect('shutcompany')
def alter(request):
    com=Companies.objects.all()
    return render(request,'altercompany.html')
def dispatch_details(request):#ann dispatch details
     return render(request,'dispatch_details.html')    
def partydetails(request):
    com=Companies.objects.all()
    return render(request,'partydetails.html')      

def altercompany_view(request):
    com=Companies.objects.all()
    return render(request,'altercompanyview1.html',{'com':com})

def listofgroup(request):
    com=Companies.objects.all()
    grp=Group.objects.all()
    return render(request,'listofgroup.html',{'com':com, 'grp':grp})
def listofsalesvouchers(request):#ann
    com=Companies.objects.all()
    grp=Group.objects.all()
    return render(request,'listofsalesvouchers.html')    

def listofledgers(request):
    com=Companies.objects.all()
    lgr=Ledger.objects.all()
    return render(request,'listofledgers.html',{'com':com, 'lgr':lgr})

def listofcostcentres(request):
    com=Companies.objects.all()
    return render(request,'listofcostcentres.html',{'com':com})

def listofcurrencies(request):
    com=Companies.objects.all()
    cur=Currency.objects.all()
    return render(request,'listofcurrencies.html',{'com':com, 'cur':cur})

def listofvouchertypes(request):
    com=Companies.objects.all()
    vhr=Voucher.objects.all()
    return render(request,'listofvouchertypes.html',{'com':com, 'vhr':vhr})
