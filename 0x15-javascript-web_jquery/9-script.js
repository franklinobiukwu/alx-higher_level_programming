$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (response) {
  const data = response.hello;
  $('DIV#hello').text(data);
});
