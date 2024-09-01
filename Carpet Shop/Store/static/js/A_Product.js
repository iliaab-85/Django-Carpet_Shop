$(document).ready(function () {

    let Info_Title = $('.Info_Title').html();
    let Brand_D = $('.Brand_div_D').html();
    let Thread_D = $('.Thread_div_D').html();
    let Thread_machine = $('.Thread_div_machine').html();
    let Rag = $('.Rag').html();
    let Size = $('.Size_div').html();
    let Result = $('.Result_div').html();
    let Brand_machine = $('.Brand_div_machine').html();
    let Shane = $('.Shane_div').html();
    let File = $('.File_div').html();
    //let File_img = $('.File_img_div').html();
    let tread_computer = $('.tread_computer_div').html();
    let tread_Accss = $('.tread_Accss_div').html();
    let Size_computer = $('.Size_computer_div').html();
    let Type_Accss = $('.Type_Accss_div').html();
    let Type_un = $('.Type_un_div').html();
    let Thread_Glim = $('.Thread_div_Glim').html();
    let Type_Glim = $('.Type_div_Glim').html();
    let Rag_Tablo = $('.Rag_div_Tablo').html();
    let Thread_Tablo = $('.Thraed_Tablo_div').html();
    let Size_Tablo = $('.Size_Tablo_div').html();
    let Size_Glim = $('.Size_Glim_div').html();
    let Size_Cusan = $('.Size_Cusan_div').html();
    let Accss_Thread = "";
    let ajax = false;

    //شروع کد

    $('#id_Product_Title').on('paste', function(e){
        e.preventDefault();
    });

    $('#id_Product_Caption').on('paste', function(e){
        e.preventDefault();
    });

    $('#id_Product_Price').keypress(function (e) {
        var key = e.which;
        if (key < 48 || key > 57) {
            e.preventDefault();
        }
    });

    $('#id_Product_Price').on('paste', function(e){
        e.preventDefault();
    });

    $('#id_Product_Price_Discount').keypress(function (e) {
        var key = e.which;
        if (key < 48 || key > 57) {
            e.preventDefault();
        }
    });

    $('#id_Product_Price_Discount').on('paste', function(e){
        e.preventDefault();
    });

    $('#id_Product_Price').on('change', function() {
        let Change = $(this).val();
        let Dis = $('.Discount').text();
        if (Change == "") {
            $('.First_Price').text("0");
            $('.Last_Price').text("0");
        }
        else {
            $('.First_Price').text(Math.floor(Change));
            if (Dis == 0) {
                $('.Last_Price').text(Math.floor(Change));
            }
            else if (Dis > 0) {
                let D_Count = Math.floor(Change) * Math.floor(Dis) / 100;
                let result = Math.floor(Change) - Math.floor(D_Count);
                $('.Last_Price').text(Math.floor(result));
            }
            else {
                $('.First_Price').text("0");
                $('.Last_Price').text("0");
                $('.Discount').text("0");
            }
        }
    });

    $('#id_Product_Price_Discount').on('change', function() {
        let Change = $(this).val();
        if (Change == "") {
            $('.Discount').text("0");
            let First = $('.First_Price').text()
            $('.Last_Price').text(Math.floor(First));
        }
        else {
            let F_P = $('.First_Price').text();
            let Discount = Math.floor(F_P) * Math.floor(Change) / 100;
            let result = Math.floor(F_P) - Math.floor(Discount);
            $('.Discount').text(Math.floor(Change));
            $('.Last_Price').text(Math.floor(result));
        }
    });

    $('.dropdown-sort-item').click(function() {
        let Sort_Text = $(this).text();
        $('.Text_Sort').text(Sort_Text);
        let Other_Info = Info_Title;
        if (Sort_Text == "دست باف") {
            Other_Info += Brand_D + Thread_D + Rag + Size + Result;
        }
        else if (Sort_Text == "ماشینی") {
            Other_Info += Brand_machine + Thread_machine + Shane + Size;
        }
        else if (Sort_Text == "نخ و نقشه کامپیوتری") {
            Other_Info += File + tread_computer + Rag + Size_computer;
        }
        else if (Sort_Text == "اکسسوری") {
            Other_Info += tread_Accss + Type_Accss;
        }
        else if (Sort_Text == "۷۰۰ شانه" || Sort_Text == "۱۰۰۰ شانه" ||
                 Sort_Text == "۱۲۰۰ شانه" || Sort_Text == "۱۵۰۰ شانه") {
            Other_Info += Brand_machine + Thread_machine + Size;
        }
        else if (Sort_Text == "کودک" || Sort_Text == "فانتزی" ||
                 Sort_Text == "کلاسیک" || Sort_Text == "بیضی و گرد") {
            Other_Info += Type_un + Size;
        }
        else if (Sort_Text == "گلیم") {
            Other_Info += Thread_Glim + Type_Glim + Size_Glim;
        }
        else if (Sort_Text == "تابلو فرش") {
            Other_Info += Thread_Tablo + Rag_Tablo + Size_Tablo;
        }
        else if (Sort_Text == "ابزار قالی بافی") {
            Other_Info = "";
        }
        $('.A_other_info').html(Other_Info);

    });

    $('.Btn-Style').click(function() {

        let A_Brand_D = $('.A_other_info .A_Select_Style .A_Brand_D').text();
        let A_Brand_machine = $('.A_other_info .A_Select_Style .A_Brand_machine').text();
        let A_thread = $('.A_other_info .A_Select_Style .A_thread').text();
        let A_Rag_Number = $('.A_other_info .A_Select_Style .A_Rag_Number').text();
        let A_Result = $('.A_other_info .A_Select_Style .A_Result').text();
        let A_Shane = $('.A_other_info .A_Select_Style .A_Shane').text();
        let A_Thread_machine = $('.A_other_info .A_Select_Style .A_Thread_machine').text();
        let A_thread_computer = $('.A_other_info .A_Select_Style .A_tread_computer').text();
        let A_tread_Accss = $('.A_other_info .A_Select_Style .A_tread_Accss').text();
        let A_Type_Accss = $('.A_other_info .A_Select_Style .A_Type_Accss').text();
        let A_un_Type = $('.A_other_info .A_Select_Style .A_un_Type').text();
        let A_thread_Glim = $('.A_other_info .A_Select_Style .A_thread_Glim').text();
        let A_Type_Glim = $('.A_other_info .A_Select_Style .A_Type_Glim').text();
        let A_Rag_Tablo = $('.A_other_info .A_Select_Style .A_Rag_Tablo').text();
        let A_Thraed_Tablo = $('.A_other_info .A_Select_Style .A_Thraed_Tablo').text();
        let C1 = $('.w_h .Counter_Size1').val();
        let C2 = $('.w_h .Counter_Size2').val();
        let pdf_File = $('.pdf_File').val();

        let txt_sort = $('.Text_Sort').text();
        let Title = $('#id_Product_Title').val();
        let Caption = $('#id_Product_Caption').val();
        let Images = $('#id_Product_Images').val();
        let Price = $('#id_Product_Price').val();
        let Error_List = "";
        if (ajax == false) {
            if (txt_sort == "خالی") {
                Error_List += "دسته بندی محصول خود را وارد کنید";
            }
            else if (Title == "") {
                Error_List += "عنوان محصول نمیتواند خالی باشد";
            }
            else if (Caption == "") {
                Error_List += "توضیحات الزامی است";
            }
            else if (Images == "") {
                Error_List += "عکس محصول الزامی است";
            }
            else if (Price == "") {
                Error_List += "قیمت محصول الزامی است";
            }
            else if (txt_sort == "دست باف") {
                if (A_Brand_D == "برند") {
                    Error_List += "برند محصول الزامی است";
                }
                else if (A_thread == "نخ") {
                    Error_List += "جنس نخ نمیتواند خالی باشد";
                }
                else if (A_Rag_Number == "رج شمار") {
                    Error_List += "رج شمار الزامی است";
                }
                else if (C1 == "" && C2 == "") {
                    Error_List += "ابعاد را وارد کنید";
                }
                else if (A_Result == "وضعیت") {
                    Error_List += "وضعیت محصول را وارد کنید";
                }
                else {
                    ajax = true;
                }
            }
            else if (txt_sort == "ماشینی") {
                if (A_Brand_machine == "برند") {
                    Error_List += "برند محصول الزامی است";
                }
                else if (A_Thread_machine == "نخ") {
                    Error_List += "جنس نخ نمیتواند خالی باشد";
                }
                else if (A_Shane == "شانه") {
                    Error_List += "شانه الزامی است";
                }
                else if (C1 == "" && C2 == "") {
                    Error_List += "ابعاد را وارد کنید";
                }
                else {
                    ajax = true;
                }
            }
            else if (txt_sort == "نخ و نقشه کامپیوتری") {
                if (pdf_File == "") {
                    Error_List += "فایل محصول الزامی است";
                }
                else if (A_thread_computer == "نخ") {
                    Error_List += "جنس نخ نمیتواند خالی باشد";
                }
                else if (A_Rag_Number == "رج شمار") {
                    Error_List += "رج شمار الزامی است";
                }
                else if (C1 == "" && C2 == "") {
                    Error_List += "ابعاد را وارد کنید";
                }
                else {
                    ajax = true;
                }
            }
            else if (txt_sort == "اکسسوری") {
                if (A_tread_Accss == "نخ") {
                    Error_List += "جنس نخ الزامی است";
                }
                else if (A_Type_Accss == "نوع") {
                    Error_List += "نوع محصول نمیتواند خالی باشد";
                }
                else if (A_Type_Accss == "کوسن") {
                    if (C1 == "" && C2 == "") {
                        Error_List += "ابعاد را وارد کنید";
                    }
                }
                else {
                    ajax = true;
                }
            }
            else if (txt_sort == "کودک" || txt_sort == "فانتزی" ||
                    txt_sort == "کلاسیک" || txt_sort == "بیضی و گرد") {

                if (A_un_Type == "دست باف") {
                    if (A_Brand_D == "برند") {
                        Error_List += "برند محصول الزامی است";
                    }
                    else if (A_thread == "نخ") {
                        Error_List += "جنس نخ نمیتواند خالی باشد";
                    }
                    else if (A_Rag_Number == "رج شمار") {
                        Error_List += "رج شمار الزامی است";
                    }
                    else if (C1 == "" && C2 == "") {
                        Error_List += "ابعاد را وارد کنید";
                    }
                    else if (A_Result == "وضعیت") {
                        Error_List += "وضعیت محصول را وارد کنید";
                    }
                    else {
                        ajax = true;
                    }
                }
                else if (A_un_Type == "ماشینی") {
                    if (A_Brand_machine == "برند") {
                        Error_List += "برند محصول الزامی است";
                    }
                    else if (A_Thread_machine == "نخ") {
                        Error_List += "جنس نخ نمیتواند خالی باشد";
                    }
                    else if (A_Shane == "شانه") {
                        Error_List += "شانه الزامی است";
                    }
                    else if (C1 == "" && C2 == "") {
                        Error_List += "ابعاد را وارد کنید";
                    }
                    else {
                        ajax = true;
                    }
                }
            }
            else if (txt_sort == "گلیم") {
                if (A_thread_Glim == "نخ") {
                    Error_List += "جنس نخ نمیتواند خالی باشد";
                }
                else if (A_Type_Glim == "نوع") {
                    Error_List += "نوع گلیم الزامی است";
                }
                else if (C1 == "" && C2 == "") {
                    Error_List += "ابعاد را وارد کنید";
                }
                else {
                    ajax = true;
                }
            }
            else if (txt_sort == "تابلو فرش") {
                if (A_Thraed_Tablo == "نخ") {
                    Error_List += "جنس نخ نمیتواند خالی باشد";
                }
                else if (A_Rag_Tablo == "نوع") {
                    Error_List += "نوع تابلو فرش الزامی است";
                }
                else if (C1 == "" && C2 == "") {
                    Error_List += "ابعاد را وارد کنید";
                }
                else {
                    ajax = true;
                }
            }
            else if (txt_sort == "ابزار قالی بافی") {
                ajax = true;
            }
        }
        else {
            let txt_sort = $('.Text_Sort').text();
            let Fill_Discount = $('#id_Product_Price_Discount').val();
            if (Fill_Discount == "") {
                $('#id_Product_Price_Discount').val("0");
            }
            let Type_Accss = $('.A_other_info .A_Select_Style .A_Type_Accss').text();
            My_Dict = {"Brand_d":A_Brand_D, "Brand_m":A_Brand_machine, "Thread":A_thread, "Rag":A_Rag_Number,
            "Result":A_Result, "Shane":A_Shane,"Thread_m":A_Thread_machine, "Thread_c":A_thread_computer,
            "Thread_Accss":A_tread_Accss, "Type_Accss":Type_Accss, "Un_Type":A_un_Type,
            "Thread_Glim":A_thread_Glim, "Type_Glim":A_Type_Glim, "Rag_Tablo":A_Rag_Tablo,
            "Thread_Tablo":A_Thraed_Tablo, "C1":C1, "C2":C2, "pdf_File":"pdf_File"};
            Dict = JSON.stringify(My_Dict);
            $.ajax({
                type:"POST",
                url:"http://" + window.location.host + "/Farshtore/add_Product_database/" + txt_sort + "/" + Dict,
                data:$(".Info_Form").serialize(),
                success:function(result) {
                    if (result == "Problem") {
                        let Error_List = "مشکلی در ثبت محصول پیش آمد دوباره تلاش کنید";
                        $(".Error-List").removeAttr("hidden");
                        $('.Error-List').html(Error_List);
                    }
                },
                error:function(e){
                    alert("error");
                }
            });
        }

        $(".Error-List").removeAttr("hidden");
        $('.Error-List').html(Error_List);
    });

    const observer = new MutationObserver(() => {

        $(".A_Select_Style").click(function() {
        let panel = this.nextElementSibling;
        if (panel.style.display === "flex") {
            panel.style.display = "none";
        }
        else {
            panel.style.display = "flex";
        }
        });

        $(".Brand_Select_D").click(function() {
            let Brand = $(this).text();
            $('.A_Brand_D').text(Brand);
        });
        
        $(".Brand_Select_machine").click(function() {
            let Brand = $(this).text();
            $('.A_Brand_machine').text(Brand);
        });

        $(".Thread_Select").click(function() {
          let Thread = $(this).text();
          $('.A_thread').text(Thread);
        });

        $(".Rag_Select").click(function() {
          let Rag = $(this).text();
          $('.A_Rag_Number').text(Rag);
        });
        
        $(".Result_Select").click(function() {
          let Result = $(this).text();
          $('.A_Result').text(Result);
        });
        
        $(".Shane_Select").click(function() {
          let Shane = $(this).text();
          $('.A_Shane').text(Shane);
        });
        
        $(".Thread_Select_machine").click(function() {
          let Brand = $(this).text();
          $('.A_Thread_machine').text(Brand);
        });
        
        $(".tread_computer_Select").click(function() {
          let tread = $(this).text();
          $('.A_tread_computer').text(tread);
        });

        $(".tread_Accss_Select").click(function() {
          let thread = $(this).text();
          $('.A_tread_Accss').text(thread);
          Accss_Thread = thread;
        });
        
        $(".Type_Accss_Select").click(function() {
          let Type = $(this).text();
          let Other_Info = Info_Title;

          if (Type == "کوسن") {
            Other_Info += tread_Accss + Type_Accss + Size_Cusan;
            $('.A_other_info').html(Other_Info);
            $('.A_Type_Accss').html(Type);
          }
          else if (Type != "کوسن") {
            Other_Info += tread_Accss + Type_Accss;
            $('.A_other_info').html(Other_Info);
            $('.A_Type_Accss').html(Type);
          }
          $('.A_tread_Accss').html(Accss_Thread);
        });
        
        $(".Glim_Thread_Select").click(function() {
          let Thread = $(this).text();
          $('.A_thread_Glim').text(Thread);
        });
        
        $(".Glim_Type_Select").click(function() {
          let Type = $(this).text();
          $('.A_Type_Glim').text(Type);
        });
        
        $(".Rag_Tablo_Select").click(function() {
          let Rag = $(this).text();
          $('.A_Rag_Tablo').text(Rag);
        });
        
        $(".Thraed_Tablo_Select").click(function() {
          let Thraed = $(this).text();
          $('.A_Thraed_Tablo').text(Thraed);
        });
        
        $(".Type_un_Select").click(function() {
          let Type = $(this).text();
          $('.A_un_Type').text(Type);
          let Other_Info = Info_Title;
          
          if (Type == "دست باف") {
            Other_Info += Type_un + Brand_D + Thread_D + Rag + Size + Result;
            $('.A_other_info').html(Other_Info)
            $('.A_un_Type').text("دست باف");
        }
        else if (Type == "ماشینی") {
            Other_Info += Type_un + Brand_machine + Thread_machine + Shane + Size;
            $('.A_other_info').html(Other_Info);
            $('.A_un_Type').text("ماشینی");
        }
        });

        $('.Counter_Size1').keypress(function (e) {
          var key = e.which;
          if (key < 48 || key > 57) {
              e.preventDefault();
          }
        });
        $('.Counter_Size2').keypress(function (e) {
          var key = e.which;
          if (key < 48 || key > 57) {
              e.preventDefault();
          }
        });
    
        $('.A_Product_Fields').on('paste', function(e){
            e.preventDefault();
        });

      });
      
      observer.observe(document.body, {
        childList: true,
        subtree: true
      });


});