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

function check_checkbox(id_checkbox, hide_elements, hide_class) {
    var checked = document.getElementById(id_checkbox).checked
    if (checked) {
        hide_elements.forEach(element => {
            document.getElementsByClassName(hide_class)[element].style.display = 'revert';
        });
    } else {
        hide_elements.forEach(element => {
            document.getElementsByClassName(hide_class)[element].style.display = 'none';
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
    check_checkbox('id_check_fechanacimiento', [0], 'hide')
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
    check_checkbox('id_check_acompanante_edad', [5], 'hide')
}

//Ocultar cuidador
document.getElementById('id_check_cuidador').onclick = function(){
    check_checkbox('id_check_cuidador', [6], 'hide')
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

function sumoftables(class_trigger, map, total_id, length){
    var values = []
    var sum = 0
    for (let index = 0; index < length; index++) {
        values.push(document.getElementsByClassName(class_trigger)[index].value)
    }
    values.forEach(element => {
         sum += map.get(element)
    });
    document.getElementById(total_id).innerHTML = sum;
}

function sumoftables2(class_trigger, map_pos, map_neg, elem_pos, elem_neg, total_id){
    var values_pos = []
    var values_neg = []
    var sum = 0
    elem_pos.forEach(element => {
        values_pos.push(document.getElementsByClassName(class_trigger)[element].value)
    });
    elem_neg.forEach(element => {
        values_neg.push(document.getElementsByClassName(class_trigger)[element].value)
    });
    values_pos.forEach(element => {
        sum += map_pos.get(element)
    });
    values_neg.forEach(element => {
        sum += map_neg.get(element)
    });
    document.getElementById(total_id).innerHTML = sum;
}

//Ocultar edad cuidador 
document.getElementById('id_check_cuidador_edad').onclick = function(){
    check_checkbox('id_check_cuidador_edad', [10], 'hide')
}

//id_check_direccion
document.getElementById('id_check_direccion').onclick = function(){
    check_checkbox('id_check_direccion', [0, 1, 2, 3, 4, 5, 6], 'hide2')
}

document.getElementById('table1').onclick = function(){
    var map = new Map();
    map.set('-', 0)
    map.set('I', 1)
    map.set('IA', 1)
    map.set('D', 0)
    map.set('Ninguna', 0)
    map.set('Se rehúsa', 0)

    sumoftables('t1', map, 'tot1', 6)
}

document.getElementById('table2').onclick = function(){
    var map = new Map();
    map.set('-', 0)
    map.set('1', 1)
    map.set('0', 0)
    map.set('Ninguna', 0)
    map.set('Se rehúsa', 0)

    sumoftables('t2', map, 'tot2', 8)
}

document.getElementById('table3').onclick = function(){
    var map_pos = new Map();
    map_pos.set('-', 0)
    map_pos.set('Sí', 1)
    map_pos.set('No', 0)
    map_pos.set('Ninguna', 0)
    map_pos.set('Se rehúsa', 0)

    var map_neg = new Map();
    map_neg.set('-', 0)
    map_neg.set('Sí', 0)
    map_neg.set('No', 1)
    map_neg.set('Ninguna', 0)
    map_neg.set('Se rehúsa', 0)

    elem_pos = [2, 4]
    elem_neg = [0, 1, 3]

    sumoftables2('t3', map_pos, map_neg, elem_pos, elem_neg, 'tot3')
}

document.getElementById('table4').onclick = function(){
    var map_pos = new Map();
    map_pos.set('-', 0)
    map_pos.set('Sí', 1)
    map_pos.set('No', 0)
    map_pos.set('Ninguna', 0)
    map_pos.set('Se rehúsa', 0)

    var map_neg = new Map();
    map_neg.set('-', 0)
    map_neg.set('Sí', 0)
    map_neg.set('No', 1)
    map_neg.set('Ninguna', 0)
    map_neg.set('Se rehúsa', 0)

    elem_pos = [0, 3]
    elem_neg = [1, 2, 4]

    sumoftables2('t4', map_pos, map_neg, elem_pos, elem_neg, 'tot4')
}