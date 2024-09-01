$(document).ready(function() {

  $(".datebirth_profile").val($("#id_Date_of_birth").val());

  let Company_Type = $(".Company_Type").text();
  $('#id_Company_Type option[value="' + Company_Type + '"]').prop('selected', true);

  $('#id_Number_Sh').keypress(function (e) {
    var key = e.which;
    if (key < 48 || key > 57) {
        e.preventDefault();
    }
  });

  $('#id_National_Code').keypress(function (e) {
    var key = e.which;
    if (key < 48 || key > 57) {
        e.preventDefault();
    }
  });

  $('#id_Number_Sh').on('paste', function(e){
    e.preventDefault();
  });

  $('#id_Phone').on('paste', function(e){
    e.preventDefault();
  });

  $('#id_Phone').keypress(function (e) {
    var key = e.which;
    if (key < 48 || key > 57) {
        e.preventDefault();
    }
  });

  $('#id_Number_Sh').on('paste', function(e){
    e.preventDefault();
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

$('.btn_datebirth_save').click(function () {
    let day = $(".days").val();
    let month = $(".months").val();
    let year = $(".years").val();
    let Error_List = "";

    if (day == "" | month == "" | year == "") {
        Error_List += "اطلاعات نادرست است"
        $('.Error_list').text(Error_List);
    }
    else {
        $('.Error_list').text("");
        $('.datebirth_profile').val(day + "/" + month + "/" + year);
        $('#id_Date_of_birth').val(day + "/" + month + "/" + year);
    }
});

$(".Change_Info").click(function() {
    let Errors = "";
    let name = $("#id_Name").val();
    let family = $("#id_Family").val();
    let national_code = $("#id_National_Code").val();
    let date_of_birth = $("#id_Date_of_birth").val();
    let phone = $("#id_Phone").val();
    let email = $("#id_Email").val();
    let job = $("#id_Job").val();
    let redirect = $("#id_redirect").val();
    let password = $("#id_Password").val();
    let repassword = $("#id_rePassword").val();
  
    if (name == "" || family == "" || national_code == "" || date_of_birth == "") {
      Errors += "<li style='margin-bottom: 5px;'>اطلاعات شخصی خود را وارد کنید</li>";

    }
    else if (password != "" && repassword == "") {
      Errors += "<li style='margin-bottom: 5px;'>تکرار گذرواژه خالی است</li>";
    }
    else if (password != repassword) {
      Errors += "<li style='margin-bottom: 5px;'>تکرار گذرواژه اشتباه است</li>";
    }
    else {
        let Res = $(".Res").text();
        if (Res == "User") {
            $.ajax({
                type:"POST",
                url:"http://" + window.location.host + "/Farshtore/Edit_Profile_user",
                data:$(".frm-Edit").serialize(),
                success:function(result) {
                },
                error:function(e){
                    alert("error");
                }
            });
        }
        else if (Res == "Support") {
            $.ajax({
                type:"POST",
                url:"http://" + window.location.host + "/Farshtore/Edit_Profile_Support",
                data:$(".frm-Edit").serialize(),
                success:function(result) {
                alert(result)
                },
                error:function(e){
                    alert("error");
                }
            });
        }
    }
        $(".Error-List").removeAttr("hidden");
        $(".Error-List").html(Errors);
  });

  $(".Change_Info_Seller").click(function() {
    let Errors = "";
    let C_name = $("#id_Company_Name").val();
    let C_type = $("#id_Company_Type").val();
    let C_national_code = $("#id_Company_National_Code").val();
    let C_Company_Economic_Code = $("#id_Company_Economic_Code").val();
    let Shaba_Number = $("#id_Shaba_Number").val();
    let Signatory = $("#id_Signatory").val();
    let ShopName = $("#id_ShopName").val();
    let password = $("#id_Password").val();
    let repassword = $("#id_rePassword").val();
    let Phone_n = $("#id_Phone").val();
    
    if (C_name == "" || C_type == "" || C_national_code == "" || C_Company_Economic_Code == "") {
      Errors += "<li style='margin-bottom: 5px;'>اطلاعات شرکت خود را وارد کنید</li>";
    }
    else if (Shaba_Number == "" || Signatory == "" || ShopName == "" || Phone_n == "") {
      Errors += "<li style='margin-bottom: 5px;'>اطلاعات جزئی خود را وارد کنید</li>";
    }
    else if (Phone_n.length < 11) {
      Errors += "<li style='margin-bottom: 5px;'>شماره تلفن معتبر نیست</li>";
    }
    else if (password != "" && repassword == "") {
      Errors += "<li style='margin-bottom: 5px;'>تکرار گذرواژه خالی است</li>";
    }
    else if (password != repassword) {
      Errors += "<li style='margin-bottom: 5px;'>تکرار گذرواژه اشتباه است</li>";
    }
    else {
        if (password == "") {
          $("#id_Password").val("None")
          $("#id_rePassword").val("None")
        }
        $.ajax({
            type:"POST",
            url:"http://" + window.location.host + "/Farshtore/Edit_Profile_Seller_user/None",
            data:$(".frm-Edit-Seller").serialize(),
            success:function(result) {
              $("#id_Password").val("")
              $("#id_rePassword").val("")
              if (result == "Exist") {
                Errors += "کاربر با این اطلاعات وجود دارد"
                $(".Error-List-Leg").removeAttr("hidden");
                $(".Error-List-Leg").html(Errors);
              }
            },
            error:function(e){
                alert("error");
            }
        });
    }
        $(".Error-List-Leg").removeAttr("hidden");
        $(".Error-List-Leg").html(Errors);
  });
    Change_Sh = "";
  let Shaba_Num = $(".Shaba_Num").text();
  let Cart_Num = $(".Cart_Num").text();
  let None_SH = $(".None_SH").text();
    if (Shaba_Num == "None") {
      if (Cart_Num != "None") {
          $("#id_Number_Sh").val(Cart_Num);
    }
  }
  else if (Cart_Num == "None") {
        $(".Seller_Gen_num").val("");
        $(".text-Change").toggleClass('changed');
        if ($(".text-Change").hasClass('changed')) {
          $(".text-Change").text("ثبت شماره کارت به‌جای شماره شبا");
          $(".lbl-N-Code").text("شماره شبا");
          $(".Seller_Gen_num").removeClass("Card-Number").addClass("Shaba-Number");
          $(".Seller_Gen_num").attr('placeholder','000000000000000000000000');
          $("#id_Number_Sh").val(Shaba_Num);
          let inputField = $('.Seller_Gen_num');

          inputField.prop('maxlength', 24);
      }
  }

  $(".Change_Info_Seller_Gen").click(function() {

    let Errors = "";
    let national_code = $("#id_National_Code").val();
    let Phone = $("#id_Phone").val();
    let Num_Sh = $("#id_Number_Sh").val();
    let Shop_Name = $("#id_ShopName").val();
    let password = $("#id_Password").val();
    let repassword = $("#id_rePassword").val();
    let Num_S = "";
    if ($("#id_Number_Sh").hasClass("Card-Number")) {
      Num_S = "Card"
    }
    else if ($("#id_Number_Sh").hasClass("Shaba-Number")) {
      Num_S = "Shaba"
    }

  
    if (national_code == "" || Num_Sh == "" || Phone == "") {
      Errors += "<li style='margin-bottom: 5px;'>اطلاعات شخصی خود را پر کنید</li>";
    }
    else if (national_code.length < 10) {
      Errors += "<li style='margin-bottom: 5px;'>کد ملی معتبر نیست</li>";
    }
    else if (Phone.length < 11) {
      Errors += "<li style='margin-bottom: 5px;'>شماره تلفن معتبر نیست</li>";
    }
    else if (Shop_Name == "") {
      Errors += "<li style='margin-bottom: 5px;'>نام فروشگاه خود را انتخاب کنید کنید</li>";
    }
    else if (password != "" && repassword == "") {
      Errors += "<li style='margin-bottom: 5px;'>تکرار گذرواژه خالی است</li>";
    }
    else if (password != repassword) {
      Errors += "<li style='margin-bottom: 5px;'>تکرار گذرواژه اشتباه است</li>";
    }
    else {
        if (password == "") {
          $("#id_Password").val("None")
          $("#id_rePassword").val("None")
        }
        $.ajax({
            type:"POST",
            url:"http://" + window.location.host + "/Farshtore/Edit_Profile_Seller_user/" + Num_S,
            data:$(".frm-Edit-Seller-Gen").serialize(),
            success:function(result) {
              $("#id_Password").val("")
              $("#id_rePassword").val("")
              if (result == "Exist") {
                Errors += "کاربری با این اطلاعات وجود دارد"
                $(".Error-List").removeAttr("hidden");
                $(".Error-List").html(Errors);
              }
            },
            error:function(e){
                alert("error");
            }
        });
    }
        $(".Error-List").removeAttr("hidden");
        $(".Error-List").html(Errors);
  });

});