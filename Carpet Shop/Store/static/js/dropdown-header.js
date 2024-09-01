$(document).ready(function () {
    let User_Id = $('#user_id').text();
    $('.Phone_dropdown').click(function () { 
        window.location.href = "/Farshtore/EditProfile/" + User_Id;
    });

    $('.Sub_dropdown').click(function () { 
        window.location.href = "/Farshtore/Subscribation";
    });

    $('.My_Order_dropdown').click(function () { 
        window.location.href = "/Farshtore/Profile/Orders";
    });

    $('.Likes_dropdown').click(function () { 
        window.location.href = "/Farshtore/Profile/Product_Likes";
    });

    $('.MyComment_dropdown').click(function () { 
        window.location.href = "/Farshtore/Profile/MyComments";
    });

    $('.Notification_dropdown').click(function () { 
        window.location.href = "/Farshtore/Profile/Message";
    });

});