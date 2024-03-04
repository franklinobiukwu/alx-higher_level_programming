$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (response) {
  const data = response.results;
  for (let i = 0; i < data.length; i++) {
    $('UL#list_movies').append('<li>' + data[i].title + '</li>');
  }
});
