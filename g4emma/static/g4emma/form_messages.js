$(document).ready(function(){

  // // display a message to the user upon submit to let them know the results
  // will take a while and scroll back to top so they can see any relevant msgs
  $("#sim_form").submit(function(){
    $("#submit-msg").text("You will be redirected to the results once the simulation is complete. This may take a while. Please do not close or refresh the page in the meantime.");
    $("html, body").animate({ scrollTop: 0 }, 'fast');
  });

});
