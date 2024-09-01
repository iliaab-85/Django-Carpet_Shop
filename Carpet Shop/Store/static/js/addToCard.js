$(document).ready(function() {
    var Product_Code = $(".Product_Code").text();
    let Count = $('.block_quantity__number').val();
    $(".button_addToCard").click(function(){
    if (Count == 0) {
        $('.block_quantity__number').val(1);
    }
    else {
        Count = $('.block_quantity__number').val();
    }
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/Farshtore/Order_Set/" + Product_Code + "/" + Count,
            success: function(Product) {
            },
            error: function(e) {
                alert("error");
            }
        });
    });
});