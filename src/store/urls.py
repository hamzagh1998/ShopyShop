from django.urls import path
from store import views

app_name = "store"

urlpatterns = [
    path('cart/', views.cartView, name="cart"),
    path('shipping-data/', views.shippingDataView, name="shipping-data"),
    path('get-validation/', views.getValidation, name="get-validation"),
    path('add-new-product/', views.productFormView, name="add-new-product"),
    path('update-product/<int:id>/', views.updateProductFormView, name="update-product"),
    path('delete-product/<int:id>/', views.deleteProduct, name="delete-product"),
    path('customers-requestes/', views.shippingView, name="customers-requestes"),
    path('order-list/<int:id>/', views.orderListView, name="order-list"),
    path('logout/', views.logOut, name="logout"),
]
