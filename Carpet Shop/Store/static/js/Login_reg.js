document.getElementById("id_UserName").placeholder = "نام کاربری";
document.getElementById("id_Password").placeholder = "گذرواژه";

$(document).ready(function() {
    $(".Check_valid").click(function() {
        let username = $('#id_UserName').val();
        let password = $('#id_Password').val();
        let Valid = "";
        if (username == "") {
            Valid += "نام کاربری را وارد کنید";
        }
        else if (password == "") {
            Valid += "گذرواژه را وارد کنید"
        }
        else {
            $.ajax({
                type:"POST",
                url:"http://127.0.0.1:8000/Farshtore/Check_Support_login",
                data:$('.frm_valid_login').serialize(),
                success:function(result){
                    if (result == "اطلاعات صحیح نیست") {
                        let Valids = "اطلاعات صحیح نیست";
                        $(".Valid_log").removeAttr("hidden");
                        $('.Valid_log').html(Valids);
                    }
                    else {
                        window.location.href = "/Farshtore/EditProfile/" + String(result);
                    }
                },

                error:function(e){
                    alert("error");
                }
        });
        }
        $(".Valid_log").removeAttr("hidden");
        $('.Valid_log').html(Valid);
    });
});