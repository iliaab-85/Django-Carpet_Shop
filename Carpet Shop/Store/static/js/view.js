$(document).ready(function() {
    var code = $(".Product_Code").text();
    var seconds = 0;
    var timer = setInterval(function() {
        seconds++;
        if (seconds == 5) {
            $.ajax({
                    type:"POST",
                    url:"http://127.0.0.1:8000/Farshtore/Addview/" + code,
                    error:function(e){
                        alert("error");
                    }
            });
            clearInterval(timer);
        }
    }, 1000);
});