let nme=document.getElementById("nme");
let nmeErr=document.getElementById("nmeError");

let admn=document.getElementById("admn");
let admnErr=document.getElementById("admnError");

let dept=document.getElementById("dept");
let deptErr=document.getElementById("depError");

let sec=document.getElementById("sec");
let secErr=document.getElementById("secError");

let tme=document.getElementById("tme");
let tmeErr=document.getElementById("tmeError");



let backbut=document.getElementById("bchome");

function Vform(){
    let isValid=true;
    if (nme.value==""){
        nmeErr.textContent="*Name must be at least 3 characters long";
        nme.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    if (admn.value==""){
        admnErr.textContent="*This field is required";
        admn.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    if (dept.value==""){
        deptErr.textContent="*Choose an Option";
        dept.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    if (sec.value==""){
        secErr.textContent="*Choose an Option";
        sec.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    if (tme.value==""){
        tmeErr.textContent="*Choose an Option";
        tme.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    return isValid;
}
backbut.addEventListener("click",function(){
    window.open("page.html","_self");
});

