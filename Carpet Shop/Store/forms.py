from django import forms
from django.forms import ModelForm
from .models import Add_Product

class Login(forms.Form):
    def __init__(self,*args,**kwargs):
        super(Login,self).__init__(*args,**kwargs)
        for item in Login.visible_fields(self):
            item.field.widget.attrs["class"] = ""

    UserName = forms.CharField(required=True,label="نام کاربری",widget=forms.TextInput(attrs={'style': 'text-align: left;'}))
    Password = forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput(attrs={'style': 'text-align: left;'}))

class Login_Support(forms.Form):
    def __init__(self,*args,**kwargs):
        super(Login_Support,self).__init__(*args,**kwargs)
        for item in Login_Support.visible_fields(self):
            item.field.widget.attrs["class"] = ""

    UserName = forms.CharField(required=True,label="نام کاربری",widget=forms.TextInput(attrs={'style': 'text-align: left;'}))
    Password = forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput(attrs={'style': 'text-align: left;'}))

class Logins_Seller_Form(forms.Form):
    def __init__(self,*args,**kwargs):
        super(Logins_Seller_Form,self).__init__(*args,**kwargs)
        for item in Logins_Seller_Form.visible_fields(self):
            item.field.widget.attrs["class"] = ""

    UserName = forms.CharField(required=True,label="نام کاربری",widget=forms.TextInput(attrs={'style': 'text-align: left;margin: 2rem 0;'}))
    Password = forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput(attrs={'style': 'text-align: left;margin: 2rem 0;'}))


class Register(forms.Form):
    def __init__(self,*args,**kwargs):
        super(Register,self).__init__(*args,**kwargs)
        for item in Register.visible_fields(self):
            item.field.widget.attrs["class"] = ""

    Name = forms.CharField(required=True,label="نام:", max_length=200, min_length=3, help_text="مثال: ایلیا",error_messages={"required": "نام خود را صحیح وارد کنید"})

    Family = forms.CharField(required=True,label="نام خانوادگی:", max_length=200, min_length=3, help_text="مثال:ابوطالبی",error_messages={"required": "نام خانوادگی خود را صحیح وارد کنید"})

    UserName = forms.CharField(required=True,label="نام کاربری:", max_length=200, min_length=3, help_text="مثال: iliaab85",error_messages={"required": "نام کاربری حود را صحیح وارد کنید"},widget=forms.TextInput(attrs={'style': 'text-align:left;'}))

    Phone = forms.CharField(required=True,label="شماره تلفن:", max_length=15, min_length=3,error_messages={"required": "شماره تماس الزامی می باشد"},widget=forms.TextInput(attrs={'style': 'text-align:left;'}))

    Email = forms.EmailField(required=True,label="ایمیل:", widget=forms.EmailInput(attrs={'style': 'text-align:left;'}))

    Password = forms.CharField(required=True,label="گذرواژه:", widget=forms.PasswordInput(attrs={'style': 'text-align: left;'}))

class Register_Support(forms.Form):
    def __init__(self,*args,**kwargs):
        super(Register_Support,self).__init__(*args,**kwargs)
        for item in Register_Support.visible_fields(self):
            item.field.widget.attrs["class"] = ""

    Name = forms.CharField(required=True,label="نام:", max_length=200, min_length=3, help_text="مثال: ایلیا",error_messages={"required": "نام خود را صحیح وارد کنید"})

    Family = forms.CharField(required=True,label="نام خانوادگی:", max_length=200, min_length=3, help_text="مثال:ابوطالبی",error_messages={"required": "نام خانوادگی خود را صحیح وارد کنید"})

    UserName = forms.CharField(required=True,label="نام کاربری:", max_length=200, min_length=3, help_text="مثال: iliaab85",error_messages={"required": "نام کاربری حود را صحیح وارد کنید"},widget=forms.TextInput(attrs={'style': 'text-align:left;'}))

    Phone = forms.CharField(required=True,label="شماره تلفن:", max_length=15, min_length=3,error_messages={"required": "شماره تماس الزامی می باشد"},widget=forms.TextInput(attrs={'style': 'text-align:left;'}))

    Email = forms.EmailField(required=True,label="ایمیل:", widget=forms.EmailInput(attrs={'style': 'text-align:left;'}))

    Password = forms.CharField(required=True,label="گذرواژه:", widget=forms.PasswordInput(attrs={'style': 'text-align: left;'}))


class Product(ModelForm):
    def __init__(self,*args,**kwargs):
        super(Product,self).__init__(*args,**kwargs)
        for item in Product.visible_fields(self):
                item.field.widget.attrs["class"] = "form-control A_Product_Fields"
    class Meta:
        model = Add_Product
        fields = ('Product_Title', 'Product_Caption', 'Product_Price',
                  'Product_Price_Discount','Product_Image')
        labels = {
            'Product_Title':'عنوان',
            'Product_Caption':'توضیحات',
            'Product_Price':'قیمت',
            'Product_Price_Discount':'تخفیف',
            'Product_Image':'عکس محصول',
        }

        widgets = {
        'Product_Caption' : forms.Textarea(attrs={'style': 'resize: none;'}),
        'Product_Price_Discount':forms.TextInput(attrs={'': ''})
        }

class edit_Profile(forms.Form):
    def __init__(self,*args,**kwargs):
        super(edit_Profile,self).__init__(*args,**kwargs)
        for item in edit_Profile.visible_fields(self):
                item.field.widget.attrs["class"] = "form-control border-color"


    Name = forms.CharField(required=True,max_length=60, label="",widget=forms.TextInput(attrs={'placeholder': 'نام', 'style': 'border-radius:10px;width:200px;margin-left:3px;display:inline-block;'}))
    Family = forms.CharField(required=True,max_length=60, label="",widget=forms.TextInput(attrs={'placeholder': 'نام خانوادگی', 'style': 'margin-left:3px;border-radius:10px;width:200px;display:inline-block;'}))
    National_Code = forms.CharField(required=True,max_length=10, label="",widget=forms.TextInput(attrs={'placeholder': 'کد ملی', 'style': 'margin-left:3px;border-radius:10px;width:200px;display:inline-block;'}))
    Date_of_birth = forms.DateField(required=True, label="تاریخ تولد", input_formats=['%Y-%m-%d'], widget=forms.DateInput(attrs={'style': 'border-radius:10px;width:187px;margin-top:20px;display:inline-block;cursor:pointer;'}))
    Phone = forms.CharField(required=True,max_length=11, label="",widget=forms.TextInput(attrs={'placeholder': 'شماره موبایل', 'style': 'margin-left:3px;border-radius:10px;width:200px;display:inline-block;text-align:left;'}))
    Email = forms.CharField(required=True, label="",widget=forms.EmailInput(attrs={'placeholder': 'ایمیل', 'style': 'margin-left:17px;border-radius:10px;width:350px;display:inline-block;'}))
    re_price = (
        ('بعدا انتخاب میکنم', 'بعدا انتخاب میکنم'),
        ('واریز به کیف پول دجیتال', 'واریز به کیف پول دجیتال'),
        ('واریز به حساب بانکی', 'واریز به حساب بانکی'),
    )
    Job = forms.CharField(required=True, label="",widget=forms.TextInput(attrs={'placeholder':'شغل','style': 'margin-left:3px;border-radius:10px;width:220px;display:inline-block;'}))
    redirect = forms.CharField(required=True, label="روش برگرداندن پول من",widget=forms.Select(choices=re_price,attrs={'style': 'margin-left:3px;border-radius:10px;width:220px;display:inline-block;background:white;'}))
    Password = forms.CharField(required=True,max_length=16, label="",widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه', 'style': 'margin-left:15px;border-radius:10px;width:220px;text-align: left;'}))
    rePassword = forms.CharField(required=True,max_length=16, label="",widget=forms.PasswordInput(attrs={'placeholder': 'تکرار گذرواژه', 'style': 'margin-left:3px;border-radius:10px;width:220px;margin-top:20px;text-align: left;'}))
    Id = forms.CharField(widget=forms.HiddenInput, label="", required=True, initial="0")
    UserName = forms.CharField(widget=forms.HiddenInput, label="", required=True, initial="None")

class Seller_Legal_Form(forms.Form):
    def __init__(self,*args,**kwargs):
        super(Seller_Legal_Form,self).__init__(*args,**kwargs)
        for item in Seller_Legal_Form.visible_fields(self):
                item.field.widget.attrs["class"] = "Seller_Leg form-control border-color"
        self.fields['Company_Economic_Code'].widget.attrs['class'] = 'Seller_Enc form-control border-color'
        self.fields['ShopName'].widget.attrs['class'] = 'Sh_Name_Leg form-control border-color'
        self.fields['Company_National_Code'].widget.attrs['class'] = 'Comp_Nc_Leg form-control border-color'
        self.fields['Shaba_Number'].widget.attrs['class'] = 'Shaba_Leg form-control border-color'

    Company_Name = forms.CharField(required=True,max_length=20,label="",widget=forms.TextInput(attrs={'placeholder':'نام شرکت','class': 'Le_C_Name'}))
    Company_National_Code = forms.CharField(required=True,max_length=10,label="",widget=forms.TextInput(attrs={'placeholder':'کد ملی شرکت','style': 'text-align: left;'}))
    Company_Economic_Code = forms.CharField(label="",max_length=20,widget=forms.TextInput(attrs={'placeholder':'کد اقتصادی شرکت','style': 'text-align: left;'}))
    Shaba_Number = forms.CharField(required=True,max_length=24,label="",widget=forms.TextInput(attrs={'placeholder':'شماره شبا','style': 'text-align: left;'}))
    Signatory = forms.CharField(required=True,max_length=50,label="",widget=forms.TextInput(attrs={'placeholder':'صاحبان امضا','class': 'Le_S'}))#صاحبان امضا
    ShopName = forms.CharField(required=True,max_length=20,label="",widget=forms.TextInput(attrs={'placeholder':'مانند آذرخش، بازارک، خانه موبایل و...','style': 'position: relative;left: 21.8rem;margin:0;direction: rtl;'}))

class Seller_Genuine_Form(forms.Form):
    def __init__(self,*args,**kwargs):
        super(Seller_Genuine_Form,self).__init__(*args,**kwargs)
        for item in Seller_Genuine_Form.visible_fields(self):
            item.field.widget.attrs["class"] = "Seller_Gen form-control border-color"
            self.fields['Number_Sh'].widget.attrs['class'] = 'Seller_Gen_num form-control border-color Card-Number'

    National_Code = forms.CharField(required=True,max_length=10,label="",widget=forms.TextInput(attrs={'placeholder':'کد ملی *','style': 'text-align: left;position: relative;left: 21.8rem;margin:0;direction: rtl;'}))
    Number_Sh = forms.CharField(label="",max_length=16,widget=forms.TextInput(attrs={'placeholder':'0000 - 0000 - 0000 - 0000','style':'text-align: left;position: relative;left: 21.8rem;margin:0;'}))
    ShopName = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'مانند آذرخش، بازارک، خانه موبایل و...','style': 'position: relative;left: 21.8rem;margin:0;direction: rtl;'}))

class Logins_Seller(forms.Form):
    def __init__(self,*args,**kwargs):
        super(Logins_Seller,self).__init__(*args,**kwargs)
        for item in Logins_Seller.visible_fields(self):
            item.field.widget.attrs["class"] = "input-login-seller"

    Name = forms.CharField(required=True,label="نام ",widget=forms.TextInput(attrs={'placeholder':'نام','style':'text-align: right;'}))
    Family = forms.CharField(required=True,label="نام خانوادگی",widget=forms.TextInput(attrs={'placeholder':'نام خانوادگی','style':'text-align: right;'}))
    Phone = forms.CharField(required=True,max_length=11, label="",widget=forms.TextInput(attrs={'placeholder': 'شماره موبایل', 'style': 'text-align: left;'}))
    Email = forms.CharField(required=True,label="ایمیل",widget=forms.EmailInput(attrs={'placeholder':'ایمیل'}))
    UserName = forms.CharField(required=True,label="نام کاربری",widget=forms.TextInput(attrs={'placeholder':'نام کاربری'}))
    Password = forms.CharField(required=True,label="رمز عبور",widget=forms.PasswordInput(attrs={'placeholder':'گذرواژه','style':'text-align: lefttext-align: left;;'}))


class edit_Profile_Seller_Legal(forms.Form):
    def __init__(self,*args,**kwargs):
        super(edit_Profile_Seller_Legal,self).__init__(*args,**kwargs)
        for item in edit_Profile_Seller_Legal.visible_fields(self):
                item.field.widget.attrs["class"] = "Seller_e_Form form-control border-color"


    Company_Name = forms.CharField(required=True,max_length=20,label="",widget=forms.TextInput(attrs={'placeholder':'نام شرکت','class': 'Le_C_Name'}))
    Company_National_Code = forms.CharField(required=True,max_length=10,label="",widget=forms.TextInput(attrs={'placeholder':'کد ملی شرکت','style': 'text-align: left;position: relative;right: 13px;'}))
    Company_Economic_Code = forms.CharField(label="",max_length=20,widget=forms.TextInput(attrs={'placeholder':'کد اقتصادی شرکت','style': 'text-align: left;position: relative;left: 13px;'}))

    Shaba_Number = forms.CharField(required=True,max_length=24,label="",widget=forms.TextInput(attrs={'placeholder':'شماره شبا','style': 'text-align: left;'}))
    Signatory = forms.CharField(required=True,max_length=50,label="",widget=forms.TextInput(attrs={'placeholder':'صاحبان امضا','class': 'Le_S'}))#صاحبان امضا
    Phone = forms.CharField(required=True,max_length=11, label="",widget=forms.TextInput(attrs={'placeholder': 'شماره موبایل', 'style': 'text-align: left;position: relative;right: 0.5rem;margin: 0;'}))
    ShopName = forms.CharField(required=True,max_length=20,label="",widget=forms.TextInput(attrs={'placeholder':'مانند آذرخش، بازارک، خانه موبایل و...','style': 'position: relative;left: 0.5rem;margin:0;direction: rtl;'}))


    Password = forms.CharField(required=True,max_length=16, label="",widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه', 'style': 'border-radius:10px;width:220px;text-align: left;'}))
    rePassword = forms.CharField(required=True,max_length=16, label="",widget=forms.PasswordInput(attrs={'placeholder': 'تکرار گذرواژه', 'style': 'border-radius:10px;width:220px;text-align: left;'}))
    Id = forms.CharField(widget=forms.HiddenInput, label="", required=True, initial="0")
    UserName = forms.CharField(widget=forms.HiddenInput, label="", required=True, initial="None")

class edit_Profile_Seller_Genuine(forms.Form):
    def __init__(self,*args,**kwargs):
        super(edit_Profile_Seller_Genuine,self).__init__(*args,**kwargs)
        for item in edit_Profile_Seller_Genuine.visible_fields(self):
                item.field.widget.attrs["class"] = "Seller_e_Form form-control border-color"
                self.fields['Number_Sh'].widget.attrs['class'] = 'Seller_Gen_num form-control border-color Card-Number'

    National_Code = forms.CharField(required=True,max_length=10,label="",widget=forms.TextInput(attrs={'placeholder':'کد ملی *','style': 'text-align: left;direction: rtl;position: relative;left: 15rem;'}))
    Phone = forms.CharField(required=True,max_length=11, label="",widget=forms.TextInput(attrs={'placeholder': 'شماره موبایل', 'style': 'text-align: left;position: relative;left: 15.1rem;'}))
    Number_Sh = forms.CharField(label="",max_length=16,widget=forms.TextInput(attrs={'placeholder':'0000 - 0000 - 0000 - 0000','style':'text-align: left;margin:0;'}))
    ShopName = forms.CharField(label="",max_length=20,widget=forms.TextInput(attrs={'placeholder':'مانند آذرخش، بازارک، خانه موبایل و...','style': 'margin:0;direction: rtl;'}))

    Password = forms.CharField(required=True,max_length=16, label="",widget=forms.PasswordInput(attrs={'placeholder': 'گذرواژه', 'style': 'border-radius:10px;width:220px;text-align: left;'}))
    rePassword = forms.CharField(required=True,max_length=16, label="",widget=forms.PasswordInput(attrs={'placeholder': 'تکرار گذرواژه', 'style': 'border-radius:10px;width:220px;text-align: left;'}))
    Id = forms.CharField(widget=forms.HiddenInput, label="", required=True, initial="0")
    UserName = forms.CharField(widget=forms.HiddenInput, label="", required=True, initial="None")