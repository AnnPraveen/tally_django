from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('company',views.company,name='company'),
    path('disp_more_reports',views.disp_more_reports,name='disp_more_reports'),#ann
    path('balancesheet',views.balancesheet,name='balancesheet'), #ann
    path('index1',views.index1,name='index1'),
    path('createcompany',views.createcompany,name='createcompany'),
    path('companycreate',views.companycreate,name='companycreate'),
    #path('ledger/<int:pk>',views.ledger,name='ledger'),

    path('costcentre/<int:pk>',views.costcentre,name='costcentre'),
    path('currency/<int:pk>',views.currency,name='currency'),
    path('features/<int:pk>',views.features,name='features'),
    path('creategroup/<int:pk>',views.creategroup,name='creategroup'),
    # path('features',views.features,name='features'),
    path('altercompanyview',views.altercompanyview,name='altercompanyview'),
    path('selectcompany',views.selectcompany,name='selectcompany'),
    path('shutcompany',views.shutcompany,name='shutcompany'),
    path('addstate',views.addstate,name='addstate'),
    path('addcountry',views.addcountry,name='addcountry'),
    path('altercompany/<int:pk>',views.altercompany,name='altercompany'),
    path('ratesofexchange/<int:pk>',views.ratesofexchange,name='ratesofexchange'),
    path('voucher/<int:pk>',views.voucher,name='voucher'),
    path('democreate',views.democreate,name='democreate'),
    path('demo1/<int:pk>',views.demo1,name='demo1'),
    # path('demo2/<int:pk>',views.demo2,name='demo2'), 
    path('voucher1',views.voucher1,name='voucher1'),#ann
    path('groupsummary/<int:lk>',views.groupsummary,name='groupsummary'),#groupsummary ann
    path('ledgergroupsummary/<int:pk>',views.ledgergroupsummary,name='ledgergroupsummary'),#groupledger ann
    path('ledgersummary/<int:lk>',views.ledgersummary,name='ledgersummary'),#groupledger ann
    # path('sales',views.sales,name='sales'),#salesann
    path('journal',views.journal,name='journal'),#journalnn
    # path('purchase',views.purchase,name='purchase'),#purchaseann
  #
    path('listofledger/<int:pk>',views.listofledger,name='listofledger'),#ann
    #urls....
    path('listofpurchasevoucher/<int:pk>',views.listofpurchasevoucher,name='listofpurchasevoucher'),#ann,#listofpurchasevouchers
    path('listjournalvouchers/<int:pk>',views.listjournalvouchers,name='listjournalvouchers'),#ann,#listofjournalvouchers
    path('listofsalesvoucher/<int:pk>',views.listofsalesvoucher,name='listofsalesvoucher'),#ann
    path('salesregister',views.salesregister,name='salesregister'),#ann
    path('purchaseregister',views.purchaseregister,name='purchaseregister'),#ann
    path('journalregister',views.journalregister,name='journalregister'),#ann
    #..urls
    path('featurecompany/<int:pk>',views.featurecompany,name='featurecompany'),
    path('disable/<int:pk>',views.disable,name='disable'),
    path('enable/<int:pk>',views.enable,name='enable'),

    path('showVouchers',views.showvouchers,name='showvouchers'),
    path('alter',views.alter,name='alter'),
    # path('dispatch_details',views.dispatch_details,name='dispatch_details'),#click party name in sale form to get delivery details
    path('altercompany_view',views.altercompany_view,name='altercompany_view'),
   
    path('listofgroup',views.listofgroup,name='listofgroup'),
    #path('listofledgers',views.listofledgers,name='listofledgers'),#ann
    path('listofcostcentres',views.listofcostcentres,name='listofcostcentres'),
    path('listofcurrencies',views.listofcurrencies,name='listofcurrencies'),
    path('listofvouchertypes',views.listofvouchertypes,name='listofvouchertypes'),
    #############Nitya
    
 path('balancesheet_new',views.balancesheet_new,name='balancesheet_new'),

    path('capital_group_summary',views.capital_group_summary,name='capital_group_summary'),
    path('ledgermonthly/<id>',views.ledgermonthly,name='ledgermonthly'),
    path('quit',views.quit,name='quit'),
    path('ledger_vouchers/<pk>/<id>',views.ledger_vouchers,name='ledger_vouchers'),
    path('vouch_delete/<pk>',views.vouch_delete,name='vouch_delete'),

    path('loanl_group_summary',views.loanl_group_summary,name='loanl_group_summary'),

    path('fixed_assets_group_summary',views.fixed_assets_group_summary,name = 'fixed_assets_group_summary'),
############Profit and loss
path('profit',views.profit,name='profit'),
    path('stockgroup',views.stockgroup,name='stockgroup'),
    path('stock_item',views.stock_items,name='stock_items'),
    path('group',views.stock_groups,name="stock_groups"),
    path('payhead',views.payhead,name='payhead'),
    path('items/<int:pk>',views.item_list,name='item_list'),
    path('payhead_list',views.payhead_list,name='payhead_list'),
    path('ledger',views.ledger,name='ledger'),
    path('save_ledger',views.save_ledger,name='save_ledger'),
    path('sales',views.sales,name='sales'),
    path('indirect',views.indirect,name='indirect'),
    path('grp_month/<int:pk>',views.grp_month,name='grp_month'),
    path('grp_month2/<int:pk>',views.grp_month_2,name='grp_month_2'),
    path('sales_month/<int:pk>',views.sales_month,name='sales_month'),
    path('sales_month2/<int:pk>',views.sales_month_2,name='sales_month_2'),
    path('payhead/<int:pk>',views.payhead_month,name='payhead_month'),
    path('stock_month/<int:pk>',views.stock_month,name='stock_month'),
    path('voucher/<int:pk>',views.pay_voucher,name='pay_voucher'),
    path('stock_voucher/<int:pk>',views.stock_voucher,name='stock_voucher'),
    path('purchase',views.purchase,name='purchase'),
    path('direct_exp',views.direct_exprenses,name='direct_exprenses'),
    path('indirect_exp',views.indirect_expenses,name='indirect_expenses'),
    path('stock_group2',views.stock_group2,name='stock_group2'),
    path('items_2/<int:pk>',views.items_2,name='items_2'),
#########Neethu
    path('investments',views.investments,name="investments"), 
    path('monthly_summary/<int:pk>',views.monthly_summary,name="monthly_summary"),
    path('ledgervouchers/<int:pk>',views.ledgervouchers,name="ledgervouchers"),
    path('currentassets',views.currentassets,name="currentassets"),
    path('stockgroupsummary',views.stockgroupsummary,name="stockgroupsummary"),
    path('stockitem/<int:pk>',views.stockitem,name="stockitem"),
    path('stockItem_monthlySummary/<int:pk>',views.stockItem_monthlySummary,name="stockItem_monthlySummary"),
    path('stockitem_vouchersApril/<int:pk>',views.stockitem_vouchersApril,name="stockitem_vouchersApril"),
    path('loans_ledger',views.loans_ledger,name="loans_ledger"),
    path('loans_monthly_summary/<int:pk>',views.loans_monthly_summary,name="loans_monthly_summary"),
    path('loans_voucher/<int:pk>',views.loans_voucher,name="loans_voucher"),
    path('sundry_ledger',views.sundry_ledger,name="sundry_ledger"),
    path('sundry_monthly_summary/<int:pk>',views.sundry_monthly_summary,name='sundry_monthly_summary'),
    path('cash',views.cash,name='cash'),
    path('cash_monthly_summary/<int:pk>',views.cash_monthly_summary,name='cash_monthly_summary'),
    path('bank',views.bank,name="bank"),
    path('bank_monthly_summary/<int:pk>',views.bank_monthly_summary,name="bank_monthly_summary"),
     # path('sales_add',views.sales_add,name='sales_add'),#ann
    # path('saleview/<int:pk>',views.saleview,name='saleview'),#ann
    # path('purchaseview/<int:pk>',views.purchaseview,name='purchaseview'),#ann
    
   
    
    # path('partydetails',views.partydetails,name='partydetails'),#ann
]



