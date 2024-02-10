document.querySelector(".login-btn").addEventListener("click", function (e) {
  e.preventDefault();
  const em = document.querySelector(".email").value;
  console.log(em);
  const pw = document.querySelector(".password").value;
  console.log(pw);
  if (em != "asingh49_be23@thapar.edu" || pw != "aviavi123") {
    alert("Wrong Credentials");
  } else window.location.href = "/category.html";
});
