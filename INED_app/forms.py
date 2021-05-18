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
    CATEGORIAS_SEXO = (
        ('', ''),
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
    )
    CATEGORIAS_ESTADO_CIVIL = (
        ('-', '-'),
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
        ('Viudo', 'Viudo'),
        ('Separado', 'Separado'),
        ('Divorciado', 'Divorciado'),
        ('Unión Libre', 'Unión Libre'),
        ('Ninguno', 'Ninguno'),
        ('Se rehúsa', 'Se rehúsa'),
    )
    CATEGORIAS_OCUPACION = (
        ('-', '-'),
        ('Inactivo(a)', 'Inactivo(a)'),
        ('Jubilado(a) sin pensión', 'Jubilado(a) sin pensión'),
        ('Jubilado(a) con pensión', 'Jubilado(a) con pensión'),
        ('Comercio informal', 'Comercio informal'),
        ('Jornalero/campesino', 'Jornalero/campesino'),
        ('Obrero(a)', 'Obrero(a)'),
        ('Empleado(a) de oficina', 'Empleado(a) de oficina'),
        ('Profesionista independiente', 'Profesionista independiente'),
        ('Patrón(a)/jefe/empresario(a)', 'Patrón(a)/jefe/empresario(a)'),
        ('Ama de casa', 'Ama de casa'),
        ('Desempleado(a)', 'Desempleado(a)'),
        ('Ninguno', 'Ninguno'),
        ('Se rehúsa', 'Se rehúsa'),
    )
    CATEGORIAS_SS = (
        ('-', '-'),
        ('IMSS', 'IMSS'),
        ('ISSSTE', 'ISSSTE'),
        ('SEDENA', 'SEDENA'),
        ('SEMAR', 'SEMAR'),
        ('PEMEX', 'PEMEX'),
        ('SSP-DF', 'SSP-DF'),
        ('INSABI', 'INSABI'),
        ('PRIVADO', 'PRIVADO'),
        ('GASTOS MÉDICOS MAYORES', 'GASTOS MÉDICOS MAYORES'),
        ('OTRO', 'OTRO'),
    )
    CATEGORIAS_ACOMPANANTE = (
        ('-', '-'),
        ('Pareja', 'Pareja'),
        ('Hijos', 'Hijos'),
        ('Otro Familiar', 'Otro Familiar'),
        ('No Familiar', 'No Familiar'),
        ('Solo', 'Solo'),
        ('No se puede documentar', 'No se puede documentar'),
        ('Se rehúsa', 'Se rehúsa'),
    )
    CATEGORIAS_CUIDADOR = (
        ('', ''),
        ('Pareja', 'Pareja'),
        ('Hijos', 'Hijos'),
        ('Otro Familiar', 'Otro Familiar'),
        ('No Familiar', 'No Familiar'),
        ('Formal(encargado del AM, Ej. Enfermera)', 'Formal(encargado del AM, Ej. Enfermera)'),
        ('Ninguno', 'Ninguno'),
        ('No sabe', 'No sabe'),
        ('No contesta', 'No contesta'),
    )
    CATEGORIAS_ACTIVIDADES_DIARIAS = (
        ('-', '-'),
        ('I', 'I'),
        ('IA', 'IA'),
        ('D', 'D'),
        ('Ninguna', 'Ninguna'),
        ('Se rehúsa', 'Se rehúsa'),
    )
    CATEGORIAS_LAWTON = (
        ('-', '-'),
        ('1', '1'),
        ('0', '0'),
        ('Ninguna', 'Ninguna'),
        ('Se rehúsa', 'Se rehúsa'),
    )
    CATEGORIAS_COGNICION = (
        ('-', '-'),
        ('Sí', 'Sí'),
        ('No', 'No'),
        ('Ninguna', 'Ninguna'),
        ('Se rehúsa', 'Se rehúsa'),
    )
    CATEGORIAS_AUTOPERCEPCION_SALUD = (
        ('-', '-'),
        ('Excelente', 'Excelente'),
        ('Muy buena', 'Muy buena'),
        ('Buena', 'Buena'),
        ('Mala', 'Mala'),
        ('Muy mala', 'Muy mala'),
        ('Ninguna', 'Ninguna'),
        ('Se rehúsa', 'Se rehúsa'),
    )
    CATEGORIAS_AUTOPERCEPCION_ACTIVIDADES = (
        ('-', '-'),
        ('Nada', 'Nada'),
        ('Poco', 'Poco'),
        ('Mucho', 'Mucho'),
        ('Mala', 'Mala'),
        ('Ninguna', 'Ninguna'),
        ('Se rehúsa', 'Se rehúsa'),
    )

    nombres = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Nombre(s)', 'class':'input-adult-1 large-input'}))
    apellido_paterno = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Apellido Paterno', 'class':'input-adult-1 large-input'}))
    apellido_materno = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Apellido Materno', 'class':'input-adult-1 large-input'}))
    check_fechanacimiento = forms.BooleanField(label="¿Cuenta con fecha de nacimiento?", required=False)
    fechanacimiento = forms.DateField(label="Fecha de nacimiento", required=False, widget=forms.DateInput(attrs={'type': 'date', 'class':'input-adult-1'}))
    lugarnacimiento = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Lugar de nacimiento', 'class':'input-adult-1 large-input'}))
    edad = forms.IntegerField(label="", required=False, widget=forms.NumberInput(attrs={'placeholder':'Edad', 'class':'input-adult-1 small-input'}))
    sexo = forms.ChoiceField(label="Sexo", choices=CATEGORIAS_SEXO, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    rfc = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'RFC', 'class':'input-adult-1 large-input'}))
    curp = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'CURP', 'class':'input-adult-1 large-input'}))
    telefono = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'Teléfono', 'class':'input-adult-1'}))
    
    estado_civil = forms.ChoiceField(label="Estado civil", choices=CATEGORIAS_ESTADO_CIVIL, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    ocupacion = forms.ChoiceField(label="¿A qué se dedica actualmente?", choices=CATEGORIAS_OCUPACION, widget=forms.Select(attrs={'class':'input-adult-1 large-input'}))
    ocupacion_anterior = forms.ChoiceField(label="¿Y anteriormente?", choices=CATEGORIAS_OCUPACION, widget=forms.Select(attrs={'class':'input-adult-1 large-input'}))
    seguridad_social = forms.ChoiceField(label="Seguridad social", choices=CATEGORIAS_SS, widget=forms.Select(attrs={'class':'input-adult-1 large-input'}))
    seguridad_social_otro = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'¿Cuál?', 'class':'input-adult-1'}))
    utiliza_seguridad_social = forms.BooleanField(label="¿Los utiliza?", required=False)
    
    acompanante = forms.ChoiceField(label="¿Con quién vive?", choices=CATEGORIAS_ACOMPANANTE, widget=forms.Select(attrs={'class':'input-adult-1 large-input'}))
    acompanante_otro = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'¿Quién?', 'class':'input-adult-1 large-input'}))
    acompanante_sexo = forms.ChoiceField(label="Sexo de acompañante", required=False, choices=CATEGORIAS_SEXO, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    check_acompanante_edad = forms.BooleanField(label="¿Se conoce la edad del acompañante?", required=False)
    acompanante_edad = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'input-adult-1', 'placeholder':'Edad acompañante'}))
    
    check_cuidador = forms.BooleanField(label="¿Tiene cuidador?", required=False)
    cuidador = forms.ChoiceField(label="Relación", required=False, choices=CATEGORIAS_CUIDADOR, widget=forms.Select(attrs={'class':'input-adult-1'}))
    cuidador_otro = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder':'¿Quién?', 'class':'input-adult-1 large-input'}))
    cuidador_sexo = forms.ChoiceField(label="Sexo del cuidador", required=False, choices=CATEGORIAS_SEXO, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    check_cuidador_edad = forms.BooleanField(label="¿Se conoce la edad del cuidador?", required=False)
    cuidador_edad = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder':'Edad cuidador', 'class':'input-adult-1'}))
    
    nombres_profesional = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Nombre(s) Profesional en servicios', 'class':'input-adult-1 large-input'}))
    apellido_paterno_profesional = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Ap. Paterno Profesional en servicios', 'class':'input-adult-1 large-input'}))
    apellido_materno_profesional = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'Ap. Materno Profesional en servicios', 'class':'input-adult-1 large-input'}))
    fechaevaluacion = forms.DateField(label="Fecha de la evaluación", widget=forms.TextInput(attrs={'type':'date', 'class':'input-adult-1'}))

    bañarse = forms.ChoiceField(choices=CATEGORIAS_ACTIVIDADES_DIARIAS, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    vestirse = forms.ChoiceField(choices=CATEGORIAS_ACTIVIDADES_DIARIAS, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    sanitario = forms.ChoiceField(choices=CATEGORIAS_ACTIVIDADES_DIARIAS, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    trasladarse = forms.ChoiceField(choices=CATEGORIAS_ACTIVIDADES_DIARIAS, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    continencia = forms.ChoiceField(choices=CATEGORIAS_ACTIVIDADES_DIARIAS, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    alimentarse = forms.ChoiceField(choices=CATEGORIAS_ACTIVIDADES_DIARIAS, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))

    lawton_telefono = forms.ChoiceField(choices=CATEGORIAS_LAWTON, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    lawton_transporte = forms.ChoiceField(choices=CATEGORIAS_LAWTON, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    lawton_medicacion = forms.ChoiceField(choices=CATEGORIAS_LAWTON, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    lawton_finanzas = forms.ChoiceField(choices=CATEGORIAS_LAWTON, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    lawton_compras = forms.ChoiceField(choices=CATEGORIAS_LAWTON, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    lawton_cocina = forms.ChoiceField(choices=CATEGORIAS_LAWTON, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    lawton_hogar = forms.ChoiceField(choices=CATEGORIAS_LAWTON, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    lawton_lavanderia = forms.ChoiceField(choices=CATEGORIAS_LAWTON, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))

    cognicion_memoria = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    cognicion_actividades = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    cognicion_tiempo = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))

    depresion_vacio = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    depresion_aburrido = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    depresion_tiempo = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    depresion_protegido = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    depresion_energia = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))

    fragilidad_cansado = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    fragilidad_escaleras = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    fragilidad_cuadras = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    fragilidad_peso = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    fragilidad_cargar = forms.ChoiceField(choices=CATEGORIAS_COGNICION, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))

    autopercepcion_salud = forms.ChoiceField(label="1. ¿En relación a otras personas de su edad como diría que se encuentra su salud?", choices=CATEGORIAS_AUTOPERCEPCION_SALUD, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))
    autopercepcion_actividades = forms.ChoiceField(label="2. ¿Hasta qué punto sus problemas de salud le impiden desempeñar sus actividades habituales?",choices=CATEGORIAS_AUTOPERCEPCION_ACTIVIDADES, widget=forms.Select(attrs={'class':'input-adult-1 small-input'}))

    class Meta:
        model = AdultoMayor
        fields = '__all__'
        required = (
       'nombres',
        )
        


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
