$(document).ready(function() {
    $(".Check_valid").click(function() {
        let name = $('#id_Name').val();
        let family = $('#id_Family').val();
        let UserName = $('#id_UserName').val();
        let Phone = $('#id_Phone').val();
        let Email = $('#id_Email').val();
        let Password = $('#id_Password').val();
        let Validation = "";

            let mobileNumber = $('#id_Phone').val();
            let mobileRegex = /^09\d{9}$/; // Iranian mobile number pattern

        if (name == "") {
            Validation += "نام را وارد کنید";
        }
        else if (family == "") {
            Validation += "نام خانوادگی را وارد کنید";
        }
        else if (UserName == "") {
            Validation += "نام کاربری را وارد کنید";
        }
        else if (Phone == "") {
            Validation += "شماره موبایل را وارد کنید"
        }
        else if (!mobileRegex.test(mobileNumber)) {
            Validation += "شماره موبایل معتبر نیست";
        }
        else if (Email == "") {
            Validation += "ایمیل را وارد کنید"
        }
        else if (Password == "") {
            Validation += "گذرواژه را وارد کنید"
        }
        else {
            $.ajax({
                type:"POST",
                url:"http://127.0.0.1:8000/Farshtore/RegisterAction",
                data:$('.frm_reg').serialize(),
                success:function(result){
                    if (result) {
                        window.location.href = "/Farshtore/login"
                    }
                },
        
                error:function(e){
                    alert("error");
                }
        });
        }
        $(".register_valid").removeAttr("hidden");
        $('.register_valid').html(Validation);
    });
});