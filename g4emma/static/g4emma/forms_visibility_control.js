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

$(document).ready(function(){
  $("#id_specify_beam_emittance").change(function(){
    $(".beam_emittance_form").toggle();
  });
});
