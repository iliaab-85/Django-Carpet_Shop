$(document).ready(function () {
    Load_Comment_Messages();

    function Load_Comment_Messages() {
        let Chat_Code = $(".Chat_Code").text();
        $.ajax({
            type:"POST",
            url:"http://" + window.location.host + "/Farshtore/Load_Comment_Product/" + Chat_Code,
            success:function(Comments) {
                if (Comments == "False") {
                    let Empty;
                    Empty =`
                    <div class="Empty" style="margin-left: 1.2rem;">
                        <div class="empty-center">
                            <img src="/../static/img/empty-cart.svg" style="width: 140px;">
                        </div>
                        <p class="text-center">هنوز نظری برای این محصول ثبت نشده است</p>
                    </div>`
                    $(".Place_Messages").html(Empty);
                }
                else {
                    let All_Comments = JSON.parse(Comments);
                    let Place_Messages = "";
                    let Rate_div = ``;
                    All_Comments.forEach((item) => {
                        rate = item.fields.Rate;
                        if (rate == "0.5") {
                        Rate_div = `<div class="block_rating clearfix" style="width: auto;display: flex;flex-direction: row-reverse;">
                                        <fieldset class="block_rating__stars" style="width: auto;">
                                            <input type="radio" id="star5" name="rating" value="5"/><label
                                                class="full" for="star5" title="عالی"></label>
                                            <input type="radio" id="star4half" name="rating"
                                                   value="4.5"/><label class="half" for="star4half"
                                                                                title="عالی"></label>
                                            <input type="radio" id="star4" name="rating" value="4"/><label
                                                class="full" for="star4" title="خوب"></label>
                                            <input type="radio" id="star3half" name="rating"
                                                   value="3.5"/><label class="half" for="star3half"
                                                                                title="خوب"></label>
                                            <input type="radio" id="star3" name="rating" value="3"/><label
                                                class="full" for="star3" title="متوسط"></label>
                                            <input type="radio" id="star2half" name="rating"
                                                   value="2.5"/><label class="half" for="star2half"
                                                                                title="متوسط"></label>
                                            <input type="radio" id="star2" name="rating" value="2"/><label
                                                class="full" for="star2"
                                                title="بد"></label>
                                            <input type="radio" id="star1half" name="rating"
                                                   value="1.5"/><label class="half" for="star1half"
                                                                                title="بد"></label>
                                            <input type="radio" id="star1" name="rating" value="1"/><label
                                                class="full" for="star1"
                                                title="خیلی بد"></label>
                                            <input type="radio" checked id="starhalf" name="rating"
                                                   value="0.5"/><label
                                                class="half" for="starhalf"
                                                title="خیلی بد"></label>
                                        </fieldset>
                                    </div>`
                        }

                        else if (rate == "1") {
                            Rate_div = `<div class="block_rating clearfix" style="width: auto;display: flex;flex-direction: row-reverse;">
                                            <fieldset class="block_rating__stars" style="width: auto;">
                                                <input type="radio" id="star5" name="rating" value="5"/><label
                                                    class="full" for="star5" title="عالی"></label>
                                                <input type="radio" id="star4half" name="rating"
                                                       value="4.5"/><label class="half" for="star4half"
                                                                                    title="عالی"></label>
                                                <input type="radio" id="star4" name="rating" value="4"/><label
                                                    class="full" for="star4" title="خوب"></label>
                                                <input type="radio" id="star3half" name="rating"
                                                       value="3.5"/><label class="half" for="star3half"
                                                                                    title="خوب"></label>
                                                <input type="radio" id="star3" name="rating" value="3"/><label
                                                    class="full" for="star3" title="متوسط"></label>
                                                <input type="radio" id="star2half" name="rating"
                                                       value="2.5"/><label class="half" for="star2half"
                                                                                    title="متوسط"></label>
                                                <input type="radio" id="star2" name="rating" value="2"/><label
                                                    class="full" for="star2"
                                                    title="بد"></label>
                                                <input type="radio" id="star1half" name="rating"
                                                       value="1.5"/><label class="half" for="star1half"
                                                                                    title="بد"></label>
                                                <input type="radio" checked id="star1" name="rating" value="1"/><label
                                                    class="full" for="star1"
                                                    title="خیلی بد"></label>
                                                <input type="radio" id="starhalf" name="rating"
                                                       value="0.5"/><label
                                                    class="half" for="starhalf"
                                                    title="خیلی بد"></label>
                                            </fieldset>
                                        </div>`
                        }

                        else if (rate == "1.5") {
                                Rate_div = `<div class="block_rating clearfix" style="width: auto;display: flex;flex-direction: row-reverse;">
                                                <fieldset class="block_rating__stars" style="width: auto;">
                                                    <input type="radio" id="star5" name="rating" value="5"/><label
                                                        class="full" for="star5" title="عالی"></label>
                                                    <input type="radio" id="star4half" name="rating"
                                                           value="4.5"/><label class="half" for="star4half"
                                                                                        title="عالی"></label>
                                                    <input type="radio" id="star4" name="rating" value="4"/><label
                                                        class="full" for="star4" title="خوب"></label>
                                                    <input type="radio" id="star3half" name="rating"
                                                           value="3.5"/><label class="half" for="star3half"
                                                                                        title="خوب"></label>
                                                    <input type="radio" id="star3" name="rating" value="3"/><label
                                                        class="full" for="star3" title="متوسط"></label>
                                                    <input type="radio" id="star2half" name="rating"
                                                           value="2.5"/><label class="half" for="star2half"
                                                                                        title="متوسط"></label>
                                                    <input type="radio" id="star2" name="rating" value="2"/><label
                                                        class="full" for="star2"
                                                        title="بد"></label>
                                                    <input type="radio" checked id="star1half" name="rating"
                                                           value="1.5"/><label class="half" for="star1half"
                                                                                        title="بد"></label>
                                                    <input type="radio" id="star1" name="rating" value="1"/><label
                                                        class="full" for="star1"
                                                        title="خیلی بد"></label>
                                                    <input type="radio" id="starhalf" name="rating"
                                                           value="0.5"/><label
                                                        class="half" for="starhalf"
                                                        title="خیلی بد"></label>
                                                </fieldset>
                                            </div>`
                        }
                            
                        else if (rate == "2") {
                                    Rate_div = `<div class="block_rating clearfix" style="width: auto;display: flex;flex-direction: row-reverse;">
                                                    <fieldset class="block_rating__stars" style="width: auto;">
                                                        <input type="radio" id="star5" name="rating" value="5"/><label
                                                            class="full" for="star5" title="عالی"></label>
                                                        <input type="radio" id="star4half" name="rating"
                                                               value="4.5"/><label class="half" for="star4half"
                                                                                            title="عالی"></label>
                                                        <input type="radio" id="star4" name="rating" value="4"/><label
                                                            class="full" for="star4" title="خوب"></label>
                                                        <input type="radio" id="star3half" name="rating"
                                                               value="3.5"/><label class="half" for="star3half"
                                                                                            title="خوب"></label>
                                                        <input type="radio" id="star3" name="rating" value="3"/><label
                                                            class="full" for="star3" title="متوسط"></label>
                                                        <input type="radio" id="star2half" name="rating"
                                                               value="2.5"/><label class="half" for="star2half"
                                                                                            title="متوسط"></label>
                                                        <input type="radio" checked id="star2" name="rating" value="2"/><label
                                                            class="full" for="star2"
                                                            title="بد"></label>
                                                        <input type="radio" id="star1half" name="rating"
                                                               value="1.5"/><label class="half" for="star1half"
                                                                                            title="بد"></label>
                                                        <input type="radio" id="star1" name="rating" value="1"/><label
                                                            class="full" for="star1"
                                                            title="خیلی بد"></label>
                                                        <input type="radio" id="starhalf" name="rating"
                                                               value="0.5"/><label
                                                            class="half" for="starhalf"
                                                            title="خیلی بد"></label>
                                                    </fieldset>
                                                </div>`
                        }

                        else if (rate == "2.5") {
                                Rate_div = `<div class="block_rating clearfix" style="width: auto;display: flex;flex-direction: row-reverse;">
                                                <fieldset class="block_rating__stars" style="width: auto;">
                                                    <input type="radio" id="star5" name="rating" value="5"/><label
                                                        class="full" for="star5" title="عالی"></label>
                                                    <input type="radio" id="star4half" name="rating"
                                                           value="4.5"/><label class="half" for="star4half"
                                                                                        title="عالی"></label>
                                                    <input type="radio" id="star4" name="rating" value="4"/><label
                                                        class="full" for="star4" title="خوب"></label>
                                                    <input type="radio" id="star3half" name="rating"
                                                           value="3.5"/><label class="half" for="star3half"
                                                                                        title="خوب"></label>
                                                    <input type="radio" id="star3" name="rating" value="3"/><label
                                                        class="full" for="star3" title="متوسط"></label>
                                                    <input type="radio" checked id="star2half" name="rating"
                                                           value="2.5"/><label class="half" for="star2half"
                                                                                        title="متوسط"></label>
                                                    <input type="radio" id="star2" name="rating" value="2"/><label
                                                        class="full" for="star2"
                                                        title="بد"></label>
                                                    <input type="radio" id="star1half" name="rating"
                                                           value="1.5"/><label class="half" for="star1half"
                                                                                        title="بد"></label>
                                                    <input type="radio" id="star1" name="rating" value="1"/><label
                                                        class="full" for="star1"
                                                        title="خیلی بد"></label>
                                                    <input type="radio" id="starhalf" name="rating"
                                                           value="0.5"/><label
                                                        class="half" for="starhalf"
                                                        title="خیلی بد"></label>
                                                </fieldset>
                                            </div>`
                        }

                        else if (rate == "3") {
                            Rate_div = `<div class="block_rating clearfix" style="width: auto;display: flex;flex-direction: row-reverse;">
                                            <fieldset class="block_rating__stars" style="width: auto;">
                                                <input type="radio" id="star5" name="rating" value="5"/><label
                                                    class="full" for="star5" title="عالی"></label>
                                                <input type="radio" id="star4half" name="rating"
                                                       value="4.5"/><label class="half" for="star4half"
                                                                                    title="عالی"></label>
                                                <input type="radio" id="star4" name="rating" value="4"/><label
                                                    class="full" for="star4" title="خوب"></label>
                                                <input type="radio" id="star3half" name="rating"
                                                       value="3.5"/><label class="half" for="star3half"
                                                                                    title="خوب"></label>
                                                <input type="radio" checked id="star3" name="rating" value="3"/><label
                                                    class="full" for="star3" title="متوسط"></label>
                                                <input type="radio" id="star2half" name="rating"
                                                       value="2.5"/><label class="half" for="star2half"
                                                                                    title="متوسط"></label>
                                                <input type="radio" id="star2" name="rating" value="2"/><label
                                                    class="full" for="star2"
                                                    title="بد"></label>
                                                <input type="radio" id="star1half" name="rating"
                                                       value="1.5"/><label class="half" for="star1half"
                                                                                    title="بد"></label>
                                                <input type="radio" id="star1" name="rating" value="1"/><label
                                                    class="full" for="star1"
                                                    title="خیلی بد"></label>
                                                <input type="radio" id="starhalf" name="rating"
                                                       value="0.5"/><label
                                                    class="half" for="starhalf"
                                                    title="خیلی بد"></label>
                                            </fieldset>
                                        </div>`
                        }

                        else if (rate == "3.5") {
                            Rate_div = `<div class="block_rating clearfix" style="width: auto;display: flex;flex-direction: row-reverse;">
                                            <fieldset class="block_rating__stars" style="width: auto;">
                                                <input type="radio" id="star5" name="rating" value="5"/><label
                                                    class="full" for="star5" title="عالی"></label>
                                                <input type="radio" id="star4half" name="rating"
                                                       value="4.5"/><label class="half" for="star4half"
                                                                                    title="عالی"></label>
                                                <input type="radio" id="star4" name="rating" value="4"/><label
                                                    class="full" for="star4" title="خوب"></label>
                                                <input type="radio" checked id="star3half" name="rating"
                                                       value="3.5"/><label class="half" for="star3half"
                                                                                    title="خوب"></label>
                                                <input type="radio" id="star3" name="rating" value="3"/><label
                                                    class="full" for="star3" title="متوسط"></label>
                                                <input type="radio" id="star2half" name="rating"
                                                       value="2.5"/><label class="half" for="star2half"
                                                                                    title="متوسط"></label>
                                                <input type="radio" id="star2" name="rating" value="2"/><label
                                                    class="full" for="star2"
                                                    title="بد"></label>
                                                <input type="radio" id="star1half" name="rating"
                                                       value="1.5"/><label class="half" for="star1half"
                                                                                    title="بد"></label>
                                                <input type="radio" id="star1" name="rating" value="1"/><label
                                                    class="full" for="star1"
                                                    title="خیلی بد"></label>
                                                <input type="radio" id="starhalf" name="rating"
                                                       value="0.5"/><label
                                                    class="half" for="starhalf"
                                                    title="خیلی بد"></label>
                                            </fieldset>
                                        </div>`
                        }

                        else if (rate == "4") {
                            Rate_div = `<div class="block_rating clearfix" style="width: auto;display: flex;flex-direction: row-reverse;">
                                            <fieldset class="block_rating__stars" style="width: auto;">
                                                <input type="radio" id="star5" name="rating" value="5"/><label
                                                    class="full" for="star5" title="عالی"></label>
                                                <input type="radio" id="star4half" name="rating"
                                                       value="4.5"/><label class="half" for="star4half"
                                                                                    title="عالی"></label>
                                                <input type="radio" checked id="star4" name="rating" value="4"/><label
                                                    class="full" for="star4" title="خوب"></label>
                                                <input type="radio" id="star3half" name="rating"
                                                       value="3.5"/><label class="half" for="star3half"
                                                                                    title="خوب"></label>
                                                <input type="radio" id="star3" name="rating" value="3"/><label
                                                    class="full" for="star3" title="متوسط"></label>
                                                <input type="radio" id="star2half" name="rating"
                                                       value="2.5"/><label class="half" for="star2half"
                                                                                    title="متوسط"></label>
                                                <input type="radio" id="star2" name="rating" value="2"/><label
                                                    class="full" for="star2"
                                                    title="بد"></label>
                                                <input type="radio" id="star1half" name="rating"
                                                       value="1.5"/><label class="half" for="star1half"
                                                                                    title="بد"></label>
                                                <input type="radio" id="star1" name="rating" value="1"/><label
                                                    class="full" for="star1"
                                                    title="خیلی بد"></label>
                                                <input type="radio" id="starhalf" name="rating"
                                                       value="0.5"/><label
                                                    class="half" for="starhalf"
                                                    title="خیلی بد"></label>
                                            </fieldset>
                                        </div>`
                        }

                        else if (rate == "4.5") {
                            Rate_div = `<div class="block_rating clearfix" style="width: auto;display: flex;flex-direction: row-reverse;">
                                            <fieldset class="block_rating__stars" style="width: auto;">
                                                <input type="radio" id="star5" name="rating" value="5"/><label
                                                    class="full" for="star5" title="عالی"></label>
                                                <input type="radio" checked id="star4half" name="rating"
                                                       value="4.5"/><label class="half" for="star4half"
                                                                                    title="عالی"></label>
                                                <input type="radio" id="star4" name="rating" value="4"/><label
                                                    class="full" for="star4" title="خوب"></label>
                                                <input type="radio" id="star3half" name="rating"
                                                       value="3.5"/><label class="half" for="star3half"
                                                                                    title="خوب"></label>
                                                <input type="radio" id="star3" name="rating" value="3"/><label
                                                    class="full" for="star3" title="متوسط"></label>
                                                <input type="radio" id="star2half" name="rating"
                                                       value="2.5"/><label class="half" for="star2half"
                                                                                    title="متوسط"></label>
                                                <input type="radio" id="star2" name="rating" value="2"/><label
                                                    class="full" for="star2"
                                                    title="بد"></label>
                                                <input type="radio" id="star1half" name="rating"
                                                       value="1.5"/><label class="half" for="star1half"
                                                                                    title="بد"></label>
                                                <input type="radio" id="star1" name="rating" value="1"/><label
                                                    class="full" for="star1"
                                                    title="خیلی بد"></label>
                                                <input type="radio" id="starhalf" name="rating"
                                                       value="0.5"/><label
                                                    class="half" for="starhalf"
                                                    title="خیلی بد"></label>
                                            </fieldset>
                                        </div>`
                        }

                        else if (rate == "5") {
                            Rate_div = `<div class="block_rating clearfix" style="width: auto;display: flex;flex-direction: row-reverse;">
                                            <fieldset class="block_rating__stars" style="width: auto;">
                                                <input type="radio" checked id="star5" name="rating" value="5"/><label
                                                    class="full" for="star5" title="عالی"></label>
                                                <input type="radio" id="star4half" name="rating"
                                                       value="4.5"/><label class="half" for="star4half"
                                                                                    title="عالی"></label>
                                                <input type="radio" id="star4" name="rating" value="4"/><label
                                                    class="full" for="star4" title="خوب"></label>
                                                <input type="radio" id="star3half" name="rating"
                                                       value="3.5"/><label class="half" for="star3half"
                                                                                    title="خوب"></label>
                                                <input type="radio" id="star3" name="rating" value="3"/><label
                                                    class="full" for="star3" title="متوسط"></label>
                                                <input type="radio" id="star2half" name="rating"
                                                       value="2.5"/><label class="half" for="star2half"
                                                                                    title="متوسط"></label>
                                                <input type="radio" id="star2" name="rating" value="2"/><label
                                                    class="full" for="star2"
                                                    title="بد"></label>
                                                <input type="radio" id="star1half" name="rating"
                                                       value="1.5"/><label class="half" for="star1half"
                                                                                    title="بد"></label>
                                                <input type="radio" id="star1" name="rating" value="1"/><label
                                                    class="full" for="star1"
                                                    title="خیلی بد"></label>
                                                <input type="radio" id="starhalf" name="rating"
                                                       value="0.5"/><label
                                                    class="half" for="starhalf"
                                                    title="خیلی بد"></label>
                                            </fieldset>
                                        </div>`
                        }

                    

                    Place_Messages += `<li class='clearfix'>
                                        <div>
                                            <div>
                                                <div class='message-data text-right'>
                                                    <span class='message-data-time' style='font-weight: bold;'>` + item.fields.Date + `</span>
                                                </div>
                                                <div>
                                                    <div class='message other-message float-right text_wrapper'>
                                                        <div class='text'>` + item.fields.Message + `</div>
                                                    </div>
                                                </div>
                                            
                                                ` + Rate_div + `
                                            </div>
                                        </div>
                                    </li>`;
                    });
                    $(".Place_Messages").html(Place_Messages);
                }
            },
            error:function(e){
                alert("error");
            }
        });
    }

    $(".send_message").click(function () {
    });

scrollToBottom();
var isButtonActive = true;
$(".send_message").click(function(){
    let Get_Message = $(".message_input").val();
    if (Get_Message.length > 0) {
        if (isButtonActive) {
            sendMessage();
        }
    }
    else {
        $(".error").removeAttr("hidden");
        $(".error").html("نظر خود را وارد کنید");
    }
    $(".message_input").val("");
});
    function sendMessage() {
    let Place_Messages = "";

    let Message_box = $(".Place_Messages").html();

    let Get_Messages = $(".message_input").val();
    let result = Get_Messages.match(/.{1,70}/g);
    let text_Enter = result.join("<br>");

    const daysOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
    const currentDate = new Date();
    const dayOfWeek = daysOfWeek[currentDate.getDay()];
    const hours = currentDate.getHours();
    const minutes = currentDate.getMinutes();
    const time = `${hours}:${minutes}`;
    const datetime = `${dayOfWeek}, ${time}`;

        $(".message_input").val("");
        let Chat_Code = $(".Chat_Code").text();
        let Rate = $("input[name='rating']:checked").val();
        let Product_Code = $(".Product_Code").text();
        scrollToBottom();
        $.ajax({
            type:"POST",
            url:"http://" + window.location.host + "/Farshtore/Save_Comment_Product/" + String(text_Enter) + "/" + Chat_Code + "/" + Product_Code + "/" + datetime + "/" + Rate,
            success:function(result) {
                if (result == "Exist") {
                    $(".error").removeAttr("hidden");
                    $(".error").html("!بیشتر از یک بار نمیتوانید برای یک محصول نظری دهید");
                }
                if (result == "Empty") {
                    $(".error").removeAttr("hidden");
                    $(".error").html("امتیاز خود را برای این محصول وارد کنید");
                }
                if (result == "Not") {
                    Place_Messages += "<li class='clearfix'>"+
                                            "<div class='message-data text-right'>"+
                                                "<span class='message-data-time'>" + datetime + "</span>"+
                                            "</div>"+
                                            "<div class='message other-message float-right text_wrapper'>"+
                                                "<div class='text'>" + text_Enter + "</div>"+
                                            "</div>"+
                                        "</li>";
                    $(".Place_Messages").html(Place_Messages);
                }
                if (result == "True") {
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
                }
            },
            error:function(e){
                alert("error");
            }
        });
}

function scrollToBottom() {
    var messages = $(".messages");
    var scrollHeight = messages.prop("scrollHeight");
    messages.scrollTop(scrollHeight);
}

$(".clearfix").click(function(){
    $(this).addClass("active").siblings().removeClass("active");
    let dataCode = $(this).attr("data-code");
    //Load_Chat_Messages(dataCode)
});

});