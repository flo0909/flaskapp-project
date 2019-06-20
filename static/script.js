//Javascript for adding functionality to Sort Page buttons , showing or hiding a div.

var one=document.getElementById('main_course').addEventListener('click', clic1);
var hide1 = document.getElementById('hideOne');
function clic1(){
  hide1.classList.toggle('show');
}

var two=document.getElementById('deserts').addEventListener('click', clic2);
var hide2 = document.getElementById('hideTwo');
function clic2(){
  hide2.classList.toggle('show');
}

var three=document.getElementById('salads').addEventListener('click', clic3);
var hide3 = document.getElementById('hideThree');
function clic3(){
  hide3.classList.toggle('show');
}
var four=document.getElementById('Allergens').addEventListener('click', clic4);
var hide4 = document.getElementById('hideFour');
function clic4(){
  hide4.classList.toggle('show');
}
var five=document.getElementById('vegetarians').addEventListener('click', clic5);
var hide5 = document.getElementById('hideFive');
function clic5(){
  hide5.classList.toggle('show');
}
var eight=document.getElementById('many_portions').addEventListener('click', clic8);
var hide8 = document.getElementById('hideSix');
function clic8(){
  hide8.classList.toggle('show');
}
var nine=document.getElementById('one_portion').addEventListener('click', clic9);
var hide9 = document.getElementById('hideSeven');
function clic9(){
  hide9.classList.toggle('show');
}
var ten=document.getElementById('cookingtime').addEventListener('click', clic10);
var hide10 = document.getElementById('hideEight');
function clic10(){
  hide10.classList.toggle('show');
}