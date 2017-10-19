// var conditional_fields = $("div.beam_emittance_form", "div.central_traj_form");
// conditional_fields.hide();
//
// $(".shipping").change(function() {
//     if ($(this).prop('checked') === 'checked') {
//         conditional_fields.show();
//     } else {
//         conditional_fields.hide();
//     }
// });

// radio buttons toggle
$(document).ready(function(){

  var optional_forms = $(".beam_emittance_form, .central_traj_form");
  optional_forms.hide();

  // toggle beam emittance form
  $("#id_specify_beam_emittance").change(function(){
    $(".beam_emittance_form").toggle();
    $(".beam_emittance_form input").val("");
  });


  // toggle central trajectory form
  $("#id_specify_central_trajectory").change(function(){
    $(".central_traj_form").toggle();
  })
});
