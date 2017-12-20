#!/bin/bash

# master branch wrapper script
# assumes that thisroot.sh and geant4.sh have already been sourced

# $1 is the MainDir
# $2 is the UserDir

# with autorun enabled
"$G4EMMA_SIM_PATH"/EMMAapp visOff $1 $2 <<< exit

