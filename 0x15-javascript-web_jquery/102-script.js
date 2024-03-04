$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#languageCode').val();
    $.getJSON(`https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`, function (response) {
      $('DIV#hello').text(response.hello);
    });
  });
});
