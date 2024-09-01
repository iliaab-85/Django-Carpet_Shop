$(document).ready(function () {
    $('.btn_login').click(function () { 
        let UserName = $('#id_UserName').val();
        let Password = $('#id_Password').val();
        let Type = $('.Type').text();
        let Error_List = ""
        if (UserName == "") {
            Error_List += "لطفا نام کاربری خود را وارد کنید"
        }
        else if (Password == "") {
            Error_List += "لطفا گذرواژه خود را وارد کنید"
        }
        else {
            $.ajax({
                type:"POST",
                url:"http://" + window.location.host + "/Farshtore/Seller_Login_Check/" + Type,
                data:$(".Seller_Login_Form").serialize(),
                success:function(result) {
                    window,location.href = "/Farshtore/EditProfile/" + result
                },
                error:function(e){
                    alert("error");
                }
            });
        }
        $(".Error_Lst").removeAttr("hidden");
        $('.Error_Lst').text(Error_List);
    });
});