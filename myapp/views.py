from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from . models import Signup,Product
import random
import requests

# Create your views here.

def index(request):
    return render(request,"index.html")

def seller_index(request):
    seller=Signup.objects.get(email=request.session['email'])
    products=Product.objects.filter(seller=seller)
    return render(request,"seller-index.html",{'products':products})

def product(request):
    return render(request,"product.html")

def shoping_cart(request):
    return render(request,"shoping-cart.html")

def blog(request):
    return render(request,"blog.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")

def product_detail(request):
    return render(request,"product-detail.html")

def signup(request):
    if request.method=="POST":
        try:
            Signup.objects.get(email = request.POST['email'])
            msg = "Email Is Already Registered , Please Enter Another Email Id"
            return render(request,"signup.html",{'msg':msg})
            
        except:
            if request.POST['password']==request.POST['cpassword']:
                Signup.objects.create(
                    user_type=request.POST['usertype'],
                    name=request.POST['name'],
                    email=request.POST['email'],
                    mobile=request.POST['mobile'],
                    address=request.POST['address'],
                    image = request.FILES['profile_picture'],
                    password=make_password(request.POST['password']),
                                    
                )
                msg = "Sign Up Successfully"
                return render(request,"login.html",{'msgs':msg}) 
            else:
                msg = "Password or Confirm Password Does Not Matched"
                return render(request,"signup.html",{'msg':msg})     
    else:   
        return render(request,"signup.html")

def login(request):
    if request.method=="POST":
        try:
            user = Signup.objects.get(email = request.POST['email'])
            
            if check_password(request.POST['password'],user.password):
                if user.user_type=="Buyer":
                    request.session['email'] = user.email
                    request.session['name']=user.name
                    request.session['image'] = user.image.url if user.image else None                
                    return render(request,"index.html")
                else:
                    request.session['email'] = user.email
                    request.session['name']=user.name
                    request.session['image'] = user.image.url if user.image else None                
                    return render(request,"seller-index.html")
            else:
                msg ="password Incorrect"
                return render(request,"login.html",{'msg':msg})
        except:
            msg ="Email Not Registered"
            return render(request,"login.html",{'msg':msg})      
            
    else:      
      return render(request,"login.html")




def forgot_password(request):
    if request.method == "POST":
        mobile = request.POST['mobile']
        user = Signup.objects.get(mobile=mobile)

        if user:
            otp = random.randint(1000, 9999)
            url = "https://www.fast2sms.com/dev/bulkV2"
            querystring = {
                "authorization": "VlO5sarhU8T76cPG0qMmvxHKYBiJ4DRZInEzfAF3L1pudekWCQf1t4D63AikUrC57TRZdJ8QMgGWbHYS",
                "variables_values": str(otp),
                "route": "otp",
                "numbers": mobile
            }
            headers = {'cache-control': "no-cache"}
            response = requests.request("GET", url, headers=headers, params=querystring)
            print(response.text)
            request.session['mobile'] = mobile
            uotp = make_password(str(otp))
            return render(request, "otp.html", {'otp': uotp})
        else:
            msg = "Mobile Number Not Exists"
            return render(request, "forgot-password.html", {'msg': msg})

    return render(request, "forgot-password.html")

    
def verify_otp(request):
    otp = request.POST['otp']
    if check_password(request.POST['uotp'],otp):
        return render(request,"new-password.html")
    else:
        msg = "Invalid otp"
        return render(request,"otp.html",{'msg':msg})

def new_password(request):
    if request.POST['new-password']==request.POST['cnew-password']:
        mobile= request.session['mobile']
        user = Signup.objects.get(mobile=mobile)
        user.password=make_password(request.POST['new-password'])
        user.save()
        return redirect('login')
    else:
        msg= "password and confirm password does not matched"  
        return render(request,"new-password.html",{'msg':msg})

def logout(request):
    del request.session['email']
    del request.session['image']
    del request.session['name']
    return render(request,"login.html")


def update_profile(request):
    user = Signup.objects.get(email = request.session['email'])
    if user.user_type=="Buyer":    
        return render(request,"update-profile.html",{'user':user})
    else:
        return render(request,"seller-update-profile.html",{'user':user})
def update_data(request):
    if request.method == "POST":
        user = Signup.objects.get(email=request.session['email'])
        
        user.name = request.POST['name']
        user.mobile = request.POST['mobile']
        user.address = request.POST['address']
        
        if 'pimage' in request.FILES:
            user.image = request.FILES['pimage']
        
        user.save()
        request.session['image'] = user.image.url if user.image else None
        msg = "Profile update successful"
        if user.user_type=="Buyer":
            return render(request, "update-profile.html", {'msg': msg, 'user': user})
        else:
            return render(request, "seller-update-profile.html", {'msg': msg, 'user': user})            
    else:
        if user.user_type=="Buyer":
            return render(request, "update-profile.html",{'user':user})
        else:
            return render(request, "seller-update-profile.html",{'user':user})

            
    
def change_password(request):
    user = Signup.objects.get(email=request.session['email'])
    if request.method=='POST':        
        if check_password(request.POST['old-password'],user.password):
            if request.POST['new-password']==request.POST['cnew-password']:
                user.password=make_password(request.POST['new-password'])                
                user.save()
                return redirect('logout')
            else:
                msg= "password or confirm password not matched"
                if user.user_type=="Buyer": 
                    return render(request,"change-password.html",{'msg':msg})
                else:
                    return render(request,"seller-change-password.html",{'msg':msg})
                    
        else:
            msg= "old Password Does Not Matched"
            if user.user_type=="Buyer": 
                return render(request,"change-password.html",{'msg':msg})
            else:
                return render(request,"seller-change-password.html",{'msg':msg})
                
    else:
        if user.user_type=="Buyer":   
            return render(request,"change-password.html")
        else:
            return render(request,"seller-change-password.html")

def seller_add_product(request):
    
    seller=Signup.objects.get(email=request.session['email'])
    if request.method=="POST":
        Product.objects.create(
            seller=seller,
            product_name=request.POST['product-name'],
            product_price=request.POST['product-price'],
            product_category=request.POST['product-category'],
            product_size=request.POST['product-size'],
            product_brand=request.POST['product-brand'],
            product_desc=request.POST['product-desc'],
            product_fimage=request.FILES['product-fimage'],
            product_bimage=request.FILES['product-bimage'],          
            
         
        )
        msg="Product Add SuccessFull"
        return render(request,"seller-add-product.html",{'msg':msg})
    else:   
        return render(request,"seller-add-product.html")

def seller_view_product(request):
    seller=Signup.objects.get(email=request.session['email'])
    products=Product.objects.filter(seller=seller)
    return render(request,"seller-view-product.html",{'products':products})


def seller_product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,"seller-product-detail.html",{'product':product})

def seller_edit_product(request,pk):
    product=Product.objects.get(pk=pk)
    if request.method=="POST":
        product.product_name=request.POST['product-name']
        product.product_price=request.POST['product-price']
        product.product_category=request.POST['product-category']
        product.product_size=request.POST['product-size']
        product.product_brand=request.POST['product-brand']
        product.product_desc=request.POST['product-desc']
        try:
            product.product_fimage=request.FILES['product-fimage']
            product.product_bimage=request.FILES['product-bimage']
        except:
            pass 
        product.save()
        msg="Product Update Successfull"
        return render(request,"seller-edit-product.html",{'product':product,'msg':msg})
    else:
        return render(request,"seller-edit-product.html",{'product':product})
    
def seller_product_delete(request,pk):
    product=Product.objects.get(pk=pk)
    product.delete()
    return redirect('seller-view-product')