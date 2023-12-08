from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('product/',views.product,name="product"),
    path('shoping-cart/',views.shoping_cart,name="shoping-cart"),
    path('blog/',views.blog,name="blog"),    
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('product-detail/',views.product_detail,name="product-detail"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('forgot-password/',views.forgot_password,name="forgot-password"),
    path('verify-otp/',views.verify_otp,name="verify-otp"),
    path('new-password/',views.new_password,name="new-password"),
    path('logout/',views.logout,name="logout"),
    path('update-profile/',views.update_profile,name="update-profile"),
    path('update_data/',views.update_data,name="update_data"),
    path('change-password/',views.change_password,name="change-password"),
    path('seller-index/',views.seller_index,name="seller-index"),
    path('seller-add-product/',views.seller_add_product,name="seller-add-product"),
    path('seller-view-product/',views.seller_view_product,name="seller-view-product"),
    path('seller-product-detail/<int:pk>/',views.seller_product_detail,name="seller-product-detail"),
    path('seller-edit-product/<int:pk>/',views.seller_edit_product,name="seller-edit-product"),
    path('seller-product-delete/<int:pk>/',views.seller_product_delete,name="seller-product-delete"),
    
    
    
    
    
    
    

    
]
