
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
        $('.card-header').html(Lst);
        $('#mySelect_List').val(Value);
    }
    if (Value == 'Users') {
        let ths =
         `<th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">شماره تماس</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">ایمیل</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نام کاربری</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نام</th>
         `

        $('.jsgrid-header-row').html(ths)

        $.ajax({
    type: "POST",
    url: "http://" + window.location.host + "/Farshtore/Admin_AllUser/0",
    success: async function(result) {
        let obj = JSON.parse(result);
        let Full_Info = "";
        let ths_User = "";
        if (result) {
            for (let i = 0; i < obj.length; i++) {
                const item = obj[i];
                await $.ajax({
                    type: "POST",
                    url: "http://" + window.location.host + "/Farshtore/Admin_AllUser/" + item.pk,
                    success: function(result) {
                        Full_Info = JSON.parse(result);
                    }
                });
                console.log(Full_Info)
                let User_name = Full_Info[0].fields.username;
                let Full_Name = `${Full_Info[0].fields.first_name} ${Full_Info[0].fields.last_name}`

                ths_User += `
                 <tr class="jsgrid-row">
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + item.fields.Phone + `</td>
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + Full_Info[0].fields.email+ `</td>
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + User_name + `</td>
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + Full_Name + `</td>
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

    else if (Value == 'Supports') {
        
        let ths =
         `<th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">شماره تماس</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">ایمیل</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نام کاربری</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نام</th>
         `

        $('.jsgrid-header-row').html(ths)

        $.ajax({
    type: "POST",
    url: "http://" + window.location.host + "/Farshtore/Admin_AllSupporter/0",
    success: async function(result) {
        let obj = JSON.parse(result);
        let Full_Info = "";
        let ths_User = "";
        if (result) {
            for (let i = 0; i < obj.length; i++) {
                const item = obj[i];
                await $.ajax({
                    type: "POST",
                    url: "http://" + window.location.host + "/Farshtore/Admin_AllSupporter/" + item.pk,
                    success: function(result) {
                        Full_Info = JSON.parse(result);
                    }
                });
                console.log(Full_Info)
                let User_name = Full_Info[0].fields.username;
                User_name = User_name.replace("_Support", "")
                let Full_Name = `${Full_Info[0].fields.first_name} ${Full_Info[0].fields.last_name}`

                ths_User += `
                 <tr class="jsgrid-row">
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + item.fields.Phone + `</td>
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + Full_Info[0].fields.email+ `</td>
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + User_name + `</td>
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + Full_Name + `</td>
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


    else if (Value == 'Sellers') {
        let ths =
         `<th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">شماره تماس</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">ایمیل</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نام کاربری</th>
          <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نام</th>
         `

        $('.jsgrid-header-row').html(ths)

        $.ajax({
    type: "POST",
    url: "http://" + window.location.host + "/Farshtore/Admin_AllUser_Seller/0",
    success: async function(result) {
        let obj = JSON.parse(result);
        console.log(obj);
        let Full_Info = "";
        let ths_User_Seller = "";
        if (result) {
            for (let i = 0; i < obj.length; i++) {
                const item = obj[i];
                await $.ajax({
                    type: "POST",
                    url: "http://" + window.location.host + "/Farshtore/Admin_AllUser_Seller/" + item.pk,
                    success: function(result) {
                        Full_Info = JSON.parse(result);
                    }
                });
                let User_name = "";
                let text = Full_Info[0].fields.username
                User_name = text.replace("_Seller_Genuine", "")

                if (User_name == Full_Info[0].fields.username) {
                    User_name = text.replace("_Seller_Legal", "")
                }
                let Full_Name = `${Full_Info[0].fields.first_name} ${Full_Info[0].fields.last_name}`

                ths_User_Seller += `
                 <tr class="jsgrid-row">
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + item.fields.Phone + `</td>
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + Full_Info[0].fields.email + `</td>
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + User_name + `</td>
                   <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + Full_Name + `</td>
                 </tr>
                 `
            }
            $('.tbl_Lists').html(ths_User_Seller)
        }
    },
    error: function(e) {
        alert("error");
    }
});
    }


    else if (Value == 'Products') {
        async function getFullName(user_Id) {
          try {
            const response = await $.ajax({
              type: "POST",
              url: "http://" + window.location.host + "/Farshtore/Admin_AllProduct/" + user_Id,
            });
            return response;
          } catch (error) {
            alert(error);
          }
        }
      
        async function getProductOrderCount(Product_Code) {
          try {
            const response = await $.ajax({
              type: "POST",
              url: "http://" + window.location.host + "/Farshtore/Admin_Product_Order_Count/" + Product_Code,
            });
            return response;
          } catch (error) {
            alert(error);
          }
        }
      
        let ths =
          `<th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">تعداد در سبد خرید</th>
           <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نام فروشنده</th>
           <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">بازدید ها</th>
           <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">علاقه مندی ها</th>
           <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">تاریخ انتشار</th>
           <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">نوع محصول</th>
            <th class="jsgrid-header-cell jsgrid-align-center" style="width: 25px;">درصد تخفیف</th>
            <th class="jsgrid-header-cell jsgrid-align-center" style="width: 50px;">قیمت</th>
            <th class="jsgrid-header-cell jsgrid-align-center" style="width: 75px;">عنوان</th>
           `
      
        $('.jsgrid-header-row').html(ths)
      
        var settings = {
          "url": "http://127.0.0.1:8000/apiread_product/?format=json",
          "method": "GET",
          "timeout": 0,
        };
        let obj;
        let ths_Product = "";
        $.ajax(settings).done(async function (response) {
          obj = response;
          console.log(obj)
          for (let i = 0; i < obj.length; i++) {
            const item = obj[i];
            const objj = await getProductOrderCount(item.Product_Code);
            const FullName = await getFullName(item.user_Id);
      
            ths_Product += `
              <tr class="jsgrid-row">
                <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + objj + `</td>
                <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + FullName + `</td>
                <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + item.Product_Visit + `</td>
                <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + item.Product_Likes + `</td>
                <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + item.Product_Date + `</td>
                <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + item.Product_Type + `</td>
                <td class="jsgrid-cell jsgrid-align-center" style="width: 25px;font-weight: bold;"><span>%</span><span style="color: red;">`+ item.Product_Price_Discount +`</span></td>
                <td class="jsgrid-cell jsgrid-align-center" style="width: 50px;">` + item.Product_Price + `</td>
                <td class="jsgrid-cell jsgrid-align-center" style="width: 75px;">` + item.Product_Title + `</td>
              </tr>
            `;
          }
          $('.tbl_Lists').html(ths_Product)
        });
      }
  }