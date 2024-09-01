$(document).ready(function() {
    Load_Order_Products()
    function Load_Order_Products() {
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/Farshtore/Order_Product",
        success: function(Order_Product) {
            let obj_order = JSON.parse(Order_Product);
            let Count = 0;
            let Price = 0;
            let my_List_Count = [];
            let Order_Len = obj_order.length;
            let product_order ="<div class='title'>"+
                                    "<div class='row'>"+
                                        "<div class='col align-self-center text-left text-muted'>"+
                                            "<bdi dir='rtl'>" + Order_Len + " محصول</bdi>"+
                                        "</div>"+
                                        "<bdi class='col align-self-center text-right text-muted' style='text-align: right;'><h4><bdi>سبد خرید</bdi></h4></bdi>"+
                                    "</div>"+
                                "</div>";
            if (Order_Len > 0) {
                for (item in obj_order)
                    {
                    if (Count == 0) {
                        Count+= 1;
                    }
                    else if (Count +1 == Order_Len) {
                    }
                    else {
                        Count+= 1;
                    }
                        product_order +=
                            "<div class='row'>"+
                        "<div class='row main align-items-center'>"+
                        "<a style='display: contents;' href=/Farshtore/product_information/" + obj_order[item].fields.Product_Code + ">"+
                            "<div class='col-2'><img class='img-fluid' src='/../static/img/picture.jpg'></div>"+
                        "</a>"+
                            "<div class='col'>"+
                                "<div class='row text-muted'>" + obj_order[item].fields.Product_Type + "</div>"+
                                "<div class='row'>" + obj_order[item].fields.Product_Title + "</div>"+
                            "</div>"+
                            "<div style='user-select:none;' class='col'>"+
                                "<div hidden class='Product_Code'>" + obj_order[item].fields.Product_Code + "</div>"+
                                "<a style='cursor:pointer;' onclick='Minus(this)'>-</a><a href='#' class='border'>" + obj_order[item].fields.Product_Count + "</a><a style='cursor:pointer;' onclick='Incrase(this)'>+</a>"+
                            "</div>"+
                            "<div class='col' style='display: flex;'><bdi>" + obj_order[item].fields.Product_Price + " تومان </bdi><span class='close' onclick='Delete_Product(" + obj_order[item].fields.Product_Code + ")'>&#10005;</span></div>"+
                        "</div>"+
                    "</div>";
                    Price += obj_order[item].fields.Product_Price

                    my_List_Count.push(obj_order[item].fields.Product_Count * obj_order[item].fields.Product_Price)
                }
            }
            else {
                product_order += "<div class='Empty'>"+
                "<div class='empty-center'>"+
                    "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                "</div>"+
                "<p class='text-center'>سبد خرید شما خالی است</p>"+
            "</div>";
            }
            var total = 0
            for (var i = 0; i < my_List_Count.length; i++) {
                total += my_List_Count[i]
            }
            $(".cart").html(product_order);
            $(".product-price").html(total);
            $(".final_prices").html(total);
            $(".Product-Count").html(obj_order.length);
        },
        error: function(e) {
            alert("error");
        }
    });
    }
});

function Load_Order_Products() {
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/Farshtore/Order_Product",
        success: function(Order_Product) {
            let obj_order = JSON.parse(Order_Product);
            let Count = 0;
            let Price = 0;
            let my_List_Count = [];
            let Order_Len = obj_order.length;
            let product_order ="<div class='title'>"+
                                    "<div class='row'>"+
                                        "<div class='col align-self-center text-left text-muted'>"+
                                            "<bdi dir='rtl'>" + Order_Len + " محصول</bdi>"+
                                        "</div>"+
                                        "<bdi class='col align-self-center text-right text-muted' style='text-align: right;'><h4><bdi>سبد خرید</bdi></h4></bdi>"+
                                    "</div>"+
                                "</div>";
            if (Order_Len > 0) {
                for (item in obj_order)
                    {
                    if (Count == 0) {
                        Count+= 1;
                    }
                    else if (Count +1 == Order_Len) {
                    }
                    else {
                        Count+= 1;
                    }
                        product_order +=
                            "<div class='row'>"+
                        "<div class='row main align-items-center'>"+
                        "<a style='display: contents;' href=/Farshtore/product_information/" + obj_order[item].fields.Product_Code + ">"+
                            "<div class='col-2'><img class='img-fluid' src='/../static/img/picture.jpg'></div>"+
                        "</a>"+
                            "<div class='col'>"+
                                "<div class='row text-muted'>" + obj_order[item].fields.Product_Type + "</div>"+
                                "<div class='row'>" + obj_order[item].fields.Product_Title + "</div>"+
                            "</div>"+
                            "<div style='user-select:none;' class='col'>"+
                                "<div hidden class='Product_Code'>" + obj_order[item].fields.Product_Code + "</div>"+
                                "<a style='cursor:pointer;' onclick='Minus(this)'>-</a><a href='#' class='border'>" + obj_order[item].fields.Product_Count + "</a><a style='cursor:pointer;' onclick='Incrase(this)'>+</a>"+
                            "</div>"+
                            "<div class='col' style='display: flex;'><bdi>" + obj_order[item].fields.Product_Price + " تومان </bdi><span class='close' onclick='Delete_Product(" + obj_order[item].fields.Product_Code + ")'>&#10005;</span></div>"+
                        "</div>"+
                    "</div>";
                    Price += obj_order[item].fields.Product_Price

                    my_List_Count.push(obj_order[item].fields.Product_Count * obj_order[item].fields.Product_Price)
                }
            }
            else {
                product_order += "<div class='Empty'>"+
                "<div class='empty-center'>"+
                    "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                "</div>"+
                "<p class='text-center'>سبد خرید شما خالی است</p>"+
            "</div>";
            }
            var total = 0
            for (var i = 0; i < my_List_Count.length; i++) {
                total += my_List_Count[i]
            }
            $(".cart").html(product_order);
            $(".product-price").html(total);
            $(".final_prices").html(total);
            $(".Product-Count").html(obj_order.length);
        },
        error: function(e) {
            alert("error");
        }
    });
    }

function Incrase(element) {
    let currentValue = parseInt(element.previousElementSibling.innerHTML);
    currentValue++;
    element.previousElementSibling.innerHTML = currentValue;
    let Prduct_Code = $(element).parents('.col');
    let Product_Code = $(Prduct_Code).find('.Product_Code').text();
    let func = "Incrase";

    $.ajax({
        type:"POST",
        url:"http://" + window.location.host + "/Farshtore/Save_Count/" + Product_Code + "/" + func,

        success:function(result) {
            Load_Order_Products()
        },
        error:function(e){
            alert("error");
        }
    });
  }

function Minus(element) {
    let currentValue = parseInt(element.nextElementSibling.innerHTML);
    if (currentValue > 1) {
        let Prduct_Code = $(element).parents('.col');
        let Product_Code = $(Prduct_Code).find('.Product_Code').text();
        let func = "Minus"
        currentValue--;
        element.nextElementSibling.innerHTML = currentValue;

        $.ajax({
                type:"POST",
                url:"http://" + window.location.host + "/Farshtore/Save_Count/" + Product_Code + "/" + func,

                success:function(result) {
                    Load_Order_Products()
                },
                error:function(e){
                    alert("error");
                }
        });
    }
  }

function Delete_Product(Product_Code) {
    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:8000/Farshtore/Delete_Set/" + Product_Code,
        success: function() {
            $.ajax({
                type: "POST",
                url: "http://127.0.0.1:8000/Farshtore/Order_Product",
                success: function(Order_Product) {
                    let obj_order = JSON.parse(Order_Product);
                    let Count = 0;
                    let Price = 0;
                    let my_List_Count = [];
                    let Order_Len = obj_order.length;
                    let product_order ="<div class='title'>"+
                                            "<div class='row'>"+
                                                "<div class='col align-self-center text-left text-muted'>"+
                                                    "<bdi dir='rtl'>" + Order_Len + " محصول</bdi>"+
                                                "</div>"+
                                                "<bdi class='col align-self-center text-right text-muted' style='text-align: right;'><h4><bdi>سبد خرید</bdi></h4></bdi>"+
                                            "</div>"+
                                        "</div>";
                    if (Order_Len > 0) {
                        for (item in obj_order)
                            {
                            if (Count == 0) {
                                Count+= 1;
                            }
                            else if (Count +1 == Order_Len) {
                            }
                            else {
                                Count+= 1;
                            }
                                product_order +=
                                    "<div class='row'>"+
                                "<div class='row main align-items-center'>"+
                                "<a style='display: contents;' href=/Farshtore/product_information/" + obj_order[item].fields.Product_Code + ">"+
                                    "<div class='col-2'><img class='img-fluid' src='/../static/img/picture.jpg'></div>"+
                                "</a>"+
                                    "<div class='col'>"+
                                        "<div class='row text-muted'>" + obj_order[item].fields.Product_Type + "</div>"+
                                        "<div class='row'>" + obj_order[item].fields.Product_Title + "</div>"+
                                    "</div>"+
                                    "<div style='user-select:none;' class='col'>"+
                                        "<div hidden class='Product_Code'>" + obj_order[item].fields.Product_Code + "</div>"+
                                        "<a style='cursor:pointer;' onclick='Minus(this)'>-</a><a href='#' class='border'>" + obj_order[item].fields.Product_Count + "</a><a style='cursor:pointer;' onclick='Incrase(this)>+</a>"+
                                    "</div>"+
                                    "<div class='col' style='display: flex;'><bdi>" + obj_order[item].fields.Product_Price + " تومان </bdi><span class='close' onclick='Delete_Product(" + obj_order[item].fields.Product_Code + ")'>&#10005;</span></div>"+
                                "</div>"+
                            "</div>";
                            Price += obj_order[item].fields.Product_Price
                            my_List_Count.push(obj_order[item].fields.Product_Count * obj_order[item].fields.Product_Price)
                            
                        }
                    }
                    else {
                        product_order += "<div class='Empty'>"+
                        "<div class='empty-center'>"+
                            "<img src='/../static/img/empty-cart.svg' style='width: 140px;'>"+
                        "</div>"+
                        "<p class='text-center'>سبد خرید شما خالی است</p>"+
                    "</div>";
                    }
                    var total = 0
                    for (var i = 0; i < my_List_Count.length; i++) {
                        total += my_List_Count[i]
                    }
                    $(".cart").html(product_order);
                    $(".product-price").html(total);
                    $(".final_prices").html(total);
                    $(".Product-Count").html(obj_order.length);
                },
                error: function(e) {
                    alert("error");
                }
            });
        },
        error: function(e) {
            alert("error");
        }
    });
}

$(".btn-final").click(function() {
        $.ajax({
                type:"POST",
                url:"http://" + window.location.host + "/Farshtore/Order_Complete/" + $('.final_prices').text(),
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
        $.ajax({
            type:"POST",
            url:"http://" + window.location.host + "/Farshtore/Order_complete_Remove",
            error:function(e){
                alert("error");
            }
        });
});