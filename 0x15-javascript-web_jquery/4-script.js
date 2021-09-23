$(function () {
  $('#toggle_header').css('cursor', 'pointer');
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});
