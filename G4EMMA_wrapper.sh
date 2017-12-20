#!/bin/bash

#server vm (set the geant4 and root env vars)
source /opt/emma/root/v5.34.36/bin/mythisroot.sh
source /opt/emma/geant4.9.6-install/bin/mygeant4.sh 

# $1 is the MainDir
# $2 is the UserDir

# with autorun enabled
"$G4EMMA_SIM_PATH"/EMMAapp visOff $1 $2 <<< exit
