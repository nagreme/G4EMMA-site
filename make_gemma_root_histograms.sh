#!/bin/bash

# This script will run a root macro on a root file containing data
# from a G4EMMA simulation to generate histograms
# It requires a G4EMMA userdir path as input (no trailing '/')

# $1 is G4EMMA userdir

# This should have already been sourced on the server but I'll 
# leave it here in case it's needed
source /opt/emma/root/v5.34.36/bin/mythisroot.sh

# path to rootanalysis folder
# the macro includes a bunch of other files: it'll work as long as 
# those files are in the same directory

root -b .x $G4EMMA_ROOT_HIST_MACRO_PATH $1 <<< .q
