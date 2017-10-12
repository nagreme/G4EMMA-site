from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from g4emma.forms import SimulationForm

def home(request):
    return render(request, 'g4emma/home.html')

def about(request):
    return render(request, 'g4emma/about.html')

def manual(request):
    return render(request, 'g4emma/manual.html')

def simulation(request):
    results = ""

    if request.method == 'POST':
        form = SimulationForm(request.POST)

        if form.is_valid():
            sim_params = form.cleaned_data

            # Call simulation with cleaned data
            # Set results to a rendering of the sims output? or put the data of the output files there somehow
            # For now echo the cleaned input back to the user
            results = sim_params

    else:
        form = SimulationForm()

    return render(request, 'g4emma/simulation.html', {'form': form, 'results':results})

def tools(request):
    return render(request, 'g4emma/tools.html')
