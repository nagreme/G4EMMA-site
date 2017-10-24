#===========================
# IMPORTS
#===========================
from django import forms
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.core.validators import RegexValidator

#===========================
# CUSTOM FIELDS AND WIDGETS
#===========================
# Hack from stackoverflow to enable me to add headers to forms
class HeaderWidget(forms.widgets.Widget):
    def render(self, name, value, attrs=None):
        attrs.update(self.attrs)
        return format_html('<div{0}>{1}</div>', flatatt(attrs), value)


class ElementWidget(forms.MultiWidget):
    def __init__(self, widgets=None, *args, **kwargs):
        self.widgets = [
            forms.NumberInput(),
            forms.NumberInput(),
            forms.NumberInput()
        ]
        super(ElementWidget, self).__init__(self.widgets, *args, **kwargs)
    def decompress(self, value):
        if value:
            return value.split(' ')
        return [None, None, None]


class ElementField(forms.MultiValueField):
    widget = ElementWidget

    def __init__(self, *args, **kwargs):
        fields = (
            forms.IntegerField(
                error_messages={'incomplete': 'Enter a proton number.'}, label="Z", help_text=", "
            ),
            forms.DecimalField(
                error_messages={'incomplete': 'Enter a molar mass.'}, label="M", help_text="g/mol, "
            ),
            forms.DecimalField(
                error_messages={'incomplete': 'Enter a weight ratio.'}, label="\u03b7", help_text="%"
            ),
        )
        super(ElementField, self).__init__(
            fields=fields, require_all_fields=True, *args, **kwargs
        )

    def compress(self, data_list):
        # Documentation says we can assume that data is valid
        return " ".join(str(x) for x in data_list)


#===========================
# FORM CLASSES
#===========================

# Note: I use 0 and 1 instead of booleans to allow the JS to use them easily

class BeamForm(forms.Form):
    name = "beam_form"
    num_events = forms.IntegerField(required=True, label="n", help_text="(Number of events)")
    beam_proton_num = forms.IntegerField(required=True, label="Z", help_text="(Proton number)")
    beam_nucleon_num = forms.IntegerField(required=True, label="A", help_text="(Nucleon number)")
    beam_charge_state = forms.IntegerField(required=True, label="Q", help_text="(Charge state)")
    beam_kinetic_e = forms.DecimalField(required=True, label="E", help_text="MeV (Kinetic energy)")


class BeamEmittanceChoiceForm(forms.Form):
    name = "beam_emittance_choice_form"
    BEAM_EMITTANCE_CHOICES = (
        (0, "Zero"), #the first value is the actual value in the code
        (1, "Specify") # the second is the value the user sees
    )
    # toggle specify/zero
    specify_beam_emittance = forms.ChoiceField(required=True, label="Beam emittance", choices = BEAM_EMITTANCE_CHOICES, initial=0)

class BeamEmittanceForm(forms.Form):
    name = "beam_emittance_form"
    beam_e_spread = forms.DecimalField(required=False, label="\u03b4E/E", help_text="% (FWHM, beam energy spread)")
    beam_diameter = forms.DecimalField(required=False, label="d", help_text="mm (beam diameter)")
    beam_trans_emittance = forms.DecimalField(required=False, label="\u03b3\u03b2\u03b5", help_text="\u03c0 mm mrad (Beam transverse emittance)")


class CentralTrajectoryChoiceForm(forms.Form):
    name = "central_traj_choice_form"
    CENTRAL_TRAJECTORY_CHOICES = (
        (0, "Same as beam"),
        (1, "Specify")
    )
    specify_central_trajectory = forms.ChoiceField(required=True,
    label="Central trajectory", choices = CENTRAL_TRAJECTORY_CHOICES,
    initial=0)

class CentralTrajectoryForm(forms.Form):
    name = "central_traj_form"
    center_traj_proton_num = forms.IntegerField(required=False, label="ZC", help_text="(Proton number)")
    center_traj_nucleon_num = forms.IntegerField(required=False, label="AC", help_text="(Nucleon number)")
    center_traj_charge_state = forms.IntegerField(required=False, label="QC", help_text="(Charge state)")
    center_traj_kinetic_e = forms.DecimalField(required=False, label="EC", help_text="MeV (Kinetic Energy)")


class ReactionChoiceForm(forms.Form):
    name = "reaction_choice_form"
    REACTION_CHOICES = (
        (0, "No"),
        (1, "Yes")
    )
    specify_reaction = forms.ChoiceField(required=True, label="Two-body reaction", choices=REACTION_CHOICES, initial=0)

class ReactionForm(forms.Form):
    name = "reaction_form"
    header_line1 = forms.CharField(widget=HeaderWidget(attrs={'class': 'form-header'}), initial='', required=False, label='Reaction: 1+2 --> 3+4')
    header_line2 = forms.CharField(widget=HeaderWidget(attrs={'class': 'form-header'}), initial='', required=False, label='Z1 = Z')
    header_line3 = forms.CharField(widget=HeaderWidget(attrs={'class': 'form-header'}), initial='', required=False, label='A1 = A')

    rxn_z2_target = forms.IntegerField(required=False, label="Z2", help_text="(Z2 target)")
    rxn_a2 = forms.IntegerField(required=False, label="A2", help_text="(A2 target)")
    rxn_z3_recoil = forms.IntegerField(required=False, label="Z3", help_text="(Z3 recoil)")
    rxn_a3 = forms.IntegerField(required=False, label="A3", help_text="(A3 recoil)")
    rxn_z4_ejectile = forms.IntegerField(required=False, label="Z4", help_text="(Z4 ejectile)")
    rxn_a4 = forms.IntegerField(required=False, label="A4", help_text="(A4 ejectile)")

    header_line4 = forms.CharField(widget=HeaderWidget(attrs={'class': 'form-header'}), initial='', required=False, label='Properties of recoil (#3):')
    rxn_min_angle = forms.DecimalField(required=False, label="\u03b8cm,min", help_text="deg (min cm angle of ejectile)")
    rxn_max_angle = forms.DecimalField(required=False, label="\u03b8cm,max", help_text="deg (max cm angle of ejectile)")
    rxn_recoil_charge = forms.IntegerField(required=False, label="Q3", help_text="(charge state of recoil)")
    rxn_recoil_excitation_e = forms.DecimalField(required=False, label="Ex", help_text="MeV (excitation energy of recoil)")

    header_line5 = forms.CharField(widget=HeaderWidget(attrs={'class': 'form-header'}), initial='', required=False, label='Cross section:')
    rxn_cross_sec = forms.DecimalField(required=False, label="d\u03c3/d\u03a9cm", help_text="mb/sr (solid-angle averaged cross section)")


class TargetChoiceForm(forms.Form):
    name = "target_choice_form"
    TARGET_CHOICES = (
        (0, "No"),
        (1, "Yes")
    )
    target_inserted = forms.ChoiceField(required=True, label="Target", choices=TARGET_CHOICES, initial=0)

class TargetForm(forms.Form):
    name = "target_form"
    target_thickness = forms.DecimalField(required=False, label="x0", help_text="\u03bcm (thickness)")
    target_z_pos = forms.DecimalField(required=False, label="z-pos", help_text="cm (target z position offset)")
    target_density = forms.DecimalField(required=False, label="\u03c1", help_text="g/cm³ (target density)")

class TargetElementsForm(forms.Form):
    name = "target_elements_form"
    NUM_ELEM_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    )
    target_num_elems = forms.ChoiceField(required=True, label="Number of elements", choices=NUM_ELEM_CHOICES, initial=1)
    elem_guideline = forms.CharField(widget=HeaderWidget(attrs={'class': 'form-header'}), initial='', required=False, label='Element #: Z = proton number, M = molar mass (g/mol), \u03b7 = weight ratio (%)', label_suffix="")
    target_elem_1 = ElementField(required=False, label="Element 1")
    target_elem_2 = ElementField(required=False, label="Element 2")
    target_elem_3 = ElementField(required=False, label="Element 3")
    target_elem_4 = ElementField(required=False, label="Element 4")
    target_elem_5 = ElementField(required=False, label="Element 5")


class Degrader1ChoiceForm(forms.Form):
    name = "degrader1_choice_form"
    DEGRADER1_CHOICES = (
        (0, "No"),
        (1, "Yes")
    )
    degrader1_inserted = forms.ChoiceField(required=True, label="Degrader 1", choices=DEGRADER1_CHOICES, initial=0)

class Degrader1Form(forms.Form):
    name = "degrader1_form"
    degrader1_thickness = forms.DecimalField(required=False, label="x0", help_text="\u03bcm (thickness)")
    degrader1_density = forms.DecimalField(required=False, label="\u03c1", help_text="g/cm³ (degrader 1 density)")

class Degrader1ElementsForm(forms.Form):
    name = "degrader1_elements_form"
    NUM_ELEM_CHOICES = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    )
    degrader1_num_elems = forms.ChoiceField(required=True, label="Number of elements", choices=NUM_ELEM_CHOICES, initial=1)
    elem_guideline = forms.CharField(widget=HeaderWidget(attrs={'class': 'form-header'}), initial='', required=False, label='Element #: Z = proton number, M = molar mass (g/mol), \u03b7 = weight ratio (%)', label_suffix="")
    degrader1_elem_1 = ElementField(required=False, label="Element 1")
    degrader1_elem_2 = ElementField(required=False, label="Element 2")
    degrader1_elem_3 = ElementField(required=False, label="Element 3")
    degrader1_elem_4 = ElementField(required=False, label="Element 4")
    degrader1_elem_5 = ElementField(required=False, label="Element 5")
