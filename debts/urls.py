from django.urls import path

from debts.views.create_debt import CreateDebtView
from debts.views.delete_debt import DeleteDebtView
from debts.views.get_debts_by_debtor import GetDebtsByDebtorView

urlpatterns = [
    path('debts', CreateDebtView.as_view(), name='create-debts'),
    path('debts/<int:debt_id>', DeleteDebtView.as_view(), name='delete-debts'),
    path('debtors/<int:debtor_id>/debts', GetDebtsByDebtorView.as_view(), name='get-debts-by-debtor'),
]