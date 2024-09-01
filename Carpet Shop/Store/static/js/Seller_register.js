$(document).ready(function () {

    $('#id_National_Code').keypress(function (e) {
        var key = e.which;
        if (key < 48 || key > 57) {
            e.preventDefault();
        }
    });

    $('#id_National_Code').on('paste', function(e){
        e.preventDefault();
    });

    $('#id_Number_Sh').keypress(function (e) {
        var key = e.which;
        if (key < 48 || key > 57) {
            e.preventDefault();
        }
    });

    $('#id_Number_Sh').on('paste', function(e){
        e.preventDefault();
    });

    $('#id_ShopName').on('paste', function(e){
        e.preventDefault();
    });

    $('.Seller_Leg').each(function() {
        $(this).attr('placeholder', '* ' + $(this).attr('placeholder'));
      });

      $('.Comp_Nc_Leg').each(function() {
        $(this).attr('placeholder', '* ' + $(this).attr('placeholder'));
      });

      $('.Shaba_Leg').each(function() {
        $(this).attr('placeholder', '* ' + $(this).attr('placeholder'));
      });

      $('.btn-Gen').click(function() {
        let Num_Sh = "";
        let Error_List = "";
        let National_Code = $('#id_National_Code').val()

        if ($('.Seller_Gen_num').hasClass("Card-Number")) {
            Num_Sh = "Card"
        }

        else if ($('.Seller_Gen_num').hasClass("Shaba-Number")) {
            Num_Sh = "Shaba"
        }

        if (National_Code == "") {
            Error_List += "کد ملی شخصی خود را وارد کنید";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else if (National_Code.length < 10){
            Error_List += "کد ملی معتبر نیست";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else {
            $('.Error-List').html("");
            $.ajax({
                type:"POST",
                url:"http://" + window.location.host + "/Farshtore/Save_Seller_Genuine_Info/" + Num_Sh,
                data:$(".Gen-Form").serialize(),
                success:function(result) {
                    window.location.href = "/Farshtore/Seller/EnterPanel";
                },
                error:function(e){
                    alert("error");
                }
            });
        }

      });

      $('#id_Company_National_Code').keypress(function (e) {
        var key = e.which;
        if (key < 48 || key > 57) {
            e.preventDefault();
        }
    });

    $('#id_Company_National_Code').on('paste', function(e){
        e.preventDefault();
    });

    $('#id_Company_Economic_Code').keypress(function (e) {
        var key = e.which;
        if (key < 48 || key > 57) {
            e.preventDefault();
        }
    });

    $('#id_Company_Economic_Code').on('paste', function(e){
        e.preventDefault();
    });

    $('#id_Shaba_Number').keypress(function (e) {
        var key = e.which;
        if (key < 48 || key > 57) {
            e.preventDefault();
        }
    });

    $('#id_Shaba_Number').on('paste', function(e){
        e.preventDefault();
    });

      $('.btn-Leg').click(function() {
        let Error_List = "";
        let Company_Name = $('#id_Company_Name').val()
        let Company_Type = $('#id_Company_Type').val()
        let Company_National_Code = $('#id_Company_National_Code').val()
        let Shaba_Number = $('#id_Shaba_Number').val()
        let Signatory = $('#id_Signatory').val()
        if (Company_Name == "") {
            Error_List += "نام شرکت الزامی است";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else if (Company_Type == ""){
            Error_List += "نوع شرکت را انتخاب نمایید";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else if (Company_National_Code == ""){
            Error_List += "کد ملی شرکت را وارد کنید";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else if (Company_National_Code.length < 10){
            Error_List += "کد ملی شرکت صحیح نیست";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else if (Shaba_Number == ""){
            Error_List += "شماره شبا را وارد کنید";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else if (Shaba_Number.length < 24){
            Error_List += "شماره شبا صحیح نیست";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else if (Signatory == ""){
            Error_List += "صاحبان امضا نباید خالی باشد";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else {
            $('.Error-List').html("");
            $.ajax({
                type:"POST",
                url:"http://" + window.location.host + "/Farshtore/Save_Seller_Legal_Info",
                data:$(".Seller_Legal_Form").serialize(),
                success:function(result) {
                    if (result == "True") {
                    window.location.href = "/Farshtore/Seller/EnterPanel";
                    }
                },
                error:function(e){
                    alert("error");
                }
            });
        }

      });

      $('.text-Change').click(function () {
        $(".Seller_Gen_num").val("");
        $(this).toggleClass('changed');
        if ($(this).hasClass('changed')) {
          $(this).text("ثبت شماره کارت به‌جای شماره شبا");
          $(".lbl-N-Code").text("شماره شبا");
          $(".Seller_Gen_num").removeClass("Card-Number").addClass("Shaba-Number");
          $(".Seller_Gen_num").attr('placeholder','000000000000000000000000');
        } else {
          $(this).text("ثبت شماره شبا به‌جای شماره کارت");
          $(".lbl-N-Code").text("شماره کارت");
          $(".Seller_Gen_num").removeClass("Shaba-Number").addClass("Card-Number");
          $(".Seller_Gen_num").attr('placeholder','0000 - 0000 - 0000 - 0000');
        }
      });

      $('.btn-enter').click(function () {
        let Error_List = "";
        let username = $('#id_UserName').val();
        let Phone = $('#id_Phone').val();
        let password = $('#id_Password').val();
        if (username == "") {
            Error_List += "نام کاربری را وارد کنید";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else if (password == "") {
            Error_List += "رمز عبور را وارد کنید";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else if (Phone == "") {
            Error_List += "شماره خود را وارد کنید";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else if (Phone.length < "11") {
            Error_List += "شماره خود را صحیح وارد کنید";
            $(".Error-List").removeAttr("hidden");
            $('.Error-List').html(Error_List);
        }
        else {
            $.ajax({
                type:"POST",
                url:"http://127.0.0.1:8000/Farshtore/Save_Seller_Account",
                data:$(".Login-Seller").serialize(),
                success: function (result) {
                    if (result == "Two_Exist") {
                        $(".Error-List").removeAttr("hidden");
                        $('.Error-List').html("هنگام ثبت مشکلی پیش آمد دوباره تلاش کنید");
                    }

                    else if (result == "Exist") {
                        $(".Error-List").removeAttr("hidden");
                        $('.Error-List').html("کاربری با این مششخصات وجود دارد");
                    }
                    else {
                        window.location.href = "/Farshtore/EditProfile/" + result
                    }
                },
                error:function(e){
                    alert("error");
                }
        });
        }
      });
    
    $('.btn-Choice').click(function () {
    let Seller_Result = $(this).val()
            $.ajax({
                    type:"POST",
                    url:"http://127.0.0.1:8000/Farshtore/Save_Seller_Result/" + Seller_Result,
                    success: function (result) {
                    },
                    error:function(e){
                        alert("error");
                    }
            });
        if (Seller_Result == "حقیقی"){
            window.location.href = "/Farshtore/Seller/Genuine/Information";
        }
        else if (Seller_Result == "حقوقی") {
            window.location.href = "/Farshtore/Seller/Legal/Information";
        }
    });
});
