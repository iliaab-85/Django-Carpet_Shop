$(document).ready(function() {
    $(".text-block-prdct,.text-block-prdct-active").click(function() {
        var $this = $(this);
        var code = $this.data("code");
        var codeString = String(code);
        var isLiked = $this.hasClass("text-block-prdct-active");
        var event = isLiked? "Remove_Like" : "Add_Like";

        $this.removeClass("text-block-prdct text-block-prdct-active").addClass(isLiked? "text-block-prdct" : "text-block-prdct-active");

        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/Farshtore/" + event + "/" + codeString,
            success: function(result) {
                $this.find(".bi").toggleClass("svg-like place-love");
            },
            error: function(e) {
                alert("error");
            }
        });
    });
});