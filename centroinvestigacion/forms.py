from django import forms
from centroinvestigacion.models import CentroInvestigacion, Enfoque


class FormCentroInvestigacion(forms.ModelForm):


    class Meta:
        model = CentroInvestigacion
        fields = '__all__'

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'calle': forms.TextInput(attrs={'class': 'form-control'}),
            'colonia': forms.TextInput(attrs={'class': 'form-control'}),
            'numExterior': forms.TextInput(attrs={'class': 'form-control'}),
            'cp': forms.TextInput(attrs={'class': 'form-control'}),                                                
            'estado': forms.TextInput(attrs={'class': 'form-control', 'value':'Zacatecas', 'readonly': 'true'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'latitud': forms.TextInput(attrs={'class': 'form-control', 'readonly' : 'true'}),
            'longitud': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'true'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'areaEnfoque': forms.Select(attrs={'class': 'form-select'}),
            'subAreaEnfoque': forms.Select(attrs={'class': 'form-select'}),
            'sitioWeb': forms.TextInput(attrs={'class': 'form-control'}),
            'nombreEncargado': forms.TextInput(attrs={'class': 'form-control'}),
            'correoEncargado': forms.TextInput(attrs={'class': 'form-control'}),
            'telefonoEncargado': forms.TextInput(attrs={'class': 'form-control'}),
        }

        imagen = forms.ImageField(widget=forms.ImageField())
        logotipo = forms.ImageField(widget=forms.ImageField())


        def __init__(self, *args, **kwargs):
            super(FormCentroInvestigacion, self).__init__(*args, **kwargs)
            self.fields['imagen'].required = False
            self.fields['logotipo'].required = False



class FormEnfoque(forms.ModelForm):

    class Meta:
        model = Enfoque
        fields = '__all__'

        widgets = {
            'area': forms.Select(attrs={'class': 'form-control'}),
            'subarea': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),

        }
