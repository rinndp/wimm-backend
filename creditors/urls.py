from django.urls import path

from creditors.views import CreateCreditorView, GetCreditorsByUserView
from creditors.views.delete_creditor import DeleteCreditorView

urlpatterns = [
    path("creditors", CreateCreditorView.as_view(), name="create-creditor"),
    path("creditors/<int:creditor_id>", DeleteCreditorView.as_view(), name="delete-creditor"),
    path("users/<slug:user_slug>/creditors", GetCreditorsByUserView.as_view(), name="get-creditors-by-user"),
]