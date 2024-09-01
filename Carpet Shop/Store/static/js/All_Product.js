$(document).ready(function() {

    var settings = {
  "url": "http://127.0.0.1:8000/apiread_product/?format=json",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
  console.log(response);
});

    let func = $('.func').text();
    let Sort = $('.Sort').text();

    const userId = $('#user_id').text();
    let All_Product;
    let Like_user_Id;
    let Like_Product_Code;
    let svg_like_Class;
    let like_Class;
    if (window.location.href == "http://127.0.0.1:8000/Farshtore/Home") {
        var settings = {
            "url": "http://127.0.0.1:8000/apiread_product/?format=json",
            "method": "GET",
            "timeout": 0,
          };
          
          $.ajax(settings).done(function (response) {
            let obj = response;

                let Product = "";
              if (obj.length == 0) {
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
                Load_Products(obj);
              }
              
          });
            }
              
    else {
        if (Sort == "None" | func == "None") {
            var settings = {
                "url": "http://127.0.0.1:8000/apiread_product/?format=json",
                "method": "GET",
                "timeout": 0,
              };
              
              $.ajax(settings).done(function (response) {
                let obj = response;
                let Product = "";
              if (obj.length == 0) {
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
                Load_Products(obj);
              }
              });
        }
    }

    function Load_Products(obj) {
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
        };
    };
});

    function Empty_Product() {
        let Product = "<div class='Empty'>"+
        "<div class='empty-center'>"+
            "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                "</div>"+
                "<p class='text-center'>محصولی یافت نشد</p>"+
                "</div>";
        $(".AllProduct").html(Product);
    };
  
  let isToggleEnabled = true;

  function Toggle_Like(element, product_Code) {
      if (!isToggleEnabled) {
          return;
      }
  
      isToggleEnabled = false;
  
      let className = element.className;
      let isLiked = $(element).hasClass("text-block-prdct-active");
      let event = isLiked ? "Remove_Like" : "Add_Like";
  
      $(element).removeClass("text-block-prdct text-block-prdct-active").addClass(isLiked ? "text-block-prdct" : "text-block-prdct-active");
      
      $.ajax({
          type: "POST",
          url: "http://127.0.0.1:8000/Farshtore/" + event + "/" + product_Code,
          success: function(result) {
              $(element).find(".bi").toggleClass("svg-like place-love");
          },
          error: function(e) {
              alert("error");
          },
          complete: function() {
              setTimeout(function() {
                  isToggleEnabled = true;
              }, 2000);
          }
      });
  }
