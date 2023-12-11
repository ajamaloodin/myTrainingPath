
function recomienda(categ){
    let edad = document.getElementById("edad").value;
    let display = document.getElementById("recomend");
    if (edad < 13) {
        switch (categ) {
            case 1:
                display.textContent = "Mi Pobre Angelito"
            break;
            case 2:
                display.textContent = "El Rey León"
            break;
            case 3:
                display.textContent = "La Novicia Rebelde"
            break;
            case 4:
                display.textContent = "Cars"
            break;
        }
    }
    if (edad >= 13 && edad < 16){
        switch (categ) {
            case 1:
                display.textContent = "Patch Adams"
            break;
            case 2:
                display.textContent = "Marco"
            break;
            case 3:
                display.textContent = "La Novicia Rebelde"
            break;
            case 4:
                display.textContent = "Rapidos y Furiosos"
            break;
        }
    }
    if (edad >= 16){
        switch (categ) {
            case 1:
                display.textContent = "Patch Adams"
            break;
            case 2:
                display.textContent = "El Padrino"
            break;
            case 3:
                display.textContent = "Lala land"
            break;
            case 4:
                display.textContent = "Enemigo al Acecho"
            break;
        }
    }

}
