$(document).ready(function () {
    $('.text-block').click(function () { 
        let Sort = $(this).text();
        var Sort_Trim = $.trim(Sort);
        let func = "Search_Sort";
        window.location.href = "/Farshtore/product/" + func + "/" + Sort_Trim;
    });
});