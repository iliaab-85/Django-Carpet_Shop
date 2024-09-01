
    let func = $('.func').text();
    let Sort = $('.Sort').text();

    if (func != "None" | Sort != "None") {

        if (func == "Search") {
        let Product = "";
            $.ajax({
                type:"POST",
                url:"http://127.0.0.1:8000/Farshtore/Search/" + String(Sort),
                success:function(Products) {
                    if (Products == "Not_found") {
                        Product += "<div class='Empty'>"+
                    "<div class='empty-center'>"+
                    "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                    "</div>"+
                    "<p class='text-center'>محصولی یافت نشد</p>"+
                    "</div>";

                    Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                            "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                        "</div>"
                    $(".AllProduct").html(Product);
                    }
                    else {
                        const obj_Product = JSON.parse(Products);
                        Load_Products(obj_Product);
                    }
                },
                error:function(e){
                    alert("error");
                }
            });
        }

        else if (func == "Search_Sort") {

            let Mylist_sorts = ["دست باف", "ماشینی", "کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک", "فانتزی",
                "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

            if (Mylist_sorts.includes(Sort)) {
                Text_Sort = $("#Brand").text();
                if (Text_Sort == "") {
                    Text_Sort = "None";
                }
            }
            else {
                Text_Sort = $("#Sort").text();
                if (Text_Sort == "") {
                    Text_Sort = "None";
                }
            }
            let Product = "";
            $.ajax({
                type:"POST",
                url:"http://127.0.0.1:8000/Farshtore/Search_Sort/" + Sort + "/" + Text_Sort + "/None/None",
                success:function(Products) {
                    if (Products == "False") {
                        Product += "<div class='Empty'>"+
                    "<div class='empty-center'>"+
                    "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                    "</div>"+
                    "<p class='text-center'>محصولی یافت نشد</p>"+
                    "</div>";

                    Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                            "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                        "</div>"
                    $(".AllProduct").html(Product);
                        Load_Sort(Sort);
                    }
                    else {
                        const obj_Product = JSON.parse(Products);
                        Load_Products_Sort(obj_Product);
                        Load_Sort(Sort);
                    }
                },
                error:function(e){
                    alert("error");
                }
            });
        }

    }


function get_text_Sort(Sort_Text) {
        let text = $(Sort_Text).text();
        let Text_res = text.trim();
        let Text_Sort;
        let Price_Start = $(".Price_Start").val();
        let Price_End = $(".Price_End").val();
        let Mylist_sorts = ["دست باف", "ماشینی", "کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک", "فانتزی",
                        "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۰۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"]

        if (Mylist_sorts.includes(Text_res)) {
            Text_Sort = $("#Brand").text();
            if (Text_Sort == "") {
                Text_Sort = "None";
            }
        }
        else {
            Text_Sort = $("#Sort").text();
            if (Text_Sort == "") {
                Text_Sort = "None";
            }
        }
        if (Price_Start == "") {
            Price_Start = "None";
        }
        if (Price_End == "") {
            Price_End = "None";
        }
        let Product = "";
        $.ajax({
            type:"POST",
            url:"http://127.0.0.1:8000/Farshtore/Search_Sort/" + Text_res + "/" + Text_Sort + "/" + String(Price_Start) + "/" + String(Price_End),
            success:function(Products) {
                if (Products == "False") {
                    Product += "<div class='Empty'>"+
                    "<div class='empty-center'>"+
                    "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                    "</div>"+
                    "<p class='text-center'>محصولی یافت نشد</p>"+
                    "</div>";

                    Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                            "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                        "</div>"
                    $(".AllProduct").html(Product);
                    Load_Sort(Text_res);
                }
                else {
                    const obj_Product = JSON.parse(Products);
                    Load_Products_Sort(obj_Product);
                    Load_Sort(Text_res);
                }
            },
            error:function(e){
                alert("error");
            }
    });
    };

function get_text_Res(Sort_Text) {
    let Res = $(Sort_Text).text();
    let Text_Res = Res.trim();
    let Product = "";
    $.ajax({
            type:"POST",
            url:"http://127.0.0.1:8000/Farshtore/Search_Res/" + Text_Res,
            success:function(Products) {
                if (Products == "Not_found") {
                    Product += "<div class='Empty'>"+
                    "<div class='empty-center'>"+
                    "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                    "</div>"+
                    "<p class='text-center'>محصولی یافت نشد</p>"+
                    "</div>";

                    Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                            "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                        "</div>"
                    $(".AllProduct").html(Product);
                }
                else {
                    const obj_Product = JSON.parse(Products);
                    Load_Products_Sort(obj_Product);
                }
            },
            error:function(e){
                alert("error");
            }
    });
}

function get_text_Rag(Sort_Text) {
    let Rag = $(Sort_Text).text();
    let Text_Rag = Rag.trim();
    let Product = "";
    $.ajax({
            type:"POST",
            url:"http://127.0.0.1:8000/Farshtore/Search_Rag/" + Text_Rag,
            success:function(Products) {
                if (Products == "Not_found") {
                    Product += "<div class='Empty'>"+
                    "<div class='empty-center'>"+
                    "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                    "</div>"+
                    "<p class='text-center'>محصولی یافت نشد</p>"+
                    "</div>";

                    Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                            "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                        "</div>"
                    $(".AllProduct").html(Product);
                }
                else {
                    const obj_Product = JSON.parse(Products);
                    Load_Products_Sort(obj_Product);
                }
            },
            error:function(e){
                alert("error");
            }
    });
}

    function Load_Products(obj) {
        console.log(obj);
        let user_st = $('.user_st').text();
        if (user_st == "True") {

            let Product = "";
            let Like_Product_Code;
            let requests = [];

            for (let i = 0; i < obj.length; i++) {
            const item = obj[i];
            const Product_Code = item.Product_Code;
            console.log(Product_Code);
            const request = $.ajax({
                type: "POST",
                url: `http://127.0.0.1:8000/Farshtore/Search_Like/${Product_Code}`,
                success: function(Read_Likes) {
                const obj_like = JSON.parse(Read_Likes);
                obj_like.forEach((items) => {
                    Like_user_Id = items.user_Id
                    Like_Product_Code = items.Product_Code
                });
                if (Product_Code == Like_Product_Code )
                {
                    like_Class = "text-block-prdct-active";
                    svg_like_Class = "svg-like";
                }
                else
                {
                    like_Class = "text-block-prdct";
                    svg_like_Class = "place-love";
                }
                Product += "<div class='col-xl-3 col-lg-4 col-md-6 wow fadeInUp' style='width:24%;' data-wow-delay='0.7s'>"+
                "<div class='product-item' style='border-radius: 20px;background:white;box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>"+
                    "<a href=/Farshtore/product_information/" + Product_Code + ">"+
                        "<div class='position-relative overflow-hidden' style='background: white;border-top-right-radius: 22px;border-top-left-radius: 22px;'>"+
                        "<div class='img-holder'>"+
                            "<img class='img-fluid w-100' src='/../static/img/picture.jpg' alt=''>"+
                        "</div>"+
                            "<div class='text-block-prdct' data-code=" + Product_Code + ">"+
                                "<i style='color:#e3dfde;text-shadow:0 0 3px black, 0 0 5px black;'>"+
                                    "<a class='text-body' style='cursor:pointer;'>"+
                                        "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-heart-fill place-love' viewBox='0 0 16 16'>"+
                                            "<path fill-rule='evenodd' d='M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314'/>"+
                                        "</svg>"+
                                    "</a>"+
                                "</i>"+
                            "</div>"+
                            "<div class='bg-secondary rounded text-white position-absolute start-0 top-0 m-4 py-1 px-3'>جدید</div>"+
                        "</div>"+
                    "</a>"+
                        "<div style='margin-top:20px;'>"+
                        "<div class='text-center prdct-footer' style=''>"+
                            "<p class='d-block h5' style='padding-bottom: 10px;cursor:pointer;'>" + item.Product_Title + "</p>"+
                            "<div class=''>"+
                                "<div>"+
                                    "<div style='display: flex;justify-content: center;'>"+
                                        "<bdi class='text-price me-1' style='margin: 0 10% 0 16%;'><span>" + item.Product_Price_Final + "</span> تومان</bdi><br>"+
                                        "<p class='p-prdct'>" + item.Product_Price_Discount + "%</p>"+
                                    "</div>"+
                                    "<div>"+
                                        "<bdi class='text-price me-1' style='margin:0;color:#eb4b4b;text-decoration: line-through;'>"+
                                        "<span>" + item.Product_Price + "</span> تومان</bdi>"+
                                    "</div>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</div>";
                }
            });
            requests.push(request);
            };

            $.when(...requests).then(function() {
            Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                            "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                        "</div>"
            $(".AllProduct").html(Product);
            });
        }
        else {
            let Product = "";
            My_List = [];
            obj.forEach((item) => {
            Product_Code = item.fields.Product_Code

            Product += "<div class='col-xl-3 col-lg-4 col-md-6 wow fadeInUp' style='width:24%;' data-wow-delay='0.7s'>"+
                "<div class='product-item' style='border-radius: 20px;background:white;box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>"+
                    "<a href=/Farshtore/product_information/" + Product_Code + ">"+
                        "<div class='position-relative overflow-hidden' style='background: white;border-top-right-radius: 22px;border-top-left-radius: 22px;'>"+
                        "<div class='img-holder'>"+
                            "<img class='img-fluid w-100' src='/../static/img/picture.jpg' alt=''>"+
                        "</div>"+
                            "<div class='text-block-prdct' data-code=" + Product_Code + ">"+
                                "<i style='color:#e3dfde;text-shadow:0 0 3px black, 0 0 5px black;'>"+
                                    "<a class='text-body' style='cursor:pointer;'>"+
                                        "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-heart-fill place-love' viewBox='0 0 16 16'>"+
                                            "<path fill-rule='evenodd' d='M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314'/>"+
                                        "</svg>"+
                                    "</a>"+
                                "</i>"+
                            "</div>"+
                            "<div class='bg-secondary rounded text-white position-absolute start-0 top-0 m-4 py-1 px-3'>جدید</div>"+
                        "</div>"+
                    "</a>"+
                        "<div style='margin-top:20px;'>"+
                        "<div class='text-center prdct-footer' style=''>"+
                            "<p class='d-block h5' style='padding-bottom: 10px;cursor:pointer;'>" + item.Product_Title + "</p>"+
                            "<div class=''>"+
                                "<div>"+
                                    "<div style='display: flex;justify-content: center;'>"+
                                        "<bdi class='text-price me-1' style='margin: 0 10% 0 16%;'><span>" + item.Product_Price_Final + "</span> تومان</bdi><br>"+
                                        "<p class='p-prdct'>" + item.Product_Price_Discount + "%</p>"+
                                    "</div>"+
                                    "<div>"+
                                        "<bdi class='text-price me-1' style='margin:0;color:#eb4b4b;text-decoration: line-through;'>"+
                                        "<span>" + item.Product_Price + "</span> تومان</bdi>"+
                                    "</div>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</div>";
        });
            My_List.push(Product);
        
        Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                        "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                    "</div>"
        $(".AllProduct").html(Product);
        }
    }
    
    function Load_Products_Sort(obj) {
        let user_st = $('.user_st').text();
        if (user_st == "True") {
        let Product = "";
        let Like_Product_Code;
        let requests = [];

        for (let i = 0; i < obj.length; i++) {
          const item = obj[i];
          const Product_Code = item.Product_Code;
          const request = $.ajax({
            type: "POST",
            url: `http://127.0.0.1:8000/Farshtore/Search_Like/${Product_Code}`,
            success: function(Read_Likes) {
              const obj_like = JSON.parse(Read_Likes);
              obj_like.forEach((items) => {
                  Like_user_Id = items.user_Id
                  Like_Product_Code = items.Product_Code
              });
              if (Product_Code == Like_Product_Code )
              {
                  like_Class = "text-block-prdct-active";
                  svg_like_Class = "svg-like";
              }
              else
              {
                  like_Class = "text-block-prdct";
                  svg_like_Class = "place-love";
              }
              Product += "<div class='col-xl-3 col-lg-4 col-md-6 wow fadeInUp' style='width:24%;' data-wow-delay='0.7s'>"+
                  "<div class='product-item' style='border-radius: 20px;background:white;box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>"+
                      "<a href=/Farshtore/product_information/" + Product_Code + ">"+
                          "<div class='position-relative overflow-hidden' style='background: white;border-top-right-radius: 22px;border-top-left-radius: 22px;'>"+
                          "<div class='img-holder'>"+
                              "<img class='img-fluid w-100' src='/../static/img/picture.jpg' alt=''>"+
                          "</div>"+
                              "<div class='" + like_Class + "' onclick=Toggle_Like(this," + Product_Code + ") data-code=" + Product_Code + ">"+
                                  "<i style='color:#e3dfde;text-shadow:0 0 3px black, 0 0 5px black;'>"+
                                      "<a class='text-body' style='cursor:pointer;'>"+
                                          "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-heart-fill " + svg_like_Class + "' viewBox='0 0 16 16'>"+
                                              "<path fill-rule='evenodd' d='M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314'/>"+
                                          "</svg>"+
                                      "</a>"+
                                  "</i>"+
                              "</div>"+
                              "<div class='bg-secondary rounded text-white position-absolute start-0 top-0 m-4 py-1 px-3'>جدید</div>"+
                          "</div>"+
                      "</a>"+
                          "<div style='margin-top:20px;'>"+
                          "<div class='text-center prdct-footer' style=''>"+
                              "<p class='d-block h5' style='padding-bottom: 10px;cursor:pointer;'>" + item.Product_Title + "</p>"+
                              "<div class=''>"+
                                  "<div>"+
                                      "<div style='display: flex;justify-content: center;'>"+
                                          "<bdi class='text-price me-1' style='margin: 0 10% 0 16%;'><span>" + item.Product_Price + "</span> تومان</bdi><br>"+
                                          "<p class='p-prdct'>20%</p>"+
                                      "</div>"+
                                      "<div>"+
                                          "<bdi class='text-price me-1' style='margin:0;color:#eb4b4b;text-decoration: line-through;'>"+
                                          "<span>" + item.Product_Price_Final + "</span> تومان</bdi>"+
                                      "</div>"+
                                  "</div>"+
                              "</div>"+
                          "</div>"+
                      "</div>"+
                  "</div>"+
              "</div>";
            }
          });

          requests.push(request);
        };
        $.when(...requests).then(function() {
          Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                          "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                      "</div>"
          $(".AllProduct").html(Product);
        });
        }
        else {
            let Product = "";
            My_List = [];
            obj.forEach((item) => {
            Product_Code = item.Product_Code

            Product += "<div class='col-xl-3 col-lg-4 col-md-6 wow fadeInUp' style='width:24%;' data-wow-delay='0.7s'>"+
                "<div class='product-item' style='border-radius: 20px;background:white;box-shadow: 0 6px 20px 0 rgba(0, 0, 0, 0.19);'>"+
                    "<a href=/Farshtore/product_information/" + Product_Code + ">"+
                        "<div class='position-relative overflow-hidden' style='background: white;border-top-right-radius: 22px;border-top-left-radius: 22px;'>"+
                        "<div class='img-holder'>"+
                            "<img class='img-fluid w-100' src='/../static/img/picture.jpg' alt=''>"+
                        "</div>"+
                            "<div class='text-block-prdct' data-code=" + Product_Code + ">"+
                                "<i style='color:#e3dfde;text-shadow:0 0 3px black, 0 0 5px black;'>"+
                                    "<a class='text-body' style='cursor:pointer;'>"+
                                        "<svg xmlns='http://www.w3.org/2000/svg' width='16' height='16' fill='currentColor' class='bi bi-heart-fill place-love' viewBox='0 0 16 16'>"+
                                            "<path fill-rule='evenodd' d='M8 1.314C12.438-3.248 23.534 4.735 8 15-7.534 4.736 3.562-3.248 8 1.314'/>"+
                                        "</svg>"+
                                    "</a>"+
                                "</i>"+
                            "</div>"+
                            "<div class='bg-secondary rounded text-white position-absolute start-0 top-0 m-4 py-1 px-3'>جدید</div>"+
                        "</div>"+
                    "</a>"+
                        "<div style='margin-top:20px;'>"+
                        "<div class='text-center prdct-footer' style=''>"+
                            "<p class='d-block h5' style='padding-bottom: 10px;cursor:pointer;'>" + item.Product_Title + "</p>"+
                            "<div class=''>"+
                                "<div>"+
                                    "<div style='display: flex;justify-content: center;'>"+
                                        "<bdi class='text-price me-1' style='margin: 0 10% 0 16%;'><span>" + item.Product_Price_Final + "</span> تومان</bdi><br>"+
                                        "<p class='p-prdct'>" + item.Product_Price_Discount + "%</p>"+
                                    "</div>"+
                                    "<div>"+
                                        "<bdi class='text-price me-1' style='margin:0;color:#eb4b4b;text-decoration: line-through;'>"+
                                        "<span>" + item.Product_Price + "</span> تومان</bdi>"+
                                    "</div>"+
                                "</div>"+
                            "</div>"+
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</div>";
        });
            My_List.push(Product);
        
        Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                        "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                    "</div>"
        $(".AllProduct").html(Product);
        }

    }

    function Load_Sort(text) {
      const sortList = ["دست باف", "ماشینی", "کامپیوتری", "اکسسوری", "تابلو فرش", "بیضی و گرد", "کلاسیک", "فانتزی",
                        "کودک", "ابزار قالی بافی", "گلیم", "۷۰۰ شانه", "۱۲۰۰ شانه", "۱۵۰۰ شانه"];
      const isSort = sortList.includes(text);
      if (isSort) {
        $("#Sort").html(text);
      }
      else {
        $("#Brand").html(text);
      }
    };

    function Load_Price(Start,End) {
        $("#Price_S").html(Start);
        $("#Price_E").html(End);
    };

    function Load_Sort_Price() {
        let Price_Start = $(".Price_Start").val();
        let Price_End = $(".Price_End").val();
        let Text_Sort = $("#Sort").text();
        let Text_Brand = $("#Brand").text();
        if (Text_Sort == "") {
            Text_Sort = "None";
        }
        if (Text_Brand == "") {
            Text_Brand = "None";
        }
        let Product = "";
        $.ajax({
            type:"POST",
            url:"http://127.0.0.1:8000/Farshtore/Search_Price/" + Price_Start + "/" + Price_End + "/" + Text_Sort + "/" + Text_Brand,
            success:function(Products) {
                if (Products == "Not_found") {
                    Product += "<div class='Empty'>"+
                    "<div class='empty-center'>"+
                    "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                    "</div>"+
                    "<p class='text-center'>محصولی یافت نشد</p>"+
                    "</div>";

                    Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                            "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                        "</div>"
                    $(".AllProduct").html(Product);
                    Load_Price(Price_Start,Price_End);
                }
                else {
                    const obj_Product = JSON.parse(Products);
                    Load_Products(obj_Product);
                    Load_Price(Price_Start,Price_End);
                }
            },
            error:function(e){
                alert("error");
            }
    });
    };

    function Search_Product() {
        let txt_Serach = $(".input_Search").val();
        if (txt_Serach == "") {
            txt_Serach ="None";
        }
        let Product = "";
        var form = new FormData();
        var settings = {
        "url": `http://127.0.0.1:8000/apiSearch_product/?format=json&q=${txt_Serach}`,
        "method": "GET",
        "timeout": 0,
        "processData": false,
        "mimeType": "multipart/form-data",
        "contentType": false,
        "data": form
        };

        $.ajax(settings).done(function (response) {
            let Products = response;
            res = "";
            const obj_Product = JSON.parse(Products);
            if (obj_Product.length == 0) {
                res = "Not_found";
            }
            if (res == "Not_found") {
                Product += "<div class='Empty'>"+
                "<div class='empty-center'>"+
                "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                "</div>"+
                "<p class='text-center'>محصولی یافت نشد</p>"+
                "</div>";

                Product += "<div class='col-12 text-center wow fadeInUp' data-wow-delay='0.1s'>"+
                        "<a class='btn btn-primary rounded-pill py-3 px-5' href='/Farshtore/product/None/None'>محصولات بیشتر</a>"+
                    "</div>"
                $(".AllProduct").html(Product);
            }
            else {
                Load_Products(obj_Product);
            }
                
        });
    }

    $(".Min").click(function(){
        var settings = {
            "url": "http://127.0.0.1:8000/apiread_product/?format=json",
            "method": "GET",
            "timeout": 0,
        };
          
        $.ajax(settings).done(function (response) {
            const Sort_Product = [...response].sort((a, b) => a.Product_Price - b.Product_Price);
            Load_Products_Sort(Sort_Product)
        });
    });

    $(".Max").click(function(){

    });

    /*myArray.sort(function(a, b) {
                  return a - b;
                  console.log(myArray);



                  var myArray = [5, 2, 8, 3, 1];
var n = myArray.length;

for (var i = 0; i < n; i++) {
  var element = myArray[i];
  console.log(element);
}
                });*/