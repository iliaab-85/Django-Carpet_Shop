from django.urls import path
from . import views

urlpatterns = [

    #Admin Urls

    path('Admin',views.Admins,name="ادمین"),
    path('Admin/Admin_Dashboard',views.Admin,name="ادمین"),
    path('Admin/Tables',views.Admin_Table,name="ادمین"),
    path('Admin_AllUser/<int:user_id>', views.Admin_AllUser,name=""),
    path('Admin_AllSupporter/<int:user_id>', views.Admin_AllSupporter,name=""),
    path('Admin_AllUser_Seller/<int:user_id>', views.Admin_AllUser_Seller,name=""),
    path('Admin_AllProduct/<int:user_id>', views.Admin_AllProduct,name=""),
    path('Admin_Product_Order_Count/<int:Product_Code>', views.Admin_Product_Order_Count,name=""),
    path('Admin_User_Info/<str:function>', views.Admin_User_Info,name=""),
    path('Admin_Order_Complete/<int:user_Id>/<str:function>', views.Admin_Order_Complete,name=""),
    path('Admin_buyed_product/<int:user_Id>/<str:Product_Code>/<str:function>', views.Admin_buyed_product,name=""),

    #Other Urls

    path('Home',views.home,name="خانه"),
    path('aboutUs',views.aboutUs,name="درباره ما"),
    path('contact',views.contact,name="ارتباط با ما"),
    path('question',views.question,name="ارتباط با ما"),
    path('404',views.Error404,name="ارور 404"),
    path('Order',views.Order,name="سبد خرید"),
    path('login',views.logins,name="ورود"),
    path('login_Support',views.login_Support,name="ورود"),
    path('Login_Seller/<str:Seller_Type>',views.Login_Seller,name="ورود"),
    path('Checklogin',views.CheckLogin,name="چک کردن ورودی کاربر"),
    path('Seller_Login_Check/<str:Type>',views.Seller_Login_Check,name="چک کردن ورودی کاربر"),
    path('Check_Support_login',views.Check_Support_login,name="چک کردن ورودی کاربر"),
    path('Logout',views.Logout,name="خارج شدن از حساب"),
    path('register',views.register,name="ثبت نام"),
    path('register_Support',views.register_Support,name="ثبت نام"),
    path('RegisterAction',views.RegisterAction,name="چک کردن ثبت نام کاربر"),
    path('Register_Support_Action',views.Register_Support_Action,name="چک کردن ثبت نام کاربر"),
    path('CheckAuth', views.CheckAuth,name="چک کردن ورود به سیستم کاربر"),

    # Profile Urls

    path('EditProfile/<int:Id>', views.EditProfile, name=""),
    path('AddProduct', views.AddProduct,name=""),
    path('Profile/Wallet', views.Wallet,name=""),
    path('Profile/Activity',views.Activity,name="آخرین بازدید"),
    path('Subscribation', views.Subscribation,name=""),
    path('Profile/Orders', views.Orders,name=""),
    path('Profile/Product_Likes', views.Product_Likes, name="علاقه مندی ها"),
    path('Profile/Chat', views.Chat,name=""),
    path('Profile/MyComments', views.Commnets,name=""),
    path('Profile/Message', views.Message,name=""),
    path('Profile/user_history', views.user_history, name="آخرین بازدید"),
    path('Profile/EditProfile', views.Find_Id,name=""),

    # Profile functions

    path('add_Product_database/<str:txt_sort>/<str:My_Dict>', views.add_Product_database, name=""),
    path('Edit_Profile_Seller_user/<str:Num_Sh>', views.Edit_Profile_Seller_user, name=""),
    path('Edit_Profile_Support', views.Edit_Profile_Support, name=""),
    path('Edit_Profile_user', views.Edit_Profile_user,name=""),

    # Product Urls

    path('ProductDataBase', views.ProductDataBase,name=""),
    path('product/<str:func>/<str:Value>', views.product, name="تمامی محصول ها"),
    path('Search/<str:txt_Search>', views.Search, name="جستجو محصول بر اساس دسته بندی"),
    path('Search_Sort/<str:txt_res>/<str:txt_sort>/<str:Price_Start>/<str:Price_End>', views.Search_Sort,
         name="جستجو محصول بر اساس دسته بندی"),
    path('Search_Res/<str:Res>', views.Search_Res,name="جستجو محصول بر اساس وضعیت"),
    path('Search_Rag/<str:Rag>', views.Search_Rag,name="جستجو محصول بر اساس وضعیت"),
    path('Search_Price/<int:Start>/<int:End>/<str:txt_Sort>/<str:txt_Brand>', views.Search_Price,
         name="جستجو محصول بر اساس دسته بندی"),
    path('product/get_product', views.get_product,name=""),
    path('product_information/<str:Code>', views.product_information,name=""),
    path('Add_Like/<str:Code>', views.Add_Like,name=""),
    path('Remove_Like/<str:Code>', views.Remove_Like,name=""),
    path('Order_Product', views.Order_Product,name=""),

    #Order Urls

    path('Order_Set/<str:Code>/<int:Count>', views.Order_Set,name=""),
    path('Order_Complete/<str:Final_Price>', views.Order_complete,name=""),
    path('Order_complete_Remove', views.Order_complete_Remove,name=""),
    path('Remove_Product_Order/<int:Id>', views.Remove_Product_Order,name=""),
    path('Delete_Set/<str:Code>', views.Delete_Set,name=""),

    #Chat Urls

    path('Support', views.Support,name=""),
    path('Seller_Chat/<str:Chat_Code>', views.Seller_Chat,name=""),
    path('Chat_Seller', views.Chat_Seller,name=""),
    path('Chat_User', views.Chat_User,name=""),
    path('Chat_Support', views.Chat_Support,name=""),

    path('User_Chat', views.User_Chat, name=""),
    path('Support_Chat', views.Support_Chat, name=""),
    path('Addview/<str:Code>', views.Addview,name=""),
    path('Search_Like/<str:Code>', views.Search_Like,name=""),
    path('Search_view/<str:Code>', views.Search_view,name=""),
    path('Chat_Read/<str:Chat_Code>/<str:Other_Id>', views.Chat_Read,name=""),
    path('Chat_Group/<str:group_Code>', views.Chat_Group,name=""),
    path('Get_Id/<str:Code>/<str:With>', views.Get_Id,name=""),
    path('Get_Id_User_Chat/<str:Code>/<str:With>', views.Get_Id_User_Chat,name=""),
    path('Chat_Read_Seller/<str:Chat_Code>/<str:Other>', views.Chat_Read_Seller,name=""),
    path('Chat_Read_User/<str:Chat_Code>/<str:Other>', views.Chat_Read_User,name=""),
    path('Chat_Read_Support/<str:Chat_Code>/<str:Other>', views.Chat_Read_Support,name=""),
    path('Get_Id_Support/<str:Chat_Code>/<str:With>', views.Get_Id_Support,name=""),

    #Login Urls

    path('Seller/CheckResult', views.Seller_CheckResult, name=""),
    path('Seller/Genuine/Information', views.Seller_Genuine_CheckInfo, name=""),
    path('Seller/Legal/Information', views.Seller_Legal_CheckInfo, name=""),
    path('Seller/Information', views.Seller_CheckInfo, name=""),
    path('Seller/Address', views.Seller_CheckAddress, name=""),
    path('Seller/Question', views.Seller_CheckQuestion, name=""),
    path('Seller/EnterPanel', views.Seller_EnterPanel, name=""),

    #Comment Urls

    path('Save_Comment_Product/<str:Message>/<str:Chat_Code>/<str:Product_Code>/<str:Message_Date>/<str:Rate>', views.Save_Comment_Product,name=""),
    path('Load_Comment_Product/<str:Chat_Code>', views.Load_Comment_Product,name=""),

    #Save Urls

    path('Save_Seller_Result/<str:Seller_Result>', views.Save_Seller_Result,name=""),
    path('Save_Count/<str:Product_Code>/<str:func>', views.Save_Count,name=""),
    path('Save_Seller_Legal_Info', views.Save_Seller_Legal_Info,name=""),
    path('Save_Seller_Genuine_Info/<str:num_res>', views.Save_Seller_Genuine_Info,name=""),
    path('Save_Seller_Account', views.Save_Seller_Account,name=""),
    path('Chat_Save/<str:Other_id>/<str:text>/<str:Chat_Code>/<str:Date>', views.Chat_Save,name=""),
    path('Chat_Save_Seller/<str:Other_id>/<str:text>/<str:Chat_Code>/<str:Date>', views.Chat_Save_Seller,name=""),
    path('Chat_Save_User/<str:Other_id>/<str:text>/<str:Chat_Code>/<str:Date>', views.Chat_Save_User,name=""),
    path('Chat_Save_Support/<str:Other_id>/<str:text>/<str:Chat_Code>/<str:Date>', views.Chat_Save_Support,name=""),
]