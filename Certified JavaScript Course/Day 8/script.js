function Empleado(estado, nombre, apellido, fecha, cargo){
    this.estado = estado;
    this.nombre = nombre;
    this.apellido = apellido;
    this.fecha = fecha;
    this.cargo = cargo;
}

function addEmpl(){
    const elementEstado = document.getElementById("legajo");
    const estado = elementEstado.value;

    const elementoNombre = document.getElementById("nombre");
    const nombre = elementoNombre.value;

    const elementoApellido = document.getElementById("apellido");
    const apellido = elementoApellido.value;

    const elementoNacimiento = document.getElementById("nacimiento");
    const fecha = elementoNacimiento.value;

    const elementoCargo = document.getElementById("cargo");
    const cargo = elementoCargo.value;

    const empleado = new Empleado(estado, nombre, apellido, fecha, cargo);
    empleados.push(empleado);
    console.log(empleados);

}

function listar(){
    let display = ''
    for (pers of empleados){
        for (emp in pers){
            display = display + `${emp}: ${pers[emp]}, `;
        }
        display = display + '\n'
    }
    
    alert(display);
}

const empleados = [];
