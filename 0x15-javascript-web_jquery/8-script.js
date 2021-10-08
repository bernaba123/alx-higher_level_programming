$(function () {
  $.get('https://swapi.co/api/films/?format=json', (data) => {
    for (let i = 0; i < data.count; i++) {
      $('#list_movies').append('<li>' + data.results[i].title + '</li>');
    }
  });
});
