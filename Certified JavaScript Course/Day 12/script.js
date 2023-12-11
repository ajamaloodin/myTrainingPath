
let tipo = document.getElementById("selector");
let botonBuscar = document.getElementById("botonBuscar");
let titulo = document.getElementById("titulo");
let resultados = document.getElementById("resultados");
let nombre = titulo.value;

let fileJson = 'peliculas.json';

tipo.addEventListener('change', () =>{
    
    let eleccion = tipo.value;
    
    if (eleccion === "1"){
        fileJson = 'peliculas.json';
        botonBuscar.value = "Buscar Película";
    }
    else {
        fileJson = 'series.json';
        botonBuscar.value = "Buscar Serie";
    }

})

titulo.addEventListener('keydown', (event) => {
    if (event.key < 'a' || event.key > 'z') {
        if (event.key < 'A' || event.key > 'Z') {
            if (event.code != 'Space')
                event.preventDefault();
        }
    }

})

botonBuscar.addEventListener('click', () => {
    nombre = titulo.value;
    if (nombre === undefined) {
        alert('Por favor, escriba el título a buscar');
    }
    else {
        nombre = nombre.toUpperCase();
        
        let datosJSON;

        fetch(fileJson)
        .then(res => res.json())
        .then((salida) => {
            datosJSON = salida; 

            for (item of datosJSON.data){
                if (item.nombre.startsWith(nombre)){
                    let salto = document.createElement('br');

                    let name = document.createElement('li');
                    name.innerText = item.nombre;

                    let sinopsis = document.createElement('p');
                    sinopsis.innerText = item.sinopsis;
                    sinopsis.id = item.nombre;
                    sinopsis.style.display = 'none';
                    name.appendChild(sinopsis);

                    resultados.appendChild(name);
                    resultados.appendChild(salto);

                    name.addEventListener('mouseover', (event) => {
                        p = document.getElementById(name);
                        sinopsis.style.display = 'block';
                    })

                    name.addEventListener('mouseout', (event) => {
                        p = document.getElementById(name);
                        sinopsis.style.display = 'none';
                    })
                }
            }

        })
    }
    

});