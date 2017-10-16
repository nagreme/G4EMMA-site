#*************************************************************
# infile_templates.py
#
# Nadège Pulgar-Vidal
# 2017-Oct-03
#
# Store template format strings used to build the input files
#*************************************************************


alphaSource_datfile = ("{alpha_source_present}\t# YES/NO\n"
                       "{alpha_source_kinetic_e}\t# alpha particle kinetic energy (MeV)\n"
                       "{alpha_source_max_angle}\t# max angle alpha source (deg)")

beam_datfile = ("{num_events}\t# number of events\n"
                "{beam_proton_num}\t# beam Z\n"
                "{beam_nucleon_num}\t# beam A\n"
                "{beam_charge_state}\t# beam charge state Q\n"
                "{beam_kinetic_e}\t# beam kinetic energy (MeV)\n"
                "{beam_e_spread}\t# fractional energy spread (FWHM)\n"
                "{beam_diameter}\t# beam-spot diameter (mm)\n"
                "{beam_trans_emittance}\t# normalized transverse emittance (pi mm mrad)\n")

centralTrajectory_datfile = ("{center_traj_proton_num}\t# Z\n"
                             "{center_traj_nucleon_num}\t# A\n"
                             "{center_traj_charge_state}\t# charge state Q\n"
                             "{center_traj_kinetic_e}\t#kinteic energy (MeV)\n")

ionChamber_datfile = ("{ion_chamber_inserted}\t# IN/OUT\n"
                      "{ion_chamber_pressure}\t# pressure (torr)\n"
                      "{ion_chamber_temp}\t# temperature (degrees Celsius)\n")

mwpc_datfile = ("{mwpc_inserted}\t# IN/OUT\n"
                "{mwpc_pressure}\t# pressure (torr)\n"
                "{mwpc_temp}\t# temperature (degrees Celsius)\n")

reaction_datfile = ("# Two-body reaction: 1 + 2 --> 3 + 4"
                    "{rxn_z1_beam}\t# Z1 beam\n"
                    "{rxn_a1}\t# A1\n"
                    "{rxn_z2_target}\t# Z2 target\n"
                    "{rxn_a2}\t# A2\n"
                    "{rxn_z3_recoil}\t# Z3 recoil\n"
                    "{rxn_a3}\t# A3\n"
                    "{rxn_z4_ejectile}\t# Z4 ejectile\n"
                    "{rxn_a4}\t# A4\n"
                    "{rxn_min_angle}\t# min c.m. angle ofejectile\n"
                    "{rxn_max_angle}\t# max c.m. angle of ejectile\n"
                    "{rxn_recoil_charge}\t# charge state of recoil\n"
                    "{rxn_recoil_excitation_e}\t# excitation energy of recoil\n"
                    "{rxn_cross_sec}\t# solid-angle averaged cross section (mb/sr) inside the angular range specified above\n")

#TODO: Is there a variable part if SLIT="IN"?
slits_datfile = ("# SLITS 1 (HORIZONTAL)"
                 "{slit_1_inserted}\t# OUT/(mm)\n"
                 "# SLITS 2 (HORIZONTAL)"
                 "{slit_2_inserted}\t# OUT/(mm)\n"
                 "# SLITS 3 (RIGHT)"
                 "{slit_3_inserted}\t# OUT/(mm)\n"
                 "# SLITS 4 (LEFT)"
                 "{slit_4_inserted}\t# OUT/(mm)\n")

targetDegraders_datfile = ("# TARGET"
                           "{target_inserted}\t# IN/OUT/\n"
                           "{target_thickness}\t# thickness (um)\n"
                           "{target_z_pos}\t# target z position offset (cm)\n"
                           "{target_density}\t# density (g/cm3)\n"
                           "{target_num_elems}\t# number of elements\n"
                           "{target_elems}\n" #variable number of elements here
                           "# DEGRADER 1"
                           "{degreder_1_inserted}\t# IN/OUT\n"
                           "{degrader_1_thickness}\t# thickness (um)\n"
                           "{degrader_1_density}\t# density (g/cm3)\n"
                           "{degrader_1_num_elems}\t# number of elements\n"
                           "{degrader_1_elems}\n" #variable number of elements here
                           "# DEGRADER 2"
                           "{degrader_2_inserted}\t# IN/OUT\n"
                           "{degrader_2_thickness}\t# thickness (um)\n"
                           "{degrader_2_density}\t# density (g/cm3)\n"
                           "{degrader_2_num_elems}\t# number of elements\n"
                           "{degrader_2_elems}\n") #variable number of elements here

element_format_str = "{elem_proton_num} {elem_molar_mass} {elem_weight_ratio}\t# element {elem_num}: Z, M, (g/mol), mass fraction"
