#*************************************************************
# g4emma_input_setup.py
#
# Nadège Pulgar-Vidal
# 2017-Oct-03
#
# Some simple functions to set up the input, folders and files
# needed to run the EMMA Geant 4 Simulation (EMMAapp)
#*************************************************************

#===========================
# IMPORTS
#===========================
from shlex import quote
import subprocess as sp
import re
from pathlib import Path
import g4emma.infile_templates as IFileTemplates

#===========================
# FUCNTIONS
#===========================

#---------------------------------------------------
# sanitize_input_dict
# PARAMETERS: The dicitonary generated by the Django form (cleaned_data)
# PURPOSE: Properly escape/quote shell metacharacters
#---------------------------------------------------
def sanitize_input_dict(form_dict):
    if isinstance(form_dict, dict):
        for k in form_dict:
            if isinstance(form_dict[k], str):
                form_dict[k] = quote(form_dict[k])
    else:
        # TODO: raise an error if not dictionary?
        print("error: sanitize_input_dict, not dict") # placeholder


#---------------------------------------------------
# setup_unique_userdir
# PARAMETERs: The location of the user directory (no trailing '/'' required)
# RETURNS: The name of the unique user dir that was
#          created
# PURPOSE: Setup unique directories so different users
#          running the simulation won't interfere with
#          each other
#
# This should work assuming that PIDs are unique during
# the entire runtime of the server. This may cause problems
# if the server is restarted but the goal is to have pretty
# stringent clean up so this should hopefully not be a problem
#---------------------------------------------------
def setup_unique_userdir(user_dirs_path):
    # Get a unique name
    unique_part = sp.check_output("ps | grep ps", shell=True)

    #the slicing strips off extra quotes and a char: b'str_content'
    matched_part = re.match("([0-9]*)", str(unique_part)[2:-1])

    # Build full path
    userdir = "{}/UserDir_{}".format(user_dirs_path, matched_part.group(1))

    # Setup the directory
    if not Path(userdir).exists():
        Path(userdir).mkdir()

    else:
        userdir = None

    # The subdirectories will be created when and where needed (where input files are written and in the wrapper script)

    return userdir

#---------------------------------------------------
# merge_with_defaults
# PARAMETERS: The user input as a dictionary
# PURPOSE: Overlay the user'S input of a set of default
#          values to get a complete set of input values
#---------------------------------------------------
def merge_with_defaults(form_dict):
    # so we need a set of default values for most of the input fields
    # and then merge the two dictionaries with the user values overwriting the defaults
    if isinstance(form_dict, dict):
        #setup default values (they're all 0/"OUT"/"NO"/empty string)
        default_vals = dict(alpha_source_present = "NO",
                            alpha_source_kinetic_e = 0,
                            alpha_source_max_angle = 0,
                            #--------
                            # These 5 are the absolute required minimum for the simulation
                            # num_events = 0, #required
                            # beam_proton_num = 0, #required
                            # beam_nucleon_num = 0, #required
                            # beam_charge_state = 0, #required
                            # beam_kinetic_e = 0, #required
                            #--------
                            beam_e_spread = 0,
                            beam_diameter = 0 ,
                            beam_trans_emittance = 0,
                            #--------
                            # These 4 should be the same as the beam params above by default
                            center_traj_proton_num = form_dict['beam_proton_num'],
                            center_traj_nucleon_num = form_dict['beam_nucleon_num'],
                            center_traj_charge_state = form_dict['beam_charge_state'],
                            center_traj_kinetic_e = form_dict['beam_kinetic_e'],
                            #--------
                            ion_chamber_inserted = "OUT",
                            ion_chamber_pressure = 0,
                            ion_chamber_temp = 0,
                            mwpc_inserted = "OUT",
                            mwpc_pressure = 0,
                            mwpc_temp = 0,
                            rxn_z1_beam = 0,
                            rxn_a1 = 0,
                            rxn_z2_target = 0,
                            rxn_a2 = 0,
                            rxn_z3_recoil = 0,
                            rxn_a3 = 0,
                            rxn_z4_ejectile = 0,
                            rxn_a4 = 0,
                            rxn_min_angle = 0,
                            rxn_max_angle = 0,
                            rxn_recoil_charge = 0,
                            rxn_recoil_excitation_e = 0,
                            rxn_cross_sec = 0,
                            slit_1_inserted = "OUT",
                            slit_2_inserted = "OUT",
                            slit_3_inserted = "OUT",
                            slit_4_inserted = "OUT",
                            target_inserted = "OUT",
                            target_thickness = 0,
                            target_z_pos = 0,
                            target_density = 0,
                            target_num_elems = 0,
                            target_elems = "",
                            target_elem_1_proton_num = 0,
                            target_elem_1_molar_mass = 0,
                            target_elem_1_elem_weight_ratio = 0,
                            target_elem_2_proton_num = 0,
                            target_elem_2_molar_mass = 0,
                            target_elem_2_elem_weight_ratio = 0,
                            target_elem_3_proton_num = 0,
                            target_elem_3_molar_mass = 0,
                            target_elem_3_elem_weight_ratio = 0,
                            target_elem_4_proton_num = 0,
                            target_elem_4_molar_mass = 0,
                            target_elem_4_elem_weight_ratio = 0,
                            target_elem_5_proton_num = 0,
                            target_elem_5_molar_mass = 0,
                            target_elem_5_elem_weight_ratio = 0,
                            degreder_1_inserted = "OUT",
                            degrader_1_thickness = 0,
                            degrader_1_density = 0,
                            degrader_1_num_elems = 0,
                            degrader_1_elems = "",
                            degrader_1_elem_1_proton_num = 0,
                            degrader_1_elem_1_molar_mass = 0,
                            degrader_1_elem_1_weight_ratio = 0,
                            degrader_1_elem_2_proton_num = 0,
                            degrader_1_elem_2_molar_mass = 0,
                            degrader_1_elem_2_weight_ratio = 0,
                            degrader_1_elem_3_proton_num = 0,
                            degrader_1_elem_3_molar_mass = 0,
                            degrader_1_elem_3_weight_ratio = 0,
                            degrader_1_elem_4_proton_num = 0,
                            degrader_1_elem_4_molar_mass = 0,
                            degrader_1_elem_4_weight_ratio = 0,
                            degrader_1_elem_5_proton_num = 0,
                            degrader_1_elem_5_molar_mass = 0,
                            degrader_1_elem_5_weight_ratio = 0,
                            degrader_2_inserted = "OUT",
                            degrader_2_thickness = 0,
                            degrader_2_density = 0,
                            degrader_2_num_elems = 0,
                            degrader_2_elems = "",
                            degrader_2_elem_1_proton_num = 0,
                            degrader_2_elem_1_molar_mass = 0,
                            degrader_2_elem_1_weight_ratio = 0,
                            degrader_2_elem_2_proton_num = 0,
                            degrader_2_elem_2_molar_mass = 0,
                            degrader_2_elem_2_weight_ratio = 0,
                            degrader_2_elem_3_proton_num = 0,
                            degrader_2_elem_3_molar_mass = 0,
                            degrader_2_elem_3_weight_ratio = 0,
                            degrader_2_elem_4_proton_num = 0,
                            degrader_2_elem_4_molar_mass = 0,
                            degrader_2_elem_4_weight_ratio = 0,
                            degrader_2_elem_5_proton_num = 0,
                            degrader_2_elem_5_molar_mass = 0,
                            degrader_2_elem_5_weight_ratio = 0)

        default_vals.update(form_dict)

    else:
        #raise an error
        print("error: merge_with_defaults, not dict") # placeholder

    return default_vals


#---------------------------------------------------
# write_input_files
# PARAMETERS: The user directory to place the files in
#             and the dictionary containing cleaned
#             user input
# PURPOSE: Set up the input files in the specified directory
#---------------------------------------------------
def write_input_files(userdir, form_dict):
    # Make the input files directory
    infile_dir_name = "/User_Input"
    if Path(userdir).exists():
        infile_dir_path = userdir + infile_dir_name
        Path(infile_dir_path).mkdir()

        # input file names
        alphaSource_file = infile_dir_path + "/alphaSource.dat"
        beam_file = infile_dir_path + "/beam.dat"
        central_traj_file = infile_dir_path + "/centralTrajectory.dat"
        ion_chamber_file = infile_dir_path + "/ionChamber.dat"
        mwpc_file = infile_dir_path + "/mwpc.dat"
        rxn_file = infile_dir_path + "/reaction.dat"
        slits_file = infile_dir_path + "/slits.dat"
        target_degraders_file = infile_dir_path + "/targetDegraders.dat"

        # write user input to the input files, be careful of the variable parts
        # write alphaSource
        f = open(alphaSource_file, 'w')
        f.write(IFileTemplates.alphaSource_datfile.format(**form_dict))
        f.close()

        # write beam
        f = open(beam_file, 'w')
        f.write(IFileTemplates.beam_datfile.format(**form_dict))
        f.close()

        # write central trajectory
        f = open(central_traj_file, 'w')
        f.write(IFileTemplates.centralTrajectory_datfile.format(**form_dict))
        f.close()

        # write ion chamber
        f = open(ion_chamber_file, 'w')
        f.write(IFileTemplates.ionChamber_datfile.format(**form_dict))
        f.close()

        # write mwpc
        f = open(mwpc_file, 'w')
        f.write(IFileTemplates.mwpc_datfile.format(**form_dict))
        f.close()

        # write reaction
        f = open(rxn_file, 'w')
        f.write(IFileTemplates.reaction_datfile.format(**form_dict))
        f.close()

        # write slits
        f = open(slits_file, 'w')
        f.write(IFileTemplates.slits_datfile.format(**form_dict))
        f.close()

        # write target degraders
        f = open(target_degraders_file, 'w')
        f.write(IFileTemplates.targetDegraders_datfile.format(**form_dict))
        f.close()

    else:
        # raise error
        print("error: write_input_files, user dir path doesn't exist")






#TODO: I might want to make a helper method to deal with writing target degraders datfile because it will be more complex



#
