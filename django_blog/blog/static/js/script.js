// Minimal JS - only for essential interactions
function toggleLike(button) {
  const count = button.querySelector(".count");
  const currentCount = parseInt(count.textContent);

  if (button.classList.contains("liked")) {
    button.classList.remove("liked");
    count.textContent = currentCount - 1;
  } else {
    button.classList.add("liked");
    count.textContent = currentCount + 1;
  }
}

function toggleBookmark(button) {
  if (button.classList.contains("bookmarked")) {
    button.classList.remove("bookmarked");
    button.innerHTML = "<span>🔖</span> Save";
  } else {
    button.classList.add("bookmarked");
    button.innerHTML = "<span>🔖</span> Saved";
  }
}

        // Minimal JS - only for the edit form toggle
        function toggleEditForm() {
            const formContainer = document.getElementById('editFormContainer');
            if (formContainer.classList.contains('active')) {
                formContainer.classList.remove('active');
            } else {
                formContainer.classList.add('active');
                // Scroll to the form
                formContainer.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }