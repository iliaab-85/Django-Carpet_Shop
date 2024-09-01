$(document).ready(function () {
    $('.btn_Search').click(function () { 
        let Search_Value = $('.input_Search').val();
        let func = "Search";
        window.location.href = "/Farshtore/product/" + func + "/" + Search_Value;
    });
});