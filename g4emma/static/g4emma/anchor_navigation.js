$(document).ready(function(){

  // Use #id anchor hrefs to navigate to the element with #id
  var $root = $('html, body');

  $('a[href^="#"]').click(function() {
      var href = $.attr(this, 'href');

      $root.animate({
          scrollTop: $(href).offset().top
      }, 'fast', function () {
          window.location.hash = href;
      });

      return false;
  });

// show back-to-top button once we start scrolling
$(window).scroll(function(){
    if ($(window).scrollTop() > 250){
      $("#top-link").show();
    }
    else {
      $("#top-link").hide();
    }
  });

});
