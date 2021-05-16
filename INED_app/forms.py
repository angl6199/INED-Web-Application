from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import AdultoMayor, Usuario
from django.forms import ModelForm
from django.forms import widgets

class FormaLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormaLogin, self).__init__(*args, **kwargs)
    
    username = forms.CharField(label='Nombre de usuario:', widget=forms.TextInput(attrs={'class':'field', 'required':'required'}))
    password = forms.CharField(label='Contraseña:', widget=forms.PasswordInput(attrs={'class': 'field', 'required':'required'}))

class FormaVisualizar(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('username', 'nombres', 'apellido_paterno', 'apellido_materno', 'tipo_contratacion', 'numero_empleado', 'tipo_usuario', 'email', 'numero_telefonico')
        widgets = {
            'username': forms.TextInput(
                attrs = {'readonly':'True','class':'register-field','autocomplete': 'off', 'placeholder':'Nombre de usuario'}
            ),
            'nombres': forms.TextInput(
                attrs = {'readonly':'True','class':'register-field','autocomplete': 'off', 'placeholder':'Nombre(s)'}
            ),
            'apellido_paterno': forms.TextInput(
                attrs = {'readonly':'True','class':'register-field','autocomplete': 'off', 'placeholder':'Apellido Paterno'}
            ),
            'apellido_materno': forms.TextInput(
                attrs = {'readonly':'True','class':'register-field','autocomplete': 'off', 'placeholder':'Apellido Materno'}
            ),
            'tipo_contratacion': forms.TextInput(
                attrs = {'readonly':'True','class':'register-field','autocomplete': 'off', 'placeholder':'Tipo de Contratación'}
            ),
            'numero_empleado': forms.NumberInput(
                attrs = {'readonly':'True','class':'register-field','autocomplete': 'off', 'placeholder':'Número de Empleado'}
            ),
            'tipo_usuario': forms.TextInput(
                attrs = {'readonly':'True','class':'register-field','autocomplete': 'off', 'placeholder':'Número de Empleado'}
            ),
            'email': forms.EmailInput(
                attrs = {'readonly':'True','class':'register-field','autocomplete': 'off', 'placeholder':'Correo Electrónico'}
            ),
            'numero_telefonico': forms.NumberInput(
                attrs = {'readonly':'True','class':'register-field','autocomplete': 'off', 'placeholder':'Número Telefónico'}
            ),
        }

class AdultoRegistro(forms.ModelForm):
    nombres = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Nombre(s)', 'class':'input-adult-1'}))
    apellido_paterno = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Apellido Paterno', 'class':'input-adult-1'}))
    apellido_materno = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Apellido Materno', 'class':'input-adult-1'}))
    check_fechanacimiento = forms.BooleanField(label="¿Cuenta con fecha de nacimiento?")
    fechanacimiento = forms.DateField(label="Fecha de nacimiento", widget=forms.DateInput(attrs={'type': 'date', 'class':'input-adult-1'}))
    sexo = forms.ChoiceField(label="Sexo", widget=forms.Select(attrs={'class':'input-adult-1'}))
    edad = forms.IntegerField(label="", widget=forms.NumberInput(attrs={'placeholder':'Edad', 'readonly':True, 'class':'input-adult-1'}))
    estado_civil = forms.ChoiceField(label="Estado civil", widget=forms.Select(attrs={'class':'input-adult-1'}))
    ocupacion = forms.ChoiceField(label="¿A qué se dedica actualmente?", widget=forms.Select(attrs={'class':'input-adult-1'}))
    ocupacion_anterior = forms.ChoiceField(label="¿Y anteriormente?", widget=forms.Select(attrs={'class':'input-adult-1'}))
    seguridad_social = forms.ChoiceField(label="Seguridad social", widget=forms.Select(attrs={'class':'input-adult-1'}))
    utiliza_seguridad_social = forms.BooleanField(label="¿Los utiliza?")
    check_vive_solo = forms.BooleanField(label="¿Vive solo?")
    acompanante = forms.ChoiceField(label="¿Con quién vive?", widget=forms.Select(attrs={'class':'input-adult-1'}))
    acompanante_sexo = forms.ChoiceField(label="Sexo de acompañante", widget=forms.Select(attrs={'class':'input-adult-1'}))
    check_acompanante_fechanacimiento = forms.BooleanField(label="¿Esta persona cuénta con fecha de nacimiento?")
    acompanante_fechanacimiento = forms.DateField(label="Fecha de nacimiento acompañante", widget=forms.TextInput(attrs={'type':'date', 'class':'input-adult-1'}))
    check_cuidador = forms.BooleanField(label="¿Tiene cuidador?")
    cuidador = forms.ChoiceField(label="¿Quién lo cuida?", widget=forms.Select(attrs={'class':'input-adult-1'}))
    cuidador_sexo = forms.ChoiceField(label="Sexo del cuidador", widget=forms.Select(attrs={'class':'input-adult-1'}))
    check_cuidador_fechanacimiento = forms.BooleanField(label="¿Esta persona cuénta con fecha de nacimiento?")
    cuidador_fechanacimiento = forms.DateField(label="Fecha de nacimiento cuidador", widget=forms.TextInput(attrs={'type':'date', 'class':'input-adult-1'}))
    nombres_profesional = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Nombre(s) Profesional en servicios', 'class':'input-adult-1'}))
    apellido_paterno_profesional = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Apellido Paterno Profesional en servicios', 'class':'input-adult-1'}))
    apellido_materno_profesional = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Apellido Materno Profesional en servicios', 'class':'input-adult-1'}))
    fechaevaluacion = forms.DateField(label="Fecha de la evaluación", widget=forms.TextInput(attrs={'type':'date', 'class':'input-adult-1'}))

    class Meta:
        model = AdultoMayor
        fields = '__all__'
        


class FormaRegistro(forms.ModelForm):
    CATEGORIAS_USUARIOS = (
        ('-', '-'),
        ('Administrador', 'Administrador'),
        ('Monitor', 'Monitor'),
        ('Supervisor de módulo', 'Supervisor de módulo'),
        ('Personal de módulo', 'Personal de módulo'),
    )
    CATEGORIAS_CONTRATACION = (
        ('-', '-'),
        ('Estructura', 'Estructura'),
        ('Nomina 8', 'Nomina 8'),
        ('Honorarios', 'Honorarios'),
        ('Base con digito sindical', 'Base con digito sindical'),
        ('Base sin digito sindical', 'Base sin digito sindical'),
    )

    password1 = forms.CharField(label = 'Contraseña', widget=forms.PasswordInput(
        attrs = {'class':'register-field','placeholder':'Escribe la contraseña', 'required':'required'}
    ))

    password2 = forms.CharField(label = 'Confirmación de contraseña', widget=forms.PasswordInput(
        attrs = {'class':'register-field','placeholder':'Escribe nuevamente la contraseña', 'required':'required'}
    ))

    tipo_contratacion = forms.ChoiceField(choices=CATEGORIAS_CONTRATACION, label='Tipo de contratación', widget=forms.Select(attrs = {'class':'register-field'}))

    tipo_usuario = forms.ChoiceField(choices=CATEGORIAS_USUARIOS, label='Tipo de usuario', widget=forms.Select(attrs = {'class':'register-field'}))

    class Meta:
        model = Usuario
        fields = ('username', 'nombres', 'apellido_paterno', 'apellido_materno', 'tipo_contratacion', 'numero_empleado', 'tipo_usuario', 'email', 'numero_telefonico', 'foto')
        widgets = {
            'username': forms.TextInput(
                attrs = {'class':'register-field','autocomplete': 'off', 'placeholder':'Nombre de usuario'}
            ),
            'nombres': forms.TextInput(
                attrs = {'class':'register-field','autocomplete': 'off', 'placeholder':'Nombre(s)'}
            ),
            'apellido_paterno': forms.TextInput(
                attrs = {'class':'register-field','autocomplete': 'off', 'placeholder':'Apellido Paterno'}
            ),
            'apellido_materno': forms.TextInput(
                attrs = {'class':'register-field','autocomplete': 'off', 'placeholder':'Apellido Materno'}
            ),
            'tipo_contratacion': forms.TextInput(
                attrs = {'class':'register-field','autocomplete': 'off', 'placeholder':'Tipo de Contratación'}
            ),
            'numero_empleado': forms.NumberInput(
                attrs = {'class':'register-field','autocomplete': 'off', 'placeholder':'Número de Empleado'}
            ),
            'email': forms.EmailInput(
                attrs = {'class':'register-field','autocomplete': 'off', 'placeholder':'Correo Electrónico'}
            ),
            'numero_telefonico': forms.NumberInput(
                attrs = {'class':'register-field','autocomplete': 'off', 'placeholder':'Número Telefónico'}
            ),
            'foto': forms.FileInput()
            
        }
    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return password2
    
    def save(self, commit=True):
        usuario = super(FormaRegistro, self).save(commit=False)
        usuario.set_password(self.cleaned_data["password1"])
        if commit:
            usuario.save()
        return usuario
