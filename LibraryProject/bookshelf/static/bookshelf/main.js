// Form Handling
document.getElementById("loginForm").addEventListener("submit", function (e) {
  e.preventDefault();

  const email = document.getElementById("loginEmail").value;
  const password = document.getElementById("loginPassword").value;

  // Basic validation
  if (!email || !password) {
    alert("Please fill in all fields");
    return;
  }

  // For Django integration, you would send this data to your backend
  alert("Login form submitted! In Django, this would authenticate the user.");

  // Example of what you might do in Django:
  // fetch('/login/', {
  //     method: 'POST',
  //     headers: {'Content-Type': 'application/json'},
  //     body: JSON.stringify({email, password})
  // }).then(response => response.json())
  //   .then(data => console.log(data));
});

document
  .getElementById("registerForm")
  .addEventListener("submit", function (e) {
    e.preventDefault();

    const name = document.getElementById("registerName").value;
    const email = document.getElementById("registerEmail").value;
    const password = document.getElementById("registerPassword").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    // Basic validation
    if (!name || !email || !password || !confirmPassword) {
      alert("Please fill in all fields");
      return;
    }

    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    if (password.length < 6) {
      alert("Password must be at least 6 characters long");
      return;
    }

    // For Django integration, you would send this data to your backend
    alert(
      "Registration form submitted! In Django, this would create a new user."
    );

    // Example of what you might do in Django:
    // fetch('/register/', {
    //     method: 'POST',
    //     headers: {'Content-Type': 'application/json'},
    //     body: JSON.stringify({name, email, password})
    // }).then(response => response.json())
    //   .then(data => console.log(data));
  });

// Handle browser back/forward buttons
window.addEventListener("popstate", function (e) {
  const hash = window.location.hash.substring(1);
  if (hash && document.getElementById(hash)) {
    showPage(hash);
  } else {
    showPage("home");
  }
});

// Initialize page based on URL hash
document.addEventListener("DOMContentLoaded", function () {
  const hash = window.location.hash.substring(1);
  if (hash && document.getElementById(hash)) {
    showPage(hash);
  }
});
