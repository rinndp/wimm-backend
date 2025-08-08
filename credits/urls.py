from django.urls import path

from credits.views import GetCreditsByCreditorView
from credits.views.create_credit import CreateCreditView
from credits.views.delete_credit import DeleteCreditView

urlpatterns = [
    path('credits', CreateCreditView.as_view(), name='create-credit'),
    path('credits/<int:credit_id>', DeleteCreditView.as_view(), name='delete-credit'),
    path('creditors/<int:creditor_id>/credits', GetCreditsByCreditorView.as_view(), name='get-credits-by-creditor'),
]