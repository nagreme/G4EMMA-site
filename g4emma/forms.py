from django import forms

class SimulationForm(forms.Form):
    num_events = forms.IntegerField(required=True, label="Number of events")
    beam_proton_num = forms.IntegerField(required=True, label="Z", help_text="(Proton number)")
    beam_nucleon_num = forms.IntegerField(required=True, label="A", help_text="(Nucleon number)")
    beam_charge_state = forms.IntegerField(required=True, label="Q", help_text="(Charge state)")
    beam_kinetic_e = forms.DecimalField(required=True, label="E", help_text="MeV (Kinetic energy)")
