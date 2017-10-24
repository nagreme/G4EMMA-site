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

//taken from online, adds regex to jquery selectors, super useful
jQuery.expr[':'].regex = function(elem, index, match) {
    var matchParams = match[3].split(','),
        validLabels = /^(data|css):/,
        attr = {
            method: matchParams[0].match(validLabels) ?
                        matchParams[0].split(':')[0] : 'attr',
            property: matchParams.shift().replace(validLabels,'')
        },
        regexFlags = 'ig',
        regex = new RegExp(matchParams.join('').replace(/^\s+|\s+$/g,''), regexFlags);
    return regex.test(jQuery(elem)[attr.method](attr.property));
}


// radio buttons toggle
$(document).ready(function(){

  // These two vars list the optional forms and what toggles their visibility
  // The order is important! A toggle must have the same index as its form
  var toggles_arr = [
    "#id_specify_beam_emittance",
    "#id_specify_central_trajectory",
    "#id_specify_reaction",
    "#id_target_inserted",
    "#id_target_inserted",
    "#id_degrader1_inserted",
    "#id_degrader1_inserted",
    "#id_degrader2_inserted",
    "#id_degrader2_inserted",
    "#id_slit1_inserted",
    "#id_slit2_inserted",
    "#id_slit3_inserted",
    "#id_slit4_inserted",
    "#id_mwpc_inserted",
    "#id_ion_chamber_inserted"
  ];

  var optional_forms_arr = [
    ".beam_emittance_form",
    ".central_traj_form",
    ".reaction_form",
    ".target_form",
    ".target_elements_form",
    ".degrader1_form",
    ".degrader1_elements_form",
    ".degrader2_form",
    ".degrader2_elements_form",
    ".slit_1_form",
    ".slit_2_form",
    ".slit_3_form",
    ".slit_4_form",
    ".mwpc_form",
    ".ion_chamber_form"
  ];

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
    $(".central_traj_form input").val("");
  })


  // toggle reaction form
  $("#id_specify_reaction").change(function(){
    $(".reaction_form").toggle();
    $(".reaction_form input").val("");
  })


  // toggle target forms
  $("#id_target_inserted").change(function(){
    $(".target_form").toggle();
    $(".target_elements_form").toggle();
    $(".target_form input").val("");
    $(".target_elements_form input").val("");
    $("#id_target_num_elems").trigger("change");
  })


  // toggle target elems visibility
  $("#id_target_num_elems").change(function(){
    //retrieve the new selected number of elements
    var num_elems = parseInt($("#id_target_num_elems").val())

    //hide and clear what we want
    switch(num_elems)
    {
      case 1:
        $(":regex(id,id_target_elem_2_[0-9])").hide();
        $(":regex(id,id_target_elem_2_[0-9])").val("");
        $("label[for='id_target_elem_2_0']").hide();
      case 2:
        $(":regex(id,id_target_elem_3_[0-9])").hide();
        $(":regex(id,id_target_elem_3_[0-9])").val("");
        $("label[for='id_target_elem_3_0']").hide();
      case 3:
        $(":regex(id,id_target_elem_4_[0-9])").hide();
        $(":regex(id,id_target_elem_4_[0-9])").val("");
        $("label[for='id_target_elem_4_0']").hide();
      case 4:
        $(":regex(id,id_target_elem_5_[0-9])").hide();
        $(":regex(id,id_target_elem_5_[0-9])").val("");
        $("label[for='id_target_elem_5_0']").hide();
    }//switch (hide/clear)

    //then show the ones we want
    switch(num_elems)
    {
      case 5:
        $(":regex(id,id_target_elem_5_[0-9])").show();
        $("label[for='id_target_elem_5_0']").show();
      case 4:
        $(":regex(id,id_target_elem_4_[0-9])").show();
        $("label[for='id_target_elem_4_0']").show();
      case 3:
        $(":regex(id,id_target_elem_3_[0-9])").show();
        $("label[for='id_target_elem_3_0']").show();
      case 2:
        $(":regex(id,id_target_elem_2_[0-9])").show();
        $("label[for='id_target_elem_2_0']").show();
      case 1:
        $(":regex(id,id_target_elem_1_[0-9])").show();
        $("label[for='id_target_elem_1_0']").show();
    }//switch (show)
  })


  // toggle degrader1 forms
  $("#id_degrader1_inserted").change(function(){
    $(".degrader1_form").toggle();
    $(".degrader1_elements_form").toggle();
    $(".degrader1_form input").val("");
    $(".degrader1_elements_form input").val("");
    $("#id_degrader1_num_elems").trigger("change");
  })


  // toggle degrader1 elems visibility
  $("#id_degrader1_num_elems").change(function(){
    //retrieve the new selected number of elements
    var num_elems = parseInt($("#id_degrader1_num_elems").val())

    //hide and clear what we want
    switch(num_elems)
    {
      case 1:
        $(":regex(id,id_degrader1_elem_2_[0-9])").hide();
        $(":regex(id,id_degrader1_elem_2_[0-9])").val("");
        $("label[for='id_degrader1_elem_2_0']").hide();
      case 2:
        $(":regex(id,id_degrader1_elem_3_[0-9])").hide();
        $(":regex(id,id_degrader1_elem_3_[0-9])").val("");
        $("label[for='id_degrader1_elem_3_0']").hide();
      case 3:
        $(":regex(id,id_degrader1_elem_4_[0-9])").hide();
        $(":regex(id,id_degrader1_elem_4_[0-9])").val("");
        $("label[for='id_degrader1_elem_4_0']").hide();
      case 4:
        $(":regex(id,id_degrader1_elem_5_[0-9])").hide();
        $(":regex(id,id_degrader1_elem_5_[0-9])").val("");
        $("label[for='id_degrader1_elem_5_0']").hide();
    }//switch (hide/clear)

    //then show the ones we want
    switch(num_elems)
    {
      case 5:
        $(":regex(id,id_degrader1_elem_5_[0-9])").show();
        $("label[for='id_degrader1_elem_5_0']").show();
      case 4:
        $(":regex(id,id_degrader1_elem_4_[0-9])").show();
        $("label[for='id_degrader1_elem_4_0']").show();
      case 3:
        $(":regex(id,id_degrader1_elem_3_[0-9])").show();
        $("label[for='id_degrader1_elem_3_0']").show();
      case 2:
        $(":regex(id,id_degrader1_elem_2_[0-9])").show();
        $("label[for='id_degrader1_elem_2_0']").show();
      case 1:
        $(":regex(id,id_degrader1_elem_1_[0-9])").show();
        $("label[for='id_degrader1_elem_1_0']").show();
    }//switch (show)
  })


  // toggle degrader2 forms
  $("#id_degrader2_inserted").change(function(){
    $(".degrader2_form").toggle();
    $(".degrader2_elements_form").toggle();
    $(".degrader2_form input").val("");
    $(".degrader2_elements_form input").val("");
    $("#id_degrader2_num_elems").trigger("change");
  })

  $("#id_degrader2_num_elems").change(function(){
    //retrieve the new selected number of elements
    var num_elems = parseInt($("#id_degrader2_num_elems").val())

    //hide and clear what we want
    switch(num_elems)
    {
      case 1:
        $(":regex(id,id_degrader2_elem_2_[0-9])").hide();
        $(":regex(id,id_degrader2_elem_2_[0-9])").val("");
        $("label[for='id_degrader2_elem_2_0']").hide();
      case 2:
        $(":regex(id,id_degrader2_elem_3_[0-9])").hide();
        $(":regex(id,id_degrader2_elem_3_[0-9])").val("");
        $("label[for='id_degrader2_elem_3_0']").hide();
      case 3:
        $(":regex(id,id_degrader2_elem_4_[0-9])").hide();
        $(":regex(id,id_degrader2_elem_4_[0-9])").val("");
        $("label[for='id_degrader2_elem_4_0']").hide();
      case 4:
        $(":regex(id,id_degrader2_elem_5_[0-9])").hide();
        $(":regex(id,id_degrader2_elem_5_[0-9])").val("");
        $("label[for='id_degrader2_elem_5_0']").hide();
    }//switch (hide/clear)

    //then show the ones we want
    switch(num_elems)
    {
      case 5:
        $(":regex(id,id_degrader2_elem_5_[0-9])").show();
        $("label[for='id_degrader2_elem_5_0']").show();
      case 4:
        $(":regex(id,id_degrader2_elem_4_[0-9])").show();
        $("label[for='id_degrader2_elem_4_0']").show();
      case 3:
        $(":regex(id,id_degrader2_elem_3_[0-9])").show();
        $("label[for='id_degrader2_elem_3_0']").show();
      case 2:
        $(":regex(id,id_degrader2_elem_2_[0-9])").show();
        $("label[for='id_degrader2_elem_2_0']").show();
      case 1:
        $(":regex(id,id_degrader2_elem_1_[0-9])").show();
        $("label[for='id_degrader2_elem_1_0']").show();
    }//switch (show)
  })


  // toggle slit 1 form
  $("#id_slit1_inserted").change(function(){
    $(".slit_1_form").toggle();
    $(".slit_1_form input").val("");
  });

  // toggle slit 2 form
  $("#id_slit2_inserted").change(function(){
    $(".slit_2_form").toggle();
    $(".slit_2_form input").val("");
  });

  // toggle slit 3 form
  $("#id_slit3_inserted").change(function(){
    $(".slit_3_form").toggle();
    $(".slit_3_form input").val("");
  });

  // toggle slit 4 form
  $("#id_slit4_inserted").change(function(){
    $(".slit_4_form").toggle();
    $(".slit_4_form input").val("");
  });


  // toggle mwpc form
  $("#id_mwpc_inserted").change(function(){
    $(".mwpc_form").toggle();
    $(".mwpc_form input").val("");
  });


  // toggle ion chamber form
  $("#id_ion_chamber_inserted").change(function(){
    $(".ion_chamber_form").toggle();
    $(".ion_chamber_form input").val("");
  });




}); //doc ready
