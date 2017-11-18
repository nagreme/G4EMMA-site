#!/bin/bash

#WRAPPER_FILE=/data/emma/wrapper_info.txt

#echo "start wrapper" >> $WRAPPER_FILE

#server vm (set the geant4 and root env vars)
source /opt/emma/root/v5.34.36/bin/mythisroot.sh
source /opt/emma/geant4.9.6-install/bin/mygeant4.sh 

#echo "sourced root and geant4" >> $WRAPPER_FILE

# $1 is the MainDir
# $2 is the UserDir

#echo "MainDir $1" >> $WRAPPER_FILE
#echo "USerDir $2" >> $WRAPPER_FILE

# with autorun enabled
"$G4EMMA_APP_PATH"/EMMAapp visOff $1 $2 <<< exit

#echo "sim done" >> $WRAPPER_FILE


