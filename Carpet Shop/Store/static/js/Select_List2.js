
function Table_List() {
    let Value = $('#mySelect_List').val()
    if ( Value != "") {
        let List = $('#mySelect_List').html();
        let Lst = "";
        
        Lst += `
        <select id="mySelect_List" class="btn btn-light btn-sm" onchange="Table_List()" style="box-shadow:0 6px 20px 0 rgba(0, 0, 0, 0.19);">
            ${List}
        </select>
        
        
        `/*<div class="Search" style="height:36px;width:23rem;">
            <div style="height: 36px;cursor: text;background-color: aliceblue;position: absolute;border-top-left-radius: 10px;border-bottom-left-radius: 10px;">
                <input type="text" class="input_Search" style="width: 330px;">
            </div>
            <button class="btn_Search" onclick="">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-search" viewBox="0 0 16 16">
                    <path d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001q.044.06.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1 1 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0"></path>
                </svg>
            </button>
        </div>*/
        $('.crd_header').html(Lst);
        $('#mySelect_List').val(Value);
    }
    
    if (Value == 'Order_Complete') {
        let Dates = $('#mySelect').val()
        let ths =
         `<th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">قیمت</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">تاریخ خرید</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">کد خرید</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نام کاربری</th>
         `

        $('.jsgrid-header-row').html(ths)
        let Start = $('#datepicker12from').val();
        let End = $('#datepicker12to').val();

        let First_Date = Start.replace(/\//g, "-");
        let Last_Date = End.replace(/\//g, "-");
        let url = `/Farshtore/Admin_Order_Complete/0/${Dates}`;
        if (Dates == "custom") {
            url = `/Farshtore/Admin_Order_Complete/0/custom.${First_Date}.${Last_Date}`
        }
        $.ajax({
            type: "POST",
            url: "http://" + window.location.host + url,
            success: async function(result) {
                let obj = JSON.parse(result);
                let User_name = "";
                let ths_User = "";
                if (result) {
                    for (let i = 0; i < obj.length; i++) {
                        const item = obj[i];
                        await $.ajax({
                            type: "POST",
                            url: "http://" + window.location.host + `/Farshtore/Admin_Order_Complete/${item.fields.user_Id}/${Dates}`,
                            success: function(result) {
                                let text = result
                                User_name = text.replace("_Seller_Genuine", "")

                                if (User_name == text) {
                                    User_name = text.replace("_Seller_Legal", "")
                                }
                                
                                if (User_name == text) {
                                    User_name = User_name.replace("_Support", "")
                                }
                            }
                        });

                        ths_User += `
                        <tr class="jsgrid-row">
                        <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;direction:rtl;"><span style="color:red;">` + item.fields.Price + `</span> تومان</td>
                        <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + item.fields.Date+ `</td>
                        <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + item.fields.Order_Code + `</td>
                        <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + User_name + `</td>
                        </tr>
                        `
                    }
                    $('.tbl_Lists').html(ths_User)
                }
            },
            error: function(e) {
                alert("error");
            }
        });
    }

    else if (Value == 'Order_Complete_Product') {
        let Dates = $('#mySelect').val()
        let ths =
        `<th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">تعداد محصول خریداری شده</th>
        <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نام فروشنده</th>
        <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نام کاربری خریدار</th>
        <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">بازدید ها</th>
        <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">علاقه مندی ها</th>
        <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">تاریخ انتشار</th>
        <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نوع محصول</th>
        <th class="jsgrid-header-cell jsgrid-align-center" style="width: 25px;">درصد تخفیف</th>
        <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">قیمت</th>
        <th class="jsgrid-header-cell jsgrid-align-center" style="width: 75px;">عنوان</th>
        `
        let Start = $('#datepicker12from').val();
        let End = $('#datepicker12to').val();

        let First_Date = Start.replace(/\//g, "-");
        let Last_Date = End.replace(/\//g, "-");
        $('.jsgrid-header-row').html(ths)
        let url = `/Farshtore/Admin_buyed_product/0/0/${Dates}`;
        if (Dates == "custom") {
            url = `/Farshtore/Admin_Order_Complete/0/${Dates}`;
        }
        let bool = true;
        if (Dates == "custom") {
            bool = false;
            if (Start != "" && End != "") {
                url = `/Farshtore/Admin_buyed_product/0/0/custom.${First_Date}.${Last_Date}`
                bool = true;
            }
        }
        if (bool) {
            let obj;
            $.ajax({
                type: "POST",
                url: "http://" + window.location.host + url,
                success: async function(result) {
                    try {
                        obj = JSON.parse(result);
                    }
                    catch {
                        obj = result;
                    }
                    console.log(obj);
                    let Full_Info = "";
                    let ths_User = "";
                    if (result) {
                        for (let i = 0; i < obj.length; i++) {
                            const item = obj[i];
                            await $.ajax({
                                type: "POST",
                                url: "http://" + window.location.host + `/Farshtore/Admin_buyed_product/${item.user_Id}/${item.Product_Code}/${Dates}`,
                                success: function(result) {
                                    Full_Info = result;
                                    alert(Full_Info);
                                }
                            });

                            ths_User += `
                            <tr class="jsgrid-row">
                                <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">${Full_Info.fields.Buyed_Product_Count}</th>
                                <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">${Full_Info.fields.Seller_Name}</th>
                                <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">${Full_Info.fields.user_name}</th>
                                <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">${Full_Info.fields.Views}</th>
                                <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">${Full_Info.fields.Likes}</th>
                                <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">${Full_Info.fields.Date_Published}</th>
                                <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">${Full_Info.fields.Type}</th>
                                <th class="jsgrid-header-cell jsgrid-align-center" style="width: 25px;">${Full_Info.fields.Discount}</th>
                                <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">${Full_Info.fields.Price}</th>
                                <th class="jsgrid-header-cell jsgrid-align-center" style="width: 75px;">${Full_Info.fields.Title}</th>
                            </tr>
                            `
                        }
                        $('.tbl_Lists').html(ths_User)
                    }
                },
                error: function(e) {
                    alert("error");
                }
            });
        }
    }

  }