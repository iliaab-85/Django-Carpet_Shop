data = "";
$(document).ready(function(){
  $("#Likes").click(function(){
  $(this).addClass("active")
  data = data+" <div class='container-xxl'>"+
  "<div class='container'>"+
      "<div class='section-header text-center mx-auto mb-5 wow fadeInUp' style='margin-right: 10%; data-wow-delay='0.1s'>"+
          "<h1 class='display-5 mb-3' style=' text-align: center;'>بازدید های اخیر</h1><br><br>"+
      "</div>"+
      "<div class='row g-4'>"+
          "<div class='col-lg-4 wow fadeInUp' data-wow-delay='0.3s'>"+
              "<img style='flex: 0 0 auto;width:80%;cursor: pointer;' class='img-fluid img-location' alt=''>"+
              "<div style='margin-bottom: 1.5rem !important;padding: 1.5rem !important;background-color: #F7F8FC !important;width:80%;'>"+
                  "<p class='d-block h5 lh-base' style='font-weight: 600; display: block !important;font-size: 1.5rem;line-height: 1.5 !important;margin-bottom: 1.5rem !important;'>How to cultivate organic fruits and vegetables in own firm</p>"+
                  "<div style='color: #6c757d !important;border-top: 1px solid #dee2e6 !important;padding-top: 1.5rem !important;'>"+
                      "<small class='me-3' style='margin-right: 1rem !important;'><i class='fa fa-user text-primary me-2' style='color: #3CB815 !important;margin-right: 0.5rem !important;'></i>Admin</small>"+
                      "<small class='me-3' style='margin-right: 1rem !important;'><i class='fa fa-calendar text-primary me-2' style='color: #3CB815 !important;margin-right: 0.5rem !important;'></i>01 Jan, 2045</small>"+
                  "</div>"+
              "</div>"+
          "</div>"+
      "</div>"+
  "</div>"+
"</div>";
  $(".html-body").html(data)
  });
  });