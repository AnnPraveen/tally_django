from calendar import month  
from datetime import date
from re import A, S
from this import s
from typing import ValuesView
from xml.etree.ElementTree import tostring
from django.db.models import Sum
from django.db.models.functions import TruncDay
from django.db.models.functions import TruncMonth
from django.db.models.functions import TruncDate
from django.db.models.functions import Extract
import calendar
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format
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
    credit=Sales.objects.all().annotate(month=TruncMonth('sales_date')).values('month').annotate(total=Sum('total')).order_by('month').values("month", "total")      
    sales=Sales.objects.all()                     
    a=sales.filter(sales_date__month='04')
    april= sum(a.values_list('total',flat=True))
    ma=sales.filter(sales_date__month='05')
    may= sum(ma.values_list('total',flat=True))
    ju=sales.filter(sales_date__month='06')
    june= sum(ju.values_list('total',flat=True))
    jl=sales.filter(sales_date__month='07')
    july= sum(jl.values_list('total',flat=True))
    au=sales.filter(sales_date__month='08')
    august= sum(au.values_list('total',flat=True))
    sep=sales.filter(sales_date__month='09')
    september= sum(sep.values_list('total',flat=True))
    oct=sales.filter(sales_date__month='10')
    october= sum(oct.values_list('total',flat=True))
    nov=sales.filter(sales_date__month='11')
    november= sum(nov.values_list('total',flat=True))
    dec=sales.filter(sales_date__month='12')
    december= sum(dec.values_list('total',flat=True))
    jan=sales.filter(sales_date__month='01')
    january= sum(jan.values_list('total',flat=True))
    feb=sales.filter(sales_date__month='02')
    febuary= sum(feb.values_list('total',flat=True))
    m=sales.filter(sales_date__month='03')
    march= sum(m.values_list('total',flat=True))
    data={}
    data['april']=april
    data['june']=june
    data['july']=july
    data['august']=august
    data['september']=september
    data['october']=october
    data['november']=november
    data['december']=december
    data['january']=january
    data['febuary']=febuary
    data['march']=march 
    data['may']=may
    total1=sum(sales.values_list('total',flat=True)) 
    return render(request,'salesregister.html',{'total1':total1,'data':data})         

def purchaseregister(request):#ann
    P=Purchase.objects.all()
    a=P.filter(purchase_date__month='04')
    april= sum(a.values_list('total',flat=True))
    ma=P.filter(purchase_date__month='05')
    may= sum(ma.values_list('total',flat=True))
    ju=P.filter(purchase_date__month='06')
    june= sum(ju.values_list('total',flat=True))
    jl=P.filter(purchase_date__month='07')
    july= sum(jl.values_list('total',flat=True))
    au=P.filter(purchase_date__month='08')
    august= sum(au.values_list('total',flat=True))
    sep=P.filter(purchase_date__month='09')
    september= sum(sep.values_list('total',flat=True))
    oct=P.filter(purchase_date__month='10')
    october= sum(oct.values_list('total',flat=True))
    nov=P.filter(purchase_date__month='11')
    november= sum(nov.values_list('total',flat=True))
    dec=P.filter(purchase_date__month='12')
    december= sum(dec.values_list('total',flat=True))
    jan=P.filter(purchase_date__month='01')
    january= sum(jan.values_list('total',flat=True))
    feb=P.filter(purchase_date__month='02')
    febuary= sum(feb.values_list('total',flat=True))
    m=P.filter(purchase_date__month='03')
    march= sum(m.values_list('total',flat=True))
    data={}
    data['april']=april
    data['june']=june
    data['july']=july
    data['august']=august
    data['september']=september
    data['october']=october
    data['november']=november
    data['december']=december
    data['january']=january
    data['febuary']=febuary
    data['march']=march 
    data['may']=may
    
    
    total1 = sum(P.values_list('total', flat=True))  
    return render(request,'purchaseregister.html',{'total1':total1,'data':data}) 

def journalregister(request):#ann
    P=Journal.objects.all()
    april=P.filter(journal_date__month='04').count()
    may=P.filter(journal_date__month='05').count()
    june=P.filter(journal_date__month='06').count()
    july=P.filter(journal_date__month='07').count()
    august=P.filter(journal_date__month='08').count()
    september=P.filter(journal_date__month='09').count()
    october=P.filter(journal_date__month='10').count()
    november=P.filter(journal_date__month='11').count()
    december=P.filter(journal_date__month='12').count()
    january=P.filter(journal_date__month='01').count()
    febuary=P.filter(journal_date__month='02').count()
    march=P.filter(journal_date__month='03').count()
    data={}
    data['april']=april
    data['june']=june
    data['july']=july
    data['august']=august
    data['september']=september
    data['october']=october
    data['november']=november
    data['december']=december
    data['january']=january
    data['febuary']=febuary
    data['march']=march 
    data['may']=may
    return render(request,'journal_report.html',{'data':data})  

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
    total1 = sum(j.values_list('total', flat=True))                      
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
    return render(request,'listjournalvouchers.html',{'journal':j,'msg1':msg1,'total1':total1})
#...views
def listofledger(request,pk):#ann
   # s=ledgers_vouchers.objects.all()
    m=pk
    l= ledgers_vouchers.objects.filter(ledgervoucher_date__year='2022', 
                   ledgervoucher_date__month=m)
    total1=0
    total2=0
    total1 = sum(l.values_list('credit', flat=True)) 
    total2 = sum(l.values_list('debit', flat=True))               
       
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
    return render(request,'listofledger.html',{'ledgers':l,'msg1':msg1,'total1':total1,'total2':total2})     

def index1(request):
    return render(request,'basepage.html')

def voucher1(request):
    return render(request,'vouchertype.html')  
#def sales(request):#ann
    sal=Sales.objects.all
    return render(request,'sales.html',{'sale':sal})      
#def saleview(request,pk):#ann
    # sal=Sales.objects.get(id=pk)
    # print(sal)
    # return render(request,'saleview.html',{'sale':sal}) 

# def purchaseview(request,pk):#ann
#     p=Purchase.objects.get(id=pk)
#     print(p)
#     return render(request,'purchaseview.html',{'purchase':p})       

# def purchase(request):#ann
#     return render(request,'purchase.html')    

def journal(request):#ann
    return render(request,'journal.html')


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
#...........ann.....#

def balancesheet(request):#ann
    v1=ledgers_vouchers.objects.filter(Group_id=1)
    v2=ledgers_vouchers.objects.filter(Group_id=2)
    total1 = sum(v1.values_list('closingbalance', flat=True)) 
    total2 = sum(v2.values_list('closingbalance', flat=True)) 
    ##Nitya...
    t_id=1###(c)
    comp = Companies.objects.get(id=t_id)
    group= tally_group.objects.filter(company_id = comp.id)

        
    blnc = total_balance.objects.filter(company_id = comp.id)
    total = 0
    for g in group:
        for b in blnc:

            if b.total_debit > b.total_credit:
                
                total = b.total_debit - b.total_credit
            else:
                total = b.total_credit - b.total_credit

            b.total = total
            b.save()
    
    context = {
        'comp' : comp,
        'group':group,
        'balance' : blnc,
        'total':total,
        'total1':total1,
        'total2':total2,

    }
    print (context)
    return render(request,'balancesheet.html',context)     

def groupsummary(request,lk):#ann
    n=lk
    msg1="April 01 to 31" 
    if n==1:
     subg1=SubGroup.objects.filter(group_id=n).values('id')
     subg=SubGroup.objects.filter(group_id=n)
     list1=list(subg1)
    #  print(list1[1])
     vals =[]
     for p in  list1:
      vals+=list(p.values())
      print (vals)
      cont=len(vals)
      print(cont)
      n=vals[0]
      cd=ledgers_vouchers.objects.filter(SubGroup_id=n) 
      print(cd)
      c=sum(cd.values_list('credit',flat=True))
      print(c)  
      d=sum(cd.values_list('debit',flat=True))
      print(d)
      v=ledgers_vouchers.objects.filter(Group_id=1)
      total1 = sum(cd.values_list('closingbalance', flat=True)) 
      name="Current Liabilities"
      return render(request,'groupsummary.html',{'msg1':msg1,'subgrp':subg,'total1':total1,'c':c,'d':d})
    if n==2:
      name1="Branch/Divisions" 
      subg=SubGroup.objects.filter(group_id=n)
      ledg=ledgers.objects.filter(group_id=n)
      ledg1=ledgers.objects.filter(group_id=n).values('id')
      v=ledgers_vouchers.objects.filter(Group_id=2)
      list1=list(ledg1)
    #  print(list1[1])
      vals =[]
    for p in  list1:
      vals+=list(p.values())
      print (vals)
      cont=len(vals)
      print(cont)
    for t in vals: 
      n=vals[0]
      cd=ledgers_vouchers.objects.filter(Group_id=2) 
      print(cd)
      c=sum(cd.values_list('credit',flat=True))
      print(c)  
      d=sum(cd.values_list('debit',flat=True))
      print(d)
      total1 = sum(v.values_list('closingbalance', flat=True))  
      return render(request,'groupsummarydb.html',{'msg1':msg1,'ledg':ledg,'total1':total1,'c':c,'d':d})       
    


def ledgergroupsummary(request,pk):#ann
    m=pk  
    ledg=ledgers.objects.filter(SubGroup_id=m)  
    gname=SubGroup.objects.filter(id=m)
    # v=ledgers_vouchers.objects.filter(ledgers_id=m)
    # c=sum(v.values_list('credit',flat=True))
    # print(c)  
    # d=sum(v.values_list('debit',flat=True))
    v=ledgers_vouchers.objects.filter(Group_id=2) 
    c=sum(v.values_list('credit',flat=True))
    print(c)  
    d=sum(v.values_list('debit',flat=True))
    total1 = sum(v.values_list('closingbalance', flat=True))  
   
    return render(request,'ledgergroupsummary.html',{'ledg':ledg,'total1':total1,'v':v,'c':c,'d':d})

# def ledgersummary1(request,lk):#ann
#     ledgname =ledgers.objects.get(id=lk)
#     v=ledgers_vouchers.objects.filter(ledgers_id=lk).annotate(month=TruncMonth('ledgervoucher_date')).values('month').annotate(credit=Sum('credit'),debit=Sum('debit')).order_by('month').values("month", "credit","debit")                              
#     #ledgname=ledgers.objects.values_list('id', 'ledger')
   
    
#     return render(request,'ledgersummary1.html',{'name':ledgname,'v':v})     
          
def ledgersummary(request,lk):#ann
    ledgname =ledgers.objects.get(id=lk)
    v=ledgers_vouchers.objects.filter(ledgers_id=lk).annotate(month=TruncMonth('ledgervoucher_date')).values('month').annotate(credit=Sum('credit'),debit=Sum('debit')).order_by('month').values("month", "credit","debit")                              
    #ledgname=ledgers.objects.values_list('id', 'ledger')
    #v=ledgers_vouchers.objects.filter(ledgers_id=lk)
    c=sum(v.values_list('credit',flat=True))
    print(c)  
    d=sum(v.values_list('debit',flat=True))
    
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
# def dispatch_details(request):#ann dispatch details
#      return render(request,'dispatch_details.html')    
# def partydetails(request):
#     com=Companies.objects.all()
#     return render(request,'partydetails.html')      

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
####




def grp_month(request,pk):
    std=Ledger.objects.get(id=pk)
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch2:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-int(std.ledger_opening_bal)+total_credit
    if opening_balance>0 :
        std.ledger_type=opening_balance
        std.save()
        
    else :
        std.provide_banking_details=opening_balance*-1
        std.save()
            
    return render(request,'group_month.html',{'std':std,'vouch2':vouch2,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def grp_month_2(request,pk):
    std=Ledger.objects.get(id=pk)
    vouch3=add_voucher3.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch3:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_credit-int(std.ledger_opening_bal)+total_debit
    if opening_balance>0 :
        std.ledger_type=opening_balance
        std.save()
        
    else :
        std.provide_banking_details=opening_balance*-1
        std.save()
            
    return render(request,'grp_voucher.html',{'std':std,'vouch2':vouch3,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def sales_month(request,pk):
    std=Ledger.objects.get(id=pk)
    
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch2:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-int(std.ledger_opening_bal)+total_credit
    
    # std.ledger_type=opening_balance
    # std.save()
    
    return render(request,'sales_month.html',{'std':std,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def sales_month_2(request,pk):
    std=Ledger.objects.get(id=pk)
    
    vouch3=add_voucher3.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch3:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_credit-int(std.ledger_opening_bal)+total_debit
    
    # std.ledger_type=opening_balance
    # std.save()
    
    return render(request,'sales_income_month.html',{'std':std,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})


def payhead_month(request,pk):
    std=create_payhead.objects.get(id=pk)
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch2:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-int(std.opening_balance)+total_credit
    return render(request,'month_payhead.html',{'std':std,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def pay_voucher(request,pk):
    std=create_payhead.objects.get(id=pk)
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    
    for i in vouch2 :
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-int(std.opening_balance)+total_credit
    
    if opening_balance>0 :
        std.leave_withpay=opening_balance
        std.save()
        
    else :
        std.leave_with_out_pay=opening_balance*-1
        std.save()
    
    return render(request,'payhead_voucher.html',{'std':std,'vouch2':vouch2,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def stock_voucher(request,pk):
    std=group_summary.objects.get(id=pk)
    vouch=add_voucher.objects.all()
    total_value=0
    total_qunity=0
    total_val=int(std.value)
    total_qun=int(std.quantity)
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value +=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
    closing_qun=total_qun-total_qunity  
    closing_val=total_val-total_value 
    
    std.rate_of_duty=closing_val
    std.additional=closing_qun
    std.save()    
    
    context={
        'std':std,
        'vouch':vouch,
        'total_sales_value':total_value,
        'total_sales_quntity':total_qunity, 
        'total_purchase_value':total_val,
        'total_purchase_quntity':total_qun,
        'closing_qun':closing_qun,
        'closing_val':closing_val,
        }        
    return render(request,'stock_voucher.html',context)


def profit(request):
    balance=Ledger.objects.all()
    balance_py=create_payhead.objects.all()
    balance_le=Ledger.objects.all()
    balance_group=group_summary.objects.all()
    total_grp=0
    total_direct=0
    total=0
    total_income=0
    total_purch=0
    total_direct_exp=0
    total_indirect=0
    #sales account total
    for i in balance:
        if(i.group_under=='Sales_Account'):
            total+=int(i.ledger_type)
            total+=int(i.provide_banking_details)
            
    #indirect income total        
    for i in balance_py:
        if(i.under=='Income(Indirect)'):
            total_income+=int(i.leave_withpay)
            total_income+=int(i.leave_with_out_pay)
    for p in balance_le:
         if(p.group_under=='income_Indirect'):
             total_income+=int(p.ledger_type) 
             total_income+=int(p.provide_banking_details)
             
    #direct income total
             
    for i in balance_py:
        if(i.under=='Direct Incomes'):
            total_direct+=int(i.leave_withpay) 
            total_direct+=int(i.leave_with_out_pay) 
    
    for p in balance_le:
        if(p.group_under=='Direct Incomes'):
            total_direct+=int(p.ledger_type) 
            total_direct+=int(p.provide_banking_details)
            
    #closing stock
    for k in  balance_group:
        total_grp+=int(k.value)
        
    #purchase account total 
    
    for i in balance:
        if(i.group_under=='Purchase_Account'):
            total_purch+=int(i.ledger_type)
            total_purch+=int(i.provide_banking_details)
    
    #direct expenses total
           
    for i in balance_py:
        if(i.under=='Direct Expenses'):
            total_direct_exp+=int(i.leave_withpay) 
            total_direct_exp+=int(i.leave_with_out_pay)     
    
    for p in balance_le:
        if(p.group_under=='Direct Expenses'):
            total_direct_exp+=int(p.ledger_type) 
            total_direct_exp+=int(p.provide_banking_details) 
            
    #indirect expenses total   
    
    for i in balance_py:
        if(i.under=='Indirect Expenses'):
            total_indirect+=int(i.leave_withpay)
            total_indirect+=int(i.leave_with_out_pay)
    for p in balance_le:
         if(p.group_under=='Expences_Indirect'):
            total_indirect+=int(p.ledger_type) 
            total_indirect+=int(p.provide_banking_details)    
            
    #closing stock
    std=group_summary.objects.all()
    # vouch=add_voucher.objects.all()
    total_val=0
    total_qun=0
    # total_value=0
    # total_qunity=0
    
    # for i in vouch:
    #     if (i.voucher_type=='sales'):
    #         total_value+=int(i.value)
    #         total_qunity+=int(i.quntity)
    #     elif (i.voucher_type=='purchase'):
    #         total_val+=int(i.value) 
    #         total_qun+=int(i.quntity)
       
    # for p in std:
    #     total_val+=int(p.value)
    #     total_qun+=int(p.quantity)
                
    
    # closing_quntity=total_qun-total_qunity        
    
    for p in std:
        total_val+=int(p.rate_of_duty)
        total_qun+=int(p.additional)
        
    closing_value=total_val      
                   
    return render(request,'profit.html',{'total':total,'total_income':total_income,'total_direct':total_direct,'total_grp':total_grp,'total_purch':total_purch,'total_direct_exp':total_direct_exp,'total_indirect':total_indirect,'closing_value':closing_value,}) 





def  payhead_list(request):
    std=create_payhead.objects.filter(under='Direct Incomes')
    stm=Ledger.objects.filter(group_under='Direct Incomes')
    balance=create_payhead.objects.all()
    balance_le=Ledger.objects.all()
    total=0
    total_d=0
    for i in balance:
        if(i.under=='Direct Incomes'):
            total+=int(i.leave_withpay)
            total_d+=int(i.leave_with_out_pay)
    for p in balance_le:
         if(p.group_under=='Direct Incomes') :
             total+=int(p.ledger_type) 
             total_d+=int(p.provide_banking_details)
         
    
    
    return render(request,'payhead_items.html',{'std':std,'stm':stm,'total':total,'total_d':total_d}) 



def direct_exprenses(request):
    std=create_payhead.objects.filter(under='Direct Expenses')
    stm=Ledger.objects.filter(group_under='Direct Expenses')
    total=0
    total_d=0
    for i in std:
        total+=int(i.leave_withpay)
        total_d+=int(i.leave_with_out_pay)
    for p in stm:
        total+=int(p.ledger_type) 
        total_d+=int(p.provide_banking_details)
    return render(request,'direct_expenses.html',{'std':std,'stm':stm,'total':total,'total_d':total_d}) 

def sales(request):
    std=Ledger.objects.filter(group_under='Sales_Account')
    balance=Ledger.objects.all()
    total=0
    total_d=0
    for i in balance:
        if (i.group_under=='Sales_Account') :
            total+=int(i.ledger_type)
            total_d+=int(i.provide_banking_details)
        
                 
    return render(request,'sales_accounts.html',{'std':std,'total':total,'total_d':total_d})

def purchase(request):
    std=Ledger.objects.filter(group_under='Purchase_Account')
    
    total=0
    total_d=0
    for i in std:
        total+=int(i.ledger_type)
        total_d+=int(i.provide_banking_details)
    return render(request,'purchase_list.html',{'std':std,'total':total,'total_d':total_d})




def stock_month(request,pk):
    std=group_summary.objects.get(id=pk)
    
    vouch=add_voucher.objects.all()
    total_value=0
    total_qunity=0
    total_val=int(std.value)
    total_qun=int(std.quantity)
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value +=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
    closing_qun=total_qun-total_qunity  
    closing_val=total_val-total_value      
    context={
        'std':std,
        'vouch':vouch,
        'total_sales_value':total_value,
        'total_sales_quntity':total_qunity, 
        'total_purchase_value':total_val,
        'total_purchase_quntity':total_qun,
        'closing_qun':closing_qun,
        'closing_val':closing_val,
        }        
    
    return render(request,'stock_month.html',context)

def item_list(request,pk):
    std=group_summary.objects.filter(CreateStockGrp_id=pk)
    ptm=CreateStockGrp.objects.get(id=pk)
    #vouch=add_voucher.objects.all()
    total=0
    total_qty=0
    
    
        
    # calculation of voucher
    # for i in vouch:
    #     if (i.voucher_type=='sales'):
    #         total_value +=int(i.value)
    #         total_qunity+=int(i.quntity)
    #     elif (i.voucher_type=='purchase'):
    #         total_val+=int(i.value) 
    #         total_qun+=int(i.quntity)
    #         closing_qun=total_qun-total_qunity  
    # closing_val=total_val-total_value 
   
   
    for i in std:
        total+=int(i.rate_of_duty)
        total_qty+=int(i.additional)
        
        
    ptm.quantities=total   
    ptm.save()
        
    return render(request,'items.html',{'std':std,'total':total,'total_qty':total_qty,}) 
 
def items_2(request,pk):
    ptm=group_summary.objects.filter(CreateStockGrp_id=pk)
    ptc=CreateStockGrp.objects.get(id=pk)
    
    vouch=add_voucher.objects.all()
    total=0
    total_qty=0
    total_value=0
    total_qunity=0
    
    for p in ptm:
        total_qun=int(p.quantity)
        total_val=int(p.value)
    # calculation of voucher
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value +=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
            closing_qun=total_qun-total_qunity  
    closing_val=total_val-total_value 
   
    
    for i in ptm:
        total+=int(i.value)
        total_qty+=int(i.quantity)
        
    ptc.alias=total
    ptc.save()    
        
    return render(request,'item_2.html',{'ptm':ptm,'closing_val':closing_val,'closing_qun':closing_qun,'total':total})
    
def stockgroup(request):
    ptm=CreateStockGrp.objects.all()
    std=group_summary.objects.all()
    vouch=add_voucher.objects.all()
    total_val=0
    total_qun=0
    total_value=0
    total_qunity=0
    
    # for i in vouch:
    #     if (i.voucher_type=='sales'):
    #         total_value+=int(i.value)
    #         total_qunity+=int(i.quntity)
    #     elif (i.voucher_type=='purchase'):
    #         total_val+=int(i.value) 
    #         total_qun+=int(i.quntity)
       
    for p in std:
        total_val+=int(p.rate_of_duty)
        total_qun+=int(p.additional)
                
    # closing_value=total_val-total_value
    # closing_quntity=total_qun-total_qunity
    return render(request,'stockgroup.html',{'std':std,'ptm':ptm,'total_val':total_val,'total_qun':total_qun})

def stock_group2(request):
    ptm=CreateStockGrp.objects.all()
    std=group_summary.objects.all()
    total_val=0
    total_qun=0
    for p in std:
        total_val+=int(p.value)
        total_qun+=int(p.quantity)
        
    return render(request,'stockgroup_2.html',{'std':std,'opening_value':total_val,'opening_quntity':total_qun,'ptm':ptm})
    

def indirect(request):
    std=create_payhead.objects.filter(under='Income(Indirect)')
    stm=Ledger.objects.filter(group_under='income_Indirect')
    
    total=0
    total_d=0
    for i in std:
        total+=int(i.leave_withpay)
        total_d+=int(i.leave_with_out_pay)
    for p in stm:
        total+=int(p.ledger_type) 
        total_d+=int(p.provide_banking_details)
    
    
    return render(request,'indirect_income.html',{'std':std,'stm':stm,'total':total,'total_d':total_d})



def indirect_expenses(request):
    std=create_payhead.objects.filter(under='Indirect Expenses')
    stm=Ledger.objects.filter(group_under='Expences_Indirect')
    
    total=0
    total_d=0
    for i in std:
        total+=int(i.leave_withpay)
        total_d+=int(i.leave_with_out_pay)
    for p in stm:
        total+=int(p.ledger_type) 
        total_d+=int(p.provide_banking_details)
    
    
    return render(request,'indirect_expences.html',{'std':std,'stm':stm,'total':total,'total_d':total_d})



def stock_groups(request):
    und=CreateStockGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        quantities=request.POST['quantities']
        stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities)
        stockgrp.save()
        return redirect('stock_items')
    return render(request,'group_stock.html',{'und':und})    



def stock_items(request):
    grp=CreateStockGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        grp1=CreateStockGrp.objects.get(id=under)
        # category=request.POST['category',FALSE]
        units=request.POST['units']
        batches=request.POST['batches']
        manufacturing_date=request.POST['manufacturing_date']
        expiry_dates=request.POST['expiry_dates']
        rate_of_duty=request.POST['rate_of_duty']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        value=request.POST['value']
        additional=request.POST['additional']
        crt=group_summary(name=name,alias=alias,under=under,units=units,batches=batches,
                           manufacturing_date=manufacturing_date,expiry_dates=expiry_dates,
                           rate_of_duty=rate_of_duty,quantity=quantity,rate=rate,per=per,value=value,additional=additional,CreateStockGrp=grp1)
        crt.save()
        return redirect('stock_items')
    return render(request,'stockitem.html',{'grp':grp})


def payhead(request):
    # att=attendance_crt.objects.all()
    pay=payhead_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        slabtype=request.POST['slab_type']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           compute=compute,
                           effective_from=effective_from,
                           #  amount_greater=amount_greaterthan,
                           amount_upto=amount_upto,
                           slab_type=slabtype,
                           value=value,
                           Rounding_Method=round_method,
                           Round_limit=limit,
                           days_of_months=days_of_months,
                           number_of_months_from=from_date,
                           to=to,
                           calculation_per_year=calculation_per_year,
                           
        )
        std.save()
        return redirect('payhead')
    return render(request,'payhead.html')   

        # std2=compute_information(Pay_head_id=idd,
        #                          compute=compute,
        #                          effective_from=effective_from,
        #                         #  amount_greater=amount_greaterthan,
        #                          amount_upto=amount_upto,
        #                          slab_type=slabtype,
        #                          value=value,
        # )
        # std2.save()

        # std3=Rounding(pay_head_id=idd,
        #              Rounding_Method=round_method,
        #              Round_limit=limit,
        # )
        # std3.save()

        # std4=gratuity(pay_head_id=idd,
        #              days_of_months=days_of_months,
        #              number_of_months_from=from_date,
        #              to=to,
        #              calculation_per_year=calculation_per_year,
        # )
        # std4.save()
        # messages.success(request,'successfully Added !!!')
         

def ledger(request):
    return render(request,'ledger.html')



def save_ledger(request):
    if request.method == 'POST':
        # Ledger Basic
        Lname = request.POST.get('ledger_name', False)
        Lalias = request.POST.get('ledger_alias', False)
        Lunder = request.POST.get('group_under', False)
        Lopening_bal = request.POST.get('ledger_opening_bal', False)
        cd_db=request.POST.get('cd_db',False)
        typ_of_ledg = request.POST.get('ledger_type', False)
        provide_banking = request.POST.get('provide_banking_details', False)

        # Banking_details
        B_od_limit = request.POST.get('od_limit', False)
        B_ac_holder_name =request.POST.get('holder_name', False)
        B_ac_no = request.POST.get('ac_number', False)
        B_ifsc = request.POST.get('ifsc', False)
        B_swift_code =request.POST.get('swift_code', False)
        B_name = request.POST.get('bank_name', False)
        B_branch = request.POST.get('branch_name', False)
        B_alter_chq_bks =request.POST.get('alter_chk_bks', False)
        B_name_enbl_chq_prtg = request.POST.get('enbl_chk_printing', False) 
        B_chqconfg= request.POST.get('chqconfg', False) 
        # Mailing_details
        Mname = request.POST.get('name', False)
        Maddress = request.POST.get('address', False)
        Mstate =request.POST.get('state', False)
        Mcountry = request.POST.get('country', False)
        Mpincode = request.POST.get('pincode', False)

        # Tax_Registration_Details
        Tgst_uin = request.POST.get('gst_uin', False)
        Treg_typ = request.POST.get('register_type', False)
        Tpan_no = request.POST.get('pan_no', False)
        T_alter_gst =request.POST.get('alter_gst_details', False)

        # Satutory Details
        assessable_calculationn = request.POST.get('assessable_calculation', False)
        Appropriate_too =request.POST.get('Appropriate_to', False)
        gst_applicablee = request.POST.get('is_gst_applicable',False)
        Set_alter_GSTT=request.POST.get('Set_alter_GST', False)
        type_of_supplyy = request.POST.get('type_of_supply',False)
        Method_of_calcc=request.POST.get('Method_of_calc', False)

        #leadger Rounding
        ledger_idd=request.POST.get('useadvc', False)
        Rounding_Methodd=request.POST.get('Rounding_Method', False)
        Round_limitt =request.POST.get('Round_limit', False)

        #ledger_tax 
        type_of_duty_or_taxx=request.POST.get('type_of_duty_or_tax', False)
        type_of_taxx=request.POST.get('type_of_tax', False)
        valuation_typee=request.POST.get('valuation_type', False)
        rate_per_unitt=request.POST.get('rate_per_unit', False)
        Persentage_of_calculationn=request.POST.get('Persentage_of_calculation', False)

        #sundry
        maintain_balance_bill_by_billl=request.POST.get('maintain_balance_bill_by_bill', False)
        Default_credit_periodd=request.POST.get('Default_credit_period', False)
        Check_for_credit_dayss=request.POST.get('Check_for_credit_days', False)

        if Ledger.objects.filter(ledger_name = Lname ).exists():
                messages.info(request,'This Name is already taken...!')
                return redirect('load_create_ledger.html')

        Lmdl = Ledger(
            ledger_name=Lname,
            ledger_alias=Lalias,
            group_under=Lunder,
            ledger_cr_db=cd_db,
            ledger_opening_bal=Lopening_bal,
            ledger_type=typ_of_ledg,
            provide_banking_details=provide_banking,
        )
        Lmdl.save()
        idd = Lmdl
        Bmdl = Ledger_Banking_Details(
        
            ledger_id=idd,
            od_limit=B_od_limit,
            holder_name=B_ac_holder_name,
            ac_number=B_ac_no,
            ifsc=B_ifsc,
            swift_code=B_swift_code,
            bank_name=B_name,
            branch_name=B_branch,
            alter_chk_bks=B_alter_chq_bks,
            enbl_chk_printing=B_name_enbl_chq_prtg,

        )
        Bmdl.save()
        M_mdl = Ledger_Mailing_Address(

            name=Mname,
            address=Maddress,
            state=Mstate,
            country=Mcountry,
            pincode=Mpincode,
        )
        M_mdl.save()
        T_mdl = Ledger_Tax_Register(
           
          
            gst_uin=Tgst_uin,
            register_type=Treg_typ,
            pan_no=Tpan_no,
            alter_gst_details=T_alter_gst,

        )
        T_mdl.save()
        LS_mdl = Ledger_Satutory(

            ledger_id=idd,
            assessable_calculation=assessable_calculationn,
            Appropriate_to =Appropriate_too ,
            gst_applicable=gst_applicablee,
            Set_alter_GST = Set_alter_GSTT,
            type_of_supply=type_of_supplyy,
            Method_of_calc = Method_of_calcc,


        )
        LS_mdl.save()

        rnd_mdl = Ledger_Rounding(
            ledger_id=idd,
            Rounding_Method=Rounding_Methodd,
            Round_limit =Round_limitt,

        )
        rnd_mdl.save()

        tax_mdl = ledger_tax(
            ledger_id=idd,
            type_of_duty_or_tax=type_of_duty_or_taxx,
            type_of_tax =type_of_taxx,
            valuation_type=valuation_typee,
            rate_per_unit=rate_per_unitt,
            Persentage_of_calculation=Persentage_of_calculationn,
        )
        tax_mdl.save()

        sndry_mdl = Ledger_sundry(
            ledger_id=idd,
            maintain_balance_bill_by_bill=maintain_balance_bill_by_billl,
            Default_credit_period=Default_credit_periodd,
            Check_for_credit_days =Check_for_credit_dayss,
        )
        sndry_mdl.save()
        # messages.info(request,'LEDGER CREATED SUCCESSFULLY')
        return redirect('ledger')
    



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
############################nitya
def balancesheet_new(request):

    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
        t_id=2
        comp = Companies.objects.get(id=t_id)
        group= tally_group.objects.filter(company_id = comp.id)

        
        blnc = total_balance.objects.filter(company_id = comp.id)
        total = 0
        for g in group:
            for b in blnc:

                if b.total_debit > b.total_credit:
                    
                    total = b.total_debit - b.total_credit
                else:
                    total = b.total_credit - b.total_credit

                b.total = total
                b.save()
       
        context = {
            'comp' : comp,
            'group':group,
            'balance' : blnc,
            'total':total,
            

        }
        return render(request,'balancesheet.html',context)
    # else:
    #         return redirect('/')


def capital_group_summary(request):

        
        group= tally_group.objects.get(group_name='Capital Account')
        comp = Companies.objects.get(id = group.company_id)
        voucher = Ledger_vouchers_new.objects.filter(group_id = group.id)
        ledger=tally_ledger.objects.filter(grp_id = group.id)
        
        debit_total = credit_total = 0

        for led in ledger:

            led.c_balance = 0 if led.c_balance is None else led.c_balance 
            if led.c_type == 'Dr':
                debit_total  = debit_total +  led.c_balance
            else:
                credit_total = credit_total + led.c_balance
           
        
        d = debit_total
        c = credit_total

        if total_balance.objects.filter(group_id = group.id).exists():
            balance = total_balance.objects.get(group_id = group.id)
            balance.total_debit = debit_total
            balance.total_credit = credit_total
            
            balance.save()
        else :
            balance = total_balance( total_debit =debit_total, total_credit = credit_total,company = comp,group = group)
            balance.save()

        context = {
                    'company':comp,
                    'ledger':ledger,
                    'group':group,
                    'voucher':voucher, 
                    'd': d,
                    'c':c,
                    
        }
            
        return render(request,'group_summary.html',context)

def ledgermonthly(request,id):

    ledger=tally_ledger.objects.get(id = id)
    comp = Companies.objects.get(id = ledger.company_id)
    group= tally_group.objects.get(id=ledger.grp_id)
       
    voucher = Ledger_vouchers_new.objects.filter(ledger_id = ledger.id)

    beg = comp.fin_begin.strftime('%m')
   

    mnths = Months.objects.all()

    current_total_debit = 0
    current_total_credit = 0

    date1 = []
    for vouch in voucher:
        
        current_total_debit+=vouch.debit
        current_total_credit += vouch.credit

        date1.append(vouch.date)
        
    d1 =[]
    for i in range(0,len(voucher)):
        if date1[i].strftime('%B') not in d1:

            d1.append(date1[i].strftime('%B'))

    
    cl =[]
    deb = cred = 0
    if ledger.type_of_ledger == 'Dr':
        deb = ledger.opening_blnc + current_total_debit
        credit = current_total_credit
        if deb > credit:
            closing_balance = deb - credit
            ctype = 'Dr'
            cl.append(closing_balance)
        else:
            closing_balance = credit - deb
            ctype = 'Cr'
            cl.append(closing_balance)

        
    else:
        cred = ledger.opening_blnc + current_total_credit
        debit = current_total_debit
        if cred > debit:

            closing_balance = cred - debit
            ctype = 'Cr'
            cl.append(closing_balance)

        else:
            closing_balance = debit - cred
            ctype = 'Dr'
            cl.append(closing_balance)
        
    if voucher is not None:
        ledger.c_balance = closing_balance
        ledger.c_type = ctype
        ledger.save()
    else:
        ledger.c_balance = ledger.opening_blnc
        if ledger.opening_blnc == 'Dr':
            ledger.c_type = 'Dr'
        else:
            ledger.c_type = 'Cr'
        ledger.save()

    clb = cl[-1]
    context = {
        'group': group,
        'ledger' : ledger,
        'voucher' :voucher,
        'company':comp,
        'deb':deb,
        'cred' : cred,
        'debit' : current_total_debit,
        'credit' :current_total_credit,
        'closing' : closing_balance,
        'date1': date1,
        'd1':d1,
        'beg': beg,
        'months':mnths,
        
        'clb':clb,
        
        
        
    }

    return render(request,'Ledgermonthly.html',context)


def ledger_vouchers(request,pk,id):

    mnth = Months.objects.all()
    ledger=tally_ledger.objects.get(id = pk)
    voucher = Ledger_vouchers_new.objects.filter(ledger_id = ledger.id)
    comp = Companies.objects.get(id = ledger.company_id)
    group= tally_group.objects.get(id=ledger.grp_id)

    
    
    current_total_debit = 0
    current_total_credit = 0

    d = []
    
    for vouch in voucher:
        
        current_total_debit+=vouch.debit
        current_total_credit += vouch.credit
        d.append(vouch.date)

    
    

    begin_of_month =date(d[0].year,d[0].month,1)
    df1 = DateFormat(begin_of_month)
    df1.format(get_format('DATE_FORMAT'))
    b = df1.format('d-M-Y')

    end_of_month = date(d[0].year,d[0].month,calendar.monthrange(d[0].year,d[0].month)[1])
    df2 = DateFormat(end_of_month)
    df2.format(get_format('DATE_FORMAT'))
    e = df2.format('d-M-Y')

    deb = cred = 0
    if ledger.type_of_ledger == 'Dr':
        deb = ledger.opening_blnc + current_total_debit
        credit = current_total_credit
        if deb > credit:
            closing_balance = deb - credit
        else:
            closing_balance = credit - deb
    else:
        cred = ledger.opening_blnc + current_total_credit
        debit = current_total_debit
        if cred > debit:
            closing_balance = cred - debit
        else:
            closing_balance = debit - cred

    context = {
        'group': group,
        'ledger' : ledger,
        'voucher' :voucher,
        'company':comp,
        'deb':deb,
        'cred' : cred,
        'debit' : current_total_debit,
        'credit' :current_total_credit,
        'closing' : closing_balance,
        'begmonth':b,
        'endmonth' : e,
        'month' : mnth,
        
        
    }
    

    return render(request,'Ledger_voucher.html',context)

def loanl_group_summary(request):

        group= tally_group.objects.get(group_name='Loans(Liability)')
        comp = Companies.objects.get(id = group.company_id)
        voucher = Ledger_vouchers_new.objects.filter(group_id = group.id)

        ledger=tally_ledger.objects.filter(grp_id = group.id)

        debit_total = credit_total = 0

        for led in ledger:
            
            led.c_balance = 0 if led.c_balance is None else led.c_balance 

            if led.c_type == 'Dr':

                debit_total  = debit_total + led.c_balance
            else:
                credit_total = credit_total + led.c_balance
           

        d = debit_total
        c = credit_total

        if total_balance.objects.filter(group_id = group.id).exists():
            balance = total_balance.objects.get(group_id = group.id)
            balance.total_debit = debit_total
            balance.total_credit = credit_total
            balance.save()
        else :
            balance = total_balance( total_debit =debit_total, total_credit = credit_total,company = comp,group = group)
            balance.save()

        context = {
                    'company':comp,
                    'ledger':ledger,
                    'group':group,
                    'voucher':voucher, 
                    'd': d,
                    'c':c,
        }
            
        return render(request,'Loansgroup_summary.html',context)

def fixed_assets_group_summary(request):

    group= tally_group.objects.get(group_name='Fixed Assets')
    comp = Companies.objects.get(id = group.company_id)
    voucher = Ledger_vouchers_new.objects.filter(group_id = group.id)

    ledger=tally_ledger.objects.filter(grp_id = group.id)

    debit_total = credit_total = 0

    for led in ledger:

        led.c_balance = 0 if led.c_balance is None else led.c_balance 
  
        if led.c_type == 'Dr':

            debit_total  = debit_total + led.c_balance
        else:
            credit_total = credit_total + led.c_balance
           

    d = debit_total
    c = credit_total

    if total_balance.objects.filter(group_id = group.id).exists():
            balance = total_balance.objects.get(group_id = group.id)
            balance.total_debit = debit_total
            balance.total_credit = credit_total
            balance.save()
    else :
            balance = total_balance( total_debit =debit_total, total_credit = credit_total,company = comp,group = group)
            balance.save()

    context = {
        'company':comp,
        'ledger':ledger,
        'group':group,
        'voucher':voucher, 
        'd': d,
        'c':c,
        }
            
    return render(request,'Fixassets_group_summary.html',context)

def quit(request):

    return redirect('index')

def vouch_delete(request,pk):

    vouch = Ledger_vouchers_new.objects.get(id = pk)
    vouch.delete()

    return redirect('capital_group_summary')


def grp_month(request,pk):
    std=Ledger.objects.get(id=pk)
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch2:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-int(std.ledger_opening_bal)+total_credit
    if opening_balance>0 :
        std.ledger_type=opening_balance
        std.save()
        
    else :
        std.provide_banking_details=opening_balance*-1
        std.save()
            
    return render(request,'group_month.html',{'std':std,'vouch2':vouch2,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def grp_month_2(request,pk):
    std=Ledger.objects.get(id=pk)
    vouch3=add_voucher3.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch3:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_credit-int(std.ledger_opening_bal)+total_debit
    if opening_balance>0 :
        std.ledger_type=opening_balance
        std.save()
        
    else :
        std.provide_banking_details=opening_balance*-1
        std.save()
            
    return render(request,'grp_voucher.html',{'std':std,'vouch2':vouch3,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def sales_month(request,pk):
    std=Ledger.objects.get(id=pk)
    
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch2:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-int(std.ledger_opening_bal)+total_credit
    
    # std.ledger_type=opening_balance
    # std.save()
    
    return render(request,'sales_month.html',{'std':std,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def sales_month_2(request,pk):
    std=Ledger.objects.get(id=pk)
    
    vouch3=add_voucher3.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch3:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_credit-int(std.ledger_opening_bal)+total_debit
    
    # std.ledger_type=opening_balance
    # std.save()
    
    return render(request,'sales_income_month.html',{'std':std,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})


def payhead_month(request,pk):
    std=create_payhead.objects.get(id=pk)
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    for i in vouch2:
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-int(std.opening_balance)+total_credit
    return render(request,'month_payhead.html',{'std':std,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def pay_voucher(request,pk):
    std=create_payhead.objects.get(id=pk)
    vouch2=add_voucher2.objects.all()
    total_debit=0
    total_credit=0
    
    for i in vouch2 :
        total_debit+=int(i.debit)
        total_credit+=int(i.credit)
        
    opening_balance=total_debit-int(std.opening_balance)+total_credit
    
    if opening_balance>0 :
        std.leave_withpay=opening_balance
        std.save()
        
    else :
        std.leave_with_out_pay=opening_balance*-1
        std.save()
    
    return render(request,'payhead_voucher.html',{'std':std,'vouch2':vouch2,'total_debit':total_debit,'total_credit':total_credit,'opening_balance':opening_balance})

def stock_voucher(request,pk):
    std=group_summary.objects.get(id=pk)
    vouch=add_voucher.objects.all()
    total_value=0
    total_qunity=0
    total_val=int(std.value)
    total_qun=int(std.quantity)
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value +=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
    closing_qun=total_qun-total_qunity  
    closing_val=total_val-total_value 
    
    std.rate_of_duty=closing_val
    std.additional=closing_qun
    std.save()    
    
    context={
        'std':std,
        'vouch':vouch,
        'total_sales_value':total_value,
        'total_sales_quntity':total_qunity, 
        'total_purchase_value':total_val,
        'total_purchase_quntity':total_qun,
        'closing_qun':closing_qun,
        'closing_val':closing_val,
        }        
    return render(request,'stock_voucher.html',context)


def profit(request):
    balance=Ledger.objects.all()
    balance_py=create_payhead.objects.all()
    balance_le=Ledger.objects.all()
    balance_group=group_summary.objects.all()
    total_grp=0
    total_direct=0
    total=0
    total_income=0
    total_purch=0
    total_direct_exp=0
    total_indirect=0
    #sales account total
    for i in balance:
        if(i.group_under=='Sales_Account'):
            total+=int(i.ledger_type)
            total+=int(i.provide_banking_details)
            
    #indirect income total        
    for i in balance_py:
        if(i.under=='Income(Indirect)'):
            total_income+=int(i.leave_withpay)
            total_income+=int(i.leave_with_out_pay)
    for p in balance_le:
         if(p.group_under=='income_Indirect'):
             total_income+=int(p.ledger_type) 
             total_income+=int(p.provide_banking_details)
             
    #direct income total
             
    for i in balance_py:
        if(i.under=='Direct Incomes'):
            total_direct+=int(i.leave_withpay) 
            total_direct+=int(i.leave_with_out_pay) 
    
    for p in balance_le:
        if(p.group_under=='Direct Incomes'):
            total_direct+=int(p.ledger_type) 
            total_direct+=int(p.provide_banking_details)
            
    #closing stock
    for k in  balance_group:
        total_grp+=int(k.value)
        
    #purchase account total 
    
    for i in balance:
        if(i.group_under=='Purchase_Account'):
            total_purch+=int(i.ledger_type)
            total_purch+=int(i.provide_banking_details)
    
    #direct expenses total
           
    for i in balance_py:
        if(i.under=='Direct Expenses'):
            total_direct_exp+=int(i.leave_withpay) 
            total_direct_exp+=int(i.leave_with_out_pay)     
    
    for p in balance_le:
        if(p.group_under=='Direct Expenses'):
            total_direct_exp+=int(p.ledger_type) 
            total_direct_exp+=int(p.provide_banking_details) 
            
    #indirect expenses total   
    
    for i in balance_py:
        if(i.under=='Indirect Expenses'):
            total_indirect+=int(i.leave_withpay)
            total_indirect+=int(i.leave_with_out_pay)
    for p in balance_le:
         if(p.group_under=='Expences_Indirect'):
            total_indirect+=int(p.ledger_type) 
            total_indirect+=int(p.provide_banking_details)    
            
    #closing stock
    std=group_summary.objects.all()
    # vouch=add_voucher.objects.all()
    total_val=0
    total_qun=0
    # total_value=0
    # total_qunity=0
    
    # for i in vouch:
    #     if (i.voucher_type=='sales'):
    #         total_value+=int(i.value)
    #         total_qunity+=int(i.quntity)
    #     elif (i.voucher_type=='purchase'):
    #         total_val+=int(i.value) 
    #         total_qun+=int(i.quntity)
       
    # for p in std:
    #     total_val+=int(p.value)
    #     total_qun+=int(p.quantity)
                
    
    # closing_quntity=total_qun-total_qunity        
    
    for p in std:
        total_val+=int(p.rate_of_duty)
        total_qun+=int(p.additional)
        
    closing_value=total_val      
                   
    return render(request,'profit.html',{'total':total,'total_income':total_income,'total_direct':total_direct,'total_grp':total_grp,'total_purch':total_purch,'total_direct_exp':total_direct_exp,'total_indirect':total_indirect,'closing_value':closing_value,}) 





def  payhead_list(request):
    std=create_payhead.objects.filter(under='Direct Incomes')
    stm=Ledger.objects.filter(group_under='Direct Incomes')
    balance=create_payhead.objects.all()
    balance_le=Ledger.objects.all()
    total=0
    total_d=0
    for i in balance:
        if(i.under=='Direct Incomes'):
            total+=int(i.leave_withpay)
            total_d+=int(i.leave_with_out_pay)
    for p in balance_le:
         if(p.group_under=='Direct Incomes') :
             total+=int(p.ledger_type) 
             total_d+=int(p.provide_banking_details)
         
    
    
    return render(request,'payhead_items.html',{'std':std,'stm':stm,'total':total,'total_d':total_d}) 



def direct_exprenses(request):
    std=create_payhead.objects.filter(under='Direct Expenses')
    stm=Ledger.objects.filter(group_under='Direct Expenses')
    total=0
    total_d=0
    for i in std:
        total+=int(i.leave_withpay)
        total_d+=int(i.leave_with_out_pay)
    for p in stm:
        total+=int(p.ledger_type) 
        total_d+=int(p.provide_banking_details)
    return render(request,'direct_expenses.html',{'std':std,'stm':stm,'total':total,'total_d':total_d}) 

def sales(request):
    std=Ledger.objects.filter(group_under='Sales_Account')
    balance=Ledger.objects.all()
    total=0
    total_d=0
    for i in balance:
        if (i.group_under=='Sales_Account') :
            total+=int(i.ledger_type)
            total_d+=int(i.provide_banking_details)
        
                 
    return render(request,'sales_accounts.html',{'std':std,'total':total,'total_d':total_d})

def purchase(request):
    std=Ledger.objects.filter(group_under='Purchase_Account')
    
    total=0
    total_d=0
    for i in std:
        total+=int(i.ledger_type)
        total_d+=int(i.provide_banking_details)
    return render(request,'purchase_list.html',{'std':std,'total':total,'total_d':total_d})




def stock_month(request,pk):
    std=group_summary.objects.get(id=pk)
    
    vouch=add_voucher.objects.all()
    total_value=0
    total_qunity=0
    total_val=int(std.value)
    total_qun=int(std.quantity)
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value +=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
    closing_qun=total_qun-total_qunity  
    closing_val=total_val-total_value      
    context={
        'std':std,
        'vouch':vouch,
        'total_sales_value':total_value,
        'total_sales_quntity':total_qunity, 
        'total_purchase_value':total_val,
        'total_purchase_quntity':total_qun,
        'closing_qun':closing_qun,
        'closing_val':closing_val,
        }        
    
    return render(request,'stock_month.html',context)

def item_list(request,pk):
    std=group_summary.objects.filter(CreateStockGrp_id=pk)
    ptm=CreateStockGrp.objects.get(id=pk)
    #vouch=add_voucher.objects.all()
    total=0
    total_qty=0
    
    
        
    # calculation of voucher
    # for i in vouch:
    #     if (i.voucher_type=='sales'):
    #         total_value +=int(i.value)
    #         total_qunity+=int(i.quntity)
    #     elif (i.voucher_type=='purchase'):
    #         total_val+=int(i.value) 
    #         total_qun+=int(i.quntity)
    #         closing_qun=total_qun-total_qunity  
    # closing_val=total_val-total_value 
   
   
    for i in std:
        total+=int(i.rate_of_duty)
        total_qty+=int(i.additional)
        
        
    ptm.quantities=total   
    ptm.save()
        
    return render(request,'items.html',{'std':std,'total':total,'total_qty':total_qty,}) 
 
def items_2(request,pk):
    ptm=group_summary.objects.filter(CreateStockGrp_id=pk)
    ptc=CreateStockGrp.objects.get(id=pk)
    
    vouch=add_voucher.objects.all()
    total=0
    total_qty=0
    total_value=0
    total_qunity=0
    
    for p in ptm:
        total_qun=int(p.quantity)
        total_val=int(p.value)
    # calculation of voucher
    for i in vouch:
        if (i.voucher_type=='sales'):
            total_value +=int(i.value)
            total_qunity+=int(i.quntity)
        elif (i.voucher_type=='purchase'):
            total_val+=int(i.value) 
            total_qun+=int(i.quntity)
            closing_qun=total_qun-total_qunity  
    closing_val=total_val-total_value 
   
    
    for i in ptm:
        total+=int(i.value)
        total_qty+=int(i.quantity)
        
    ptc.alias=total
    ptc.save()    
        
    return render(request,'item_2.html',{'ptm':ptm,'closing_val':closing_val,'closing_qun':closing_qun,'total':total})
    
def stockgroup(request):
    ptm=CreateStockGrp.objects.all()
    std=group_summary.objects.all()
    vouch=add_voucher.objects.all()
    total_val=0
    total_qun=0
    total_value=0
    total_qunity=0
    
    # for i in vouch:
    #     if (i.voucher_type=='sales'):
    #         total_value+=int(i.value)
    #         total_qunity+=int(i.quntity)
    #     elif (i.voucher_type=='purchase'):
    #         total_val+=int(i.value) 
    #         total_qun+=int(i.quntity)
       
    for p in std:
        total_val+=int(p.rate_of_duty)
        total_qun+=int(p.additional)
                
    # closing_value=total_val-total_value
    # closing_quntity=total_qun-total_qunity
    return render(request,'stockgroup.html',{'std':std,'ptm':ptm,'total_val':total_val,'total_qun':total_qun})

def stock_group2(request):
    ptm=CreateStockGrp.objects.all()
    std=group_summary.objects.all()
    total_val=0
    total_qun=0
    for p in std:
        total_val+=int(p.value)
        total_qun+=int(p.quantity)
        
    return render(request,'stockgroup_2.html',{'std':std,'opening_value':total_val,'opening_quntity':total_qun,'ptm':ptm})
    

def indirect(request):
    std=create_payhead.objects.filter(under='Income(Indirect)')
    stm=Ledger.objects.filter(group_under='income_Indirect')
    
    total=0
    total_d=0
    for i in std:
        total+=int(i.leave_withpay)
        total_d+=int(i.leave_with_out_pay)
    for p in stm:
        total+=int(p.ledger_type) 
        total_d+=int(p.provide_banking_details)
    
    
    return render(request,'indirect_income.html',{'std':std,'stm':stm,'total':total,'total_d':total_d})



def indirect_expenses(request):
    std=create_payhead.objects.filter(under='Indirect Expenses')
    stm=Ledger.objects.filter(group_under='Expences_Indirect')
    
    total=0
    total_d=0
    for i in std:
        total+=int(i.leave_withpay)
        total_d+=int(i.leave_with_out_pay)
    for p in stm:
        total+=int(p.ledger_type) 
        total_d+=int(p.provide_banking_details)
    
    
    return render(request,'indirect_expences.html',{'std':std,'stm':stm,'total':total,'total_d':total_d})



def stock_groups(request):
    und=CreateStockGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        quantities=request.POST['quantities']
        stockgrp=CreateStockGrp(name=name,alias=alias,under_name=under_name,quantities=quantities)
        stockgrp.save()
        return redirect('stock_items')
    return render(request,'group_stock.html',{'und':und})    



def stock_items(request):
    grp=CreateStockGrp.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        grp1=CreateStockGrp.objects.get(id=under)
        # category=request.POST['category',FALSE]
        units=request.POST['units']
        batches=request.POST['batches']
        manufacturing_date=request.POST['manufacturing_date']
        expiry_dates=request.POST['expiry_dates']
        rate_of_duty=request.POST['rate_of_duty']
        quantity=request.POST['quantity']
        rate=request.POST['rate']
        per=request.POST['per']
        value=request.POST['value']
        additional=request.POST['additional']
        crt=group_summary(name=name,alias=alias,under=under,units=units,batches=batches,
                           manufacturing_date=manufacturing_date,expiry_dates=expiry_dates,
                           rate_of_duty=rate_of_duty,quantity=quantity,rate=rate,per=per,value=value,additional=additional,CreateStockGrp=grp1)
        crt.save()
        return redirect('stock_items')
    return render(request,'stockitem.html',{'grp':grp})


def payhead(request):
    # att=attendance_crt.objects.all()
    pay=payhead_crt.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        production_type=request.POST['ptype']
        opening_balance=request.POST['balance']

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        slabtype=request.POST['slab_type']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=production_type,
                           opening_balance=opening_balance,
                           compute=compute,
                           effective_from=effective_from,
                           #  amount_greater=amount_greaterthan,
                           amount_upto=amount_upto,
                           slab_type=slabtype,
                           value=value,
                           Rounding_Method=round_method,
                           Round_limit=limit,
                           days_of_months=days_of_months,
                           number_of_months_from=from_date,
                           to=to,
                           calculation_per_year=calculation_per_year,
                           
        )
        std.save()
        return redirect('payhead')
    return render(request,'payhead.html')   

        # std2=compute_information(Pay_head_id=idd,
        #                          compute=compute,
        #                          effective_from=effective_from,
        #                         #  amount_greater=amount_greaterthan,
        #                          amount_upto=amount_upto,
        #                          slab_type=slabtype,
        #                          value=value,
        # )
        # std2.save()

        # std3=Rounding(pay_head_id=idd,
        #              Rounding_Method=round_method,
        #              Round_limit=limit,
        # )
        # std3.save()

        # std4=gratuity(pay_head_id=idd,
        #              days_of_months=days_of_months,
        #              number_of_months_from=from_date,
        #              to=to,
        #              calculation_per_year=calculation_per_year,
        # )
        # std4.save()
        # messages.success(request,'successfully Added !!!')
         

def ledger(request):
    return render(request,'ledger.html')



def save_ledger(request):
    if request.method == 'POST':
        # Ledger Basic
        Lname = request.POST.get('ledger_name', False)
        Lalias = request.POST.get('ledger_alias', False)
        Lunder = request.POST.get('group_under', False)
        Lopening_bal = request.POST.get('ledger_opening_bal', False)
        cd_db=request.POST.get('cd_db',False)
        typ_of_ledg = request.POST.get('ledger_type', False)
        provide_banking = request.POST.get('provide_banking_details', False)

        # Banking_details
        B_od_limit = request.POST.get('od_limit', False)
        B_ac_holder_name =request.POST.get('holder_name', False)
        B_ac_no = request.POST.get('ac_number', False)
        B_ifsc = request.POST.get('ifsc', False)
        B_swift_code =request.POST.get('swift_code', False)
        B_name = request.POST.get('bank_name', False)
        B_branch = request.POST.get('branch_name', False)
        B_alter_chq_bks =request.POST.get('alter_chk_bks', False)
        B_name_enbl_chq_prtg = request.POST.get('enbl_chk_printing', False) 
        B_chqconfg= request.POST.get('chqconfg', False) 
        # Mailing_details
        Mname = request.POST.get('name', False)
        Maddress = request.POST.get('address', False)
        Mstate =request.POST.get('state', False)
        Mcountry = request.POST.get('country', False)
        Mpincode = request.POST.get('pincode', False)

        # Tax_Registration_Details
        Tgst_uin = request.POST.get('gst_uin', False)
        Treg_typ = request.POST.get('register_type', False)
        Tpan_no = request.POST.get('pan_no', False)
        T_alter_gst =request.POST.get('alter_gst_details', False)

        # Satutory Details
        assessable_calculationn = request.POST.get('assessable_calculation', False)
        Appropriate_too =request.POST.get('Appropriate_to', False)
        gst_applicablee = request.POST.get('is_gst_applicable',False)
        Set_alter_GSTT=request.POST.get('Set_alter_GST', False)
        type_of_supplyy = request.POST.get('type_of_supply',False)
        Method_of_calcc=request.POST.get('Method_of_calc', False)

        #leadger Rounding
        ledger_idd=request.POST.get('useadvc', False)
        Rounding_Methodd=request.POST.get('Rounding_Method', False)
        Round_limitt =request.POST.get('Round_limit', False)

        #ledger_tax 
        type_of_duty_or_taxx=request.POST.get('type_of_duty_or_tax', False)
        type_of_taxx=request.POST.get('type_of_tax', False)
        valuation_typee=request.POST.get('valuation_type', False)
        rate_per_unitt=request.POST.get('rate_per_unit', False)
        Persentage_of_calculationn=request.POST.get('Persentage_of_calculation', False)

        #sundry
        maintain_balance_bill_by_billl=request.POST.get('maintain_balance_bill_by_bill', False)
        Default_credit_periodd=request.POST.get('Default_credit_period', False)
        Check_for_credit_dayss=request.POST.get('Check_for_credit_days', False)

        if Ledger.objects.filter(ledger_name = Lname ).exists():
                messages.info(request,'This Name is already taken...!')
                return redirect('load_create_ledger.html')

        Lmdl = Ledger(
            ledger_name=Lname,
            ledger_alias=Lalias,
            group_under=Lunder,
            ledger_cr_db=cd_db,
            ledger_opening_bal=Lopening_bal,
            ledger_type=typ_of_ledg,
            provide_banking_details=provide_banking,
        )
        Lmdl.save()
        idd = Lmdl
        Bmdl = Ledger_Banking_Details(
        
            ledger_id=idd,
            od_limit=B_od_limit,
            holder_name=B_ac_holder_name,
            ac_number=B_ac_no,
            ifsc=B_ifsc,
            swift_code=B_swift_code,
            bank_name=B_name,
            branch_name=B_branch,
            alter_chk_bks=B_alter_chq_bks,
            enbl_chk_printing=B_name_enbl_chq_prtg,

        )
        Bmdl.save()
        M_mdl = Ledger_Mailing_Address(

            name=Mname,
            address=Maddress,
            state=Mstate,
            country=Mcountry,
            pincode=Mpincode,
        )
        M_mdl.save()
        T_mdl = Ledger_Tax_Register(
           
          
            gst_uin=Tgst_uin,
            register_type=Treg_typ,
            pan_no=Tpan_no,
            alter_gst_details=T_alter_gst,

        )
        T_mdl.save()
        LS_mdl = Ledger_Satutory(

            ledger_id=idd,
            assessable_calculation=assessable_calculationn,
            Appropriate_to =Appropriate_too ,
            gst_applicable=gst_applicablee,
            Set_alter_GST = Set_alter_GSTT,
            type_of_supply=type_of_supplyy,
            Method_of_calc = Method_of_calcc,


        )
        LS_mdl.save()

        rnd_mdl = Ledger_Rounding(
            ledger_id=idd,
            Rounding_Method=Rounding_Methodd,
            Round_limit =Round_limitt,

        )
        rnd_mdl.save()

        tax_mdl = ledger_tax(
            ledger_id=idd,
            type_of_duty_or_tax=type_of_duty_or_taxx,
            type_of_tax =type_of_taxx,
            valuation_type=valuation_typee,
            rate_per_unit=rate_per_unitt,
            Persentage_of_calculation=Persentage_of_calculationn,
        )
        tax_mdl.save()

        sndry_mdl = Ledger_sundry(
            ledger_id=idd,
            maintain_balance_bill_by_bill=maintain_balance_bill_by_billl,
            Default_credit_period=Default_credit_periodd,
            Check_for_credit_days =Check_for_credit_dayss,
        )
        sndry_mdl.save()
        # messages.info(request,'LEDGER CREATED SUCCESSFULLY')
        return redirect('ledger')
##############Neethu
def investments(request):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        ld=Ledger_vouchers.objects.all()
        talled=tally_ledger.objects.get(name='investments')
        balance=talled.opening_blnc
        voucher = Ledger_vouchers.objects.all()
        credit= sum(voucher.values_list('credit', flat=True))
        debit= sum(voucher.values_list('debit', flat=True))
        total_debit=balance+debit
        print(total_debit)

        deb_balance=total_debit-credit
        
        ledg=Ledger_vouchers.objects.raw('SELECT app1_tally_ledger.id,app1_tally_ledger.name,sum(app1_ledger_vouchers.debit) as debit,sum(app1_ledger_vouchers.credit) as credit FROM `app1_ledger_vouchers` inner join app1_tally_ledger on app1_ledger_vouchers.ledger_id=app1_tally_ledger.id group by app1_ledger_vouchers.ledger_id')
        return render(request,'groupsummaryinvestments.html',{'cmp':tally,'led':talled,'deb_balance':deb_balance})
    # else:
        # return redirect('/')
def monthly_summary(request,pk):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
        t_id=3  
        tally = Companies.objects.filter(id=t_id)  
        ledg=Ledger_vouchers.objects.raw('SELECT app1_tally_ledger.id,monthname( app1_ledger_vouchers.date) as date,case when sum(app1_ledger_vouchers.debit) =0 then 0 else sum(app1_ledger_vouchers.debit) end as debit,case when sum(app1_ledger_vouchers.credit)=0 then 0 else sum(app1_ledger_vouchers.credit) end as credit FROM `app1_ledger_vouchers` inner join app1_tally_ledger on app1_ledger_vouchers.ledger_id=app1_tally_ledger.id where app1_tally_ledger.id=3 and month(app1_ledger_vouchers.date)>=4 group by app1_ledger_vouchers.date')
        
        
        
        open=tally_ledger.objects.get(id=pk)
        month="2022-4-01"
        voucher = Ledger_vouchers.objects.filter(ledger=pk)
        
        print(voucher)
        credit= sum(voucher.values_list('credit', flat=True))
        print(credit)
        debit= sum(voucher.values_list('debit', flat=True))
        print(debit)
        talled=tally_ledger.objects.get(name='investments')
        balance=talled.opening_blnc
        total_debit=balance+debit
        if total_debit>credit:
            deb_balance=total_debit-credit
        else:
            cred_balance=credit-total_debit
        return render(request,'monthlysummary.html',{'cmp':tally,'led':ledg,'open':open,'credit':credit,'debit':debit,'deb_balance':deb_balance,'talled':talled})
    # else:
        # return redirect('/')
def ledgervouchers(request,pk):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        comp= Companies.objects.get(id=t_id)
        talled=tally_ledger.objects.get(name='investments')
        balance=talled.opening_blnc
        print(balance)
        a=comp.fin_begin
        month=a.month
        if a.month==4:
            msg1="1-Apr-2022 to 30-Apr-2022"
        

        # debit=Ledger_vouchers.objects.aggregate(Sum('debit'))
        # credit=Ledger_vouchers.objects.aggregate(Sum('credit'))
        
        voucher = Ledger_vouchers.objects.filter(ledger=pk)
        credit= sum(voucher.values_list('credit', flat=True))
        debit= sum(voucher.values_list('debit', flat=True))
        total_debit=balance+debit
        print(total_debit)
        if total_debit>credit:
            deb_balance=total_debit-credit
        else:
            cred_balance=credit-total_debit
        ledg=Ledger_vouchers.objects.raw('SELECT app1_tally_ledger.id,app1_ledger_vouchers.date as date,app1_ledger_vouchers.account as account,app1_ledger_vouchers.voucher_no as voucher_no,app1_ledger_vouchers.voucher_type as voucher_type, app1_tally_ledger.name,app1_ledger_vouchers.debit as debit,app1_ledger_vouchers.credit as credit FROM `app1_ledger_vouchers` inner join app1_tally_ledger on app1_ledger_vouchers.ledger_id=app1_tally_ledger.id ')
        return render(request,'ledgervouchers.html',{'cmp':tally,'led':ledg,'comp':comp,'msg1':msg1,'talled':talled,'credit':credit,'debit':debit,'deb_balance':deb_balance, 'month':month,'voucher':voucher})
    # else:
    #  return redirect('/')

def currentassets(request):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
        t_id=3   
        tally = Companies.objects.filter(id=t_id)
        ld=Ledger_vouchers.objects.all()
        t=tally_ledger.objects.all()
        stocks=StockGroup.objects.all()
        total=sum(stocks.values_list('closing_balance', flat=True))
        total1=round(total)
        l=tally_ledger.objects.filter(under='Loans & Advances')
        loans=sum(l.values_list('closing_balance', flat=True))
        s=tally_ledger.objects.filter(under='Sundry Debtors')
        sundry=sum(s.values_list('closing_balance', flat=True))
        c=tally_ledger.objects.filter(under='Cash in Hand')
        cash=sum(c.values_list('closing_balance', flat=True))
        b=tally_ledger.objects.filter(under='Bank Accounts')
        bank=sum(b.values_list('closing_balance', flat=True))
        grand_total=sum(t.values_list('closing_balance', flat=True))
        return render(request,'currentassets.html',{'cmp':tally,'total':total1,'loans':loans,'sundry':sundry,'cash':cash,'bank':bank,'grand_total':grand_total})
    # else:
        # return redirect('/')

def stockgroupsummary(request):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
    t_id=3
    tally = Companies.objects.filter(id=t_id)
    stockgrp=StockGroup.objects.all()
    balance = sum(stockgrp.values_list('closing_balance', flat=True))     
    return render(request,'stockgroupsummary.html',{'cmp':tally,'stockgrp':stockgrp,'balance':balance})
def stockitem(request,pk):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
    t_id=3
    tally = Companies.objects.get(id=t_id)
    stockgroup=StockGroup.objects.get(id=pk)
    a=stockgroup.id
    print(stockgroup.grp_name)
    stockitem=stock_item.objects.get(id=pk)
    # total= sum(stockitem.values_list('value', flat=True))
    voucher=voucherlist.objects.filter(item=pk)
    opening_quantity=stockitem.quantity
    opening_value=stockitem.value
    purchase=voucherlist.objects.filter(vouch_type='purchase')
    quantity = sum(purchase.values_list('quantity', flat=True))
    quantity2=quantity+opening_quantity
    value = sum(purchase.values_list('value', flat=True))
    value2=value+opening_value
    sales=voucherlist.objects.filter(vouch_type='sales')
    quantity3 = sum(sales.values_list('quantity', flat=True)) 
    value3=sum(sales.values_list('value', flat=True))
    if quantity2>quantity3:
            closing_quantity=quantity2-quantity3
    else:
             closing_quantity=quantity3-quantity2
             rate=stockitem.rateper 
             rate1=sum(purchase.values_list('rateper', flat=True))
             count2=voucherlist.objects.filter(vouch_type='purchase').count()
             count1=count2+1
             avg=rate+rate1
             average=avg/count1
             closing_balance=average * closing_quantity          
    return render(request,'stockitemsummary.html',{'cmp':tally,'stockitem':stockitem,'stockgroup':stockgroup,'closing_quantity':closing_quantity,'closing_balance':closing_balance,'average':average})
def stockItem_monthlySummary(request,pk):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        stockitem=stock_item.objects.get(id=pk)
        b=stockitem.id
        opening_quantity=stockitem.quantity
        opening_value=stockitem.value
        msg1="1-Apr-2022 to 30-Apr-2022"
        voucher=voucherlist.objects.filter(item=pk)
        purchase=voucherlist.objects.filter(vouch_type='purchase')
        quantity = sum(purchase.values_list('quantity', flat=True))
        quantity2=quantity+opening_quantity
        value = sum(purchase.values_list('value', flat=True))
        value2=value+opening_value
        sales=voucherlist.objects.filter(vouch_type='sales')
        quantity3 = sum(sales.values_list('quantity', flat=True)) 
        value3=sum(sales.values_list('value', flat=True))
        if quantity2>quantity3:
            closing_quantity=quantity2-quantity3
        else:
             closing_quantity=quantity3-quantity2
        rate=stockitem.rateper 
        rate1=sum(purchase.values_list('rateper', flat=True))
        count2=voucherlist.objects.filter(vouch_type='purchase').count()
        count1=count2+1
        avg=rate+rate1
        average=avg/count1
        closing_balance=average * closing_quantity
        s=StockGroup.objects.get(id=pk)
        g=s.id
        print(g)
        stocks_table = StockGroup.objects.get(id=pk)
        
        stocks_table.closing_balance=closing_balance
        stocks_table.save()
        return render(request,'stockItem_monthlySummary.html',{'cmp':tally,'st':stockitem,'opening_quantity':opening_quantity,'opening_value':opening_value,'quantity':quantity,'value':value,'quantity3':quantity3,'value3':value3,'quantity2':closing_quantity,'closing_balance':closing_balance})        
    
def stockitem_vouchersApril(request,pk):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        stockitem=stock_item.objects.get(id=pk)
        opening_quantity=stockitem.quantity
        opening_value=stockitem.value
        msg1="1-Apr-2022 to 30-Apr-2022"
        voucher=voucherlist.objects.filter(item=pk)
        purchase=voucherlist.objects.filter(vouch_type='purchase')
        quantity = sum(purchase.values_list('quantity', flat=True))
        quantity2=quantity+opening_quantity
        value = sum(purchase.values_list('value', flat=True))
        value2=value+opening_value
        sales=voucherlist.objects.filter(vouch_type='sales')
        quantity3 = sum(sales.values_list('quantity', flat=True)) 
        value3=sum(sales.values_list('value', flat=True))
        if quantity2>quantity3:
            closing_quantity=quantity2-quantity3
        else:
             closing_quantity=quantity3-quantity2
        rate=stockitem.rateper 
        rate1=sum(purchase.values_list('rateper', flat=True))
        count2=voucherlist.objects.filter(vouch_type='purchase').count()
        count1=count2+1
        avg=rate+rate1
        average=avg/count1
        closing_balance=average * closing_quantity
        return render(request,'stockItem_vouchersApril.html',{'cmp':tally,'st':stockitem,'msg1':msg1,'voucher':voucher,'quantity':quantity2,'value':value2,'quantity3':quantity3,'value3':value3,'closing_quantity':closing_quantity,'closing_balance':closing_balance})        
    
def loans_ledger(request):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
    t_id=3
    tally = Companies.objects.filter(id=t_id)
    grp= tally_group.objects.get(group_name='Loans & Advances')
    ledger=tally_ledger.objects.filter(grp_id=grp.id)
    total=sum(ledger.values_list('closing_balance', flat=True))
    return render(request,'groupsummaryloans.html',{'cmp':tally,'ledger':ledger,'total':total})
def loans_monthly_summary(request,pk):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')  
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        led=tally_ledger.objects.get(id=pk)
        led1=Ledger_vouchers.objects.filter(ledger=pk)
        
        led_id=Ledger_vouchers.objects.filter(ledger=pk)[0]
        print(led_id.ledger)
        led_name=led_id.ledger
        ledg=tally_ledger.objects.get(name=led_name)
        opening_balance=ledg.opening_blnc
        credit=sum(led1.values_list('credit', flat=True))
        debit=sum(led1.values_list('debit', flat=True))
        balance=tally_ledger.objects.get(id=pk)
        close_balance=balance.closing_balance
        return render(request,'loansmonthlysummary.html',{'cmp':tally,'led':led,'opening_balance':opening_balance,'ledg':ledg,'credit':credit,'debit':debit,'close_balance':close_balance})
    
def loans_voucher(request,pk):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        comp=Companies.objects.get(id=t_id)
        led=Ledger_vouchers.objects.filter(ledger=pk)
        
        a=comp.fin_begin
        month=a.month
        if a.month==4:
            msg1="1-Apr-2022 to 30-Apr-2022"
        led_id=Ledger_vouchers.objects.filter(ledger=pk)[0]
        print(led_id.ledger)
        led_name=led_id.ledger
        ledg=tally_ledger.objects.get(name=led_name)
        opening_balance=ledg.opening_blnc
        credit=sum(led.values_list('credit', flat=True))
        debit=sum(led.values_list('debit', flat=True))
        deb_balance=opening_balance+debit
        closing_balance=deb_balance-credit
        ledg.closing_balance=closing_balance
        ledg.save()
        return render(request,'loan_voucher.html',{'cmp':tally,'msg1':msg1,'led':led,'ledg':ledg,'credit':credit,'debit':debit,'closing_balance':closing_balance})
def sundry_ledger(request):   
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        grp= tally_group.objects.get(group_name='Sundry Debtors')
        ledger=tally_ledger.objects.filter(grp_id=grp.id)
        total=sum(ledger.values_list('closing_balance', flat=True))
        return render(request,'sundry_ledger.html',{'cmp':tally,'ledger':ledger,'total':total})
    
def sundry_monthly_summary(request,pk):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')  
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        led=tally_ledger.objects.get(id=pk)
        ledg=Ledger_vouchers.objects.filter(ledger=pk)
        credit=sum(ledg.values_list('credit', flat=True))
        debit=sum(ledg.values_list('debit', flat=True))
        deb_balance=led.opening_blnc+debit
        closing_balance=deb_balance-credit
        
        return render(request,'sundrymonthlysummary.html',{'cmp':tally,'led':led,'credit':credit,'debit':debit,'closing_balance':closing_balance,'deb_balance':deb_balance})
 
def cash(request):
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        grp= tally_group.objects.get(group_name='Cash in Hand')
        ledger=tally_ledger.objects.filter(grp_id=grp.id)
        total=sum(ledger.values_list('closing_balance', flat=True))
        return render(request,'cashledger.html',{'cmp':tally,'ledger':ledger,'total':total})

def cash_monthly_summary(request,pk):     
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/')  
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        led=tally_ledger.objects.get(id=pk)
        ledg=Ledger_vouchers.objects.filter(ledger=pk)
        credit=sum(ledg.values_list('credit', flat=True))
        debit=sum(ledg.values_list('debit', flat=True))
        deb_balance=led.opening_blnc+debit
        closing_balance=deb_balance-credit
        
        return render(request,'cashmonthlysummary.html',{'cmp':tally,'led':led,'credit':credit,'debit':debit,'closing_balance':closing_balance,'deb_balance':deb_balance})  

def bank(request):
#    if 't_id' in request.session:
#         if request.session.has_key('t_id'):
#             t_id = request.session['t_id']
#         else:
#             return redirect('/')
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        grp= tally_group.objects.get(group_name='Bank Accounts')
        ledger=tally_ledger.objects.filter(grp_id=grp.id)
        total=sum(ledger.values_list('closing_balance', flat=True))
        return render(request,'bankledger.html',{'cmp':tally,'ledger':ledger,'total':total})     
    
def bank_monthly_summary(request,pk):  
    # if 't_id' in request.session:
    #     if request.session.has_key('t_id'):
    #         t_id = request.session['t_id']
    #     else:
    #         return redirect('/') 
        t_id=3
        tally = Companies.objects.filter(id=t_id)
        led=tally_ledger.objects.get(id=pk)
        ledg=Ledger_vouchers.objects.filter(ledger=pk)
        credit=sum(ledg.values_list('credit', flat=True))
        debit=sum(ledg.values_list('debit', flat=True))
        deb_balance=led.opening_blnc+debit
        closing_balance=deb_balance-credit
        
        return render(request,'bankmonthlysummary.html',{'cmp':tally,'led':led,'credit':credit,'debit':debit,'closing_balance':closing_balance,'deb_balance':deb_balance})
