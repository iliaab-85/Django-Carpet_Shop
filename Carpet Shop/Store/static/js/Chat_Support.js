$(document).ready(function () {

    let Name = "";
    let Other = "";
    scrollToBottom();
    var isButtonActive = true;
    $(".send_message").click(function(){
        let Get_Message = $(".message_input").val();
        if (Get_Message.length > 0) {
            if (isButtonActive) {
                sendMessage();
                disableButtonForOneMinute();
            }

        }
        $(".message_input").val("");
    });
        function sendMessage() {
        let Place_Messages = "";

        let Message_box = $(".Place_Messages").html();

        let Get_Messages = $(".message_input").val();
        let result = Get_Messages.match(/.{1,70}/g);
        let text_Enter = result.join("<br>");
        let Enter = result.join("\n");

        const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
        const currentDate = new Date();
        const dayOfWeek = daysOfWeek[currentDate.getDay()];
        const hours = currentDate.getHours();
        const minutes = currentDate.getMinutes();
        const time = `${hours}:${minutes}`;
        const datetime = `${dayOfWeek}, ${time}`;

            Place_Messages += "<li class='clearfix'>"+
                                "<div class='message-data text-right'>"+
                                    "<span class='message-data-time'>" + datetime + "</span>"+
                                "</div>"+
                                "<div class='message other-message float-right text_wrapper'>"+
                                    "<div class='text'>" + text_Enter + "</div>"+
                                "</div>"+
                            "</li>";
            Message_box += Place_Messages;
            $(".Place_Messages").html(Message_box);
            $(".message_input").val("");
            let dataCode = $("li.active").data("code");
            scrollToBottom();
            let Other_Id = $('#Other_Id').text();
            $.ajax({
                type:"POST",
                url:"http://" + window.location.host + "/Farshtore/Chat_Save_Support/" + Other_Id + "/" +
                                                        String(text_Enter) + "/" + dataCode + "/" + datetime,

                success:function(result) {
                },
                error:function(e){
                    alert("error");
                }
            });
            setTimeout(function () {
            }, 60000);
    }

    function scrollToBottom() {
        var messages = $(".messages");
        var scrollHeight = messages.prop("scrollHeight");
        messages.scrollTop(scrollHeight);
    }

    function disableButtonForOneMinute() {
        isButtonActive = false;
        $(".send_message").prop("disabled", true);

        var remainingTime = 60;

        var countdownInterval = setInterval(function () {
            remainingTime--;
            $(".send_message").text(" زمان مانده: " + remainingTime + " ثانیه");

            if (remainingTime <= 0) {
                clearInterval(countdownInterval);
                isButtonActive = true;
                $(".send_message").prop("disabled", false);
                $(".send_message").text("ارسال");
            }
        }, 1000);

        setTimeout(function () {
            clearInterval(countdownInterval);
            isButtonActive = true;
            $(".send_message").prop("disabled", false);
            $(".send_message").text("ارسال");
        }, 60000);
    }

    function Load_Chat_Messages(Code) {
        let With = $('.list-unstyled .active .With').text();
        $.ajax({
            type: "POST",
            url: "http://127.0.0.1:8000/Farshtore/Get_Id_User_Chat/" + Code + "/" + With,
            success: function(result) {
                Other = result;
                if (result != "False") {
                    $("#Other_Id").text(result);
                $.ajax({
                    type:"POST",
                    url:"http://" + window.location.host + "/Farshtore/Chat_Read_Support/" + Code + "/" + Other,
                    success:function(result) {
                        if (result != "False") {
                            All_Chat = JSON.parse(result);
                            Get_Str = "";
                            All_Chat.forEach((item) => {
                                if (User_Id == item.fields.Seender) {
                                    Get_Str += `<li class="clearfix">
                                                    <div class="message-data text-right">
                                                        <span class="message-data-time">` + item.fields.Chat_Message_Date + `</span>
                                                    </div>
                                                    <div class="message other-message float-right text_wrapper">
                                                        <div class="text">` + item.fields.Message + `</div>
                                                    </div>
                                                </li>
                                                `
                                }
                                else {
                                    Get_Str += `<li class="clearfix">
                                                    <div class="message-data">
                                                        <span class="message-data-time">` + item.fields.Chat_Message_Date + `</span>
                                                    </div>
                                                    <div class="message my-message text_wrapper">
                                                        <div class="text">` + item.fields.Message + `</div>
                                                    </div>
                                                </li>`
                                }
                            });

                            let Head = `<div class="col-lg-6">
                                            <div class="chat-about">
                                                <h6 class="m-b-0">` + Name + `</h6>
                                            </div>
                                        </div>`
                            $(".Place_Messages").html(Get_Str);
                            $(".row-v").html(Head);
                            $(".input-v").removeAttr("hidden");
                        }
            },
            error:function(e){
                alert("error");
            }

                });
                }
            },
            error: function(e) {
                alert("error");
            }
        });

        let User_Id = $("#user_id").text();
        if (User_Id == "") {
            User_Id = $("#Seller_id").text();
        }
    }

    $(".list-unstyled .clearfix").click(function(){
        $(this).addClass("active").siblings().removeClass("active");
        let dataCode = $(this).attr("data-code");
        Name = $('.people-list .list-unstyled .active .about .name').text();
            scrollToBottom();
            Load_Chat_Messages(dataCode);
    });
});