#*************************************************************
# infile_templates.py
#
# Nadège Pulgar-Vidal
# 2017-Oct-03
#
# Store template format strings used to build the input files
#*************************************************************

#TODO: name all the placeholders to be able to feed form_dict

alphaSource_datfile = ("{}\t# YES/NO\n"
                       "{}\t# alpha particle kinetic energy (MeV)\n"
                       "{}\t# max angle alpha source (deg)")

beam_datfile = ("{}\t# number of events\n"
                "{}\t# beam Z\n"
                "{}\t# beam A\n"
                "{}\t# beam kinetic energy (MeV)\n"
                "{}\t# fractional energy spread (FWHM)\n"
                "{}\t# beam-spot diameter (mm)\n"
                "{}\t# normalized transverse emittance (pi mm mrad)\n")

centralTrajectory_datfile = ("{}\t# Z\n"
                             "{}\t# A\n"
                             "{}\t# charge state Q\n"
                             "{}\t#kinteic energy (MeV)\n")

ionChamber_datfile = ("{}\t# IN/OUT\n"
                      "{}\t# pressure (torr)\n"
                      "{}\t# temperature (degrees Celsius)\n")

mwpc_datfile = ("{}\t# IN/OUT\n"
                      "{}\t# pressure (torr)\n"
                      "{}\t# temperature (degrees Celsius)\n")

reaction_datfile = ("# Two-body reaction: 1 + 2 --> 3 + 4"
                    "{}\t# Z1 beam\n"
                    "{}\t# A1\n"
                    "{}\t# Z2 beam\n"
                    "{}\t# A2\n"
                    "{}\t# Z3 recoil\n"
                    "{}\t# A3\n"
                    "{}\t# Z4 ejectile\n"
                    "{}\t# A4\n"
                    "{}\t# min c.m. angle ofejectile\n"
                    "{}\t# max c.m. angle of ejectile\n"
                    "{}\t# charge state of recoil\n"
                    "{}\t# excitation energy of recoil\n"
                    "{}\t# solid-angle averaged cross section (mb/sr) inside the angular range specified above\n")

slits_datfile = ("# SLITS 1 (HORIZONTAL)"
                 "{}\t# OUT/(mm)\n"
                 "# SLITS 2 (HORIZONTAL)"
                 "{}\t# OUT/(mm)\n"
                 "# SLITS 3 (RIGHT)"
                 "{}\t# OUT/(mm)\n"
                 "# SLITS 4 (LEFT)"
                 "{}\t# OUT/(mm)\n")

targetDegraders_datfile = ("# TARGET"
                           "{}\t# IN/OUT/\n"
                           "{}\t# thickness (um)\n"
                           "{}\t# target z position offset (cm)\n"
                           "{}\t# density (g/cm3)\n"
                           "{}\t# number of elements\n"
                           "{}\n" #variable number of elements here
                           "# DEGRADER 1"
                           "{}\t# IN/OUT\n"
                           "{}\t# thickness (um)\n"
                           "{}\t# density (g/cm3)\n"
                           "{}\t# number of elements\n"
                           "{}\n" #variable number of elements here
                           "# DEGRADER 2"
                           "{}\t# IN/OUT\n"
                           "{}\t# thickness (um)\n"
                           "{}\t# density (g/cm3)\n"
                           "{}\t# number of elements\n"
                           "{}\n") #variable number of elements here

element_format_str = "{} {} {}\t# element {elem_num}: Z, M, (g/mol), mass fraction"
