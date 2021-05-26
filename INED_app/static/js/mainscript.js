// document.getElementById("demo").onclick = function() {myFunction()};

// function myFunction() {
//   document.getElementById("demo").innerHTML = "YOU CLICKED ME!";
// }

// parent.addEventListener('click', function() {
//     parent.style.background = 'skyblue';
//     console.log('Click');
// });

navigator.geolocation.getCurrentPosition(function(position){
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    document.getElementById('id_latitud').value = latitude.toFixed(7);
    document.getElementById('id_longitud').value = longitude.toFixed(7);
});

function check_checkbox(id_checkbox, hide_elements) {
    var checked = document.getElementById(id_checkbox).checked
    if (checked) {
        hide_elements.forEach(element => {
            document.getElementsByClassName('hide')[element].style.display = 'revert';
        });
    } else {
        hide_elements.forEach(element => {
            document.getElementsByClassName('hide')[element].style.display = 'none';
        });
    }
}

function get_select_input(id_select){
    var list = document.getElementById(id_select);
    var index = list.selectedIndex;
    var selected = list.options[index];
    var finaltext = selected.text;
    return finaltext;
}

function check_select(id_select, values, hide_elements) {
    var input = get_select_input(id_select);
    if (values.includes(input)) {
        hide_elements.forEach(element => {
            document.getElementsByClassName('hide')[element].style.display = 'revert';
        });
    } else {
        hide_elements.forEach(element => {
            document.getElementsByClassName('hide')[element].style.display = 'none';
        });
    }
}

function check_multiple_select(id_select, map) {
    var input = get_select_input(id_select);
    var values = map.get(input);
    if (values[0]!=null) {
        values[0].forEach(element => {
            document.getElementsByClassName('hide')[element].style.display = 'revert';
        }); 
    }
    if (values[1]!=null) {
        values[1].forEach(element => {
            document.getElementsByClassName('hide')[element].style.display = 'none';
        });
    }
}

//Ocultar fecha de nacimiento
document.getElementById('id_check_fechanacimiento').onclick = function(){
    check_checkbox('id_check_fechanacimiento', [0])
}

//Calcular edad
function calcularEdad(fecha) {
    var hoy = new Date();
    var cumpleanos = new Date(fecha);
    var edad = hoy.getFullYear() - cumpleanos.getFullYear();
    var m = hoy.getMonth() - cumpleanos.getMonth();

    if (m < 0 || (m === 0 && hoy.getDate() < cumpleanos.getDate())) {
        edad--;
    }

    return edad;
}

document.getElementById('id_edad').onclick = function(){
    var value = document.getElementById('id_fechanacimiento').value
    if (value != '' || value != null) {
        document.getElementById('id_edad').value = calcularEdad(value);
        console.log(calcularEdad(value))
    }
}

//Ocultar campo 'otros' en seguridad social
document.getElementById('id_seguridad_social').onclick = function(){
    check_select('id_seguridad_social', ['OTRO'], [1])
}

//Ocultar campos de acompañante
document.getElementById('id_acompanante').onclick = function(){
    var map = new Map();
    map.set('-', [[],[2,3,4,5]])
    map.set('Solo', [[],[2,3,4,5]])
    map.set('No se puede documentar', [[],[2,3,4,5]])
    map.set('Se rehúsa', [[],[2,3,4,5]])
    map.set('Pareja', [[3,4],[2]])
    map.set('Hijos', [[3,4],[2]])
    map.set('Otro Familiar', [[2,3,4],[]])
    map.set('No Familiar', [[2,3,4],[]])
    check_multiple_select('id_acompanante', map);
}

//Ocultar edad acompañante 
document.getElementById('id_check_acompanante_edad').onclick = function(){
    check_checkbox('id_check_acompanante_edad', [5])
}

//Ocultar cuidador
document.getElementById('id_check_cuidador').onclick = function(){
    check_checkbox('id_check_cuidador', [6])
}

//Ocultar detalles relacion cuidador
document.getElementById('id_cuidador').onclick = function(){
    var map = new Map();
    map.set('', [[],[7, 8, 9]])
    map.set('Ninguno', [[],[7, 8, 9]])
    map.set('No sabe', [[],[7, 8, 9]])
    map.set('No contesta', [[],[7, 8, 9]])
    map.set('Pareja', [[8, 9],[7]])
    map.set('Hijos', [[8, 9],[7]])
    map.set('Formal (encargado del AM, Ej. Enfermera)', [[8, 9],[7]])
    map.set('Otro Familiar', [[7, 8, 9],[]])
    map.set('No Familiar', [[7, 8, 9],[]])
    check_multiple_select('id_cuidador', map);
}

//Ocultar edad cuidador 
document.getElementById('id_check_cuidador_edad').onclick = function(){
    check_checkbox('id_check_cuidador_edad', [10])
}