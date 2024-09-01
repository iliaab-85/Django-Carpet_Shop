from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import Login, Register, edit_Profile, Product, \
    Seller_Legal_Form, Seller_Genuine_Form, Logins_Seller, \
    edit_Profile_Seller_Legal, edit_Profile_Seller_Genuine, \
    Register_Support, Login_Support, Logins_Seller_Form

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import User_Save, Add_Product, Product_Order, Like, \
    User_View, Chats, Chats_Code, Product_Comment, Seller_Legal, Seller_Genuine, Supporter, Order_Complete, Product_buyed

from .UserAuth import UserAuth
import datetime
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import socket
import random
from django.db.models import Q
import json
from datetime import datetime, timedelta
from jdatetime import datetime as jdatetime
import itertools
import requests

yesterday = datetime.now() - timedelta(0)
Times = jdatetime.fromgregorian(day=yesterday.day, month=yesterday.month,
                                year=yesterday.year).strftime("%Y/%m/%d")
'''
import jdatetime

# تاریخ ورودی
date_string = "07/28/2024 08:01:52 AM"

# تبدیل تاریخ به فرمت datetime
date_object = datetime.strptime(date_string, "%m/%d/%Y %I:%M:%S %p")

# تبدیل تاریخ به شمسی
jalali_date = jdatetime.date.fromgregorian(date=date_object.date())

# چاپ تاریخ شمسی
print(jalali_date)
'''
# Create your views here.


hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)


def home(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        icons = ""
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        incll = "incl2.html"
        user = User_Save.objects.filter(Id=user_st["User"].id).first()
        script = '/static/js/tm.js'
        incl = "include.html"
        include = "include4.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        user_likes = Like.objects.filter(user_Id=user_st["User"].id).first()

        Legal = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
        My_user = User_Save.objects.filter(Id=user_st["User"].id).all()
        if Legal.exists():
            user = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif Genuine.exists():
            user = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif My_user.exists():
            user = User_Save.objects.filter(Id=user_st["User"].id).all()
            Res = "User"
        else:
            user = Supporter.objects.filter(Id=user_st["User"].id).all()
            Res = "Support"

        Product_Code = ""
        AllProduct = ""
        url = "http://127.0.0.1:8000/apiread_product/?format=json"

        response = requests.request("GET", url)
        obj = json.loads(response.text)

        if len(obj) > 0:
            for product in obj:
                Product_Code = str(product["Product_Code"])
        else:
            AllProduct = "Empty"
        return render(request=request, template_name="home.html",
                      context={"icon": icon, "circle": circle, "href": href, "Res": Res,
                               "script": script, "user": user, "AllProduct": AllProduct,
                               "user_st": user_st, "incl": incl, "include": include,
                               "user_likes": user_likes, "Product_Code": Product_Code,
                               "icons": icons, "incll": incll, "Mylist_sorts": Mylist_sorts})
    else:
        icons = "bi bi-box-arrow-in-left"
        text = "ورود | ثبت‌نام"
        href = "/Farshtore/login"
        style = "border-radius: 5px;width: 100%;padding: 15% 15% 15% 15%;border:1px solid;padding:8;"
        script = '/static/js/user.js'
        incl = "include2.html"
        include = "include4.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        AllProduct = Add_Product.objects.all()

        return render(request=request, template_name="home.html",
                      context={"icons": icons, "style": style, "text": text, "href": href,
                               "script": script, "incl": incl, "AllProduct": AllProduct,
                               "include": include, "user_st": user_st, "incll": incll,
                               "Mylist_sorts": Mylist_sorts})


def aboutUs(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Legal = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
        My_user = User_Save.objects.filter(Id=user_st["User"].id).all()
        if Legal.exists():
            user = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif Genuine.exists():
            user = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif My_user.exists():
            user = User_Save.objects.filter(Id=user_st["User"].id).all()
            Res = "User"
        else:
            user = Supporter.objects.filter(Id=user_st["User"].id).all()
            Res = "Support"

        return render(request=request, template_name="about.html",
                      context={"icon": icon, "circle": circle, "href": href,
                               "script": script, "user": user, "Res": Res, "Mylist_sorts": Mylist_sorts,
                               "user_st": user_st, "incl": str(incl), "incll": incll})
    else:
        icon = "bi bi-box-arrow-in-left"
        text = "ورود | ثبت‌نام"
        href = "/Farshtore/login"
        style = "border-radius: 5px;width: 100%;padding: 15% 15% 15% 15%;border:1px solid;padding:8;"
        script = '/static/js/user.js'
        incl = "include2.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        return render(request=request, template_name="about.html",
                      context={"icon": icon, "style": style, "text": text, "href": href,
                               "script": script, "incl": str(incl), "incll": incll, "Mylist_sorts": Mylist_sorts})


def contact(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Legal = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
        My_user = User_Save.objects.filter(Id=user_st["User"].id).all()
        if Legal.exists():
            user = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif Genuine.exists():
            user = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif My_user.exists():
            user = User_Save.objects.filter(Id=user_st["User"].id).all()
            Res = "User"
        else:
            user = Supporter.objects.filter(Id=user_st["User"].id).all()
            Res = "Support"

        return render(request=request, template_name="contact.html",
                      context={"icon": icon, "circle": circle, "href": href,
                               "script": script, "user": user, "Res": Res,
                               "user_st": user_st, "incl": str(incl), "incll": incll, "Mylist_sorts": Mylist_sorts})
    else:
        icon = "bi bi-box-arrow-in-left"
        text = "ورود | ثبت‌نام"
        href = "/Farshtore/login"
        style = "border-radius: 5px;width: 100%;padding: 15% 15% 15% 15%;border:1px solid;padding:8;"
        script = '/static/js/user.js'
        incl = "include2.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        return render(request=request, template_name="contact.html",
                      context={"icon": icon, "style": style, "text": text, "href": href,
                               "script": script, "incl": str(incl), "incll": incll, "Mylist_sorts": Mylist_sorts})


def question(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Legal = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
        My_user = User_Save.objects.filter(Id=user_st["User"].id).all()
        if Legal.exists():
            user = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif Genuine.exists():
            user = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif My_user.exists():
            user = User_Save.objects.filter(Id=user_st["User"].id).all()
            Res = "User"
        else:
            user = Supporter.objects.filter(Id=user_st["User"].id).all()
            Res = "Support"

        return render(request=request, template_name="question.html",
                      context={"icon": icon, "circle": circle, "href": href,
                               "script": script, "user": user, "Res": Res,
                               "user_st": user_st, "incl": str(incl), "incll": incll, "Mylist_sorts": Mylist_sorts})
    else:
        icon = "bi bi-box-arrow-in-left"
        text = "ورود | ثبت‌نام"
        href = "/Farshtore/login"
        style = "border-radius: 5px;width: 100%;padding: 15% 15% 15% 15%;border:1px solid;padding:8;"
        script = '/static/js/user.js'
        incl = "include2.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        return render(request=request, template_name="question.html",
                      context={"icon": icon, "style": style, "text": text, "href": href,
                               "script": script, "incl": str(incl), "incll": incll, "Mylist_sorts": Mylist_sorts})


def CheckLogin(request):
    forms = Login(request.POST)
    if forms.is_valid():
        user = authenticate(request, username=forms.data["UserName"], password=forms.data["Password"])
        if user is not None:
            login(request, user)
            user_st = UserAuth().StateLogin(request)
            User_Id = user_st["User"].id
            return HttpResponse(str(User_Id))
        else:
            return HttpResponse("اطلاعات صحیح نیست")


def Seller_Login_Check(request, Type):
    forms = Logins_Seller_Form(request.POST)
    if forms.is_valid():
        username = forms.data["UserName"] + "_Seller_" + Type
        user = authenticate(request, username=username, password=forms.data["Password"])
        if user is not None:
            login(request, user)
            user_st = UserAuth().StateLogin(request)
            User_Id = user_st["User"].id
            return HttpResponse(str(User_Id))
        else:
            return HttpResponse("اطلاعات صحیح نیست")


@csrf_exempt
def Check_Support_login(request):
    forms = Login_Support(request.POST)
    if forms.is_valid():
        user = authenticate(request, username=forms.data["UserName"] + "_Support", password=forms.data["Password"])
        if user is not None:
            login(request, user)
            user_st = UserAuth().StateLogin(request)
            User_Id = user_st["User"].id
            return HttpResponse(str(User_Id))
        else:
            return HttpResponse("اطلاعات صحیح نیست")


@csrf_exempt
def RegisterAction(request):
    if request.method == "POST":
        forms = Register(request.POST)
        if forms.is_valid():
            users = User.objects.filter(username=forms.data["UserName"]).all()
            if users.exists():
                return HttpResponse("این کاربر وجود دارد")
            else:
                Legal = Seller_Legal.objects.all()
                Genuine = Seller_Genuine.objects.all()
                Support = Supporter.objects.all()
                Users = User_Save.objects.all()

                My_Id = []

                User_Ids = max(obj.Id for obj in Users) if Users else 0
                My_Id.append(User_Ids)
                Support_Ids = max(obj.Id for obj in Support) if Support else 0
                My_Id.append(Support_Ids)

                Legal_Ids = max(obj.Seller_Id for obj in Legal) if Legal else 0
                My_Id.append(Legal_Ids)
                Genuine_Ids = max(obj.Seller_Id for obj in Genuine) if Genuine else 0
                My_Id.append(Genuine_Ids)

                Add_Id = max(My_Id) + 1

                us = User.objects.create_user(id=Add_Id, username=forms.data["UserName"],
                                              password=forms.data["Password"], first_name=forms.data["Name"],
                                              last_name=forms.data["Family"], email=forms.data["Email"])
                us.save()
                Saved_data = User_Save(Id=Add_Id, name=forms.data["Name"], family=forms.data["Family"],
                                       UserName=forms.data["UserName"], Email=forms.data["Email"],
                                       Phone=forms.data["Phone"])
                Saved_data.save()
            return HttpResponseRedirect("/Farshtore/login")

        else:
            return HttpResponse("فرم نامعتبر می باشد")


@csrf_exempt
def Register_Support_Action(request):
    if request.method == "POST":
        forms = Register_Support(request.POST)
        if forms.is_valid():
            username = forms.data["UserName"] + "_Support"
            users = User.objects.filter(username=username).all()
            Chat_Code = random.randint(0, 10000)
            if users.exists():
                return HttpResponse("این کاربر وجود دارد")
            else:
                Legal = Seller_Legal.objects.all()
                Genuine = Seller_Genuine.objects.all()
                Support = Supporter.objects.all()
                Users = User_Save.objects.all()

                My_Id = []

                User_Ids = max(obj.Id for obj in Users) if Users else 0
                My_Id.append(User_Ids)
                Support_Ids = max(obj.Id for obj in Support) if Support else 0
                My_Id.append(Support_Ids)

                Legal_Ids = max(obj.Seller_Id for obj in Legal) if Legal else 0
                My_Id.append(Legal_Ids)
                Genuine_Ids = max(obj.Seller_Id for obj in Genuine) if Genuine else 0
                My_Id.append(Genuine_Ids)

                Add_Id = max(My_Id) + 1

                us = User.objects.create_user(id=Add_Id, username=username, password=forms.data["Password"],
                                              first_name=forms.data["Name"],
                                              last_name=forms.data["Family"], email=forms.data["Email"])
                us.save()
                Saved_data = Supporter(Id=Add_Id, name=forms.data["Name"], family=forms.data["Family"],
                                       UserName=username, Email=forms.data["Email"],
                                       Phone=forms.data["Phone"], Chat_Code=Chat_Code)
                Saved_data.save()
            return HttpResponseRedirect("/Farshtore/login_Support")

        else:
            return HttpResponse("فرم نامعتبر می باشد")


def logins(request):
    forms = Login()
    return render(request=request, template_name="login.html", context={"form": forms})


def login_Support(request):
    forms = Login_Support()
    return render(request=request, template_name="login_Support.html", context={"form": forms})


def Login_Seller(request, Seller_Type):
    forms = Logins_Seller_Form()
    return render(request=request, template_name="login_Seller.html", context={"form": forms,
                                                                               "Type": Seller_Type})


def register(request):
    forms = Register()
    return render(request=request, template_name="Register.html", context={"form": forms})


def register_Support(request):
    forms = Register_Support()
    return render(request=request, template_name="Register_Support.html", context={"form": forms})


def Logout(request):
    logout(request)
    return HttpResponseRedirect("/Farshtore/login")


def Error404(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Legal = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
        My_user = User_Save.objects.filter(Id=user_st["User"].id).all()
        if Legal.exists():
            user = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif Genuine.exists():
            user = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif My_user.exists():
            user = User_Save.objects.filter(Id=user_st["User"].id).all()
            Res = "User"
        else:
            user = Supporter.objects.filter(Id=user_st["User"].id).all()
            Res = "Support"

        return render(request=request, template_name="404.html", context={"icon": icon, "circle": circle, "href": href,
                                                                          "script": script, "user": user, "Res": Res,
                                                                          "user_st": user_st, "incl": str(incl),
                                                                          "incll": incll, "Mylist_sorts": Mylist_sorts})
    else:
        icon = "bi bi-box-arrow-in-left"
        text = "ورود | ثبت‌نام"
        href = "/Farshtore/login"
        style = "border-radius: 5px;width: 100%;padding: 15% 15% 15% 15%;border:1px solid;padding:8;"
        script = '/static/js/user.js'
        incl = "include2.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        return render(request=request, template_name="404.html",
                      context={"icon": icon, "style": style, "text": text, "href": href,
                               "script": script, "incl": str(incl), "incll": incll, "Mylist_sorts": Mylist_sorts})


@csrf_exempt
def Edit_Profile_user(request):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        User_Id = user_st["User"].id
        if user_st["State"]:
            form = edit_Profile(request.POST)
            print(request.POST)
            if not form.is_valid():
                Id = form.data["Id"]
                us = User.objects.create_user(id=Id, username=form.data["UserName"], password=form.data["Password"],
                                              first_name=form.data["Name"],
                                              last_name=form.data["Family"], email=form.data["Email"])

                us2 = User_Save(Id=Id, name=form.data["Name"], family=form.data["Family"],
                                UserName=form.data["UserName"],
                                date_of_birth=form.data["Date_of_birth"], job=form.data["Job"],
                                national_code=form.data["National_Code"], password=form.data["Password"],
                                repassword=form.data["rePassword"], redirect=form.data["redirect"],
                                Phone=form.data["Phone"])

                user = authenticate(request, username=form.data["UserName"], password=form.data["Password"])
                if user is not None:
                    us.save()
                    us2.save()
                    login(request, user)
                    return HttpResponseRedirect("/Farshtore/EditProfile/" + str(User_Id))
                else:
                    return HttpResponse("مشکلی در تغییر اطلاعات بوجود آمده است لطفا دوباره تلاش کنید")
            else:
                return HttpResponse("False")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Edit_Profile_Support(request):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        User_Id = user_st["User"].id
        if user_st["State"]:
            form = edit_Profile(request.POST)
            if not form.is_valid():
                username = form.data["UserName"] + "_Support"
                Id = form.data["Id"]
                us = User.objects.create_user(id=Id, username=form.data["UserName"], password=form.data["Password"],
                                              first_name=form.data["Name"],
                                              last_name=form.data["Family"], email=form.data["Email"])

                us2 = Supporter(Id=Id, name=form.data["Name"], family=form.data["Family"],
                                UserName=form.data["UserName"],
                                date_of_birth=form.data["Date_of_birth"], job=form.data["Job"],
                                national_code=form.data["National_Code"], password=form.data["Password"],
                                repassword=form.data["rePassword"], redirect=form.data["redirect"],
                                Phone=form.data["Phone"])

                user = authenticate(request, username=form.data["UserName"], password=form.data["Password"])
                if user is not None:
                    us.save()
                    us2.save()
                    login(request, user)
                    return HttpResponseRedirect("/Farshtore/EditProfile/" + str(User_Id))
                else:
                    return HttpResponse("مشکلی در تغییر اطلاعات بوجود آمده است لطفا دوباره تلاش کنید")
            else:
                return HttpResponse("False")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Edit_Profile_Seller_user(request, Num_Sh):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            User_Id = user_st["User"].id
            Legal = Seller_Legal.objects.filter(Seller_Id=User_Id).all()
            Genuine = Seller_Genuine.objects.filter(Seller_Id=User_Id).all()
            if Legal.exists():
                form = edit_Profile_Seller_Legal(request.POST)
                if form.is_valid():
                    Id = form.data["Id"]
                    Password = form.data["Password"]
                    if Password == "None":
                        S_Password = Seller_Legal.objects.filter(Seller_Id=User_Id).first()
                        Save_Password = S_Password.password
                    else:
                        Save_Password = form.data["Password"]

                    Search_User = User.objects.filter(id=Id).first()
                    us = User.objects.create_user(id=Id, username=str(Search_User.username),
                                                  password=str(Save_Password),
                                                  first_name=str(Search_User.first_name),
                                                  last_name=str(Search_User.last_name), email=str(Search_User.email))

                    us2 = Seller_Legal(Seller_Id=Id, Company_Name=str(form.data["Company_Name"]),
                                       Company_Type=str(form.data["Company_Type"]),
                                       Company_National_Code=str(form.data["Company_National_Code"]),
                                       Shaba_number=str(form.data["Shaba_Number"]),
                                       Economic_Code_Company=str(form.data["Company_Economic_Code"]),
                                       Signatory=str(form.data["Signatory"]),
                                       Shop_Name=str(form.data["ShopName"]), password=str(Save_Password),
                                       Phone=str(form.data["Phone"]), State="Login")

                    user = authenticate(request, username=Search_User.username, password=Save_Password)
                    if user is not None:
                        us.save()
                        us2.save()
                        login(request, user)
                        user_st = UserAuth().StateLogin(request)
                        New_User_Id = user_st["User"].id
                        return HttpResponse("True")
                    else:
                        return HttpResponse("Exist")
                else:
                    return HttpResponse("False")

            elif Genuine.exists():
                form = edit_Profile_Seller_Genuine(request.POST)
                if form.is_valid():
                    Id = form.data["Id"]
                    Password = form.data["Password"]
                    if Password == "None":
                        S_Password = Seller_Genuine.objects.filter(Seller_Id=User_Id).first()
                        Save_Password = S_Password.password
                    else:
                        Save_Password = form.data["Password"]

                    Search_User = User.objects.filter(id=Id).first()
                    us = User.objects.create_user(id=Id, username=str(Search_User.username),
                                                  password=str(Save_Password),
                                                  first_name=str(Search_User.first_name),
                                                  last_name=str(Search_User.last_name), email=str(Search_User.email))
                    us2 = ""
                    if Num_Sh == "Card":
                        us2 = Seller_Genuine(Seller_Id=Id, National_Code=str(form.data["National_Code"]),
                                             Phone=str(form.data["Phone"]), Cart_Number=str(form.data["Number_Sh"]),
                                             Shop_Name=str(form.data["ShopName"]), password=str(Save_Password),
                                             State="Login")

                    elif Num_Sh == "Shaba":
                        us2 = Seller_Genuine(Seller_Id=Id, National_Code=str(form.data["National_Code"]),
                                             Phone=str(form.data["Phone"]), Shaba_Number=str(form.data["Number_Sh"]),
                                             Shop_Name=str(form.data["ShopName"]), password=str(Save_Password),
                                             State="Login")

                    user = authenticate(request, username=Search_User.username, password=Save_Password)
                    if user is not None:
                        us.save()
                        us2.save()
                        login(request, user)
                        user_st = UserAuth().StateLogin(request)
                        New_User_Id = user_st["User"].id
                        return HttpResponse("Genuine")
                    else:
                        return HttpResponse("Exist")
                else:
                    return HttpResponse("False")
        else:
            return HttpResponse("/Farshtore/login")
    else:
        return HttpResponse("/Farshtore/404")


def Order(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Id = user_st["User"].id
        AllProduct = Product_Order.objects.all()
        Len = len(AllProduct)

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        My_user = User_Save.objects.filter(Id=Id).all()
        if Legal.exists():
            user = Seller_Legal.objects.filter(Seller_Id=Id).all()
            Res = "Seller"
        elif Genuine.exists():
            user = Seller_Genuine.objects.filter(Seller_Id=Id).all()
            Res = "Seller"
        elif My_user.exists():
            user = User_Save.objects.filter(Id=Id).all()
            Res = "User"
        else:
            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"

        Empty_prdct = "include4.html"
        if Len == 0:
            Empty_prdct = "Empty_prdct.html"

            return render(request=request, template_name="Order.html",
                          context={"Order": AllProduct, "icon": icon, "href": href, "Len": Len,
                                   "Empty_prdct": Empty_prdct,
                                   "scripts": script, "incl": incl, "user": user, "user_st": user_st,
                                   "Res": Res, "incll": incll, "Mylist_sorts": Mylist_sorts})
        else:
            return render(request=request, template_name="Order.html",
                          context={"Order": AllProduct, "icon": icon, "href": href, "Len": Len,
                                   "Empty_prdct": Empty_prdct,
                                   "scripts": script, "incl": incl, "user": user, "user_st": user_st,
                                   "Res": Res, "incll": incll, "Mylist_sorts": Mylist_sorts})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def Orders(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        Search_Order = Product_Order.objects.filter(user_Id=user_st["User"].id).all()
        length = len(Search_Order)
        price = 0
        for item in Search_Order:
            price += item.Product_Price
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Id = user_st["User"].id

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        User = User_Save.objects.filter(Id=Id).all()

        User_Niotif = ""

        if Legal.exists() or Genuine.exists():
            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                                Chat_user_Id=user_st["User"].id).all()

            Notification_Support = Chats.objects.filter(With="Seller_Support",
                                                        Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Seller)
                for item in Notification_Support:
                    Notif_List.append(item.Visit_Seller)

            User_Niotif = sum(Notif_List)
            Res = "Seller"
            if Legal.exists():
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()

            elif Genuine.exists():
                user = Seller_Genuine.objects.filter(Seller_Id=Id).all()

        elif User.exists():

            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                                Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_User)

            User_Niotif = sum(Notif_List)

            user = User_Save.objects.filter(Id=Id).all()
            Res = "User"
        else:

            Notification = Chats.objects.filter(Q(With="Seller_Support") | Q(With="User_Support"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Support_Seller", Chat_user2_Id=Id).all()

            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Support)

                for item in Notification_Support:
                    Notif_List.append(item.Visit_Support)

            User_Niotif = sum(Notif_List)

            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"

        return render(request=request, template_name="Orders.html",
                      context={"user": user, "icon": icon, "href": href, "user_st": user_st,
                               "circle": circle, "script": script, "incl": incl,
                               "price": price, "length": length, "Res": Res,
                               "active5": "active", "User_Niotif": User_Niotif, "incll": incll,
                               "Mylist_sorts": Mylist_sorts})
    else:
        return HttpResponseRedirect("/Farshtore/register")


def Message(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        user = ""
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Id = user_st["User"].id

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        Users = User_Save.objects.filter(Id=Id).all()

        User_Niotif = ""
        Notif_List = []
        Name_List = ""
        Chat_Code_List = ""
        Name_List = []
        Chat_Code_List = []

        if Legal.exists() or Genuine.exists():
            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Seller_Support",
                                                        Chat_user2_Id=Id).all()
            Notif_List = []
            Name_List = []
            Chat_Code_List = []
            if Notification.exists():
                for item in Notification_Support:
                    Notif_List.append(item.Visit_Seller)

                    Name = User.objects.filter(id=item.Chat_user2_Id).first()
                    Name_List.append(Name.first_name + " " + Name.last_name)
                    Visit_Seller = Chats.objects.filter(Visit_Seller=item.Visit_Seller).first()

                    Chat_Code_List.append(Visit_Seller.Chat_Code)

                for item in Notification:
                    Notif_List.append(item.Visit_Seller)

                    Name = User.objects.filter(id=item.Chat_user2_Id).first()
                    Name_List.append(Name.first_name + " " + Name.last_name)
                    Visit_Seller = Chats.objects.filter(Visit_Seller=item.Visit_Seller).first()

                    Chat_Code_List.append(Visit_Seller.Chat_Code)

            User_Niotif = sum(Notif_List)

            Res = "Seller"
            if Legal.exists():
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()

            elif Genuine.exists():
                user = Seller_Genuine.objects.filter(Seller_Id=Id).all()

        elif Users.exists():

            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                                Chat_user2_Id=Id).all()
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_User)

                    Name = User.objects.filter(id=item.Chat_user_Id).first()
                    Name_List.append(Name.first_name + " " + Name.last_name)
                    Visit_Seller = Chats.objects.filter(Visit_User=item.Visit_User).first()

                    Chat_Code_List.append(Visit_Seller.Chat_Code)

            User_Niotif = sum(Notif_List)

            user = User_Save.objects.filter(Id=Id).all()

            Res = "User"

        else:

            Notification = Chats.objects.filter(Q(With="Seller_Support") | Q(With="User_Support"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Support_Seller", Chat_user2_Id=Id).all()

            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Support)

                    Name = User.objects.filter(id=item.Chat_user_Id).first()
                    Name_List.append(Name.first_name + " " + Name.last_name)
                    Visit_Support = Chats.objects.filter(Visit_Support=item.Visit_Support).first()

                    Chat_Code_List.append(Visit_Support.Chat_Code)

                for item in Notification_Support:
                    Notif_List.append(item.Visit_Support)

                    Name = User.objects.filter(id=item.Chat_user2_Id).first()
                    Name_List.append(Name.first_name + " " + Name.last_name)
                    Visit_Support = Chats.objects.filter(Visit_Support=item.Visit_Support).first()

                    Chat_Code_List.append(Visit_Support.Chat_Code)

            User_Niotif = sum(Notif_List)

            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"

        data = list(zip(Name_List, Notif_List, Chat_Code_List))
        Group_List = [{'name': name, 'number': number, 'Chat_Code': Chat_Code}
                      for name, number, Chat_Code in data]
        return render(request=request, template_name="Message.html",
                      context={"user": user, "icon": icon, "href": href, "user_st": user_st,
                               "circle": circle, "script": script, "incl": incl, "Res": Res,
                               "active9": "active", "User_Niotif": User_Niotif,
                               "Group_List": Group_List,"incll":incll,"Mylist_sorts":Mylist_sorts})
    else:
        return HttpResponseRedirect("/Farshtore/register")


def Chat(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Id = user_st["User"].id

        Chat_Lst = ""

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        Users = User_Save.objects.filter(Id=Id).all()

        User_Niotif = ""
        List_Name = ""

        if Legal.exists() or Genuine.exists():
            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Seller_Support",
                                                        Chat_user2_Id=Id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Seller)
                for item in Notification_Support:
                    Notif_List.append(item.Visit_Seller)

            User_Niotif = sum(Notif_List)

            Chat_List = Chats.objects.filter(Q(Chat_user_Id=Id) | Q(Chat_user2_Id=Id),
                                             Q(With="User_Seller") | Q(With="Support_Seller") |
                                             Q(With="Seller_Support")).all()

            Chat_Lst = []
            List_Name = []

            for item in Chat_List:
                Chat_Lst.append(item.Chat_user_Id)
                Chat_Lst.append(item.Chat_user2_Id)

            while Id in Chat_Lst:
                Chat_Lst.remove(Id)

            for item in Chat_Lst:
                Search_Name = User.objects.filter(id=item).first()
                List_Name.append(Search_Name.first_name + " " + Search_Name.last_name)

            Res = "Seller"
            if Legal.exists():
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()

            elif Genuine.exists():
                user = Seller_Genuine.objects.filter(Seller_Id=Id).all()

        elif Users.exists():

            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                                Chat_user2_Id=Id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_User)

            User_Niotif = sum(Notif_List)

            user = User_Save.objects.filter(Id=Id).all()
            Chat_List = Chats.objects.filter(Q(Chat_user_Id=Id) | Q(Chat_user2_Id=Id),
                                             Q(With="User_Seller") | Q(With="User_Support")).all()

            Chat_Lst = []
            List_Name = []

            for item in Chat_List:
                Chat_Lst.append(item.Chat_user_Id)
                Chat_Lst.append(item.Chat_user2_Id)

            while Id in Chat_Lst:
                Chat_Lst.remove(Id)

            for item in Chat_Lst:
                Search_Name = User.objects.filter(id=item).first()
                List_Name.append(Search_Name.first_name + " " + Search_Name.last_name)
            Res = "User"
        else:

            Notification = Chats.objects.filter(Q(With="Support_Seller") | Q(With="User_Support"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Seller_Support", Chat_user2_Id=Id).all()

            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Support)

            elif Notification_Support.exists():
                for item in Notification_Support:
                    Notif_List.append(item.Visit_Support)

            User_Niotif = sum(Notif_List)

            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"

            Chat_List = Chats.objects.filter(Q(Chat_user_Id=Id) | Q(Chat_user2_Id=Id),
                                             Q(With="Support_Seller") | Q(With="User_Support") |
                                             Q(With="Seller_Support")).all()

            Chat_Lst = []
            List_Name = []

            for item in Chat_List:
                Chat_Lst.append(item.Chat_user_Id)
                Chat_Lst.append(item.Chat_user2_Id)

            while Id in Chat_Lst:
                Chat_Lst.remove(Id)

            for item in Chat_Lst:
                Search_Name = User.objects.filter(id=item).first()
                List_Name.append(Search_Name.first_name + " " + Search_Name.last_name)

        return render(request=request, template_name="Chats.html",
                      context={"user": user, "icon": icon, "href": href, "user_st": user_st,
                               "circle": circle, "script": script, "incl": incl, "Res": Res,
                               "active7": "active", "User_Niotif": User_Niotif,
                               "List_Name": List_Name, "Notif_List": Notif_List,
                               "incll":incll,"Mylist_sorts":Mylist_sorts})
    else:
        return HttpResponseRedirect("/Farshtore/register")


def Commnets(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        MyComment = Product_Comment.objects.filter(user_Id=user_st["User"].id).all()
        MyComment_Products = ""
        for item in MyComment:
            MyComment_Products += item.Product_Code

        Id = user_st["User"].id

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        User = User_Save.objects.filter(Id=Id).all()
        User_Niotif = ""

        if Legal.exists() or Genuine.exists():
            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                                Chat_user_Id=user_st["User"].id).all()

            Notification_Support = Chats.objects.filter(With="Seller_Support",
                                                        Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Seller)
                for item in Notification_Support:
                    Notif_List.append(item.Visit_Seller)

            User_Niotif = sum(Notif_List)
            Res = "Seller"
            if Legal.exists():
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()

            elif Genuine.exists():
                user = Seller_Genuine.objects.filter(Seller_Id=Id).all()

        elif User.exists():

            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                                Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_User)

            User_Niotif = sum(Notif_List)

            user = User_Save.objects.filter(Id=Id).all()
            Res = "User"
        else:

            Notification = Chats.objects.filter(Q(With="Seller_Support") | Q(With="User_Support"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Support_Seller", Chat_user2_Id=Id).all()

            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Support)

                for item in Notification_Support:
                    Notif_List.append(item.Visit_Support)

            User_Niotif = sum(Notif_List)

            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"

        return render(request=request, template_name="MyComments.html",
                      context={"user": user, "icon": icon, "href": href, "user_st": user_st,
                               "circle": circle, "script": script, "incl": incl,
                               "MyComment": MyComment, "Res": Res,"incll":incll,"Mylist_sorts":Mylist_sorts,
                               "active8": "active", "User_Niotif": User_Niotif})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def user_history(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        func = "/../static/js/User_view.js"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Id = user_st["User"].id

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        User = User_Save.objects.filter(Id=Id).all()

        User_Niotif = ""

        if Legal.exists() or Genuine.exists():
            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                                Chat_user_Id=user_st["User"].id).all()

            Notification_Support = Chats.objects.filter(With="Seller_Support",
                                                        Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Seller)
                for item in Notification_Support:
                    Notif_List.append(item.Visit_Seller)

            User_Niotif = sum(Notif_List)
            Res = "Seller"
            if Legal.exists():
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()

            elif Genuine.exists():
                user = Seller_Genuine.objects.filter(Seller_Id=Id).all()

        elif User.exists():

            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                                Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_User)

            User_Niotif = sum(Notif_List)

            user = User_Save.objects.filter(Id=Id).all()
            Res = "User"
        else:

            Notification = Chats.objects.filter(Q(With="Seller_Support") | Q(With="User_Support"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Support_Seller", Chat_user2_Id=Id).all()

            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Support)

                for item in Notification_Support:
                    Notif_List.append(item.Visit_Support)

            User_Niotif = sum(Notif_List)

            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"

        return render(request=request, template_name="user_history.html",
                      context={"user": user, "icon": icon, "href": href, "user_st": user_st,
                               "circle": circle, "script": script, "incl": incl,
                               "func": func, "Res": Res, "active10": "active",
                               "User_Niotif": User_Niotif,"incll":incll,"Mylist_sorts":Mylist_sorts})
    else:
        return HttpResponseRedirect("/Farshtore/register")


def Activity(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Id = user_st["User"].id
        Count_Order = ""

        Ordr = Product_Order.objects.filter(user_Id=Id).first()
        if Ordr:
            Count_Order = 1

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        User = User_Save.objects.filter(Id=Id).all()

        User_Niotif = ""

        if Legal.exists() or Genuine.exists():
            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                                Chat_user_Id=user_st["User"].id).all()

            Notification_Support = Chats.objects.filter(With="Seller_Support",
                                                        Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Seller)
                for item in Notification_Support:
                    Notif_List.append(item.Visit_Seller)

            User_Niotif = sum(Notif_List)
            Res = "Seller"
            if Legal.exists():
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()

            elif Genuine.exists():
                user = Seller_Genuine.objects.filter(Seller_Id=Id).all()

        elif User.exists():

            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                                Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_User)

            User_Niotif = sum(Notif_List)

            user = User_Save.objects.filter(Id=Id).all()
            Res = "User"
        else:

            Notification = Chats.objects.filter(Q(With="Seller_Support") | Q(With="User_Support"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Support_Seller", Chat_user2_Id=Id).all()

            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Support)

                for item in Notification_Support:
                    Notif_List.append(item.Visit_Support)

            User_Niotif = sum(Notif_List)

            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"

        return render(request=request, template_name="Activity.html",
                      context={"user": user, "icon": icon, "href": href, "user_st": user_st,
                               "circle": circle, "script": script, "incl": incl,
                               "Res": Res, "active3": "active", "User_Niotif": User_Niotif,
                               "Count_Order": Count_Order,"incll":incll,"Mylist_sorts":Mylist_sorts})
    else:
        return HttpResponseRedirect("/Farshtore/register")


def Product_Likes(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        func = "/../static/js/Like_product.js"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        P_Likes = Like.objects.filter(user_Id=user_st["User"].id).all()

        Id = user_st["User"].id

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        User = User_Save.objects.filter(Id=Id).all()

        User_Niotif = ""

        if Legal.exists() or Genuine.exists():
            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                                Chat_user_Id=user_st["User"].id).all()

            Notification_Support = Chats.objects.filter(With="Seller_Support",
                                                        Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Seller)
                for item in Notification_Support:
                    Notif_List.append(item.Visit_Seller)

            User_Niotif = sum(Notif_List)
            Res = "Seller"
            if Legal.exists():
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()

            elif Genuine.exists():
                user = Seller_Genuine.objects.filter(Seller_Id=Id).all()

        elif User.exists():

            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                                Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_User)

            User_Niotif = sum(Notif_List)

            user = User_Save.objects.filter(Id=Id).all()
            Res = "User"
        else:

            Notification = Chats.objects.filter(Q(With="Seller_Support") | Q(With="User_Support"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Support_Seller", Chat_user2_Id=Id).all()

            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Support)

                for item in Notification_Support:
                    Notif_List.append(item.Visit_Support)

            User_Niotif = sum(Notif_List)

            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"
        return render(request=request, template_name="Product_Likes.html",
                      context={"user": user, "icon": icon, "href": href, "P_Likes": P_Likes,
                               "circle": circle, "script": script, "incl": incl,
                               "uset_st": user_st, "user_st": user_st,
                               "func": func, "Res": Res, "active6": "active",
                               "User_Niotif": User_Niotif,"incll":incll,"Mylist_sorts":Mylist_sorts})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def CheckAuth(request):
    if request.user.is_authenticated:
        return HttpResponse("کاربر وارد شده است")
    else:
        return HttpResponse("کاربر وارد نشده است")


def EditProfile(request, Id):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Day_List = []
        days = 1
        for day in range(0, 31):
            Day_List.append(days)
            days += 1
        Month_List = ['فروردین', 'اردیبهشت', 'خرداد', 'تیر', 'مرداد', 'شهریور',
                      'مهر', 'آبان', 'آذر', 'دی', 'بهمن', 'اسفند'
                      ]
        Year_List = []
        Years = 1350
        while Years < 1403:
            Year_List.append(Years)
            Years += 1

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        User = User_Save.objects.filter(Id=Id).all()
        Shaba_Num = ""
        Cart_Num = ""
        User_Niotif = ""
        None_SH = False
        if Legal.exists() or Genuine.exists():
            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Seller_Support",
                                                        Chat_user2_Id=Id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Seller)
                for item in Notification_Support:
                    Notif_List.append(item.Visit_Seller)

            User_Niotif = sum(Notif_List)
            Res = "Seller"
            if Legal.exists():
                File_Name = "EditProfile_Seller_Legal"
                result = Seller_Legal.objects.filter(Seller_Id=Id).first()
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()

                forms = edit_Profile_Seller_Legal(initial={"Id": Id, "Company_Name": result.Company_Name,
                                                           "Company_National_Code": result.Company_National_Code,
                                                           "Company_Economic_Code": result.Economic_Code_Company,
                                                           "Shaba_Number": result.Shaba_number,
                                                           "Signatory": result.Signatory,
                                                           "ShopName": result.Shop_Name, "Phone": result.Phone})

                Company_Types = ['سهامی عام', 'سهامی خاص', 'مسئولیت محدود', 'تعاونی', 'تضامنی', 'موسسه', 'سایر']

                return render(request=request, template_name=File_Name + ".html",
                              context={"form": forms, "user_st": user_st, "user": user, "Res": Res,
                                       "incl": incl, "script": script, "circle": circle,
                                       "Co_Type": result.Company_Type, "active1": "active",
                                       "active11": "active", "href": href, "icon": icon,
                                       "Company_Types": Company_Types, "User_Niotif": User_Niotif,
                                       "incll": incll, "Mylist_sorts": Mylist_sorts})

            elif Genuine.exists():
                File_Name = "EditProfile_Seller_Genuine"
                user = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
                result = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).first()
                if result.Cart_Number == "0":
                    Shaba_Num = result.Shaba_Number
                    Cart_Num = "None"
                elif result.Shaba_Number == "0":
                    Cart_Num = result.Cart_Number
                    Shaba_Num = "None"
                elif result.Cart_Number != "0" and result.Shaba_Number != "0":
                    Cart_Num = "Fill"
                    Shaba_Num = "Fill"

                if result.Cart_Number == "0" and result.Shaba_Number == "0":
                    None_SH = True

                if result.Shop_Name == "None":
                    Check_Shop_Name = ""
                else:
                    Check_Shop_Name = result.Shop_Name
                forms = edit_Profile_Seller_Genuine(
                    initial={"Id": Id, "National_Code": result.National_Code, "ShopName": Check_Shop_Name,
                             "Phone": result.Phone})

                return render(request=request, template_name=File_Name + ".html",
                              context={"form": forms, "user_st": user_st, "user": user,
                                       "incl": incl, "script": script, "circle": circle,
                                       "href": href, "icon": icon, "Shaba_Num": Shaba_Num,
                                       "Cart_Num": Cart_Num, "None_SH": None_SH, "Res": Res,
                                       "active1": "active", "active11": "active",
                                       "User_Niotif": User_Niotif, "incll": incll, "Mylist_sorts": Mylist_sorts})

        elif User.exists():

            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                                Chat_user2_Id=Id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_User)

            User_Niotif = sum(Notif_List)

            File_Name = "EditProfile"
            result = User_Save.objects.filter(Id=Id).first()
            user = User_Save.objects.filter(Id=Id).all()

            forms = edit_Profile(
                initial={"Id": Id, "Name": result.name, "Family": result.family, "National_Code": result.national_code,
                         "Date_of_birth": result.date_of_birth, "Phone": result.Phone, "Email": result.Email,
                         "Job": result.job, "redirect": result.redirect, "Password": result.password,
                         "rePassword": result.repassword,
                         "UserName": result.UserName})
            Res = "User"
            return render(request=request, template_name=File_Name + ".html",
                          context={"form": forms, "user_st": user_st, "user": user,
                                   "incl": incl, "script": script, "circle": circle,
                                   "href": href, "icon": icon, "Res": Res,
                                   "active1": "active", "active11": "active",
                                   "User_Niotif": User_Niotif, "Day_List": Day_List,
                                   "Month_List": Month_List, "incll": incll,
                                   "Year_List": Year_List, "Mylist_sorts": Mylist_sorts})
        else:

            Notification = Chats.objects.filter(Q(With="Seller_Support") | Q(With="User_Support"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Support_Seller", Chat_user2_Id=Id).all()

            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Support)

                for item in Notification_Support:
                    Notif_List.append(item.Visit_Support)

            User_Niotif = sum(Notif_List)

            File_Name = "EditProfile"
            result = Supporter.objects.filter(Id=Id).first()
            user = Supporter.objects.filter(Id=Id).all()

            forms = edit_Profile(
                initial={"Id": Id, "Name": result.name, "Family": result.family, "National_Code": result.national_code,
                         "Date_of_birth": result.date_of_birth, "Phone": result.Phone, "Email": result.Email,
                         "Job": result.job, "redirect": result.redirect, "Password": result.password,
                         "rePassword": result.repassword,
                         "UserName": result.UserName})
            Res = "Support"
            return render(request=request, template_name=File_Name + ".html",
                          context={"form": forms, "user_st": user_st, "user": user,
                                   "incl": incl, "script": script, "circle": circle,
                                   "href": href, "icon": icon, "Res": Res, "active1": "active",
                                   "active11": "active", "User_Niotif": User_Niotif, "Day_List": Day_List,
                                   "Month_List": Month_List, "incll": incll,
                                   "Year_List": Year_List, "Mylist_sorts": Mylist_sorts})

    else:
        return HttpResponseRedirect("/Farshtore/login")


def AddProduct(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        incl = "include.html"
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        Id = user_st["User"].id
        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()

        if Legal.exists():
            user = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif Genuine.exists():
            user = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        else:
            user = User_Save.objects.filter(Id=user_st["User"].id).all()
            Res = "User"

        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Mylist_brand_machine = ["ندارد", "فرش بهشتی", "قالی سلیمان", "فرش قیطران", "ستاره کویر یزد",
                                "فرش فرهی", "فرش محتشم کاشان", "فرش ساوین", "یلدای کویر کاشان",
                                "فرش دیبا", "فرش پاتریس", "فرش داریوش", "فرش زمرد مشهد", "فرش نگین مشهد"]

        Mylist_brand_Dast = ["ندارد", "فرش دستباف کرمان", "فرش دستباف کاشان", "فرش دستباف تبریز",
                             "فرش دستباف اصفهان", "فرش دستباف قم", "فرش دستباف سلطان آباد", "فرش دستباف بیجار",
                             "فرش دستباف کاشمر"]

        Mylist_Rag = ["15", "20", "25", "30", "35", "40", "45", "50", "60", "70", "80", "90", "120"]

        Mylist_thread_Dast = ["پشم", "کرک", "مرینوس", "ابریشم"]

        Mylist_Result = ["نو", "کارکرده"]

        Mylist_thread_machine = ["پرو پیلن", "پلی استر", "نایلون", "ابریشم مصنوعی", "اکریلیک", "پشم", "پنبه", "ویسکوز"]

        Mylist_Shane = ["۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        Mylist_thread_computer = ["ندارد", "پشم", "کرک", "مرینوس", "ابریشم"]

        Mylist_thread_Accss = ["کاموا", "کرک", "مرینوس", "ابریشم"]

        Mylist_Type_Accss = ["دست بند", "کمر بند", "بند عینک", "جا سوئیچی", "گردنبند",
                             "بند کیف", "رومیزی", "کوسن", "جا کنترلی"]

        Mylist_un_Sorts = ["دست باف", "ماشینی"]

        Mylist_Thread_Glim = ["پشم", "کرک"]

        Mylist_Type_Glim = ["گلیم دو رو", "گلیم پیچ", "گلیم ورنی", "گلیم برجسته", "گلیم ساده"]

        Mylist_Rag_Tablo = ["40", "45", "50", "60", "70", "80"]

        Mylist_Thraed_Tablo = ["مرینوس", "ابریشم"]

        form = Product()

        return render(request=request, template_name="Add_Product.html",
                      context={"incl": incl, "Mylist_sorts": Mylist_sorts, "form": form, "href": href, "icon": icon,
                               "user": user, "Res": Res, "Mylist_brand_machine": Mylist_brand_machine,
                               "Mylist_brand_Dast": Mylist_brand_Dast, "Mylist_thread_Dast": Mylist_thread_Dast,
                               "Mylist_thread_machine": Mylist_thread_machine, "Mylist_Rag": Mylist_Rag,
                               "Mylist_Result_Dast": Mylist_Result, "Mylist_Shane": Mylist_Shane,
                               "Mylist_thread_computer": Mylist_thread_computer,
                               "Mylist_thread_Accss": Mylist_thread_Accss,
                               "Mylist_Type_Accss": Mylist_Type_Accss, "Mylist_un_Sorts": Mylist_un_Sorts,
                               "Mylist_Rag_Tablo": Mylist_Rag_Tablo, "Mylist_Thraed_Tablo": Mylist_Thraed_Tablo,
                               "Mylist_Thread_Glim": Mylist_Thread_Glim, "Mylist_Type_Glim": Mylist_Type_Glim})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def ProductDataBase(request):
    if request.method == "POST":
        form = Product(request.POST)
        if form.is_valid():
            user_st = UserAuth().StateLogin(request)
            data_set = Add_Product.objects.filter(Product_Title=form.data["Product_Title"]).all()
            if data_set.exists():
                return HttpResponse("exists")
            Time = datetime.datetime.now()
            AddProduct = Add_Product(Product_Title=form.data["Product_Title"], Product_Price=form.data["Product_Price"],
                                     Product_Caption=form.data["Product_Caption"],
                                     Product_Type=form.data["Product_Type"],
                                     User_Address=form.data["User_Address"], Product_Size=form.data["Product_Size"],
                                     Product_Result=form.data["Product_Result"],
                                     Product_Date=Time)
            # , Product_Image=request.FILES['image'])
            AddProduct.save()
            return HttpResponse("success")


def Find_Id(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        MyUser = User_Save.objects.filter(UserName=user_st["User"]).all()
        forms = edit_Profile()
        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        return render(request=request, template_name="EditProfile.html",
                      context={"MyUser": MyUser, "form": forms, "user_st": user_st, "user": user})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def product(request, func, Value):
    user_st = UserAuth().StateLogin(request)
    incll = "incl2.html"

    Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش",
                    "بیضی و گرد", "کلاسیک", "فانتزی", "کودک", "ابزار قالی بافی", "گلیم",
                    "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

    Mylist_brand = ["ندارد", "فرش بهشتی", "قالی سلیمان", "فرش قیطران", "ستاره کویر یزد",
                    "فرش فرهی", "فرش محتشم کاشان", "فرش ساوین", "یلدای کویر کاشان",
                    "فرش دیبا", "فرش پاتریس", "فرش داریوش", "فرش زمرد مشهد", "فرش نگین مشهد",

                    "فرش دستباف کرمان", "فرش دستباف کاشان", "فرش دستباف تبریز",
                    "فرش دستباف اصفهان", "فرش دستباف قم", "فرش دستباف سلطان آباد",
                    "فرش دستباف بیجار", "فرش دستباف کاشمر"
                    ]

    MyList_Result = ["نو", "کارکرده"]

    Mylist_Rag = ["15", "20", "25", "30", "35", "40", "45", "50", "60", "70", "80", "90", "120"]

    if user_st["State"]:
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        Res = ""
        user_likes = Like.objects.filter(user_Id=user_st["User"].id).all()

        Legal = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
        My_user = User_Save.objects.filter(Id=user_st["User"].id).all()
        if Legal.exists():
            user = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif Genuine.exists():
            user = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
            Res = "Seller"
        elif My_user.exists():
            user = User_Save.objects.filter(Id=user_st["User"].id).all()
            Res = "User"
        else:
            user = Supporter.objects.filter(Id=user_st["User"].id).all()
            Res = "Support"

        if user_likes.exists():
            user_find = Like.objects.filter(Like_Id=0).all()
            find = len(user_find)
            incl = "include.html"
            include = "include4.html"
            AllProduct = Add_Product.objects.all()
            script = '/static/js/tm.js'
            liked = "liked"
            return render(request=request, template_name="Prdct.html",
                          context={"AllProduct": AllProduct, "user_st": user_st, "Find": find,
                                   "user": user, "icon": icon, "Mylist_sorts": Mylist_sorts, "href": href,
                                   "Mylist_brand": Mylist_brand, "incl": incl, "include": include,
                                   "script": script, "liked": liked, "Res": Res,
                                   "func": func, "Value": Value, "MyList_Result": MyList_Result,
                                   "Mylist_Rag": Mylist_Rag, "incll": incll})
        else:
            icon = "User_Icon_include.html"
            href = "/Farshtore/EditProfile/"
            AllProduct = Add_Product.objects.all()
            incl = "include.html"
            include = "include3.html"

            return render(request=request, template_name="Prdct.html",
                          context={"AllProduct": AllProduct, "icon": icon, "href": href,
                                   "Mylist_sorts": Mylist_sorts, "user_st": user_st,
                                   "Mylist_brand": Mylist_brand, "user": user,
                                   "incl": incl, "inc": include, "Res": Res, "Mylist_Rag": Mylist_Rag,
                                   "func": func, "Value": Value, "MyList_Result": MyList_Result,
                                   "incll": incll})
    else:
        icons = "bi bi-box-arrow-in-left"
        text = "ورود | ثبت‌نام"
        href = "/Farshtore/login"
        style = "border-radius: 5px;width: 100%;padding: 15% 15% 15% 15%;border:1px solid;padding:8;"
        script = '/static/js/user.js'
        incl = "include2.html"
        include = "include3.html"

        AllProduct = Add_Product.objects.all()

        return render(request=request, template_name="Prdct.html",
                      context={"icons": icons, "text": text, "href": href,
                               "style": style, "script": script, "Mylist_sorts": Mylist_sorts,
                               "Mylist_brand": Mylist_brand, "incl": incl, "include": include,
                               "func": func, "Value": Value, "AllProduct": AllProduct,
                               "user_st": user_st, "MyList_Result": MyList_Result,
                               "Mylist_Rag": Mylist_Rag, "incll": incll})


def get_product(request):
    if request.method == "GET":
        AllProduct = Add_Product.objects.all()
        product_json = serializers.serialize("json", AllProduct)
        return HttpResponse(product_json)
    else:
        return HttpResponse("Not POST Method")


@csrf_exempt
def Order_Set(request, Code, Count):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            if str(Count) == "0":
                Count = "1"
            All_Product = Add_Product.objects.filter(Product_Code=Code).all()
            Product_Order_Set = Product_Order.objects.filter(Product_Code=Code, user_Id=user_st["User"].id).all()
            Order_Code = random.randint(0, 100000)
            MyList = []
            Product_Orders = Product_Order.objects.filter(user_Id=user_st["User"].id).all()
            for item in Product_Orders:
                MyList.append(item.Order_Code)

            List = list(set(MyList))
            print(List)
            if List != []:
                Order_Code = List[0]

            if not Product_Order_Set.exists():
                for item in All_Product:
                    Order = Product_Order(Product_Title=item.Product_Title, Product_Price=item.Product_Price_Final,
                                          Product_Caption=item.Product_Caption,
                                          Product_Type=item.Product_Type, Product_Size=item.Product_Size,
                                          user_Id=user_st["User"].id,
                                          Product_Brand=item.Product_Brand, Product_Image=item.Product_Image,
                                          Product_Result=item.Product_Result,
                                          Product_Code=item.Product_Code, Product_Count=Count,
                                          Order_Code=Order_Code)
                    Order.save()
                return HttpResponse("True")
            else:
                return HttpResponse("True")
        else:
            return HttpResponseRedirect("/Farshtore/404")
    else:
        return HttpResponseRedirect("/Farshtore/login")


@csrf_exempt
def Order_complete(request, Final_Price):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            if Final_Price == "0":
                return HttpResponse("False")
            Product_Orders = Product_Order.objects.filter(user_Id=user_st["User"].id).first()
            if Product_Orders is None:
                return HttpResponse("False")
            yesterday = datetime.now() - timedelta(0)

            Time = jdatetime.fromgregorian(day=yesterday.day, month=yesterday.month,
                                           year=yesterday.year).strftime("%Y/%m/%d")

            Order = Order_Complete(user_Id=user_st["User"].id, Price=Final_Price,
                                   Date=Time, Order_Code=Product_Orders.Order_Code)
            Order.save()
            return HttpResponse("True")
        else:
            return HttpResponseRedirect("/Farshtore/404")
    else:
        return HttpResponseRedirect("/Farshtore/login")


@csrf_exempt
def Order_complete_Remove(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            MyList = []
            Product_Orders = Product_Order.objects.filter(user_Id=user_st["User"].id).all()
            for item in Product_Orders:
                MyList.append(item.Product_Code)
            if len(MyList) == 0:
                return HttpResponse("False")
            yesterday = datetime.now() - timedelta(0)

            Time = jdatetime.fromgregorian(day=yesterday.day, month=yesterday.month,
                                           year=yesterday.year).strftime("%Y/%m/%d")
            if len(MyList) > 0:
                for Product_Code in MyList:
                    Order = Product_buyed(user_Id=user_st["User"].id, Product_Code=Product_Code,
                                          Date=Time)
                    Order.save()
            Order_D = Product_Order.objects.filter(user_Id=user_st["User"].id).all()
            Order_D.delete()
            return HttpResponse("True")
        else:
            return HttpResponseRedirect("/Farshtore/404")
    else:
        return HttpResponseRedirect("/Farshtore/login")

@csrf_exempt
def Delete_Set(request, Code):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            Product_Order_Set = Product_Order.objects.filter(Product_Code=Code, user_Id=user_st["User"].id).all()
            Product_Order_Set.delete()
            return HttpResponse("True")
        else:
            return HttpResponseRedirect("/Farshtore/404")
    else:
        return HttpResponseRedirect("/Farshtore/login")


def Remove_Product_Order(request, Id):
    result = Product_Order.objects.filter(Product_Id=Id).first()
    result.delete()
    AllProduct = Product_Order.objects.all()
    return HttpResponseRedirect("/Farshtore/Order")


def product_information(request, Code):
    prdct_card_Code = Add_Product.objects.filter(Product_Code=Code).first()

    Search_Name = User.objects.filter(id=prdct_card_Code.user_Id).first()

    Seller_Name = Search_Name.first_name + " " + Search_Name.last_name

    Add = prdct_card_Code

    Type = Add.Product_Type

    Info_Product = ""
    Ghali = ""
    Empty_prdct = "include4.html"
    include = "include4.html"
    incll = "incl2.html"
    Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                    "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

    if Type == "دست باف":
        Info_Product = ["برند : " + Add.Product_Brand, "جنس نخ : " + Add.Product_Thread,
                        "ابعاد : " + Add.Product_Size, "رج شمار : " + Add.Product_Rag,
                        "وضعیت : " + Add.Product_Result]

    elif Type == "ماشینی":
        Info_Product = ["برند : " + Add.Product_Brand, "جنس نخ : " + Add.Product_Thread,
                        "ابعاد : " + Add.Product_Size, "تعداد شانه : " + Add.Product_Shane]

    elif Type == "اکسسوری":
        if Add.Product_Accss_Type != "کوسن":
            Info_Product = ["جنس نخ : " + Add.Product_Thread, "نوع : " + Add.Product_Accss_Type]
        else:
            Info_Product = ["جنس نخ : " + Add.Product_Thread, "نوع : " + Add.Product_Accss_Type,
                            "ابعاد : " + Add.Product_Size]

    elif Type == "تابلو فرش":
        Info_Product = ["جنس نخ : " + Add.Product_Thread, "ابعاد : " + Add.Product_Size,
                        "رج شمار : " + Add.Product_Rag]

    elif Type == "بیضی و گرد" or Type == "کلاسیک" or Type == "فانتزی" or Type == "کودک":
        if Add.Product_Un_Type_Sort == "ماشینی":
            Info_Product = ["برند : " + Add.Product_Brand, "جنس نخ : " + Add.Product_Thread,
                            "ابعاد : " + Add.Product_Size, "تعداد شانه : " + Add.Product_Shane,
                            "نوع فرش : " + Add.Product_Un_Type_Type]

        elif Add.Product_Un_Type_Sort == "دست باف":
            Info_Product = ["برند : " + Add.Product_Brand, "جنس نخ : " + Add.Product_Thread,
                            "ابعاد : " + Add.Product_Size, "رج شمار : " + Add.Product_Rag,
                            "وضعیت : " + Add.Product_Result, "نوع فرش : " + Add.Product_Un_Type_Sort]

    elif Type == "ابزار قالی بافی":
        Ghali = "Empty"

    elif Type == "گلیم":
        Info_Product = ["جنس نخ : " + Add.Product_Thread, "ابعاد : " + Add.Product_Size,
                        "نوع گلیم : " + Add.Product_Glim_Type]

    elif Type == "۷۰۰ شانه" or Type == "۱۰۰۰ شانه" or \
            Type == "۱۲۰۰ شانه" or Type == "۱۵۰۰ شانه":

        Info_Product = ["برند : " + Add.Product_Brand, "جنس نخ : " + Add.Product_Thread,
                        "ابعاد : " + Add.Product_Size, "تعداد شانه : " + Add.Product_Shane]
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        icons = ""
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        Legal = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
        Support = Supporter.objects.filter(Id=user_st["User"].id).all()

        script = '/static/js/tm.js'
        incl = "include.html"
        MyUser = User_Save.objects.filter(UserName=user_st["User"]).all()
        user_likes = Like.objects.filter(user_Id=user_st["User"].id).all()

        Id = user_st["User"].id

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        Users = User_Save.objects.filter(Id=Id).all()

        user = ""

        if Legal.exists() or Genuine.exists():

            Res = "Seller"
            if Legal.exists():
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()

            elif Genuine.exists():
                user = Seller_Genuine.objects.filter(Seller_Id=Id).all()

        elif Users.exists():

            user = User_Save.objects.filter(Id=Id).all()
            Res = "User"
        else:

            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"

        return render(request=request, template_name="prdct_card.html",
                      context={"icon": icon, "circle": circle, "href": href,
                               "script": script, "user": user, "user_likes": user_likes,
                               "user_st": user_st, "incl": incl, "include": include,
                               "MyUser": MyUser, "prdct_card": prdct_card_Code,
                               "Info_Product": Info_Product, "Ghali": Ghali,
                               "Empty_prdct": Empty_prdct, "Seller_Name": Seller_Name,
                               "icons": icons, "Res": Res, "incll": incll, "Mylist_sorts": Mylist_sorts})

    else:
        icons = "bi bi-box-arrow-in-left"
        text = "ورود | ثبت‌نام"
        href = "/Farshtore/login"
        style = "border-radius: 5px;width: 100%;padding: 15% 15% 15% 15%;border:1px solid;padding:8;"
        script = '/static/js/user.js'
        incl = "include2.html"
        Empty_prdct = "include4.html"

        return render(request=request, template_name="prdct_card.html",
                      context={"icons": icons, "style": style, "text": text, "href": href,
                               "script": script, "incl": incl, "Empty_prdct": Empty_prdct,
                               "prdct_card": prdct_card_Code, "Seller_Name": Seller_Name,
                               "Info_Product": Info_Product, "include": include,
                               "user_st": user_st, "incll": incll, "Mylist_sorts": Mylist_sorts})


def Wallet(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:

        Id = user_st["User"].id

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        User = User_Save.objects.filter(Id=Id).all()

        user = ""
        User_Niotif = ""

        if Legal.exists() or Genuine.exists():
            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Seller_Support", Chat_user2_Id=Id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Seller)
                for item in Notification_Support:
                    Notif_List.append(item.Visit_Seller)

            User_Niotif = sum(Notif_List)
            Res = "Seller"
            if Legal.exists():
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()

            elif Genuine.exists():
                user = Seller_Genuine.objects.filter(Seller_Id=Id).all()

        elif User.exists():

            Notification = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                                Chat_user2_Id=user_st["User"].id).all()
            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_User)

            User_Niotif = sum(Notif_List)

            user = User_Save.objects.filter(Id=Id).all()
            Res = "User"
        else:

            Notification = Chats.objects.filter(Q(With="Seller_Support") | Q(With="User_Support"),
                                                Chat_user_Id=Id).all()

            Notification_Support = Chats.objects.filter(With="Support_Seller", Chat_user2_Id=Id).all()

            Notif_List = []
            if Notification.exists():
                for item in Notification:
                    Notif_List.append(item.Visit_Support)

                for item in Notification_Support:
                    Notif_List.append(item.Visit_Support)

            User_Niotif = sum(Notif_List)

            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"

        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        incll = "incl2.html"
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی", "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        return render(request=request, template_name="Wallet.html",
                      context={"user": user, "icon": icon, "href": href,
                               "circle": circle, "script": script,
                               "incl": incl, "Res": Res, "active2": "active",
                               "User_Niotif": User_Niotif,"incll":incll,
                               "Mylist_sorts":Mylist_sorts})

    else:
        return HttpResponseRedirect("/Farshtore/login")


def Subscribation(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        icon = "User_Icon_include.html"
        href = "/Farshtore/EditProfile/"
        circle = "rounded-circle"
        script = '/static/js/tm.js'
        incl = "include.html"
        return render(request=request, template_name="Subscribation.html",
                      context={"user": user, "icon": icon, "href": href,
                               "circle": circle, "script": script, "incl": incl})

    else:
        return HttpResponseRedirect("/Farshtore/login")


def Seller_CheckResult(request):
    icon = "User_Icon_include.html"
    href = "/Farshtore/EditProfile/"
    circle = "rounded-circle"
    script = '/static/js/tm.js'
    incl = "include.html"
    return render(request=request, template_name="Seller_result.html",
                  context={"incl": incl, "script": script, "circle": circle,
                           "href": href, "icon": icon})


def Seller_Genuine_CheckInfo(request):
    icon = "User_Icon_include.html"
    href = "/Farshtore/EditProfile/"
    circle = "rounded-circle"
    script = '/static/js/tm.js'
    incl = "include.html"

    S_Genuine = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address, State="Login").first()

    S_Legal = Seller_Legal.objects.filter(Seller_IpAddress=ip_address, State="Login").first()
    S_Id = ""
    if S_Legal:
        S_Id = S_Legal.Seller_Id

    elif S_Genuine:
        S_Id = S_Genuine.Seller_Id
    try:
        S_Search_Id = User.objects.filter(id=S_Id).first()
        if S_Search_Id:
            return HttpResponseRedirect("/Farshtore/Login_Seller/Genuine")
    except:
        Search_Genuine = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address).all()
        Search_Legal = Seller_Legal.objects.filter(Seller_IpAddress=ip_address).all()

        Legal = Seller_Legal.objects.all()
        Genuine = Seller_Genuine.objects.all()
        Support = Supporter.objects.all()
        Users = User_Save.objects.all()

        My_Id = []

        User_Ids = max(obj.Id for obj in Users) if Users else 0
        My_Id.append(User_Ids)
        Support_Ids = max(obj.Id for obj in Support) if Support else 0
        My_Id.append(Support_Ids)

        Legal_Ids = max(obj.Seller_Id for obj in Legal) if Legal else 0
        My_Id.append(Legal_Ids)
        Genuine_Ids = max(obj.Seller_Id for obj in Genuine) if Genuine else 0
        My_Id.append(Genuine_Ids)

        Add_Id = max(My_Id) + 1

        if Search_Legal.exists():
            if not Search_Genuine.exists():
                Search_Legal.delete()
                Save_Result = Seller_Genuine(Seller_Id=Add_Id, Seller_IpAddress=ip_address)
                Save_Result.save()
            else:
                Search_Legal.delete()
        else:
            if not Search_Genuine.exists():
                Save_Result = Seller_Genuine(Seller_Id=Add_Id, Seller_IpAddress=ip_address)
                Save_Result.save()
            else:
                pass

        form = Seller_Genuine_Form()

        return render(request=request, template_name="Seller_Genuine_Information.html",
                      context={"incl": incl, "script": script, "circle": circle,
                               "href": href, "icon": icon, "form": form})


def Seller_Legal_CheckInfo(request):
    icon = "User_Icon_include.html"
    href = "/Farshtore/EditProfile/"
    circle = "rounded-circle"
    script = '/static/js/tm.js'
    incl = "include.html"

    S_Genuine = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address, State="Login").first()

    S_Legal = Seller_Legal.objects.filter(Seller_IpAddress=ip_address, State="Login").first()
    S_Id = ""
    if S_Legal:
        S_Id = S_Legal.Seller_Id

    elif S_Genuine:
        S_Id = S_Genuine.Seller_Id
    try:
        S_Search_Id = User.objects.filter(id=S_Id).first()
        if S_Search_Id:
            return HttpResponseRedirect("/Farshtore/Login_Seller/Legal")
    except:
        Search_Genuine = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address).all()
        Search_Legal = Seller_Legal.objects.filter(Seller_IpAddress=ip_address).all()

        Legal = Seller_Legal.objects.all()
        Genuine = Seller_Genuine.objects.all()
        Support = Supporter.objects.all()
        Users = User_Save.objects.all()

        My_Id = []

        User_Ids = max(obj.Id for obj in Users) if Users else 0
        My_Id.append(User_Ids)
        Support_Ids = max(obj.Id for obj in Support) if Support else 0
        My_Id.append(Support_Ids)

        Legal_Ids = max(obj.Seller_Id for obj in Legal) if Legal else 0
        My_Id.append(Legal_Ids)
        Genuine_Ids = max(obj.Seller_Id for obj in Genuine) if Genuine else 0
        My_Id.append(Genuine_Ids)

        Add_Id = max(My_Id) + 1

        if Search_Genuine.exists():
            if not Search_Legal.exists():
                Search_Genuine.delete()
                Save_Result = Seller_Legal(Seller_Id=Add_Id, Seller_IpAddress=ip_address)
                Save_Result.save()
            else:
                Search_Genuine.delete()
        else:
            if not Search_Legal.exists():
                Save_Result = Seller_Legal(Seller_Id=Add_Id, Seller_IpAddress=ip_address)
                Save_Result.save()
            else:
                pass

        if Search_Genuine.exists():
            if not Search_Genuine.exists():
                Search_Genuine.delete()
                Save_Result = Seller_Legal(Seller_IpAddress=ip_address)
                Save_Result.save()
            else:
                Search_Genuine.delete()
                Save_Result = Seller_Legal(Seller_IpAddress=ip_address)
                Save_Result.save()

        form = Seller_Legal_Form()

        Company_Types = ['سهامی عام', 'سهامی خاص', 'مسئولیت محدود', 'تعاونی', 'تضامنی', 'موسسه', 'سایر']

        return render(request=request, template_name="Seller_Legal_Information.html",
                      context={"incl": incl, "script": script, "circle": circle,
                               "href": href, "icon": icon, "form": form,
                               "Company_Types": Company_Types})


def Seller_CheckInfo(request):
    Search_Genuine = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address).all()
    Search_Legal = Seller_Legal.objects.filter(Seller_IpAddress=ip_address).all()
    if Search_Genuine.exists():
        return HttpResponseRedirect("/Farshtore/Seller/Genuine/Information")
    elif Search_Legal.exists():
        return HttpResponseRedirect("/Farshtore/Seller/Legal/Information")
    else:
        return HttpResponseRedirect("/Farshtore/Seller/CheckResult")


def Seller_CheckAddress(request):
    icon = "User_Icon_include.html"
    href = "/Farshtore/EditProfile/"
    circle = "rounded-circle"
    script = '/static/js/tm.js'
    incl = "include.html"

    return render(request=request, template_name="Seller_Address.html",
                  context={"incl": incl, "script": script, "circle": circle,
                           "href": href, "icon": icon})


def Seller_CheckQuestion(request):
    icon = "User_Icon_include.html"
    href = "/Farshtore/EditProfile/"
    circle = "rounded-circle"
    script = '/static/js/tm.js'
    incl = "include.html"

    return render(request=request, template_name="Seller_Question.html",
                  context={"incl": incl, "script": script, "circle": circle,
                           "href": href, "icon": icon})


def Seller_EnterPanel(request):
    icon = "User_Icon_include.html"
    href = "/Farshtore/EditProfile/"
    circle = "rounded-circle"
    script = '/static/js/tm.js'
    incl = "include.html"
    form = Logins_Seller()

    return render(request=request, template_name="Seller_EnterPanel.html",
                  context={"incl": incl, "script": script, "circle": circle,
                           "href": href, "icon": icon, "Login_Seller": Logins_Seller})


@csrf_exempt
def Addview(request, Code):
    user_st = UserAuth().StateLogin(request)
    if request.method == "POST":
        if user_st["State"]:
            yesterday = datetime.now() - timedelta(0)

            Time = jdatetime.fromgregorian(day=yesterday.day, month=yesterday.month,
                                           year=yesterday.year).strftime("%Y/%m/%d")

            users = User_View.objects.filter(Product_Code=str(Code), user_Id=user_st["User"].id).all()
            if users.exists():
                pass
            else:
                Saved_Data = User_View(Product_Code=str(Code), user_Id=user_st["User"].id,
                                       Date=Time)
                Saved_Data.save()

                Add_View = Add_Product.objects.filter(Product_Code=str(Code)).first()
                Add_View.Product_Visit = Add_View.Product_Visit + 1
                Add_View.save()
        else:
            pass

        return HttpResponse("True")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Add_Like(request, Code):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            user_likes = Like.objects.filter(Product_Code=str(Code), user_Id=user_st["User"].id)
            if user_likes.exists():
                return HttpResponse("False")
            else:
                yesterday = datetime.now() - timedelta(0)

                Time = jdatetime.fromgregorian(day=yesterday.day, month=yesterday.month,
                                               year=yesterday.year).strftime("%Y/%m/%d")

                add_like = Like(Product_Code=str(Code), user_Id=user_st["User"].id,
                                Date=Time)
                add_like.save()
                Srch_Like = Add_Product.objects.filter(Product_Code=str(Code)).first()
                Srch_Like.Product_Likes = Srch_Like.Product_Likes + 1
                Srch_Like.save()
                return HttpResponse("Add")
        else:
            return HttpResponseRedirect("/Farshtore/404")
    else:
        return HttpResponseRedirect("/Farshtore/login")


@csrf_exempt
def Remove_Like(request, Code):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            add_like = Like.objects.filter(Product_Code=str(Code), user_Id=user_st["User"].id)
            add_like.delete()
            Srch_Like = Add_Product.objects.filter(Product_Code=str(Code)).first()
            Srch_Like.Product_Likes = Srch_Like.Product_Likes - 1
            Srch_Like.save()
            return HttpResponse("Delete")
        else:
            return HttpResponseRedirect("/Farshtore/404")
    else:
        return HttpResponseRedirect("/Farshtore/login")


@csrf_exempt
def Search_Like(request, Code):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            User_Likes = Like.objects.filter(Product_Code=Code, user_Id=user_st["User"].id).all()
            Read_Likes = serializers.serialize("json", User_Likes)
            return HttpResponse(Read_Likes)
        else:
            return HttpResponseRedirect("/Farshtore/404")

    else:
        return HttpResponseRedirect("/Farshtore/login")


@csrf_exempt
def Search_view(request, Code):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            User_view = User_View.objects.filter(Product_Code=Code, user_Id=user_st["User"].id).all()
            Read_view = serializers.serialize("json", User_view)
            return HttpResponse(Read_view)
        else:
            return HttpResponseRedirect("/Farshtore/404")

    else:
        return HttpResponseRedirect("/Farshtore/login")


@csrf_exempt
def Admin_AllProduct(request, user_id):
    if request.method == "POST":
        if int(user_id) != 0:
            user_name = User.objects.filter(id=user_id).first()
            Full_Name = f"{user_name.first_name} {user_name.last_name}"
            return HttpResponse(Full_Name)
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Admin_Product_Order_Count(request,Product_Code):
    print(Product_Code)
    if request.method == "POST":
        Product_Orders = Product_Order.objects.filter(Product_Code=Product_Code).all()
        print(len(Product_Orders))
        return HttpResponse(len(Product_Orders))
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Admin_AllUser(request, user_id):
    if request.method == "POST":
        if int(user_id) == 0:
            AllUser = User_Save.objects.all()

            Read_User = serializers.serialize("json", AllUser)
            return HttpResponse(Read_User)
        else:
            User_info = User.objects.filter(id=user_id).first()
            info = serializers.serialize("json", [User_info])
            return HttpResponse(info)
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Admin_AllSupporter(request, user_id):
    if request.method == "POST":
        if int(user_id) == 0:
            AllUser = Supporter.objects.all()

            Read_User = serializers.serialize("json", AllUser)
            return HttpResponse(Read_User)
        else:
            User_info = User.objects.filter(id=user_id).first()
            info = serializers.serialize("json", [User_info])
            return HttpResponse(info)
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Admin_AllUser_Seller(request, user_id):
    if request.method == "POST":
        if int(user_id) == 0:
            AllUser = list(itertools.chain(
                Seller_Legal.objects.all(),
                Seller_Genuine.objects.all()
            ))

            Read_User_Seller = serializers.serialize("json", AllUser)
            print(Read_User_Seller)
            return HttpResponse(Read_User_Seller)
        else:
            print(user_id)
            User_info = User.objects.filter(id=user_id).first()
            info = serializers.serialize("json", [User_info])
            return HttpResponse(info)
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Order_Product(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            AllProduct_Order = Product_Order.objects.filter(user_Id=user_st["User"].id).all()
            Read_Product_Order = serializers.serialize("json", AllProduct_Order)
            return HttpResponse(Read_Product_Order)
        else:
            return HttpResponseRedirect("/Farshtore/404")

    else:
        return HttpResponseRedirect("/Farshtore/login")


@csrf_exempt
def Search(request, txt_Search):
    if request.method == "POST":
        if txt_Search == "None":
            url = "http://127.0.0.1:8000/apiread_product/"

            response = requests.request("GET", url)

            obj = json.loads(response.text)
            if len(obj) == 0:
                return HttpResponse("Not_found")
            return HttpResponse(obj)
        else:
            url = f"http://127.0.0.1:8000/apiSearch_product/?format=json&q={txt_Search}"

            response = requests.request("GET", url)
            obj = json.loads(response.text)
            if len(obj) == 0:
                return HttpResponse("Not_found")
            return HttpResponse(obj)
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Search_Sort(request, txt_res, txt_sort, Price_Start, Price_End):
    Search_Product = None
    if request.method == "POST":
        Mylist_sorts = ["دست باف", "ماشینی", "نخ و نقشه کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک",
                        "فانتزی",
                        "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        print(txt_res)
        print(txt_sort)
        if txt_sort != "None" and Price_Start == "None" and Price_End == "None":
            if txt_sort in Mylist_sorts:
                Search_Product = Add_Product.objects.filter(Q(Product_Brand=txt_res, Product_Type=txt_sort) |
                                                            Q(Product_Shane=txt_res)).all()
            else:
                Search_Product = Add_Product.objects.filter(Product_Brand=txt_sort, Product_Type=txt_res).all()

        elif txt_sort == "None" and Price_Start == "None" and Price_End == "None":
            if txt_res in Mylist_sorts:
                Search_Product = Add_Product.objects.filter(Q(Product_Type=txt_res) |
                                                            Q(Product_Shane=txt_res)).all()
            else:
                Search_Product = Add_Product.objects.filter(Q(Product_Brand=txt_res) |
                                                            Q(Product_Shane=txt_res)).all()

        elif txt_sort != "None" and Price_Start != "None" and Price_End != "None":
            if txt_sort in Mylist_sorts:
                Search_Product = Add_Product.objects.filter(Q(Product_Brand=txt_res, Product_Type=txt_sort) |
                                                            Q(Product_Shane=txt_res),
                                                            Product_Price__gte=Price_Start,
                                                            Product_Price__lte=Price_End).all()
            else:
                Search_Product = Add_Product.objects.filter(Product_Brand=txt_sort, Product_Type=txt_res,
                                                            Product_Price__gte=Price_Start,
                                                            Product_Price__lte=Price_End).all()

        elif txt_sort == "None" and Price_Start != "None" and Price_End != "None":
            if txt_res in Mylist_sorts:
                Search_Product = Add_Product.objects.filter(Product_Type=txt_res, Product_Price__gte=Price_Start,
                                                            Product_Price__lte=Price_End).all()
            else:
                Search_Product = Add_Product.objects.filter(Q(Product_Brand=txt_res) |
                                                            Q(Product_Shane=txt_res),
                                                            Product_Price__gte=Price_Start,
                                                            Product_Price__lte=Price_End).all()

        if Search_Product is not None:
            if not Search_Product.exists():
                return HttpResponse("False")
            else:
                Read_Sort_Product = serializers.serialize("json", Search_Product)
                return HttpResponse(Read_Sort_Product)
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Search_Res(request, Res):
    if request.method == "POST":
        Search_Product = Add_Product.objects.filter(Product_Result=Res).all()
        if len(Search_Product) == 0:
            return HttpResponse("Not_found")
        Read_Product_Search = serializers.serialize("json", Search_Product)
        return HttpResponse(Read_Product_Search)
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Search_Rag(request, Rag):
    if request.method == "POST":
        Search_Product = Add_Product.objects.filter(Product_Rag=Rag).all()
        if len(Search_Product) == 0:
            return HttpResponse("Not_found")
        Read_Product_Search = serializers.serialize("json", Search_Product)
        return HttpResponse(Read_Product_Search)
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Search_Price(request, Start, End, txt_Sort, txt_Brand):
    if request.method == "POST":
        if txt_Sort != "None":
            Search_Product = Add_Product.objects.filter(Product_Price_Final__gte=Start, Product_Price_Final__lte=End,
                                                        Product_Type=txt_Sort).all()
        elif txt_Brand != "None":
            Search_Product = Add_Product.objects.filter(Product_Price_Final__gte=Start, Product_Price_Final__lte=End,
                                                        Product_Brand=txt_Brand).all()
        elif txt_Sort != "None" and txt_Brand != "None":
            Search_Product = Add_Product.objects.filter(Product_Price_Final__gte=Start, Product_Price_Final__lte=End,
                                                        Product_Type=txt_Sort, Product_Brand=txt_Brand).all()
        else:
            Search_Product = Add_Product.objects.filter(Product_Price_Final__gte=Start,
                                                        Product_Price_Final__lte=End).all()

        if len(Search_Product) == 0:
            return HttpResponse("Not_found")
        Read_Price_Product = serializers.serialize("json", Search_Product)
        return HttpResponse(Read_Price_Product)
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Chat_Save(request, Other_id, text, Chat_Code, Date):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            Id = user_st["User"].id

            Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
            Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
            Users = User_Save.objects.filter(Id=Id).all()

            Support = Supporter.objects.filter(Id=Id).all()

            User_Seller = Chats.objects.filter(Chat_user_Id=Other_id, Chat_user2_Id=Id,
                                               With="User_Seller", Chat_Code=Chat_Code).first()

            User_Support = Chats.objects.filter(Chat_user_Id=Other_id, Chat_user2_Id=Id,
                                                With="User_Support", Chat_Code=Chat_Code).first()

            Visited_Support = Chats.objects.filter(Chat_user_Id=Other_id, Chat_user2_Id=Id,
                                                   With="Seller_Support", Chat_Code=Chat_Code).first()

            Visited_Seller_Support = Chats.objects.filter(Chat_user_Id=Other_id, Chat_user2_Id=Id,
                                                          With="Support_Seller", Chat_Code=Chat_Code
                                                          ).first()

            Visited_Seller_Sup = Chats.objects.filter(Chat_user2_Id=Other_id, Chat_user_Id=Id,
                                                      With="Seller_Support", Chat_Code=Chat_Code
                                                      ).first()

            Visited_User_Sup = Chats.objects.filter(Chat_user2_Id=Other_id, Chat_user_Id=Id,
                                                    With="User_Support", Chat_Code=Chat_Code
                                                    ).first()

            Visited_User_Support = Chats.objects.filter(Chat_user_Id=Id, Chat_user2_Id=Other_id,
                                                        With="Seller_Support", Chat_Code=Chat_Code
                                                        ).first()

            Visited_support_Seller = Chats.objects.filter(Chat_user_Id=Id, Chat_user2_Id=Other_id,
                                                          With="Support_Seller", Chat_Code=Chat_Code
                                                          ).first()

            Save_Seller = Chats.objects.filter(Chat_user_Id=Other_id, Chat_user2_Id=Id,
                                               With="User_Support", Chat_Code=Chat_Code
                                               ).first()

            chat_objects = Chats.objects.filter(Chat_Code=Chat_Code).all()
            max_counter = max(obj.counter for obj in chat_objects) if chat_objects else 0
            max_counter += 1

            if Genuine.exists() or Legal.exists() or Users.exists():
                if Visited_User_Support:
                    Save_data = Chats(Message=str(text), counter=max_counter, Chat_user_Id=Id,
                                      Chat_user2_Id=Other_id, Chat_Code=Chat_Code, Chat_Message_Date=Date,
                                      Seender=Id)
                else:
                    Save_data = Chats(Message=str(text), counter=max_counter, Chat_user2_Id=Id,
                                      Chat_user_Id=Other_id, Chat_Code=Chat_Code, Chat_Message_Date=Date,
                                      Seender=Id)
                Save_data.save()

            else:
                Save_data = Chats(Message=str(text), counter=max_counter, Chat_user_Id=Id,
                                  Chat_user2_Id=Other_id, Chat_Code=Chat_Code, Chat_Message_Date=Date,
                                  Seender=Id)
                Save_data.save()

                if Visited_Seller_Sup:
                    Visited_Seller_Sup.Visit_Seller += 1
                    Visited_Seller_Sup.save()

                elif Visited_User_Sup:
                    Visited_User_Sup.Visit_User += 1
                    Visited_User_Sup.save()

                elif Visited_support_Seller:
                    Visited_support_Seller.Visit_Seller += 1
                    Visited_support_Seller.save()

            if Legal.exists() or Genuine.exists():
                if User_Seller:
                    User_Seller.Visit_User += 1
                    User_Seller.save()

                elif Visited_Seller_Sup:
                    Visited_Seller_Sup.Visit_Support += 1
                    Visited_Seller_Sup.save()

                elif Visited_Support:
                    Visited_Support.Visit_Support += 1
                    Visited_Support.save()

            else:
                if User_Seller:
                    User_Seller.Visit_Seller += 1
                    User_Seller.save()

                elif User_Support:
                    User_Support.Visit_Support += 1
                    User_Support.save()

            return HttpResponse("items")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Chat_Save_Seller(request, Other_id, text, Chat_Code, Date):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            Id = user_st["User"].id
            chat_objects = Chats.objects.filter(Chat_Code=Chat_Code).all()
            Seller = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user2_Id=Id,
                                          Chat_user_Id=Other_id, With="Seller_Support").first()

            User_Load = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                             Chat_Code=Chat_Code, Chat_user2_Id=Id,
                                             Chat_user_Id=Other_id).first()

            User_Seller = Chats.objects.filter(With="User_Seller",
                                               Chat_Code=Chat_Code, Chat_user2_Id=Id,
                                               Chat_user_Id=Other_id).first()

            User_Support = Chats.objects.filter(With="User_Support",
                                                Chat_Code=Chat_Code, Chat_user2_Id=Id,
                                                Chat_user_Id=Other_id).first()

            max_counter = max(obj.counter for obj in chat_objects) if chat_objects else 0
            max_counter += 1
            if Seller:
                Save_data = Chats(Message=str(text), counter=max_counter, Chat_user2_Id=Id,
                                  Chat_user_Id=Other_id, Chat_Code=Chat_Code, Chat_Message_Date=Date,
                                  Seender=Id)
            elif User_Load:
                Save_data = Chats(Message=str(text), counter=max_counter, Chat_user2_Id=Id,
                                  Chat_user_Id=Other_id, Chat_Code=Chat_Code, Chat_Message_Date=Date,
                                  Seender=Id)
            else:
                Save_data = Chats(Message=str(text), counter=max_counter, Chat_user_Id=Id,
                                  Chat_user2_Id=Other_id, Chat_Code=Chat_Code, Chat_Message_Date=Date,
                                  Seender=Id)
            Save_data.save()

            Visited_Seller = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                                  Chat_user2_Id=Other_id, Chat_user_Id=Id,
                                                  Chat_Code=Chat_Code).first()

            Visited_Support = Chats.objects.filter(Chat_user_Id=Other_id, Chat_user2_Id=Id,
                                                   With="Support_Seller").first()

            Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
            Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()

            if Legal.exists() or Genuine.exists():
                if Visited_Seller:
                    if Visited_Seller.With == "User_Seller":
                        Visited_Seller.Visit_User += 1
                        Visited_Seller.save()

                    else:
                        Visited_Seller.Visit_Support += 1
                        Visited_Seller.save()

                elif Seller:
                    Seller.Visit_Support += 1
                    Seller.save()


            else:
                if Visited_Seller:
                    Visited_Seller.Visit_Seller += 1
                    Visited_Seller.save()

                elif Visited_Support:
                    Visited_Support.Visit_Seller += 1
                    Visited_Support.save()

                elif User_Seller:
                    User_Seller.Visit_Seller += 1
                    User_Seller.save()
                elif User_Support:
                    User_Support.Visit_Support += 1
                    User_Support.save()

            return HttpResponse("items")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Chat_Save_User(request, Other_id, text, Chat_Code, Date):
    print(Other_id)
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            Id = user_st["User"].id
            chat_objects = Chats.objects.filter(Chat_Code=Chat_Code).all()

            max_counter = max(obj.counter for obj in chat_objects) if chat_objects else 0
            max_counter += 1
            Save_data = Chats(Message=str(text), counter=max_counter, Chat_user2_Id=Id,
                              Chat_user_Id=Other_id, Chat_Code=Chat_Code, Chat_Message_Date=Date,
                              Seender=Id)
            Save_data.save()

            Visited = Chats.objects.filter(Chat_user_Id=Other_id, Chat_user2_Id=Id,
                                           With="User_Seller").first()
            Visited.Visit_Seller += 1
            Visited.save()

            return HttpResponse("items")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Chat_Save_Support(request, Other_id, text, Chat_Code, Date):
    print(Other_id)
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            Id = user_st["User"].id
            chat_objects = Chats.objects.filter(Chat_Code=Chat_Code).all()

            max_counter = max(obj.counter for obj in chat_objects) if chat_objects else 0
            max_counter += 1
            Save_data = Chats(Message=str(text), counter=max_counter, Chat_user2_Id=Other_id,
                              Chat_user_Id=Id, Chat_Code=Chat_Code, Chat_Message_Date=Date,
                              Seender=Id)
            Save_data.save()

            Visited = Chats.objects.filter(With="User_Support",
                                           Chat_user_Id=Id, Chat_user2_Id=Other_id,
                                           ).first()

            Visited2 = Chats.objects.filter(With="Support_Seller",
                                            Chat_user_Id=Id, Chat_user2_Id=Other_id,
                                            ).first()

            Visited3 = Chats.objects.filter(With="Seller_Support",
                                            Chat_user_Id=Other_id, Chat_user2_Id=Id,
                                            ).first()
            if Visited:
                Visited.Visit_User += 1
                Visited.save()

            elif Visited2:
                Visited2.Visit_Seller += 1
                Visited2.save()

            elif Visited3:
                Visited3.Visit_Seller += 1
                Visited3.save()

            return HttpResponse("items")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Chat_Read(request, Chat_Code, Other_Id):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            if Chat_Code != "undefined":
                Id = user_st["User"].id
                Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
                Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
                Users = User_Save.objects.filter(Id=Id).all()
                Support = Supporter.objects.filter(Id=Id).all()

                chat_code = ""

                if Legal.exists() or Genuine.exists() or Users.exists():
                    chat_code = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user2_Id=Id).all()
                    if not chat_code.exists():
                        chat_code = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user_Id=Id).all()

                elif Support.exists():

                    Visited = Chats.objects.filter(With="User_Support", Chat_user2_Id=Other_Id,
                                                   Chat_user_Id=Id,
                                                   Chat_Code=Chat_Code).first()

                    Visit = Chats.objects.filter(With="Support_Seller", Chat_user2_Id=Other_Id,
                                                 Chat_user_Id=Id,
                                                 Chat_Code=Chat_Code).first()
                    try:
                        Visited.Visit_Support = 0
                        Visited.save()
                    except:
                        Visit.Visit_Support = 0
                        Visit.save()
                    chat_code = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user_Id=Id,
                                                     Chat_user2_Id=Other_Id).all()

                chat_messages = sorted(chat_code, key=lambda x: x.counter)
                serialized_chat_messages = serializers.serialize("json", chat_messages)
                return HttpResponse(serialized_chat_messages)
            else:
                return HttpResponse("False")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Chat_Group(request, group_Code):
    if request.method == "POST":
        user_state = UserAuth().StateLogin(request)
        if user_state["State"]:
            Sort_Group = Chats_Code.objects.filter(Chat_Code=group_Code).first()
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


def Support(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        Id = user_st["User"].id
        Read_Chat = Chats.objects.filter(Chat_user_Id=Id).all()
        Sort_Group = Chats_Code.objects.all()

        random_Support = Supporter.objects.all()
        Support_List = []
        for item in random_Support:
            Support_List.append(item.Chat_Code)

        Support = ""
        Search_User = ""
        User_List = []
        Support_lst = []
        Seller_List = []
        With_List = []

        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        support = Supporter.objects.filter(Id=Id).all()
        Users = User_Save.objects.filter(Id=Id).all()
        if Genuine.exists() or Legal.exists():
            if Legal.exists():
                user = Seller_Legal.objects.filter(Seller_Id=Id).all()
            else:
                user = Seller_Genuine.objects.filter(Seller_Id=Id).all()
            Search_all = Chats.objects.filter(With="Seller_Support").all()

            user_result = "Seller"
            Res = "Seller"

        elif support.exists():
            user = Supporter.objects.filter(Id=Id).all()
            Search_all = Chats.objects.filter(Q(With="User_Support") | Q(With="Seller_Support"),
                                              Chat_user_Id=Id).all()
            user_result = "Support"
            Res = "Support"

        else:
            user = User_Save.objects.filter(Id=Id).all()
            Search_all = Chats.objects.filter(Q(With="User_Support") | Q(With="Seller_Support")).all()
            Search_User = Chats.objects.filter(With="User_Support", Chat_user2_Id=Id).all()

            user_result = "User"
            Res = "User"

        if not Search_all.exists():
            if Users.exists():
                Support_Code = random.choice(Support_List)
                Support = Supporter.objects.filter(Chat_Code=Support_Code).first()
                import datetime
                Date = datetime.datetime.now().strftime("%A, %H:%M")
                text = "سلام دوست عزیز چطور میتونم به شما کمک کنم؟"
                Add = Chats(Message=text, counter=1, Chat_user_Id=Support.Id, Chat_Code=Support_Code,
                            Chat_Message_Date=Date, Chat_user2_Id=Id,
                            Seender=Support.Id, With=user_result + "_Support")
                Add.save()

                for item in Search_User:
                    User_List.append(item.Chat_Code)
                    With_List.append(item.With)

                data = list(zip(User_List, With_List))
                Group_List = [
                    {"Chat_Code": Chat_Code_List, "With": With_List}
                    for Chat_Code_List, With_List in data]

            elif Legal.exists() or Genuine.exists():
                Support_Code = random.choice(Support_List)
                Support = Supporter.objects.filter(Chat_Code=Support_Code).first()
                Date = datetime.datetime.now().strftime("%A, %H:%M")
                text = "سلام دوست عزیز چطور میتونم به شما کمک کنم؟"
                Add = Chats(Message=text, counter=1, Chat_user2_Id=Support.Id, Chat_Code=Support_Code,
                            Chat_Message_Date=Date, Chat_user_Id=Id,
                            Seender=Support.Id, With=user_result + "_Support")
                Add.save()

                for item in Search_all:
                    User_List.append(item.Chat_Code)
                    With_List.append(item.With)

                data = list(zip(User_List, With_List))
                Group_List = [
                    {"Chat_Code": Chat_Code_List, "With": With_List}
                    for Chat_Code_List, With_List in data]

                return render(request=request, template_name="chat_app.html",
                              context={"user_st": user_st, "Read_Chat": Read_Chat,
                                       "user": user, "Sort_Group": Sort_Group,
                                       "Support": Support, "Res": Res, "Other": "User",
                                       "Code_List": Group_List})
        else:
            if support.exists():
                for item in Search_all:
                    Support_lst.append(item.Chat_Code)
                    With_List.append(item.With)

            elif Users.exists():
                for item in Search_User:
                    User_List.append(item.Chat_Code)
                    With_List.append(item.With)

                data = list(zip(User_List, With_List))
                Group_List = [
                    {"Chat_Code": Chat_Code_List, "With": With_List}
                    for Chat_Code_List, With_List in data]

                return render(request=request, template_name="chat_app.html",
                              context={"user_st": user_st, "Read_Chat": Read_Chat,
                                       "user": user, "Sort_Group": Sort_Group,
                                       "Support": Support, "Res": Res, "Other": "User",
                                       "Code_List": Group_List})

            else:
                for item in Search_all:
                    Seller_List.append(item.Chat_Code)
                    With_List.append(item.With)

                data = list(zip(Seller_List, With_List))
                Group_List = [
                    {"Chat_Code": Chat_Code_List, "With": With_List}
                    for Chat_Code_List, With_List in data]

                return render(request=request, template_name="chat_app.html",
                              context={"user_st": user_st, "Read_Chat": Read_Chat,
                                       "user": user, "Sort_Group": Sort_Group,
                                       "Support": Support, "Res": Res, "Other": "Support",
                                       "Code_List": Group_List})

            data = list(zip(Support_lst, With_List))
            Group_List = [
                {"Chat_Code": Chat_Code_List, "With": With_List}
                for Chat_Code_List, With_List in data]
            return render(request=request, template_name="chat_app.html",
                          context={"user_st": user_st, "Read_Chat": Read_Chat,
                                   "user": user, "Sort_Group": Sort_Group,
                                   "Support": Support, "Res": Res, "Other": "Support",
                                   "Code_List": Group_List})

        Chat_Code_List = []
        for item in Search_all:
            Chat_Code_List.append(item.Chat_Code)

        Code_List = list(set(Chat_Code_List))

        data = list(zip(User_List, With_List))
        Group_List = [
            {"Chat_Code": Chat_Code_List, "With": With_List}
            for Chat_Code_List, With_List in data]

        if Legal.exists() or Genuine.exists():
            Other = "Seller"

        elif support.exists():
            Other = "Support"

        else:
            Other = "User"
        return render(request=request, template_name="chat_app.html",
                      context={"user_st": user_st, "Read_Chat": Read_Chat,
                               "user": user, "Sort_Group": Sort_Group,
                               "Support": Support, "Res": Res, "Other": Other,
                               "Code_List": Code_List})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def Seller_Chat(request, Chat_Code):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        Id = user_st["User"].id

        Code = Add_Product.objects.filter(Chat_Code=Chat_Code).first()

        Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
        support = Supporter.objects.filter(Id=Id).all()
        Search_Product = Add_Product.objects.filter(Chat_Code=Chat_Code).first()
        Read_Chat = Chats.objects.filter(Chat_user_Id=Id).all()
        Users = User_Save.objects.filter(Id=Id).all()
        Seller_Chat_Exist = Chats.objects.filter(Chat_Code=Chat_Code,
                                                 Chat_user2_Id=Id).all()

        Support_Exists = Chats.objects.filter(Chat_user_Id=Id, With="Support_Seller",
                                              Chat_Code=Chat_Code).first()

        Search_User = Chats.objects.filter(With="User_Seller", Chat_user2_Id=Id).all()

        if Legal.exists() or Genuine.exists():
            return HttpResponseRedirect("/Farshtore/product_information/" + Code.Product_Code)

        elif support.exists() or Users.exists():

            if support.exists():
                user = Supporter.objects.filter(Id=Id).all()
                Res = "Support"
                Search_all = Chats.objects.filter(With="Support_Seller").all()
                With = "Support_Seller"
            else:
                user = User_Save.objects.filter(Id=Id).all()
                Res = "User"
                Search_all = Chats.objects.filter(With="User_Seller").all()
                With = "User_Seller"

            Seller_Name = User.objects.filter(id=Search_Product.user_Id).first()
            Name = Seller_Name.first_name + " " + Seller_Name.last_name

            Sort_Group = Chats_Code.objects.all()

            if not Seller_Chat_Exist.exists():
                if support.exists():
                    if not Support_Exists:
                        Seller_Chat = Chats.objects.filter(Chat_Code=Chat_Code).first()
                        Date = datetime.datetime.now().strftime("%A, %H:%M")
                        text = "سلام دوست عزیز سوالی درمورد محصول داری؟ بپرس."
                        Add = Chats(Message=text, counter=1, Chat_user_Id=Id, With=With,
                                    Chat_Code=Chat_Code, Chat_Message_Date=Date,
                                    Chat_user2_Id=Search_Product.user_Id, Seender=Search_Product.user_Id)
                        Add.save()
                else:
                    Seller_Chat = Chats.objects.filter(Chat_Code=Chat_Code).first()
                    import datetime
                    Date = datetime.datetime.now().strftime("%A, %H:%M")
                    text = "سلام دوست عزیز سوالی درمورد محصول داری؟ بپرس."
                    Add = Chats(Message=text, counter=1, Chat_user_Id=Search_Product.user_Id,
                                Chat_Code=Chat_Code, Chat_Message_Date=Date,
                                Chat_user2_Id=Id, Seender=Search_Product.user_Id,
                                With=With)
                    Add.save()

            User_List = []
            With_List = []
            for item in Search_all:
                User_List.append(item.Chat_Code)
                With_List.append(item.With)

            Code_List = list(set(User_List))

            data = list(zip(User_List, With_List))
            Group_List = [
                {"Chat_Code": User_List, "With": With_List}
                for User_List, With_List in data]
            print(Group_List)

            return render(request=request, template_name="chat_app.html",
                          context={"user_st": user_st, "Read_Chat": Read_Chat, "user": user,
                                   "Sort_Group": Sort_Group, "Res": Res, "Code_List": Group_List,
                                   "Chat_Code": Chat_Code, "Seller_Name": Name,
                                   "Other": "Seller"})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def Chat_Seller(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        Res = ""
        Legal = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()
        Genuine = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
        Users = User_Save.objects.filter(Id=user_st["User"].id).all()
        Chat_Code_List = []
        Chat_User_List = []
        Chat_user_name_list = []
        With_List = []

        if Genuine.exists() or Legal.exists():
            Res = "Seller"
            Seller_C = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller") |
                                            Q(With="Seller_Support")).all()
            for item in Seller_C:
                Chat_User_List.append(item.Chat_user2_Id)
                Chat_Code_List.append(item.Chat_Code)
                With_List.append(item.With)
            for item in Chat_User_List:
                Search_name = User.objects.filter(id=item).first()
                Chat_user_name_list.append(Search_name.first_name + " " + Search_name.last_name)
            if Genuine.exists():
                user = Seller_Genuine.objects.filter(Seller_Id=user_st["User"].id).all()
            else:
                user = Seller_Legal.objects.filter(Seller_Id=user_st["User"].id).all()

        elif Users.exists():
            user = User_Save.objects.filter(Id=user_st["User"].id).all()
            Res = "User"
        else:
            user = Supporter.objects.filter(Id=user_st["User"].id).all()
            Res = "Support"

        Read_Chat = Chats.objects.filter(Chat_user_Id=user_st["User"].id).all()

        Code_List = list(set(Chat_User_List))
        data = list(zip(Chat_user_name_list, Code_List, Chat_Code_List, With_List))
        Group_List = [{'name': Chat_user_name_list, 'Code': Code_List, "Chat_Code": Chat_Code_List, "With": With_List}
                      for Chat_user_name_list, Code_List, Chat_Code_List, With_List in data]

        return render(request=request, template_name="Chat_App_Chat.html",
                      context={"user_st": user_st, "Read_Chat": Read_Chat, "user": user,
                               "Res": Res, "Code_List": Code_List, "Group_List": Group_List,
                               "Other": "Seller", "Chat_user_name_list": Chat_user_name_list})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def User_Chat(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        Res = ""
        Chat_Code_List = []
        Chat_User_List = []
        With_List = []
        Chat_user_name_list = []

        User_Search = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"), ).all()
        for item in User_Search:
            Chat_User_List.append(item.Chat_user_Id)
            Chat_Code_List.append(item.Chat_Code)
            With_List.append(item.With)

        for item in Chat_User_List:
            Search_name = User.objects.filter(id=item).first()
            Chat_user_name_list.append(Search_name.first_name + " " + Search_name.last_name)

        user = User_Save.objects.filter(Id=user_st["User"].id).all()
        Res = "User"

        Read_Chat = Chats.objects.filter(Chat_user_Id=user_st["User"].id).all()

        data = list(zip(Chat_user_name_list, Chat_User_List, Chat_Code_List, With_List))
        Group_List = [{'name': Chat_user_name_list, 'Code': Code_List, "Chat_Code": Chat_Code_List, "With": With_List}
                      for Chat_user_name_list, Code_List, Chat_Code_List, With_List in data]
        print(Group_List)
        return render(request=request, template_name="Chat_App_Chat.html",
                      context={"user_st": user_st, "Read_Chat": Read_Chat, "user": user,
                               "Res": Res, "Code_List": Chat_User_List, "Group_List": Group_List,
                               "Other": "Seller", "Chat_user_name_list": Chat_user_name_list})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def Support_Chat(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        Res = ""
        Chat_Code_List = []
        Chat_User_List = []
        With_List = []
        Chat_user_name_list = []

        User_Search = Chats.objects.filter(Q(With="Support_Seller") | Q(With="User_Support"),
                                           Chat_user_Id=user_st["User"].id).all()

        User_Search2 = Chats.objects.filter(With="Seller_Support",
                                            Chat_user2_Id=user_st["User"].id).all()

        for item in User_Search:
            Chat_User_List.append(item.Chat_user2_Id)
            Chat_Code_List.append(item.Chat_Code)
            With_List.append(item.With)

        for item in User_Search2:
            Chat_User_List.append(item.Chat_user_Id)
            Chat_Code_List.append(item.Chat_Code)
            With_List.append(item.With)

        for item in Chat_User_List:
            Search_name = User.objects.filter(id=item).first()
            Chat_user_name_list.append(Search_name.first_name + " " + Search_name.last_name)

        user = Supporter.objects.filter(Id=user_st["User"].id).all()
        Res = "Support"

        Read_Chat = Chats.objects.filter(Chat_user_Id=user_st["User"].id).all()

        data = list(zip(Chat_user_name_list, Chat_User_List, Chat_Code_List, With_List))
        Group_List = [{'name': Chat_user_name_list, 'Code': Code_List, "Chat_Code": Chat_Code_List, "With": With_List}
                      for Chat_user_name_list, Code_List, Chat_Code_List, With_List in data]
        print(Group_List)
        return render(request=request, template_name="Chat_Support.html",
                      context={"user_st": user_st, "Read_Chat": Read_Chat, "user": user,
                               "Res": Res, "Code_List": Chat_User_List, "Group_List": Group_List,
                               "Other": "Seller", "Chat_user_name_list": Chat_user_name_list})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def Chat_User(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        Id = user_st["User"].id
        Res = ""
        user = ""
        Users = User_Save.objects.filter(Id=Id).all()
        Chat_Code_List = []
        Chat_User_List = []
        Chat_user_name_list = []
        With_List = []

        if Users.exists():

            User_Chat = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support")).all()
            for item in User_Chat:
                Chat_User_List.append(item.Chat_user2_Id)
                Chat_Code_List.append(item.Chat_Code)
                With_List.append(item.With)
            for item in Chat_User_List:
                Search_name = User.objects.filter(id=item).first()
                Chat_user_name_list.append(Search_name.first_name + " " + Search_name.last_name)

            user = User_Save.objects.filter(Id=Id).all()
            Res = "User"

        Read_Chat = Chats.objects.filter(Chat_user_Id=Id).all()

        Code_List = list(set(Chat_User_List))

        data = list(zip(Chat_user_name_list, Code_List, Chat_Code_List, With_List))
        Group_List = [{'name': Chat_user_name_list, 'Code': Code_List, "Chat_Code": Chat_Code_List, "With": With_List}
                      for Chat_user_name_list, Code_List, Chat_Code_List, With_List in data]
        print(Group_List)

        return render(request=request, template_name="Chat_User.html",
                      context={"user_st": user_st, "Read_Chat": Read_Chat, "user": user,
                               "Res": Res, "Code_List": Code_List, "Group_List": Group_List,
                               "Other": "Seller", "Chat_user_name_list": Chat_user_name_list})
    else:
        return HttpResponseRedirect("/Farshtore/login")


def Chat_Support(request):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        Id = user_st["User"].id
        Res = ""
        user = ""
        support = Supporter.objects.filter(Id=Id).all()
        Chat_Code_List = []
        Chat_Support_List = []
        Chat_user_name_list = []
        With_List = []

        if support.exists():

            Support_Chat = Chats.objects.filter(Q(With="Support_Seller") | Q(With="User_Support"),
                                                Chat_user_Id=Id).all()

            Support_Chat2 = Chats.objects.filter(With="Seller_Support", Chat_user2_Id=Id).all()

            for item in Support_Chat:
                Chat_Support_List.append(item.Chat_user2_Id)
                Chat_Code_List.append(item.Chat_Code)
                With_List.append(item.With)

            for item in Support_Chat2:
                Chat_Support_List.append(item.Chat_user_Id)
                Chat_Code_List.append(item.Chat_Code)
                With_List.append(item.With)

            for item in Chat_Support_List:
                Search_name = User.objects.filter(id=item).first()
                Chat_user_name_list.append(Search_name.first_name + " " + Search_name.last_name)

            user = Supporter.objects.filter(Id=Id).all()
            Res = "Support"

        Read_Chat = Chats.objects.filter(Chat_user_Id=Id).all()

        Code_List = list(set(Chat_Support_List))

        data = list(zip(Chat_user_name_list, Code_List, Chat_Code_List, With_List))
        Group_List = [{'name': Chat_user_name_list, 'Code': Code_List, "Chat_Code": Chat_Code_List, "With": With_List}
                      for Chat_user_name_list, Code_List, Chat_Code_List, With_List in data]
        print(Group_List)

        return render(request=request, template_name="Chat_Support.html",
                      context={"user_st": user_st, "Read_Chat": Read_Chat, "user": user,
                               "Res": Res, "Code_List": Code_List, "Group_List": Group_List,
                               "Other": "Seller", "Chat_user_name_list": Chat_user_name_list})
    else:
        return HttpResponseRedirect("/Farshtore/login")


@csrf_exempt
def Save_Comment_Product(request, Message, Chat_Code, Product_Code, Message_Date, Rate):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            Find = Product_Comment.objects.filter(user_Id=user_st["User"].id, Product_Code=Product_Code).all()
            if Find.exists():
                return HttpResponse("Exist")

            elif Rate == "undefined":
                return HttpResponse("Empty")

            elif Find.exists():
                Save_data = Product_Comment(Message=str(Message), Chat_Code=Chat_Code, Product_Code=Product_Code,
                                            user_Id=user_st["User"].id,
                                            Rate=Rate, Date=Message_Date)
                Save_data.save()
                return HttpResponse("Not")

            else:
                Save_data = Product_Comment(Message=str(Message), Chat_Code=Chat_Code, Product_Code=Product_Code,
                                            user_Id=user_st["User"].id,
                                            Rate=Rate, Date=Message_Date)
                Save_data.save()
                return HttpResponse("True")
        else:
            return HttpResponseRedirect("/Farshtore/404")

    else:
        return HttpResponseRedirect("/Farshtore/login")


@csrf_exempt
def Load_Comment_Product(request, Chat_Code):
    if request.method == "POST":
        All_Comment = Product_Comment.objects.filter(Chat_Code=Chat_Code).all()
        if All_Comment.exists():
            Read_Comment = serializers.serialize("json", All_Comment)
            return HttpResponse(Read_Comment)
        else:
            return HttpResponse("False")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Save_Seller_Result(request, Seller_Result):
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":

            Legal = Seller_Legal.objects.all()
            Genuine = Seller_Genuine.objects.all()
            Support = Supporter.objects.all()
            Users = User_Save.objects.all()

            My_Id = []

            User_Ids = max(obj.Id for obj in Users) if Users else 0
            My_Id.append(User_Ids)
            Support_Ids = max(obj.Id for obj in Support) if Support else 0
            My_Id.append(Support_Ids)

            Legal_Ids = max(obj.Seller_Id for obj in Legal) if Legal else 0
            My_Id.append(Legal_Ids)
            Genuine_Ids = max(obj.Seller_Id for obj in Genuine) if Genuine else 0
            My_Id.append(Genuine_Ids)

            Add_Id = max(My_Id) + 1

            S_Genuine = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address, State="Login").first()

            S_Legal = Seller_Legal.objects.filter(Seller_IpAddress=ip_address, State="Login").first()
            S_Id = ""
            if S_Legal:
                S_Id = S_Legal.Seller_Id

            elif S_Genuine:
                S_Id = S_Genuine.Seller_Id
            try:
                S_Search_Id = User.objects.filter(id=S_Id).first()
                if S_Search_Id:
                    if Seller_Result == "حقوقی":
                        Seller_Type = "Legal"
                    else:
                        Seller_Type = "Genuine"
                    return HttpResponseRedirect("/Farshtore/Login_Seller/" + Seller_Type)
            except:
                if Seller_Result == "حقیقی":
                    Search_Genuine = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address).all()
                    if not Search_Genuine.exists():
                        Search_Legal = Seller_Legal.objects.filter(Seller_IpAddress=ip_address).all()
                        if Search_Legal.exists():
                            Search_Legal.delete()
                            Save_Result = Seller_Genuine(Seller_Id=Add_Id, Seller_IpAddress=ip_address)
                            Save_Result.save()
                            return HttpResponse("DeleteAdd")
                        else:
                            Save_Result = Seller_Genuine(Seller_Id=Add_Id, Seller_IpAddress=ip_address)
                            Save_Result.save()
                            return HttpResponse("Add")
                    else:
                        return HttpResponse("exist")
                else:
                    Search_Legal = Seller_Legal.objects.filter(Seller_IpAddress=ip_address).all()
                    if not Search_Legal.exists():
                        Search_Genuine = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address).all()
                        if Search_Genuine.exists():

                            Search_Genuine.delete()
                            Save_Result = Seller_Legal(Seller_Id=Add_Id, Seller_IpAddress=ip_address)
                            Save_Result.save()
                            return HttpResponse("DeleteAdd")
                        else:
                            Save_Result = Seller_Legal(Seller_Id=Add_Id, Seller_IpAddress=ip_address)
                            Save_Result.save()
                            return HttpResponse("Add")
                    else:
                        return HttpResponse("exist")
        else:
            return HttpResponseRedirect("/Farshtore/404")

    else:
        return HttpResponseRedirect("/Farshtore/login")


def Save_Seller_Genuine_Info(request, num_res):
    if request.method == "POST":
        forms = Seller_Genuine_Form(request.POST)
        if forms.is_valid():
            Search_Info = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address).first()
            if num_res == "Card":
                if Search_Info.Shaba_Number != 0:
                    Search_Info.Shaba_Number = 0

                    Search_Info.National_Code = forms.data["National_Code"]
                    Search_Info.Cart_Number = str(forms.data["Number_Sh"])
                    Search_Info.Shop_Name = forms.data["ShopName"]
                else:
                    Search_Info.National_Code = forms.data["National_Code"]
                    Search_Info.Cart_Number = "0"
                    Search_Info.Shop_Name = forms.data["ShopName"]

                Search_Info.save()
                return HttpResponse("Card")

            elif num_res == "Shaba":
                if Search_Info.Cart_Number != 0:
                    Search_Info.Cart_Number = 0
                    Search_Info.National_Code = forms.data["National_Code"]
                    Search_Info.Shaba_Number = forms.data["Number_Sh"]
                    Search_Info.Shop_Name = forms.data["ShopName"]
                else:
                    Search_Info.National_Code = forms.data["National_Code"]
                    Search_Info.Shaba_Number = "0"
                    Search_Info.Shop_Name = forms.data["ShopName"]

                Search_Info.save()
                return HttpResponse("Shaba")
        else:
            return HttpResponse("False")
    else:
        return HttpResponseRedirect("/Farshtore/404")


def Save_Seller_Legal_Info(request):
    if request.method == "POST":
        forms = Seller_Legal_Form(request.POST)
        if forms.is_valid():

            Search_Info = Seller_Legal.objects.filter(Seller_IpAddress=ip_address).all()
            if Search_Info.exists():
                Save_Info = Seller_Legal.objects.filter(Seller_IpAddress=ip_address).first()
                Save_Info.Company_Name = forms.data["Company_Name"]
                Save_Info.Company_Type = forms.data["Company_Type"]
                Save_Info.Company_National_Code = forms.data["Company_National_Code"]
                Save_Info.Economic_Code_Company = forms.data["Company_Economic_Code"]
                Save_Info.Shaba_number = forms.data["Shaba_Number"]
                Save_Info.Signatory = forms.data["Signatory"]
                Save_Info.Shop_Name = forms.data["ShopName"]
                Save_Info.save()
            else:
                Save_Result = Seller_Legal(Seller_IpAddress=ip_address)
                Save_Result.save()
                Save_New_Info = Seller_Legal.objects.filter(Seller_IpAddress=ip_address).first()
                Save_New_Info.Company_Name = forms.data["Company_Name"]
                Save_New_Info.Company_Type = forms.data["Company_Type"]
                Save_New_Info.Company_National_Code = forms.data["Company_National_Code"]
                Save_New_Info.Economic_Code_Company = forms.data["Company_Economic_Code"]
                Save_New_Info.Shaba_number = forms.data["Shaba_Number"]
                Save_New_Info.Signatory = forms.data["Signatory"]
                Save_New_Info.Shop_Name = forms.data["ShopName"]
                Save_New_Info.save()

            return HttpResponse("True")
        else:
            return HttpResponse("False")
    else:
        return HttpResponseRedirect("/Farshtore/404")


def Save_Seller_Account(request):
    forms = Logins_Seller(request.POST)
    if forms.is_valid():
        User_Seller = ""
        Legal = Seller_Legal.objects.filter(Seller_IpAddress=ip_address).all()
        Genuine = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address).all()
        if Legal.exists():
            if not Genuine.exists():
                User_Seller = forms.data["UserName"] + "_Seller_Legal"
            else:
                return HttpResponse("Two_Exist")

        if Genuine.exists():
            if not Legal.exists():
                User_Seller = forms.data["UserName"] + "_Seller_Genuine"
            else:
                return HttpResponse("Two_Exist")

        Search = User.objects.filter(username=User_Seller).all()
        if Search.exists():
            return HttpResponse("Exist")
        else:
            Legal = Seller_Legal.objects.all()
            Genuine = Seller_Genuine.objects.all()
            Support = Supporter.objects.all()
            Users = User_Save.objects.all()

            My_Id = []

            User_Ids = max(obj.Id for obj in Users) if Users else 0
            My_Id.append(User_Ids)
            Support_Ids = max(obj.Id for obj in Support) if Support else 0
            My_Id.append(Support_Ids)

            Legal_Ids = max(obj.Seller_Id for obj in Legal) if Legal else 0
            My_Id.append(Legal_Ids)
            Genuine_Ids = max(obj.Seller_Id for obj in Genuine) if Genuine else 0
            My_Id.append(Genuine_Ids)

            Add_Id = max(My_Id) + 1

            us = User.objects.create_user(id=Add_Id, username=User_Seller, password=forms.data["Password"],
                                          first_name=forms.data["Name"],
                                          last_name=forms.data["Family"], email=forms.data["Email"])
            us.save()

        User_Search = User.objects.filter(username=User_Seller).first()
        Seller_Id = User_Search.id

        if Legal.exists():
            Edit_Legal = Seller_Legal.objects.filter(Seller_IpAddress=ip_address).first()
            Edit_Legal.Seller_Id = Seller_Id
            Edit_Legal.password = forms.data["Password"]
            Edit_Legal.Phone = forms.data["Phone"]
            Edit_Legal.State = "Login"
            Edit_Legal.save()
            try:
                Delete_Legal = Seller_Legal.objects.exclude(Seller_Id=Seller_Id).first()
                Delete_Legal.delete()
            except:
                pass

        elif Genuine.exists():
            Edit_Genuine = Seller_Genuine.objects.filter(Seller_IpAddress=ip_address).first()
            Edit_Genuine.Seller_Id = Seller_Id
            Edit_Genuine.password = forms.data["Password"]
            Edit_Genuine.Phone = forms.data["Phone"]
            Edit_Genuine.State = "Login"
            Edit_Genuine.save()
            try:
                Delete_Genuine = Seller_Genuine.objects.exclude(Seller_Id=Seller_Id).first()
                Delete_Genuine.delete()
            except:
                pass

        user = authenticate(request, username=User_Seller, password=forms.data["Password"])
        if user is not None:
            login(request, user)
            user_st = UserAuth().StateLogin(request)
            User_Id = user_st["User"].id

            return HttpResponse(str(User_Id))
        else:
            return HttpResponse("Exist")


def add_Product_database(request, txt_sort, My_Dict):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            form = Product(request.POST, request.FILES)
            Dict = json.loads(My_Dict)
            if form.is_valid():
                yesterday = datetime.now() - timedelta(0)

                Time = jdatetime.fromgregorian(day=yesterday.day, month=yesterday.month,
                                               year=yesterday.year).strftime("%Y/%m/%d")

                Product_Code = random.randint(0, 100000)
                Chat_Code = random.randint(0, 100000)
                Title = form.data["Product_Title"]
                Search_Product = Add_Product.objects.filter(
                    Q(Product_Code=Product_Code) | Q(Chat_Code=Chat_Code)).all()
                if Search_Product.exists():
                    return HttpResponse("Problem")
                else:
                    Discount = int(form.data["Product_Price"]) * int(form.data["Product_Price_Discount"]) / 100
                    Price_Final = int(form.data["Product_Price"]) - Discount
                    try:
                        Save_data = Add_Product(Product_Code=Product_Code, Product_Title=Title,
                                                Product_Caption=form.data["Product_Caption"],
                                                Product_Price=int(form.data["Product_Price"]),
                                                Product_Price_Discount=int(form.data["Product_Price_Discount"]),
                                                Product_Price_Final=int(Price_Final),
                                                Product_Type=txt_sort, Chat_Code=Chat_Code,
                                                Product_Date=Time,
                                                user_Id=user_st["User"].id,
                                                )  # Product_Image=form.data["Product_Image"]
                        Save_data.save()
                        Search = Add_Product.objects.filter(Product_Code=Product_Code).all()
                        if Search.exists():
                            Search_Sorts = Add_Product.objects.filter(Product_Code=Product_Code).first()
                        else:
                            return HttpResponse("Problem")
                        if txt_sort == "دست باف":
                            Search_Sorts.Product_Brand = Dict["Brand_d"]
                            Search_Sorts.Product_Thread = Dict["Thread"]
                            Search_Sorts.Product_Rag = Dict["Rag"]
                            Search_Sorts.Product_Result = Dict["Result"]
                            Search_Sorts.Product_Size = Dict["C1"] + " در " + Dict["C2"] + " متر"

                        elif txt_sort == "ماشینی":
                            Search_Sorts.Product_Brand = Dict["Brand_m"]
                            Search_Sorts.Product_Shane = Dict["Shane"]
                            Search_Sorts.Product_Thread = Dict["Thread_m"]
                            Search_Sorts.Product_Size = Dict["C1"] + " در " + Dict["C2"] + " متر"

                        elif txt_sort == "نخ و نقشه کامپیوتری":
                            # Search_Sort.Product_pdf_File = Dict["pdf_File"]
                            Search_Sorts.Product_Thread = Dict["Thread_c"]
                            Search_Sorts.Product_Rag = Dict["Rag"]
                            Search_Sorts.Product_Size = Dict["C1"] + " در " + Dict["C2"] + " پیکسل"

                        elif txt_sort == "اکسسوری":
                            Search_Sorts.Product_Thread = Dict["Thread_Accss"]
                            Search_Sorts.Product_Accss_Type = Dict["Type_Accss"]
                            if Dict["Type_Accss"] == "کوسن":
                                Search_Sorts.Product_Size = Dict["C1"] + " در " + Dict["C2"] + " سانتی متر"

                        elif txt_sort == "تابلو فرش":
                            Search_Sorts.Product_Thread = Dict["Thread_Tablo"]
                            Search_Sorts.Product_Rag = Dict["Rag_Tablo"]
                            Search_Sorts.Product_Size = Dict["C1"] + " در " + Dict["C2"] + " سانتی متر"

                        elif txt_sort == "بیضی و گرد" or txt_sort == "کلاسیک" or \
                                txt_sort == "فانتزی" or txt_sort == "کودک":
                            if Dict["Un_Type"] == "دست باف":
                                Search_Sorts.Product_Un_Type_Sort = Dict["Un_Type"]
                                Search_Sorts.Product_Brand = Dict["Brand_d"]
                                Search_Sorts.Product_Thread = Dict["Thread"]
                                Search_Sorts.Product_Rag = Dict["Rag"]
                                Search_Sorts.Product_Result = Dict["Result"]
                                Search_Sorts.Product_Size = Dict["C1"] + " در " + Dict["C2"] + " متر"
                            elif Dict["Un_Type"] == "ماشینی":
                                Search_Sorts.Product_Un_Type_Sort = Dict["Un_Type"]
                                Search_Sorts.Product_Brand = Dict["Brand_m"]
                                Search_Sorts.Product_Shane = Dict["Shane"]
                                Search_Sorts.Product_Thread = Dict["Thread_m"]
                                Search_Sorts.Product_Size = Dict["C1"] + " در " + Dict["C2"] + " متر"

                        elif txt_sort == "گلیم":
                            Search_Sorts.Product_Thread = Dict["Thread_Glim"]
                            Search_Sorts.Product_Glim_Type = Dict["Type_Glim"]
                            Search_Sorts.Product_Size = Dict["C1"] + " در " + Dict["C2"] + " سانتی متر"

                        elif txt_sort == "۷۰۰ شانه" or txt_sort == "۱۰۰۰ شانه" or \
                                txt_sort == "۱۲۰۰ شانه" or txt_sort == "۱۵۰۰ شانه":
                            Search_Sorts.Product_Brand = Dict["Brand_m"]
                            Search_Sorts.Product_Thread = Dict["Thread_m"]
                            Search_Sorts.Product_Size = Dict["C1"] + " در " + Dict["C2"] + " متر"
                        Search_Sorts.save()
                    except:
                        pass

                return HttpResponse("True")
            else:
                print("iii")
                return HttpResponse("False")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Get_Id(request, Code, With):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            if Code != "undefined":
                Id = user_st["User"].id
                Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
                Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
                Support = Supporter.objects.filter(Id=Id).all()

                User_List = []
                With_List = []

                if Legal.exists() or Genuine.exists():
                    Codes = Chats.objects.filter(Chat_Code=Code, Chat_user2_Id=Id,
                                                 With=With).first()
                    if Codes:
                        return HttpResponse(Codes.Chat_user_Id)
                    else:
                        Codes = Chats.objects.filter(Chat_Code=Code, Chat_user_Id=Id,
                                                     With=With).first()
                        return HttpResponse(Codes.Chat_user2_Id)

                elif Support.exists():
                    Cod = Chats.objects.filter(Chat_Code=Code, Chat_user2_Id=Id,
                                               With="Support_Seller").first()
                    return HttpResponse(Cod.Chat_user_Id)
                else:

                    Cod = Chats.objects.filter(Chat_Code=Code, Chat_user2_Id=Id,
                                               With="User_Seller").first()
                    if not Cod:
                        Cod = Chats.objects.filter(Chat_Code=Code, Chat_user2_Id=Id,
                                                   With="User_Support").first()

                    return HttpResponse(Cod.Chat_user_Id)
            else:
                return HttpResponse("False")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Get_Id_User_Chat(request, Code, With):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            if Code != "undefined":
                Id = user_st["User"].id
                Codes = Chats.objects.filter(Chat_Code=Code, With=With, Chat_user_Id=Id).first()
                if Codes:
                    return HttpResponse(Codes.Chat_user2_Id)
                else:
                    Codes = Chats.objects.filter(Chat_Code=Code, With=With, Chat_user2_Id=Id).first()
                    return HttpResponse(Codes.Chat_user_Id)
            else:
                return HttpResponse("False")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Chat_Read_Seller(request, Chat_Code, Other):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            if Chat_Code != "undefined":
                Id = user_st["User"].id

                Visited = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller"),
                                               Chat_user2_Id=Other, Chat_user_Id=Id,
                                               Chat_Code=Chat_Code).first()

                Users = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                             Chat_user2_Id=Id, Chat_user_Id=Other,
                                             Chat_Code=Chat_Code).first()

                Visit_Sell_Supp = Chats.objects.filter(With="Seller_Support", Chat_user2_Id=Id,
                                                       Chat_user_Id=Other, Chat_Code=Chat_Code).first()

                if Visit_Sell_Supp:
                    chat_code = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user_Id=Other,
                                                     Chat_user2_Id=Id).all()

                    chat_messages = sorted(chat_code, key=lambda x: x.counter)
                    serialized_chat_messages = serializers.serialize("json", chat_messages)
                    return HttpResponse(serialized_chat_messages)

                if Visited:
                    Visited.Visit_Seller = 0
                    Visited.save()
                elif Users:
                    Users.Visit_User = 0
                    Users.save()

                else:
                    Visiteds = Chats.objects.filter(Q(With="User_Seller") | Q(With="Support_Seller") |
                                                    Q(With="Seller_Support"), Chat_user2_Id=Id,
                                                    Chat_user_Id=Other, Chat_Code=Chat_Code).first()
                    Visiteds.Visit_Seller = 0
                    Visiteds.save()

                chat_code = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user2_Id=Other,
                                                 Chat_user_Id=Id).all()

                chat_codes = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user2_Id=Id,
                                                  Chat_user_Id=Other).all()

                chat_messages = sorted(chat_code, key=lambda x: x.counter)
                serialized_chat_messages = serializers.serialize("json", chat_messages)

                if serialized_chat_messages == "[]":
                    chat_messages = sorted(chat_codes, key=lambda x: x.counter)
                    serialized_chat_messages = serializers.serialize("json", chat_messages)

                return HttpResponse(serialized_chat_messages)
            else:
                return HttpResponse("False")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Chat_Read_User(request, Chat_Code, Other):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            if Chat_Code != "undefined":
                Id = user_st["User"].id

                Visited = Chats.objects.filter(Q(With="User_Seller") | Q(With="User_Support"),
                                               Chat_user2_Id=Id, Chat_user_Id=Other,
                                               Chat_Code=Chat_Code).first()

                if Visited:
                    Visited.Visit_User = 0
                    Visited.save()

                chat_code = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user2_Id=Id,
                                                 Chat_user_Id=Other).all()

                chat_messages = sorted(chat_code, key=lambda x: x.counter)
                serialized_chat_messages = serializers.serialize("json", chat_messages)
                return HttpResponse(serialized_chat_messages)
            else:
                return HttpResponse("False")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Chat_Read_Support(request, Chat_Code, Other):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            if Chat_Code != "undefined":
                Id = user_st["User"].id

                Visited = Chats.objects.filter(With="Support_Seller",
                                               Chat_user_Id=Id, Chat_user2_Id=Other,
                                               Chat_Code=Chat_Code).first()

                Visited2 = Chats.objects.filter(Q(With="Seller_Support"),
                                                Chat_user_Id=Other, Chat_user2_Id=Id,
                                                Chat_Code=Chat_Code).first()

                Visited3 = Chats.objects.filter(With="User_Support",
                                                Chat_user_Id=Id, Chat_user2_Id=Other,
                                                Chat_Code=Chat_Code).first()

                if Visited:
                    Visited.Visit_Support = 0
                    Visited.save()
                elif Visited2:
                    Visited2.Visit_Support = 0
                    Visited2.save()
                elif Visited3:
                    Visited3.Visit_Support = 0
                    Visited3.save()

                chat_code = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user2_Id=Id,
                                                 Chat_user_Id=Other).all()

                if not chat_code.exists():
                    chat_code = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user2_Id=Other,
                                                     Chat_user_Id=Id).all()

                chat_messages = sorted(chat_code, key=lambda x: x.counter)
                serialized_chat_messages = serializers.serialize("json", chat_messages)
                return HttpResponse(serialized_chat_messages)
            else:
                return HttpResponse("False")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Get_Id_Support(request, Chat_Code, With):
    if request.method == "POST":
        user_st = UserAuth().StateLogin(request)
        if user_st["State"]:
            if Chat_Code != "undefined":
                Id = user_st["User"].id
                Genuine = Seller_Genuine.objects.filter(Seller_Id=Id).all()
                Legal = Seller_Legal.objects.filter(Seller_Id=Id).all()
                Support = Supporter.objects.filter(Id=Id).all()

                if Legal.exists() or Genuine.exists():
                    Codes = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user2_Id=Id).first()
                    return HttpResponse(Codes.Chat_user_Id)

                elif Support.exists():
                    Cod = Chats.objects.filter(Chat_Code=Chat_Code, Chat_user2_Id=Id,
                                               With="Support_Seller").first()
                    if not Cod:
                        Cod = Chats.objects.filter(With=With, Chat_Code=Chat_Code,
                                                   Chat_user_Id=Id).first()
                        return HttpResponse(Cod.Chat_user2_Id)
                    else:
                        return HttpResponse(Cod.Chat_user_Id)
            else:
                return HttpResponse("False")
        else:
            return HttpResponseRedirect("/Farshtore/login")
    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Save_Count(request, Product_Code, func):
    print(Product_Code)
    user_st = UserAuth().StateLogin(request)
    if user_st["State"]:
        if request.method == "POST":
            Search_Product_Code = Product_Order.objects.filter(Product_Code=Product_Code,
                                                               user_Id=user_st["User"].id).first()
            if func == "Minus":
                Search_Product_Code.Product_Count -= 1
            elif func == "Incrase":
                Search_Product_Code.Product_Count += 1

            Search_Product_Code.save()
            return HttpResponse("True")
        else:
            return HttpResponseRedirect("/Farshtore/404")
    else:
        return HttpResponseRedirect("/Farshtore/login")


def Admins(request):
    return HttpResponseRedirect("/Farshtore/Admin/Admin_Dashboard")


def Admin(request):
    import jdatetime
    from jdatetime import datetime as jalali_datetime

    dict_list = []
    today = jdatetime.date.today()
    Order = Order_Complete.objects.filter(Date=Times).all()

    View = User_View.objects.filter(Date=Times).all()

    Register = User.objects.all()
    for item in Register:
        dt_obj = datetime.fromisoformat(str(item.date_joined))
        jalali_date = jalali_datetime.fromgregorian(date=dt_obj).date()

        dict_list.append({
            "fields": {
                "Id": item.id,
                "Date": jalali_date
            }
        })
    Register = [item for item in dict_list if item['fields']['Date'] == today]

    Likes = Like.objects.filter(Date=Times).all()

    return render(request=request, template_name="Admin_Dashboard.html",
                  context={"Active1": "active", "Order": len(Order), "View": len(View),
                           "Register": len(Register), "Likes": len(Likes)})


def Admin_Table(request):
    return render(request=request, template_name="Admin_Table.html", context={"Active2": "active"})


@csrf_exempt
def Admin_User_Info(request, function):

    import jdatetime
    from jdatetime import datetime as jalali_datetime, timedelta

    def custom(day):
        Day = day
        days = [date.replace('-', '/') for date in day]
        dict_list = []
        MyList_Order = []
        MyList_View = []
        MyList_Like = []
        for day in days:
            MyList_Order.append(Order_Complete.objects.filter(Date=day).all())

            MyList_View.append(User_View.objects.filter(Date=day).all())

            MyList_Like.append(Like.objects.filter(Date=day).all())

        Order_List = []
        for items in MyList_Order:
            if items.exists():
                Order_List.append(items)

        View_List = []
        for items in MyList_Order:
            if items.exists():
                View_List.append(items)

        seen = set()
        Likes_List = []
        for itm in MyList_Like:
            if itm.exists() and itm not in seen:
                seen.add(itm)
                Likes_List.append(itm)

        total_count = sum(len(queryset) for queryset in Likes_List)

        Register = User.objects.all()
        for item in Register:
            dt_obj = datetime.fromisoformat(str(item.date_joined))
            jalali_date = jalali_datetime.fromgregorian(date=dt_obj).date()
            dict_list.append({
                "fields": {
                    "Id": item.id,
                    "Date": jalali_date
                }
            })
        Like_List = []
        for Days in Day:
            day_date = jdatetime.datetime.strptime(Days, '%Y-%m-%d').date()
            Register = [item for item in dict_list if item['fields']['Date'] == day_date]
            Like_List.append(Register)

        Like_Count = sum(len(sublist) for sublist in Like_List)

        data = {
            "Order": len(Order_List),
            "View": len(View_List),
            "Register": Like_Count,
            "Likes": total_count
        }
        return data

    if "custom" in function:
        from jdatetime import date as jdate, timedelta

        date_str = str(function)

        parts = date_str.split(".")

        date1, date2 = parts[1:]

        dt1 = jdate(int(date1.split('-')[2]), int(date1.split('-')[1]), int(date1.split('-')[0]))
        dt2 = jdate(int(date2.split('-')[2]), int(date2.split('-')[1]), int(date2.split('-')[0]))

        dates = [dt1]
        while dates[-1] < dt2:
            dates.append(dates[-1] + timedelta(days=1))

        formatted_dates = [f"{dt.year}-{dt.month:02}-{dt.day:02}" for dt in dates]
        Info = custom(formatted_dates)
        return JsonResponse(Info)

    if function == "today":
        dict_list = []
        today = jdatetime.date.today()
        Order = Order_Complete.objects.filter(Date=Times).all()

        View = User_View.objects.filter(Date=Times).all()

        Register = User.objects.all()
        for item in Register:
            dt_obj = datetime.fromisoformat(str(item.date_joined))
            jalali_date = jalali_datetime.fromgregorian(date=dt_obj).date()

            dict_list.append({
                "fields": {
                    "Id": item.id,
                    "Date": jalali_date
                }
            })

        Register = [item for item in dict_list if item['fields']['Date'] == today]

        Likes = Like.objects.filter(Date=Times).all()

        data = {
            "Order": len(Order),
            "View": len(View),
            "Register": len(Register),
            "Likes": len(Likes)
        }
        return JsonResponse(data)

    if function == "Yesterday":

        dict_list = []
        yesterday = jdatetime.date.today() - timedelta(1)
        date = datetime.strptime(str(yesterday), "%Y-%m-%d")
        date_obj = datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
        date = date_obj.strftime("%Y/%m/%d")

        Order = Order_Complete.objects.filter(Date=date).all()

        View = User_View.objects.filter(Date=date).all()

        Register = User.objects.all()
        for item in Register:
            dt_obj = datetime.fromisoformat(str(item.date_joined))
            jalali_date = jalali_datetime.fromgregorian(date=dt_obj).date()

            dict_list.append({
                "fields": {
                    "Id": item.id,
                    "Date": jalali_date
                }
            })

        Register = [item for item in dict_list if item['fields']['Date'] == yesterday]

        Likes = Like.objects.filter(Date=date).all()

        data = {
            "Order": len(Order),
            "View": len(View),
            "Register": len(Register),
            "Likes": len(Likes)
        }
        return JsonResponse(data)

    if function == "last_week":

        def lasts_day(days):
            from datetime import datetime, timedelta
            from jdatetime import datetime as jdatetime

            # Get the current date in Gregorian calendar
            today = datetime.today()

            # Get the dates of the last week
            last_week_dates = [(today - timedelta(days=i)).date() for i in range(6, -1, -1)]

            # Convert the dates to Persian calendar
            persian_dates = [jdatetime.fromgregorian(date=day).strftime("%Y-%m-%d") for day in last_week_dates]
            return persian_dates

        day = lasts_day(7)
        Day = day
        days = [date.replace('-', '/') for date in day]
        dict_list = []
        MyList_Order = []
        MyList_View = []
        MyList_Like = []
        for day in days:
            MyList_Order.append(Order_Complete.objects.filter(Date=day).all())

            MyList_View.append(User_View.objects.filter(Date=day).all())

            MyList_Like.append(Like.objects.filter(Date=day).all())

        Order_List = []
        for items in MyList_Order:
            if items.exists():
                Order_List.append(items)

        View_List = []
        for items in MyList_Order:
            if items.exists():
                View_List.append(items)

        seen = set()
        Likes_List = []
        for itm in MyList_Like:
            if itm.exists() and itm not in seen:
                seen.add(itm)
                Likes_List.append(itm)

        total_count = sum(len(queryset) for queryset in Likes_List)

        Register = User.objects.all()
        for item in Register:
            dt_obj = datetime.fromisoformat(str(item.date_joined))
            jalali_date = jalali_datetime.fromgregorian(date=dt_obj).date()
            dict_list.append({
                "fields": {
                    "Id": item.id,
                    "Date": jalali_date
                }
            })
        Like_List = []
        for Days in Day:
            day_date = jdatetime.datetime.strptime(Days, '%Y-%m-%d').date()
            Register = [item for item in dict_list if item['fields']['Date'] == day_date]
            Like_List.append(Register)

        Like_Count = sum(len(sublist) for sublist in Like_List)

        data = {
            "Order": len(Order_List),
            "View": len(View_List),
            "Register": Like_Count,
            "Likes": total_count
        }
        return JsonResponse(data)

    if function == "last_30day":

        def lasts_day(days):
            from datetime import datetime, timedelta
            from jdatetime import datetime as jdatetime

            # Get the current date in Gregorian calendar
            today = datetime.today()

            # Get the dates of the last week
            last_week_dates = [(today - timedelta(days=i)).date() for i in range(29, -1, -1)]

            # Convert the dates to Persian calendar
            persian_dates = [jdatetime.fromgregorian(date=day).strftime("%Y-%m-%d") for day in last_week_dates]
            return persian_dates

        day = lasts_day(7)
        Day = day
        days = [date.replace('-', '/') for date in day]
        dict_list = []
        MyList_Order = []
        MyList_View = []
        MyList_Like = []
        for day in days:
            MyList_Order.append(Order_Complete.objects.filter(Date=day).all())

            MyList_View.append(User_View.objects.filter(Date=day).all())

            MyList_Like.append(Like.objects.filter(Date=day).all())

        Order_List = []
        for items in MyList_Order:
            if items.exists():
                Order_List.append(items)

        View_List = []
        for items in MyList_Order:
            if items.exists():
                View_List.append(items)

        seen = set()
        Likes_List = []
        for itm in MyList_Like:
            if itm.exists() and itm not in seen:
                seen.add(itm)
                Likes_List.append(itm)

        total_count = sum(len(queryset) for queryset in Likes_List)

        Register = User.objects.all()
        for item in Register:
            dt_obj = datetime.fromisoformat(str(item.date_joined))
            jalali_date = jalali_datetime.fromgregorian(date=dt_obj).date()
            dict_list.append({
                "fields": {
                    "Id": item.id,
                    "Date": jalali_date
                }
            })
        Like_List = []
        for Days in Day:
            day_date = jdatetime.datetime.strptime(Days, '%Y-%m-%d').date()
            Register = [item for item in dict_list if item['fields']['Date'] == day_date]
            Like_List.append(Register)

        Like_Count = sum(len(sublist) for sublist in Like_List)

        data = {
            "Order": len(Order_List),
            "View": len(View_List),
            "Register": Like_Count,
            "Likes": total_count
        }
        return JsonResponse(data)

    if function == "this_month":

        def this_month():
            import jdatetime

            MyList = []
            # Get the current date
            current_date = jdatetime.datetime.now()

            # Get the month and year of the current Jalali date
            month = current_date.month
            year = current_date.year

            # Create a date range for the current month
            date_range = [jdatetime.datetime(year, month, day) for day in range(1, 32)]

            # Print the Jalali dates for the current month
            for date in date_range:
                try:
                    MyList.append(date.strftime("%Y-%m-%d"))
                except ValueError:
                    break
            return MyList

        day = this_month()
        Day = day
        days = [date.replace('-', '/') for date in day]
        dict_list = []
        MyList_Order = []
        MyList_View = []
        MyList_Like = []
        for day in days:
            MyList_Order.append(Order_Complete.objects.filter(Date=day).all())

            MyList_View.append(User_View.objects.filter(Date=day).all())

            MyList_Like.append(Like.objects.filter(Date=day).all())

        Order_List = []
        for items in MyList_Order:
            if items.exists():
                Order_List.append(items)

        View_List = []
        for items in MyList_Order:
            if items.exists():
                View_List.append(items)

        seen = set()
        Likes_List = []
        for itm in MyList_Like:
            if itm.exists() and itm not in seen:
                seen.add(itm)
                Likes_List.append(itm)

        total_count = sum(len(queryset) for queryset in Likes_List)

        Register = User.objects.all()
        for item in Register:
            dt_obj = datetime.fromisoformat(str(item.date_joined))
            jalali_date = jalali_datetime.fromgregorian(date=dt_obj).date()
            dict_list.append({
                "fields": {
                    "Id": item.id,
                    "Date": jalali_date
                }
            })
        Like_List = []
        for Days in Day:
            day_date = jdatetime.datetime.strptime(Days, '%Y-%m-%d').date()
            Register = [item for item in dict_list if item['fields']['Date'] == day_date]
            Like_List.append(Register)

        Like_Count = sum(len(sublist) for sublist in Like_List)

        data = {
            "Order": len(Order_List),
            "View": len(View_List),
            "Register": Like_Count,
            "Likes": total_count
        }
        return JsonResponse(data)

    if function == "last_month":

        def last_month():
            import jdatetime

            MyList = []
            # Get the current date
            current_date = jdatetime.datetime.now()

            # Get the previous month and year
            if current_date.month == 1:
                previous_month = 12
                previous_year = current_date.year - 1
            else:
                previous_month = current_date.month - 1
                previous_year = current_date.year

            # Create a date range for the previous month
            date_range = [jdatetime.datetime(previous_year, previous_month, day) for day in range(1, 32)]

            # Print the Jalali dates for the previous month
            for date in date_range:
                try:
                    MyList.append(date.strftime("%Y-%m-%d"))
                except ValueError:
                    break
            return MyList

        day = last_month()
        Day = day
        days = [date.replace('-', '/') for date in day]
        dict_list = []
        MyList_Order = []
        MyList_View = []
        MyList_Like = []
        for day in days:
            MyList_Order.append(Order_Complete.objects.filter(Date=day).all())

            MyList_View.append(User_View.objects.filter(Date=day).all())

            MyList_Like.append(Like.objects.filter(Date=day).all())

        Order_List = []
        for items in MyList_Order:
            if items.exists():
                Order_List.append(items)

        View_List = []
        for items in MyList_Order:
            if items.exists():
                View_List.append(items)

        seen = set()
        Likes_List = []
        for itm in MyList_Like:
            if itm.exists() and itm not in seen:
                seen.add(itm)
                Likes_List.append(itm)

        total_count = sum(len(queryset) for queryset in Likes_List)

        Register = User.objects.all()
        for item in Register:
            dt_obj = datetime.fromisoformat(str(item.date_joined))
            jalali_date = jalali_datetime.fromgregorian(date=dt_obj).date()
            dict_list.append({
                "fields": {
                    "Id": item.id,
                    "Date": jalali_date
                }
            })
        Like_List = []
        for Days in Day:
            day_date = jdatetime.datetime.strptime(Days, '%Y-%m-%d').date()
            Register = [item for item in dict_list if item['fields']['Date'] == day_date]
            Like_List.append(Register)

        Like_Count = sum(len(sublist) for sublist in Like_List)

        data = {
            "Order": len(Order_List),
            "View": len(View_List),
            "Register": Like_Count,
            "Likes": total_count
        }
        return JsonResponse(data)

@csrf_exempt
def Admin_Order_Complete(request, user_Id, function):
    if request.method == "POST":
        import jdatetime
        from jdatetime import datetime as jalali_datetime, timedelta

        def custom(day):
            Day = day
            days = [date.replace('-', '/') for date in day]
            if int(user_Id) == 0:
                MyList = []
                for date in days:
                    Product = Order_Complete.objects.filter(Date=date).all()
                    MyList.append(Product)

                flattened_queryset = itertools.chain(*MyList)
                Prdct = serializers.serialize("json", flattened_queryset)
                return Prdct

        if "custom" in function:
            from jdatetime import date as jdate, timedelta

            date_str = str(function)

            if date_str == "custom":
                Find_User = User.objects.filter(id=user_Id).first()
                User_Id = Find_User.username
                return HttpResponse(User_Id)

            parts = date_str.split(".")

            date1, date2 = parts[1:]

            dt1 = jdate(int(date1.split('-')[2]), int(date1.split('-')[1]), int(date1.split('-')[0]))
            dt2 = jdate(int(date2.split('-')[2]), int(date2.split('-')[1]), int(date2.split('-')[0]))

            dates = [dt1]
            while dates[-1] < dt2:
                dates.append(dates[-1] + timedelta(days=1))

            formatted_dates = [f"{dt.year}-{dt.month:02}-{dt.day:02}" for dt in dates]
            Info = custom(formatted_dates)
            return HttpResponse(Info)

        if function == "today":
            if int(user_Id) == 0:
                Product = Order_Complete.objects.filter(Date=Times).all()
                Prdct = serializers.serialize("json", Product)
                return HttpResponse(Prdct)
            else:
                print(user_Id)
                Find_User = User.objects.filter(id=user_Id).first()
                User_Id = Find_User.username
                return HttpResponse(User_Id)

        if function == "Yesterday":

            yesterday = jdatetime.date.today() - timedelta(1)
            date = datetime.strptime(str(yesterday), "%Y-%m-%d")
            date_obj = datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
            date = date_obj.strftime("%Y/%m/%d")

            if int(user_Id) == 0:
                Product = Order_Complete.objects.filter(Date=date).all()
                Prdct = serializers.serialize("json", Product)
                return HttpResponse(Prdct)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                User_Id = Find_User.username
                return HttpResponse(User_Id)

        if function == "last_week":

            def lasts_day(days):
                from datetime import datetime, timedelta
                from jdatetime import datetime as jdatetime

                today = datetime.today()

                # Get the dates of the last week
                last_week_dates = [(today - timedelta(days=i)).date() for i in range(6, -1, -1)]

                # Convert the dates to Persian calendar
                persian_dates = [jdatetime.fromgregorian(date=day).strftime("%Y-%m-%d") for day in last_week_dates]
                return persian_dates

            day = lasts_day(7)
            Day = day
            my_list = []
            days = [date.replace('-', '/') for date in day]
            if int(user_Id) == 0:
                MyList = []
                for date in days:
                    Product = Order_Complete.objects.filter(Date=date).all()
                    MyList.append(Product)

                flattened_queryset = itertools.chain(*MyList)
                Prdct = serializers.serialize("json", flattened_queryset)

                return HttpResponse(Prdct)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                User_Id = Find_User.username
                return HttpResponse(User_Id)

        if function == "last_30day":

            def lasts_day():
                from datetime import datetime, timedelta
                from jdatetime import datetime as jdatetime

                # Get the current date in Gregorian calendar
                today = datetime.today()

                # Get the dates of the last week
                last_week_dates = [(today - timedelta(days=i)).date() for i in range(29, -1, -1)]

                # Convert the dates to Persian calendar
                persian_dates = [jdatetime.fromgregorian(date=day).strftime("%Y-%m-%d") for day in last_week_dates]
                return persian_dates

            day = lasts_day()
            Day = day
            days = [date.replace('-', '/') for date in day]
            if int(user_Id) == 0:
                MyList = []
                for date in days:
                    Product = Order_Complete.objects.filter(Date=date).all()
                    MyList.append(Product)

                flattened_queryset = itertools.chain(*MyList)
                Prdct = serializers.serialize("json", flattened_queryset)

                return HttpResponse(Prdct)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                User_Id = Find_User.username
                return HttpResponse(User_Id)

        if function == "this_month":

            def this_month():
                import jdatetime

                MyList = []
                # Get the current date
                current_date = jdatetime.datetime.now()

                # Get the month and year of the current Jalali date
                month = current_date.month
                year = current_date.year

                # Create a date range for the current month
                date_range = [jdatetime.datetime(year, month, day) for day in range(1, 32)]

                # Print the Jalali dates for the current month
                for date in date_range:
                    try:
                        MyList.append(date.strftime("%Y-%m-%d"))
                    except ValueError:
                        break
                return MyList

            day = this_month()
            Day = day
            days = [date.replace('-', '/') for date in day]
            if int(user_Id) == 0:
                MyList = []
                for date in days:
                    Product = Order_Complete.objects.filter(Date=date).all()
                    MyList.append(Product)

                flattened_queryset = itertools.chain(*MyList)
                Prdct = serializers.serialize("json", flattened_queryset)

                return HttpResponse(Prdct)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                User_Id = Find_User.username
                return HttpResponse(User_Id)

        if function == "last_month":

            def last_month():
                import jdatetime

                MyList = []
                # Get the current date
                current_date = jdatetime.datetime.now()

                # Get the previous month and year
                if current_date.month == 1:
                    previous_month = 12
                    previous_year = current_date.year - 1
                else:
                    previous_month = current_date.month - 1
                    previous_year = current_date.year

                # Create a date range for the previous month
                date_range = [jdatetime.datetime(previous_year, previous_month, day) for day in range(1, 32)]

                # Print the Jalali dates for the previous month
                for date in date_range:
                    try:
                        MyList.append(date.strftime("%Y-%m-%d"))
                    except ValueError:
                        break
                return MyList

            day = last_month()
            Day = day
            days = [date.replace('-', '/') for date in day]
            if int(user_Id) == 0:
                MyList = []
                for date in days:
                    Product = Order_Complete.objects.filter(Date=date).all()
                    MyList.append(Product)

                flattened_queryset = itertools.chain(*MyList)
                Prdct = serializers.serialize("json", flattened_queryset)

                return HttpResponse(Prdct)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                User_Id = Find_User.username
                return HttpResponse(User_Id)


    else:
        return HttpResponseRedirect("/Farshtore/404")


@csrf_exempt
def Admin_buyed_product(request, user_Id, Product_Code, function):
    if request.method == "POST":
        import jdatetime
        from jdatetime import datetime as jalali_datetime, timedelta

        def custom(day):
            Day = day
            days = [date.replace('-', '/') for date in day]
            if int(user_Id) == 0:
                product_dict_list = []
                for date in days:
                    Product = Product_buyed.objects.filter(Date=date).all()
                    product_dict = list(Product.values())
                    product_dict = {d['Product_Code']: d for d in product_dict}.values()
                    product_dict_list.extend(list(product_dict))
                return JsonResponse(product_dict_list, safe=False)

        if "custom" in function:
            from jdatetime import date as jdate, timedelta

            date_str = str(function)

            if date_str == "custom":
                Find_User = User.objects.filter(id=user_Id).first()
                user_name = Find_User.username
                Find_Product = Add_Product.objects.filter(Product_Code=Product_Code).first()
                Users = User.objects.filter(id=Find_Product.user_Id).first()
                Seller_Name = f"{Users.first_name} {Users.last_name}"

                Count = Product_buyed.objects.filter(Product_Code=Product_Code).all()
                Count = len(Count)

                def DateTime():
                    from datetime import datetime, timedelta
                    import jdatetime

                    dt = datetime.strptime(Find_Product.Product_Date, '%Y-%m-%d %H:%M:%S.%f')
                    tomorrow = dt
                    return jdatetime.date.fromgregorian(day=tomorrow.day, month=tomorrow.month, year=tomorrow.year)

                shamsi_date = DateTime()
                dictionary = {
                    "fields": {
                        "user_name": user_name,
                        "Title": Find_Product.Product_Title,
                        "Price": Find_Product.Product_Price,
                        "Discount": Find_Product.Product_Price_Discount,
                        "Type": Find_Product.Product_Type,
                        "Date_Published": str(shamsi_date),
                        "Likes": Find_Product.Product_Likes,
                        "Views": Find_Product.Product_Visit,
                        "Seller_Name": Seller_Name,
                        "Buyed_Product_Count": Count
                    }
                }
                return JsonResponse(dictionary)

            parts = date_str.split(".")

            date1, date2 = parts[1:]

            dt1 = jdate(int(date1.split('-')[2]), int(date1.split('-')[1]), int(date1.split('-')[0]))
            dt2 = jdate(int(date2.split('-')[2]), int(date2.split('-')[1]), int(date2.split('-')[0]))

            dates = [dt1]
            while dates[-1] < dt2:
                dates.append(dates[-1] + timedelta(days=1))

            formatted_dates = [f"{dt.year}-{dt.month:02}-{dt.day:02}" for dt in dates]
            Info = custom(formatted_dates)
            print(Info)
            return HttpResponse(Info)

        if function == "today":
            MyList = []
            if int(user_Id) == 0:
                Product = Product_buyed.objects.filter(Date=Times).all()
                product_dict = list(Product.values())
                product_dict = {d['Product_Code']: d for d in product_dict}.values()
                return JsonResponse(list(product_dict), safe=False)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                user_name = Find_User.username
                Find_Product = Add_Product.objects.filter(Product_Code=Product_Code).first()
                Users = User.objects.filter(id=Find_Product.user_Id).first()
                Seller_Name = f"{Users.first_name} {Users.last_name}"

                Count = Product_buyed.objects.filter(Product_Code=Product_Code).all()
                Count = len(Count)

                def DateTime():

                    from datetime import datetime, timedelta
                    import jdatetime

                    dt = datetime.strptime(Find_Product.Product_Date, '%Y-%m-%d %H:%M:%S.%f')
                    tomorrow = dt
                    return jdatetime.date.fromgregorian(day=tomorrow.day, month=tomorrow.month, year=tomorrow.year)

                shamsi_date = DateTime()
                dictionary = {
                    "fields": {
                        "user_name": user_name,
                        "Title": Find_Product.Product_Title,
                        "Price": Find_Product.Product_Price,
                        "Discount": Find_Product.Product_Price_Discount,
                        "Type": Find_Product.Product_Type,
                        "Date_Published": str(shamsi_date),
                        "Likes": Find_Product.Product_Likes,
                        "Views": Find_Product.Product_Visit,
                        "Seller_Name": Seller_Name,
                        "Buyed_Product_Count": Count
                    }
                }
                return JsonResponse(dictionary)

        if function == "Yesterday":

            yesterday = jdatetime.date.today() - timedelta(1)
            date = datetime.strptime(str(yesterday), "%Y-%m-%d")
            date_obj = datetime.strptime(str(date), "%Y-%m-%d %H:%M:%S")
            date = date_obj.strftime("%Y/%m/%d")

            if int(user_Id) == 0:
                Product = Product_buyed.objects.filter(Date=date).all()
                product_dict = list(Product.values())
                product_dict = {d['Product_Code']: d for d in product_dict}.values()
                return JsonResponse(list(product_dict), safe=False)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                user_name = Find_User.username
                Find_Product = Add_Product.objects.filter(Product_Code=Product_Code).first()
                Users = User.objects.filter(id=Find_Product.user_Id).first()
                Seller_Name = f"{Users.first_name} {Users.last_name}"

                Count = Product_buyed.objects.filter(Product_Code=Product_Code).all()
                Count = len(Count)

                def DateTime():

                    from datetime import datetime, timedelta
                    import jdatetime

                    dt = datetime.strptime(Find_Product.Product_Date, '%Y-%m-%d %H:%M:%S.%f')
                    tomorrow = dt
                    return jdatetime.date.fromgregorian(day=tomorrow.day, month=tomorrow.month, year=tomorrow.year)

                shamsi_date = DateTime()
                dictionary = {
                    "fields": {
                        "user_name": user_name,
                        "Title": Find_Product.Product_Title,
                        "Price": Find_Product.Product_Price,
                        "Discount": Find_Product.Product_Price_Discount,
                        "Type": Find_Product.Product_Type,
                        "Date_Published": str(shamsi_date),
                        "Likes": Find_Product.Product_Likes,
                        "Views": Find_Product.Product_Visit,
                        "Seller_Name": Seller_Name,
                        "Buyed_Product_Count": Count
                    }
                }
                return JsonResponse(dictionary)

        if function == "last_week":

            def lasts_day(days):
                from datetime import datetime, timedelta
                from jdatetime import datetime as jdatetime

                today = datetime.today()

                # Get the dates of the last week
                last_week_dates = [(today - timedelta(days=i)).date() for i in range(6, -1, -1)]

                # Convert the dates to Persian calendar
                persian_dates = [jdatetime.fromgregorian(date=day).strftime("%Y-%m-%d") for day in last_week_dates]
                return persian_dates

            day = lasts_day(7)
            Day = day
            my_list = []
            days = [date.replace('-', '/') for date in day]
            if int(user_Id) == 0:
                product_dict_list = []
                for date in days:
                    Product = Product_buyed.objects.filter(Date=date).all()
                    product_dict = list(Product.values())
                    product_dict = {d['Product_Code']: d for d in product_dict}.values()
                    product_dict_list.extend(list(product_dict))
                return JsonResponse(product_dict_list, safe=False)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                user_name = Find_User.username
                Find_Product = Add_Product.objects.filter(Product_Code=Product_Code).first()
                Users = User.objects.filter(id=Find_Product.user_Id).first()
                Seller_Name = f"{Users.first_name} {Users.last_name}"

                Count = Product_buyed.objects.filter(Product_Code=Product_Code).all()
                Count = len(Count)

                def DateTime():

                    from datetime import datetime, timedelta
                    import jdatetime

                    dt = datetime.strptime(Find_Product.Product_Date, '%Y-%m-%d %H:%M:%S.%f')
                    tomorrow = dt
                    return jdatetime.date.fromgregorian(day=tomorrow.day, month=tomorrow.month, year=tomorrow.year)

                shamsi_date = DateTime()
                dictionary = {
                    "fields": {
                        "user_name": user_name,
                        "Title": Find_Product.Product_Title,
                        "Price": Find_Product.Product_Price,
                        "Discount": Find_Product.Product_Price_Discount,
                        "Type": Find_Product.Product_Type,
                        "Date_Published": str(shamsi_date),
                        "Likes": Find_Product.Product_Likes,
                        "Views": Find_Product.Product_Visit,
                        "Seller_Name": Seller_Name,
                        "Buyed_Product_Count": Count
                    }
                }
                return JsonResponse(dictionary)

        if function == "last_30day":

            def lasts_day():
                from datetime import datetime, timedelta
                from jdatetime import datetime as jdatetime

                # Get the current date in Gregorian calendar
                today = datetime.today()

                # Get the dates of the last week
                last_week_dates = [(today - timedelta(days=i)).date() for i in range(29, -1, -1)]

                # Convert the dates to Persian calendar
                persian_dates = [jdatetime.fromgregorian(date=day).strftime("%Y-%m-%d") for day in last_week_dates]
                return persian_dates

            day = lasts_day()
            Day = day
            days = [date.replace('-', '/') for date in day]
            if int(user_Id) == 0:
                product_dict_list = []
                for date in days:
                    Product = Product_buyed.objects.filter(Date=date).all()
                    product_dict = list(Product.values())
                    product_dict = {d['Product_Code']: d for d in product_dict}.values()
                    product_dict_list.extend(list(product_dict))
                return JsonResponse(product_dict_list, safe=False)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                user_name = Find_User.username
                Find_Product = Add_Product.objects.filter(Product_Code=Product_Code).first()
                Users = User.objects.filter(id=Find_Product.user_Id).first()
                Seller_Name = f"{Users.first_name} {Users.last_name}"

                Count = Product_buyed.objects.filter(Product_Code=Product_Code).all()
                Count = len(Count)

                def DateTime():

                    from datetime import datetime, timedelta
                    import jdatetime

                    dt = datetime.strptime(Find_Product.Product_Date, '%Y-%m-%d %H:%M:%S.%f')
                    tomorrow = dt
                    return jdatetime.date.fromgregorian(day=tomorrow.day, month=tomorrow.month, year=tomorrow.year)

                shamsi_date = DateTime()
                dictionary = {
                    "fields": {
                        "user_name": user_name,
                        "Title": Find_Product.Product_Title,
                        "Price": Find_Product.Product_Price,
                        "Discount": Find_Product.Product_Price_Discount,
                        "Type": Find_Product.Product_Type,
                        "Date_Published": str(shamsi_date),
                        "Likes": Find_Product.Product_Likes,
                        "Views": Find_Product.Product_Visit,
                        "Seller_Name": Seller_Name,
                        "Buyed_Product_Count": Count
                    }
                }
                return JsonResponse(dictionary)

        if function == "this_month":

            def this_month():
                import jdatetime

                MyList = []
                # Get the current date
                current_date = jdatetime.datetime.now()

                # Get the month and year of the current Jalali date
                month = current_date.month
                year = current_date.year

                # Create a date range for the current month
                date_range = [jdatetime.datetime(year, month, day) for day in range(1, 32)]

                # Print the Jalali dates for the current month
                for date in date_range:
                    try:
                        MyList.append(date.strftime("%Y-%m-%d"))
                    except ValueError:
                        break
                return MyList

            day = this_month()
            Day = day
            days = [date.replace('-', '/') for date in day]
            if int(user_Id) == 0:
                product_dict_list = []
                for date in days:
                    Product = Product_buyed.objects.filter(Date=date).all()
                    product_dict = list(Product.values())
                    product_dict = {d['Product_Code']: d for d in product_dict}.values()
                    product_dict_list.extend(list(product_dict))
                return JsonResponse(product_dict_list, safe=False)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                user_name = Find_User.username
                Find_Product = Add_Product.objects.filter(Product_Code=Product_Code).first()
                Users = User.objects.filter(id=Find_Product.user_Id).first()
                Seller_Name = f"{Users.first_name} {Users.last_name}"

                Count = Product_buyed.objects.filter(Product_Code=Product_Code).all()
                Count = len(Count)

                def DateTime():

                    from datetime import datetime, timedelta
                    import jdatetime

                    dt = datetime.strptime(Find_Product.Product_Date, '%Y-%m-%d %H:%M:%S.%f')
                    tomorrow = dt
                    return jdatetime.date.fromgregorian(day=tomorrow.day, month=tomorrow.month, year=tomorrow.year)

                shamsi_date = DateTime()
                dictionary = {
                    "fields": {
                        "user_name": user_name,
                        "Title": Find_Product.Product_Title,
                        "Price": Find_Product.Product_Price,
                        "Discount": Find_Product.Product_Price_Discount,
                        "Type": Find_Product.Product_Type,
                        "Date_Published": str(shamsi_date),
                        "Likes": Find_Product.Product_Likes,
                        "Views": Find_Product.Product_Visit,
                        "Seller_Name": Seller_Name,
                        "Buyed_Product_Count": Count
                    }
                }
                return JsonResponse(dictionary)

        if function == "last_month":

            def last_month():
                import jdatetime

                MyList = []
                # Get the current date
                current_date = jdatetime.datetime.now()

                # Get the previous month and year
                if current_date.month == 1:
                    previous_month = 12
                    previous_year = current_date.year - 1
                else:
                    previous_month = current_date.month - 1
                    previous_year = current_date.year

                # Create a date range for the previous month
                date_range = [jdatetime.datetime(previous_year, previous_month, day) for day in range(1, 32)]

                # Print the Jalali dates for the previous month
                for date in date_range:
                    try:
                        MyList.append(date.strftime("%Y-%m-%d"))
                    except ValueError:
                        break
                return MyList

            day = last_month()
            Day = day
            days = [date.replace('-', '/') for date in day]
            if int(user_Id) == 0:
                product_dict_list = []
                for date in days:
                    Product = Product_buyed.objects.filter(Date=date).all()
                    product_dict = list(Product.values())
                    product_dict = {d['Product_Code']: d for d in product_dict}.values()
                    product_dict_list.extend(list(product_dict))
                return JsonResponse(product_dict_list, safe=False)
            else:
                Find_User = User.objects.filter(id=user_Id).first()
                user_name = Find_User.username
                Find_Product = Add_Product.objects.filter(Product_Code=Product_Code).first()
                Users = User.objects.filter(id=Find_Product.user_Id).first()
                Seller_Name = f"{Users.first_name} {Users.last_name}"

                Count = Product_buyed.objects.filter(Product_Code=Product_Code).all()
                Count = len(Count)

                def DateTime():

                    from datetime import datetime, timedelta
                    import jdatetime

                    dt = datetime.strptime(Find_Product.Product_Date, '%Y-%m-%d %H:%M:%S.%f')
                    tomorrow = dt
                    return jdatetime.date.fromgregorian(day=tomorrow.day, month=tomorrow.month, year=tomorrow.year)

                shamsi_date = DateTime()
                dictionary = {
                    "fields": {
                        "user_name": user_name,
                        "Title": Find_Product.Product_Title,
                        "Price": Find_Product.Product_Price,
                        "Discount": Find_Product.Product_Price_Discount,
                        "Type": Find_Product.Product_Type,
                        "Date_Published": str(shamsi_date),
                        "Likes": Find_Product.Product_Likes,
                        "Views": Find_Product.Product_Visit,
                        "Seller_Name": Seller_Name,
                        "Buyed_Product_Count": Count
                    }
                }
                return JsonResponse(dictionary)


    else:
        return HttpResponseRedirect("/Farshtore/404")