$(document).ready(function () {
    let func = $('.func').text();
    let Sort = $('.Sort').text();

    if (func != "None" | Sort != "None") {
        if (func == "Search") {
            $.ajax({
                type:"POST",
                url:"http://127.0.0.1:8000/Farshtore/Search/" + String(Sort),
                success:function(Products) {
                    if (Products == "False") {
                        Empty_Product();
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

        }
    }
});