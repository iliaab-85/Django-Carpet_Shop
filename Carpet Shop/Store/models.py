from django.db import models

# Create your models here.
class User_Save(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30,verbose_name="نام")
    family = models.CharField(max_length=30,verbose_name="نام خانوادگی")
    national_code = models.CharField(max_length=10,verbose_name="کد ملی",default=0)
    date_of_birth = models.CharField(max_length=10,verbose_name="تاریخ تولد",default="None")
    Phone = models.IntegerField(verbose_name="شماره موبایل",default=0)
    Email = models.EmailField(max_length=30,verbose_name="ایمیل")
    job = models.CharField(max_length=30,verbose_name="شغل",default="None")
    redirect = models.CharField(max_length=20,verbose_name="روش برگرداندن پول",default="None")
    UserName = models.CharField(max_length=30,verbose_name="نام کاربری")
    password = models.CharField(max_length=20,verbose_name="گذرواژه",default="None")
    repassword = models.CharField(max_length=20,verbose_name="تکرار گذرواژه",default="None")
    #Rol = models.CharField(max_length=20,verbose_name="رول",default="None")

    class Meta:
        verbose_name = "حساب"
        verbose_name_plural = "حساب ها"

class Add_Product(models.Model):
    Product_Id = models.AutoField(primary_key=True,verbose_name="آیدی محصول")
    Product_Code = models.CharField(max_length=10,default="0",verbose_name="کد محصول")
    Product_Title = models.CharField(max_length=60,verbose_name="عنوان")
    Product_Caption = models.CharField(max_length=1000,verbose_name="توضیحات محصول")
    Product_Price = models.CharField(max_length=12,verbose_name="قیمت محصول",default="0")
    Product_Price_Discount = models.CharField(max_length=5,verbose_name="تخفیف محصول",default="0")
    Product_Price_Final = models.CharField(max_length=12,verbose_name="قیمت نهایی محصول",default="0")
    Product_Image = models.ImageField(null=True,blank=True,upload_to="files/Img_Product",verbose_name="عکس محصول")

    Product_Type = models.CharField(max_length=20,verbose_name="نوع محصول(دست باف,ماشینی,کامپیوتری)")
    Product_Date = models.CharField(max_length=30,verbose_name="تاریخ انتشار")
    Chat_Code = models.CharField(max_length=30,default=0)
    user_Id = models.IntegerField(verbose_name="نام کاربری",default=0)
    Product_Likes = models.IntegerField(verbose_name="علاقه مندی ها",default="0")
    Product_Visit = models.IntegerField(verbose_name="بازدید",default="0")
    Rate = models.CharField(max_length=15,default="0")

    Product_Brand = models.CharField(max_length=20,verbose_name="برند محصول",default="null")
    Product_Thread = models.CharField(max_length=20,verbose_name="جنس نخ محصول",default="null")
    Product_Size = models.CharField(max_length=15,verbose_name="ابعاد محصول",default="null")
    Product_Result = models.CharField(max_length=35,verbose_name="وضعیت محصول",default="null")
    Product_Rag = models.CharField(max_length=5,verbose_name="رج",default="null")
    Product_Shane = models.CharField(max_length=5,verbose_name="شانه",default="null")
    Product_Type_Sort = models.CharField(max_length=20,verbose_name="نوع دسته دبندی(دست باف,ماشینی)",default="null")
    Product_pdf_File = models.FileField(upload_to="files/file_Product",verbose_name="فایل محصول",default="null")
    Product_Accss_Type = models.CharField(max_length=20,verbose_name="نوع اکسسوری",default="null")
    Product_Glim_Type = models.CharField(max_length=15,verbose_name="نوع گلیم",default="null")
    Product_Un_Type_Sort = models.CharField(max_length=20,verbose_name="نوع دسته بندی",default="null")

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"


class Product_Order(models.Model):
    Product_Id = models.AutoField(primary_key=True)
    Product_Code = models.CharField(max_length=100,default=0)
    Product_Title = models.CharField(max_length=60,verbose_name="عنوان")
    Product_Caption = models.CharField(max_length=50,verbose_name="توضیحات محصول")
    Product_Type = models.CharField(max_length=20,verbose_name="نوع محصول(دست باف,ماشینی,کامپیوتری)")
    Product_Brand = models.CharField(max_length=20, verbose_name="برند محصول", default="None")
    Product_Price = models.IntegerField(verbose_name="قیمت محصول",default="0")
    Product_Count = models.IntegerField(default=1,verbose_name="تعداد محصول")
    Product_Size = models.CharField(max_length=35,verbose_name="ابعاد محصول")
    Product_Result = models.CharField(max_length=35,verbose_name="وضعیت محصول")
    Product_Image = models.ImageField(verbose_name="عکس محصول")
    user_Id = models.IntegerField(verbose_name="نام کاربری",default=0)
    Order_Code = models.CharField(verbose_name="", max_length=10, default=0)


    class Meta:
        verbose_name = "خرید"
        verbose_name_plural = "خریدات"

class Like(models.Model):
    Like_Id = models.AutoField(primary_key=True)
    Product_Code = models.CharField(max_length=100,default=0)
    user_Id = models.IntegerField()
    Date = models.CharField(max_length=30, default=0)


    class Meta:
        verbose_name = "لایک"
        verbose_name_plural = "لایک ها"

class User_View(models.Model):
    View_Id = models.AutoField(primary_key=True)
    Product_Code = models.CharField(max_length=100,default=0)
    user_Id = models.IntegerField()
    Date = models.CharField(max_length=30, default=0)

    class Meta:
        verbose_name = "بازدید"
        verbose_name_plural = "بازدید ها"

class Chats(models.Model):
    Chat_Id = models.AutoField(primary_key=True)
    Message = models.CharField(max_length=400)
    counter = models.IntegerField()
    Chat_user_Id = models.IntegerField()
    Chat_Code = models.CharField(max_length=30,default="0")
    Chat_Message_Date = models.CharField(max_length=20,default="None")
    Chat_user2_Id = models.IntegerField(default="0")
    Seender = models.IntegerField(default="0")
    With = models.CharField(max_length=25,default="None")
    Visit_Seller = models.IntegerField(default="0")
    Visit_User = models.IntegerField(default="0")
    Visit_Support = models.IntegerField(default="0")

    class Meta:
        verbose_name = "چت"
        verbose_name_plural = "چت ها"

class Chats_Code(models.Model):
    Chats_Code_Id = models.AutoField(primary_key=True)
    Chat_Code = models.CharField(max_length=30,default="0")

    class Meta:
        verbose_name = "کد چت"
        verbose_name_plural = "کد چت ها"

class Product_Comment(models.Model):
    Chat_Id = models.AutoField(primary_key=True)
    Chat_Code = models.CharField(max_length=30,default="0")
    Product_Code = models.CharField(max_length=30,default="None")
    Message = models.CharField(max_length=30,default="None")
    Rate = models.CharField(max_length=15,default="0")
    Date = models.CharField(max_length=20,default="None")
    user_Id = models.IntegerField()

    class Meta:
        verbose_name = "کد کامنت"
        verbose_name_plural = "کد کامنت ها"

class Seller_Genuine(models.Model):#حقیقی
    Seller_Id = models.AutoField(primary_key=True)
    Phone = models.CharField(verbose_name="شماره موبایل",default=0,max_length=11)
    National_Code = models.CharField(default="0",max_length=10)
    Cart_Number = models.CharField(default="0",max_length=16)
    Shaba_Number = models.CharField(default="0",max_length=24)
    Shop_Name = models.CharField(max_length=20,default="None")
    Seller_IpAddress = models.CharField(max_length=30, default="None")
    password = models.CharField(max_length=20, verbose_name="گذرواژه", default="None")
    State = models.CharField(max_length=20,default="Create")

    class Meta:
        verbose_name = "فروشنده حقیقی"
        verbose_name_plural = "فروشنده های حقیقی"

class Seller_Legal(models.Model):#حقوقی
    Seller_Id = models.AutoField(primary_key=True)
    Phone = models.CharField(verbose_name="شماره موبایل",default=0,max_length=11)
    Company_Name = models.CharField(max_length=30,default="None")
    Company_Type = models.CharField(max_length=30,default="None")
    Company_National_Code = models.CharField(default="0",max_length=10)
    Economic_Code_Company = models.CharField(default="0",max_length=24)#کد اقتصادی شرکت
    Shaba_number = models.CharField(default="0",max_length=24)
    Signatory = models.CharField(max_length=40,default="None")#صاحبان امضا
    Shop_Name = models.CharField(max_length=30,default="None")
    Seller_IpAddress = models.CharField(max_length=30, default="None")
    password = models.CharField(max_length=20, verbose_name="گذرواژه", default="None")
    State = models.CharField(max_length=20,default="Create")

    class Meta:
        verbose_name = "فروشنده حقوقی"
        verbose_name_plural = "فروشنده های حقوقی"

class Supporter(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name="نام")
    family = models.CharField(max_length=30, verbose_name="نام خانوادگی")
    national_code = models.CharField(max_length=10, verbose_name="کد ملی", default=0)
    date_of_birth = models.CharField(max_length=10, verbose_name="تاریخ تولد", default="None")
    Phone = models.IntegerField(verbose_name="شماره موبایل", default=0)
    Email = models.EmailField(max_length=30, verbose_name="ایمیل")
    job = models.CharField(max_length=30, verbose_name="شغل", default="None")
    redirect = models.CharField(max_length=20, verbose_name="روش برگرداندن پول", default="None")
    UserName = models.CharField(max_length=30, verbose_name="نام کاربری")
    password = models.CharField(max_length=20, verbose_name="گذرواژه", default="None")
    repassword = models.CharField(max_length=20, verbose_name="تکرار گذرواژه", default="None")
    Chat_Code = models.CharField(max_length=30,default="0")
    #Rol = models.CharField(max_length=20, verbose_name="رول", default="None")

class Order_Complete(models.Model):
    Id = models.AutoField(primary_key=True)
    Price = models.CharField(max_length=30, verbose_name="قیمت")
    user_Id = models.IntegerField(verbose_name="")
    Date = models.CharField(max_length=30, verbose_name="", default="None")
    Order_Code = models.CharField(verbose_name="", max_length=10)

class Product_buyed(models.Model):
    Product_Id = models.AutoField(primary_key=True)
    Product_Code = models.CharField(max_length=100,default=0)
    Date = models.CharField(max_length=30, verbose_name="", default="None")
    user_Id = models.IntegerField(verbose_name="نام کاربری",default=0)


    class Meta:
        verbose_name = "خرید"
        verbose_name_plural = "خریدات"