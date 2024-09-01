
var settings = {
  "url": "http://127.0.0.1:8000/apiread_product/?format=json",
  "method": "GET",
  "timeout": 0,
};

$.ajax(settings).done(function (response) {
    Load_Products(response);
});

function Load_Products(obj) {
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
                  Product +="<div class='Product-Div'>"+
                  "<a href='/Farshtore/product_information/" + Product_Code + "'>"+
                      "<div>"+
                          "<div class='row main align-items-center'>"+
                              "<div class='col-1'>"+
                                  "<img class='img-fluid' style='width: 100px;height: 100%;' src='/../static/img/picture.jpg'>"+
                              "</div>"+
                              "<div class='col' style='font-size: 1rem;color:black;'>"+
                                  "<bdi>" + item.Product_Title + "</bdi>"+
                              "</div>"+
                              "<div class='col' style='font-size: 1rem;color:black;'>"+
                                  "<bdi><span> قیمت :</span> <span style='color:orange;'>" + item.Product_Price + "&nbsp;</span>تومان</bdi>"+
                              "</div>"+
                          "</div>"+
                      "</div>"+
                  "</a>"+
              "</div>";
              }
            }
          });
          requests.push(request);
        };

        $.when(...requests).then(function() {
          $(".Prdct_Like").html(Product);
        });
    };