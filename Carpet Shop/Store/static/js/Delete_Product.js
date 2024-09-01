$(document).ready(function() {
    var Product_Code = $(".Product_Code").text();
    $(".close").click(function(){
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/Farshtore/Delete_Set/" + Product_Code,
            success: function(Product) {
            },
            error: function(e) {
                alert("error");
            }
        });
    });
});