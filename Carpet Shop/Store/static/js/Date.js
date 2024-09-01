$(document).ready(function() {

     $("#last_date").pDatepicker({
    format: 'YYYY/MM/DD',
    onSelect: function(unix) {
      console.log(unix);
    }
  });

  $('#first_date').on('input', function() {
  var date = $(this).val();
  var regex = /^\d{4}\/\d{2}\/\d{2}$/;

  if (!regex.test(date)) {
    $(this).val('');
  }
});

  $('#last_date').persianDatepicker({
    format: 'YYYY/MM/DD',
    lang: 'fa',
    minDate: '1400/01/01',
    maxDate: '1400/12/31',
    onSelect: function(date) {
      console.log(date);
    }
  });


});

  $('#mySelect').change(function() {
    if ($(this).val() === 'custom') {
      alert('شما روی آپشن سفارشی کلیک کردید!');
    }
  });