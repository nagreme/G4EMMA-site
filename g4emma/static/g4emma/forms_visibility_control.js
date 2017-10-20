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

  // These two vars list the optional forms and what toggles their visibility
  // The order is important! A toggle must have the same index as its form
  var toggles_arr = ["#id_specify_beam_emittance", "#id_specify_central_trajectory"];
  var optional_forms_arr = [".beam_emittance_form", ".central_traj_form"];

  // Then show optional forms that are already toggled
  for (i = 0; i < toggles_arr.length; i++)
  {
    if (!parseInt($(toggles_arr[i]).val()))
    {
      $(optional_forms_arr[i]).hide();
    }
  }


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
