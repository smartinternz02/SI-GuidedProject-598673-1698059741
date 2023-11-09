function formValidation() {
  let age = document.getElementById("age").value;
  let annualSal = document.getElementById("annualSal").value;
  let gender = document.getElementById("gender").value;
  var ageError = document.getElementById("ageError");
  var annualSalError = document.getElementById("annualSalError");
  var genderError = document.getElementById("genderError");
  let ageChk;
  let annualSalChk;
  let genderChk;
  if (age < 18 || age > 110) {
    ageError.style.display = "block";
    ageChk = false;
  } else {
    ageError.style.display = "none";
    ageChk = true;
  }
  if (annualSal < 1) {
    annualSalError.style.display = "block";
    annualSalChk = false;
  } else {
    annualSalError.style.display = "none";
    annualSalChk = true;
  }
  if (gender == "Select...") {
    genderError.style.display = "block";
    genderChk = false;
  } else {
    genderError.style.display = "none";
    genderChk = true;
  }
  if (ageChk && annualSalChk && genderChk) {
    document.getElementById("customerForm").submit();
  }
}
