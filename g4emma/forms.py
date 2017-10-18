from django import forms

class BeamForm(forms.Form):
    num_events = forms.IntegerField(required=True, label="n", help_text="(Number of events)")
    beam_proton_num = forms.IntegerField(required=True, label="Z", help_text="(Proton number)")
    beam_nucleon_num = forms.IntegerField(required=True, label="A", help_text="(Nucleon number)")
    beam_charge_state = forms.IntegerField(required=True, label="Q", help_text="(Charge state)")
    beam_kinetic_e = forms.DecimalField(required=True, label="E", help_text="MeV (Kinetic energy)")

class BeamEmittanceForm(forms.Form):
    BEAM_EMITTANCE_CHOICES = (
        (False, "Zero"), #the first value is the actual value in the code
        (True, "Specify") # the second is the value the user sees
    )
    # toggle specify/zero
    specify_beam_emittance = forms.ChoiceField(required=True, label="Beam emittance", widget=forms.RadioSelect(), choices = BEAM_EMITTANCE_CHOICES, initial=False)
    beam_e_spread = forms.DecimalField(label="\u03b4E/E", help_text="% (FWHM, beam energy spread)")
    beam_diameter = forms.DecimalField(label="d", help_text="mm (beam diameter)")
    beam_trans_emittance = forms.DecimalField(label="\u03b3\u03b2\u03b5", help_text="\u03c0 mm mrad (Beam transverse emittance)")

class CentralTrajectoryForm(forms.Form):
    CENTRAL_TRAJECTORY_CHOICES = (
        (False, "Same as beam"),
        (True, "Specify")
    )
    specify_central_trajectory = forms.ChoiceField(required=True,
    label="Central trajectory", choices = CENTRAL_TRAJECTORY_CHOICES,
    initial=False)
    center_traj_proton_num = forms.IntegerField(label="ZC", help_text="(Proton number)")
    center_traj_nucleon_num = forms.IntegerField(label="AC", help_text="(Nucleon number)")
    center_traj_charge_state = forms.IntegerField(label="QC", help_text="(Charge state)")
    center_traj_kinetic_e = forms.DecimalField(label="EC", help_text="MeV (Kinetic Energy)")
