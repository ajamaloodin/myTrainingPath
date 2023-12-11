
function showGrades(){
    let display = document.getElementById("result");
    let result = 'Your grades are: '
    for (grade of grades){
        result = result + grade + ', ';
    }
    display.textContent = result;
}

function average(){
    let display = document.getElementById("result");
    let result = 'Your average is: '
    let total = 0;
    for (grade of grades){
        total = total + grade;
    }
    display.textContent = result + total/5;
}

function higher(){
    let display = document.getElementById("result");
    let result = 'Your higher grade is: '
    let maxi = 0;
    for (grade of grades){
        if (grade >= maxi) maxi = grade;
    }
    display.textContent = result + maxi;
}

function failgrade(){
    let display = document.getElementById("result");
    let result = 'There is a fail grade: '
    let mini = 20;
    for (grade of grades){
        if (grade <= mini) mini = grade;
    }
    display.textContent = result + mini;
}
var grades = [17, 20, 12, 3, 15];