from django.urls import path

from debtors.views import CreateDebtorView
from debtors.views.get_debtors_by_user import GetDebtorsByUserView

urlpatterns = [
    path("debtors", CreateDebtorView.as_view(), name="create-debtor"),
    path("users/debtors/<slug:user_slug>", GetDebtorsByUserView.as_view(), name="get-debtors-by-user"),
]