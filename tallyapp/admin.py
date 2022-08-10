from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Countries,CountriesAdmin)

#admin.site.register(States)
class StatesAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(States,StatesAdmin)

#admin.site.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Companies,CompaniesAdmin)


# #admin.site.register(SALES)'ANN'
# class SalesAdmin(admin.ModelAdmin):
#     list_display=('sales',)
# admin.site.register(Sales,SalesAdmin)

# #admin.site.register(PURCHASE)'ANN'
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display=('purchases',)
# admin.site.register(Purchase,PurchaseAdmin)

#admin.site.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Group,GroupAdmin)

admin.site.register(Features)
admin.site.register(Costcentre)

#admin.site.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display=('symbol',)
admin.site.register(Currency,CurrencyAdmin)

#admin.site.register(Voucher)
class VoucherAdmin(admin.ModelAdmin):
    list_display=('voucher_name',)
admin.site.register(Voucher,VoucherAdmin)


#admin.site.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display=('name',)
admin.site.register(Ledger,LedgerAdmin)

admin.site.register(Ledger_Mailing_Details)
admin.site.register(Ledger_Banking_Details)
admin.site.register(Ledger_Asset_Rounding)
admin.site.register(Ledger_Asset_Statutory)

admin.site.register(Purchase)#ann
admin.site.register(Sales)#ann
admin.site.register(Journal)#ann
admin.site.register(Particular)#ann
