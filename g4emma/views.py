from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import g4emma.forms as G4Forms
import subprocess as sp
import g4emma.g4emma_input_setup as G4ISetup
from django.conf import settings
from os import environ

def home(request):
    return render(request, 'g4emma/home.html')

def about(request):
    return render(request, 'g4emma/about.html')

def manual(request):
    return render(request, 'g4emma/manual.html')

def simulation(request):
    results = "" #if there has been no post request, there are no results

    forms_list = [G4Forms.AlphaSourceChoiceForm,
    G4Forms.AlphaSourceForm,
    G4Forms.BeamForm,
    G4Forms.BeamEmittanceChoiceForm,
    G4Forms.BeamEmittanceForm,
    G4Forms.CentralTrajectoryChoiceForm,
    G4Forms.CentralTrajectoryForm,
    G4Forms.ReactionChoiceForm,
    G4Forms.ReactionForm,
    G4Forms.TargetChoiceForm,
    G4Forms.TargetForm,
    G4Forms.TargetElementsForm,
    G4Forms.Degrader1ChoiceForm,
    G4Forms.Degrader1Form,
    G4Forms.Degrader1ElementsForm,
    G4Forms.Degrader2ChoiceForm,
    G4Forms.Degrader2Form,
    G4Forms.Degrader2ElementsForm,
    G4Forms.Slit1ChoiceForm,
    G4Forms.Slit1Form,
    G4Forms.Slit2ChoiceForm,
    G4Forms.Slit2Form,
    G4Forms.Slit3ChoiceForm,
    G4Forms.Slit3Form,
    G4Forms.Slit4ChoiceForm,
    G4Forms.Slit4Form,
    G4Forms.MWPCForm,
    G4Forms.IonChamberChoiceForm,
    G4Forms.IonChamberForm
    ]

    if request.method == 'POST':
        forms_are_all_valid = True

        for index, input_form in enumerate(forms_list):
            #setup the forms
            forms_list[index] = input_form(request.POST)

            #test their validity
            forms_are_all_valid = forms_are_all_valid and forms_list[index].is_valid()


        if forms_are_all_valid:
            sim_params = {} #setup a blank start

            for input_form in forms_list:
                #agglomerate all the forms' input into one dictionary
                sim_params.update(input_form.cleaned_data)

            # Do some cleanup before adding another user dir
            G4ISetup.cleanup_old_userdirs()

            # Setup a user directory, save its path
            user_dirs_path = settings.MEDIA_ROOT
            userdir = G4ISetup.setup_unique_userdir(user_dirs_path)
            userdir_path = "{}{}".format(user_dirs_path, userdir)

            if userdir is None:
                #raise error
                print("error: we weren't able to setup a userdir") #placeholder


            # Overlay the user input on a set of default values so that we have a complete input set
            sim_params = G4ISetup.merge_with_defaults(sim_params)

            # write to input files
            G4ISetup.write_input_files(userdir_path, sim_params)

            
            # Build command to call simulation wrapper 
            wrapper_path = environ['G4EMMA_VENV_BIN'] + "/G4EMMA_wrapper.sh"
            command = " ".join((wrapper_path, environ['G4EMMA_APP_PATH'], userdir_path + "/"))  #this last slash is important!!!
            #command = '/opt/emma/g4emma/venv/bin/test.sh'


            try:
                results = sp.check_output(command, shell=True, universal_newlines=True)
            except sp.CalledProcessError as e:
                # let user know that something went wrong (give some ideas of what it could be)
                err_msg = ("An error occured when trying to run the simulation. Check that target and "
                          "degrader thickness is greater than 1e-5, that elements chosen are possible, "
                          "and that the magnetic and electric rigidities determined by central "
                          "trajectory parameters do not exceed maximum allowed values.\n\n")

                if (Path(userdir_path+"/Results/rigidities.dat").exists()):
                    # read rigidities file and set form errors render form
                    with open(userdir_path+"/Results/rigidities.dat") as r_file:
                        magnetic_rigidity = r_file.readline() #the first two lines are constant
                        electric_rigidity = r_file.readline()
                        # then will be 2-4 warning/error lines
                        rigidity_err_msgs = r_file.read()

                    rigidity_err_msgs = ("Magnetic rigidity: {}\n"
                                         "Electric rigidity: {}\n"
                                         "{}").format(magnetic_rigidity,
                                         electric_rigidity,
                                         rigidity_err_msgs)
                else:
                    rigidity_err_msgs = ""

                return render(request, 'g4emma/simulation.html',
                {'forms_list':forms_list, 'general_err_msg':err_msg, 'rigidity_err_msg':rigidity_err_msgs})



            #get a list of the generated output files
            outfiles = str(sp.check_output("ls -l "+userdir_path+"/Results/ | awk '{print $9;}'", shell=True, universal_newlines=True))

            # make a list from that command's output
            outfiles_list = outfiles.strip().splitlines()

            # TODO: These request.sessions are causing an error upon subsequent redirect... But why...?
            # Store the results in a session so that the page we redirect to can access them
            request.session['cmd'] = command
            request.session['results'] = results
            request.session['outdir'] = "/media/"+userdir+"/Results/"
            request.session['outfiles'] = outfiles_list

            with open("/data/emma/userdirs/xinfo.txt", 'w') as f:
                f.write("userdir: " + userdir + "\n")
                f.write("userdir_path :" + userdir_path + " \n")
                f.write("outfiles: " + outfiles + "\n\n")
                f.write("outfiles list: " + str(outfiles_list) + "\n\n")

            # I could use a single return statement but I feel it would be a bit much here
            return redirect('results')
            #return redirect('about')

    else:
        for index, input_form in enumerate(forms_list):
            #setup the forms
            forms_list[index] = input_form()

    return render(request, 'g4emma/simulation.html', {'forms_list': forms_list})


def tools(request):
    return render(request, 'g4emma/tools.html')

def results(request):
    return render(request, 'g4emma/results.html',
        {'results':request.session.pop('results', {}),
         'outfiles':request.session.pop('outfiles', {}),
         'outdir':request.session.pop('outdir', "#"),
          'cmd':request.session.pop('cmd', "command not generated")})
