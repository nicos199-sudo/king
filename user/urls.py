from django.urls import path
from . import views

urlpatterns = {
    path('user/', views.index, name='user'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.user_password, name='user_password'),
    path('login/', views.login_form, name='login_form'),
    path('signup/', views.signup_form, name='signup_form'),
    path('logout/', views.logout_func, name='logout'),
    path('orders/', views.user_orders, name='user_orders'),
    path('orderdetail/<int:id>', views.user_orderdetail, name='user_orderdetail'),
    path('orders_product/', views.user_orders_product, name='user_orders_product'),
    path('order_product_detail/<int:id>/<int:oid>', views.user_order_product_detail, name='user_order_product_detail'),

    path('comments/', views.user_comments, name='user_comments'),
    path('deletecomments/<int:id>', views.user_deletecomments, name='user_deletecomments'),

}
