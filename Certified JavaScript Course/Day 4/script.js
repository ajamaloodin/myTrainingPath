
let display = document.getElementById("result")

function plus(){
    let num1 = +document.getElementById("num1").value;
    let num2 = +document.getElementById("num2").value;
    showresult(num1 + num2);
}

function minus(){
    let num1 = +document.getElementById("num1").value;
    let num2 = +document.getElementById("num2").value;
    showresult(num1 - num2);
}

function mult(){
    let num1 = +document.getElementById("num1").value;
    let num2 = +document.getElementById("num2").value;
    showresult(num1 * num2);
}

function div(){
    let num1 = +document.getElementById("num1").value;
    let num2 = +document.getElementById("num2").value;
    if (num2 !== 0) {
        let total = num1 / num2;
        showresult(total);
    }
    else alert("Division by cero!");
    
}

function power(){
    let num1 = +document.getElementById("num1").value;
    let num2 = +document.getElementById("num2").value;
    showresult(Math.pow(num1,num2));
}

function raiz(){
    let num1 = +document.getElementById("num1").value;
    let num2 = +document.getElementById("num2").value;
    showresult(Math.sqrt(num1));
}

function inver(){
    let num1 = +document.getElementById("num1").value;
    if (num1 !== 0) {
        let total = 1 / num1;
        showresult(total);
    }
    else alert("Division by cero!");
    
}

function rand(){
    let num1 = +document.getElementById("num1").value;
    let num2 = +document.getElementById("num2").value;
    showresult(Math.floor(Math.random()* (num2-num1) + num1));
}


function showresult(toshow){
    display.value = toshow;
}