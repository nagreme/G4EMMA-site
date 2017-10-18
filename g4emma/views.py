from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import g4emma.forms as G4Forms
import subprocess as sp
import g4emma.g4emma_input_setup as G4ISetup

def home(request):
    return render(request, 'g4emma/home.html')

def about(request):
    return render(request, 'g4emma/about.html')

def manual(request):
    return render(request, 'g4emma/manual.html')

def simulation(request):
    results = "" #if there has been no post request, there are no results

    forms_list = [G4Forms.BeamForm, G4Forms.BeamEmittanceForm, G4Forms.CentralTrajectoryForm]

    if request.method == 'POST':
        # beam_form = G4Forms.BeamForm(request.POST)
        # beam_emit_form = G4Forms.BeamEmittanceForm(request.POST)
        # central_traj_form = G4Forms.CentralTrajectoryForm(request.POST)

        forms_are_all_valid = True

        for index, input_form in enumerate(forms_list):
            #setup the forms
            forms_list[index] = input_form(request.POST)

            #test their validity
            forms_are_all_valid = forms_are_all_valid and forms_list[index].is_valid()


        if forms_are_all_valid:
            # sim_params = form.cleaned_data
            sim_params = {} #setup a blank start

            for input_form in forms_list:
                #agglomerate all the forms' input into one dictionary
                sim_params.update(input_form.cleaned_data)

            # Properly escape/quote strings (the numbers are restrained by django)
            G4ISetup.sanitize_input_dict(sim_params)

            # Setup a user directory, save its path
            # user_dirs_path = "/data/emma" #location in VM
            user_dirs_path = "/home/npulgar-vidal/test_location"
            userdir = G4ISetup.setup_unique_userdir(user_dirs_path)

            if userdir is None:
                #raise error
                print("error: we weren't able to setup a userdir") #placeholder

            # Overlay the user input on a set of default values so that we have a complete input set
            sim_params = G4ISetup.merge_with_defaults(sim_params)

            # write to input files
            G4ISetup.write_input_files(userdir, sim_params)

            # build command

            # execute it

            # any post sim actions
            # upload results?
            # cleanup userdir?

            # Set results to a rendering of the sims output? or put the data of the output files there somehow
            command = ". G4EMMA_wrapper.sh {num_events} {beam_proton_num} {beam_nucleon_num} {beam_charge_state} {beam_kinetic_e}".format(**sim_params)

            # results = sp.check_output(". G4EMMA_wrapper.sh", shell=True, universal_newlines=True)
            # results = str(results) + str(sim_params)

            results = command + str(sim_params)

    else:
        for index, input_form in enumerate(forms_list):
            #setup the forms
            forms_list[index] = input_form()

    return render(request, 'g4emma/simulation.html', {'forms_list': forms_list, 'results':results})


def tools(request):
    return render(request, 'g4emma/tools.html')
