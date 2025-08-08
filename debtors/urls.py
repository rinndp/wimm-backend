from django.urls import path

from debtors.views import CreateDebtorView
from debtors.views.delete_debtor import DeleteDebtorView
from debtors.views.get_debtors_by_user import GetDebtorsByUserView

urlpatterns = [
    path("debtors", CreateDebtorView.as_view(), name="create-debtor"),
    path("debtors/<int:debtor_id>", DeleteDebtorView.as_view(), name="delete-debtor"),
    path("users/<slug:user_slug>/debtors", GetDebtorsByUserView.as_view(), name="get-debtors-by-user"),
]