let name=document.getElementById("name");
let nmeErr=document.getElementById("nameError");
let rno=document.getElementById("rollno");
let rnoErr=document.getElementById("rollnoError");

let sub1thr=document.getElementById("sub1thr");
let sub1thrErr=document.getElementById("sub1thrError");
let sub1prc=document.getElementById("sub1prc");
let sub1prcErr=document.getElementById("sub1prcError");

let sub2thr=document.getElementById("sub2thr");
let sub2thrErr=document.getElementById("sub2thrError");
let sub2prc=document.getElementById("sub2prc");
let sub2prcErr=document.getElementById("sub2prcError");

let sub3thr=document.getElementById("sub3thr");
let sub3thrErr=document.getElementById("sub3thrError");
let sub3prc=document.getElementById("sub3prc");
let sub3prcErr=document.getElementById("sub3prcError");

let sub4thr=document.getElementById("sub4thr");
let sub4thrErr=document.getElementById("sub4thrError");
let sub4prc=document.getElementById("sub4prc");
let sub4prcErr=document.getElementById("sub4prcError");

let sub5thr=document.getElementById("sub5thr");
let sub5thrErr=document.getElementById("sub5thrError");
let sub5prc=document.getElementById("sub5prc");
let sub5prcErr=document.getElementById("sub5prcError");

let result=document.getElementById("resultText");
let cgpa=document.getElementById("cgpaText");
let avg=document.getElementById("averageText");
let grd=document.getElementById("gradeText");
let isValid=true;
function validateForm(){
    isValid=true;
    if (name.value.length<3){
        nmeErr.textContent="*Name must be at least 3 characters long";
        name.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    if(rno.value=="" || rno.value.length<7){
        rnoErr.textContent="*required minimum length of 7 characters";
        rno.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }


    if (sub1thr.value===""){
        sub1thrErr.textContent="*This field is required";
        sub1thr.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    else if(sub1thr.value>80){
        sub1thrErr.textContent="*Exceeded max awardable marks";
        sub1thr.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }


    if (sub2thr.value===""){
        sub2thrErr.textContent="*This field is required";
        sub2thr.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    else if(sub2thr.value>80){
        sub2thrErr.textContent="*Exceeded max awardable marks";
        sub2thr.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }


    if (sub3thr.value===""){
        sub3thrErr.textContent="*This field is required";
        sub3thr.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    else if(sub3thr.value>80){
        sub3thrErr.textContent="*Exceeded max awardable marks";
        sub3thr.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }


    if (sub4thr.value===""){
        sub4thrErr.textContent="*This field is required";
        sub4thr.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    else if(sub4thr.value>80){
        sub4thrErr.textContent="*Exceeded max awardable marks";
        sub4thr.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }


    if (sub5thr.value===""){
        sub5thrErr.textContent="*This field is required";
        sub5thr.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    else if(sub5thr.value>80){
        sub5thrErr.textContent="*Exceeded max awardable marks";
        sub5thr.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }


    if (sub1prc.value===""){
        sub1prcErr.textContent="*This field is required";
        sub1prc.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    else if(sub1prc.value>20){
        sub1prcErr.textContent="*Exceeded max awardable marks";
        sub1prc.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }


    if (sub2prc.value===""){
        sub2prcErr.textContent="*This field is required";
        sub2prc.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    else if(sub2prc.value>20){
        sub2prcErr.textContent="*Exceeded max awardable marks";
        sub2prc.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }


    if (sub3prc.value===""){
        sub3prcErr.textContent="*This field is required";
        sub3prc.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    else if(sub3prc.value>20){
        sub3prcErr.textContent="*Exceeded max awardable marks";
        sub3prc.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }


    if (sub4prc.value===""){
        sub4prcErr.textContent="*This field is required";
        sub4prc.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    else if(sub4prc.value>20){
        sub4prcErr.textContent="*Exceeded max awardable marks";
        sub4prc.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }


    if (sub5prc.value===""){
        sub5prcErr.textContent="*This field is required";
        sub5prc.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }
    else if(sub5prc.value>20){
        sub5prcErr.textContent="*Exceeded max awardable marks";
        sub5prc.style.backgroundColor="rgb(255, 209, 209)";
        isValid=false;
    }

    if(isValid){
        nmeErr.textContent="";
        sub1thr.style.backgroundColor="rgb(205, 247, 205)";
        sub1prc.style.backgroundColor="rgb(205, 247, 205)";
        sub2thr.style.backgroundColor="rgb(205, 247, 205)";
        sub2prc.style.backgroundColor="rgb(205, 247, 205)";
        sub3thr.style.backgroundColor="rgb(205, 247, 205)";
        sub3prc.style.backgroundColor="rgb(205, 247, 205)";
        sub4thr.style.backgroundColor="rgb(205, 247, 205)";
        sub4prc.style.backgroundColor="rgb(205, 247, 205)";
        sub5thr.style.backgroundColor="rgb(205, 247, 205)";
        sub5prc.style.backgroundColor="rgb(205, 247, 205)";
        name.style.backgroundColor="rgb(205, 247, 205)";
        rnoErr.textContent="";
        rno.style.backgroundColor="rgb(205, 247, 205)";
        nmeErr.textContent="";
        sub1thrErr.textContent="";
        sub1prcErr.textContent="";
        sub2thrErr.textContent="";
        sub2prcErr.textContent="";
        sub3thrErr.textContent="";
        sub3prcErr.textContent="";
        sub4thrErr.textContent="";
        sub4prcErr.textContent="";
        sub5thrErr.textContent="";
        sub5prcErr.textContent="";
        confirm("Form submitted successfully!");
        setres();
        return false;
    }
    else{
        alert("Please correct the errors in the form.");
    }
    return isValid;
}
function setres(){
    let sub1 = parseInt(sub1thr.value)+parseInt(sub1prc.value);
    let sub2 = parseInt(sub2thr.value)+parseInt(sub2prc.value);
    let sub3 = parseInt(sub3thr.value)+parseInt(sub3prc.value);
    let sub4 = parseInt(sub4thr.value)+parseInt(sub4prc.value);
    let sub5 = parseInt(sub5thr.value)+parseInt(sub5prc.value);
    if(sub1>50 && sub2>50 && sub3>50 && sub4>50 && sub5>50){
        result.style.color="green";
        result.textContent="PASS";
    }
    else{
        result.style.color="red";
        result.textContent="FAIL";
    }
    cgpa.style.color="blue";
    avg.style.color="blue";
    let totalMarks = sub1 + sub2 + sub3 + sub4 + sub5;
    let averageMarks = totalMarks / 5;
    if (averageMarks>90){
        grd.textContent="A";
    }
    else if (averageMarks>80){
        grd.textContent="B";
    }
    else if (averageMarks>70){
        grd.textContent="C";
    }
    else if (averageMarks>60){
        grd.textContent="D";
    }
    else if (averageMarks>50){
        grd.textContent="E";
    }
    else{
        grd.textContent="F";
    }
    let calculatedCgpa = (averageMarks / 10).toFixed(2);
    cgpa.textContent = calculatedCgpa;
    avg.textContent = averageMarks.toFixed(2);
}