
class Animal {
    constructor(nombre, peso, edad){
        this.nombre = nombre;
        this.peso = peso;
        this.edad = edad;
    }

    informacion () {
        alert (`Nombre: ${this.nombre}
                 Peso: ${this.peso}
                 Edad: ${this.edad}`);
    }
}

class Perro extends Animal {
    constructor(nombre, peso, edad, raza){ 
        super(nombre, peso, edad);
        this.raza = raza;
    }

    informacion () {
        alert (`Nombre: ${this.nombre}
                 Peso: ${this.peso}
                 Edad: ${this.edad}
                 Raza: ${this.raza}`);
    }
}

class Gato extends Animal {
    constructor(nombre, peso, edad, sexo) {
        super(nombre, peso, edad);
        this.sexo = sexo;
    }

    informacion () {
        alert (`Nombre: ${this.nombre}
                 Peso: ${this.peso}
                 Edad: ${this.edad}
                 Sexo: ${this.sexo}`);
    }
}

class Conejo extends Animal {
    constructor(nombre, peso, edad, color) {
        super(nombre, peso, edad);
        this.color = color;
    }

    informacion () {
        alert (`Nombre: ${this.nombre}
                 Peso: ${this.peso}
                 Edad: ${this.edad}
                 Color: ${this.color}`);
    }
}

let perro = new Perro('Toto', 20, 6, 'Pastor');

let gato = new Gato('Sophie', 10, 8, 'hembra');

let conejo = new Conejo('Batu', 8, 5, 'marron');