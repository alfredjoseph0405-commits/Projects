const name=document.getElementById("name");
const admn=document.getElementById("admn");
const mgndr=document.getElementById("mgndr");
const fgndr=document.getElementById("fgndr");
const eml=document.getElementById("eml");
const nameError=document.getElementById("nmeError");
const admnError=document.getElementById("admnError");
const gndrError=document.getElementById("gndrError");
const emlError=document.getElementById("emlError");
let valid=true;

function validte(){ 
    valid=true;   
    if(name.value.length<3){
        nameError.textContent="*Name must be at least 3 characters long";
        name.style.backgroundColor="rgb(255, 209, 209)";
        valid=false;
    } 
    else {
        nameError.textContent="";
    }
    if(!mgndr.checked && !fgndr.checked){
        gndrError.textContent="*Please select your gender";
        valid=false;
    }
    else if(mgndr.checked && fgndr.checked){
        gndrError.textContent="*Select only one option";
        valid=false;
    }
    else {
        gndrError.textContent="";
    }
    if (eml.value.includes("@")===false || eml.value.includes(".")===false){
        emlError.textContent="*Please enter a valid email address";
        eml.style.backgroundColor="rgb(255, 209, 209)";
        valid=false;
    }
    else {
        emlError.textContent="";
    }
    if (admn.value.length==0){
        admnError.textContent="*ADMN number cannot be empty";
        admn.style.backgroundColor="rgb(255, 209, 209)";
        valid=false;
    }
    if (valid){
        confirm("Form submitted successfully!");
    }
    return valid;
}
