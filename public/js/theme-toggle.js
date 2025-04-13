const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

themeToggle.addEventListener('change', () => {
  if (themeToggle.checked) {
    body.classList.add('dark-theme');
    localStorage.setItem('theme', 'dark');
  } else {
    body.classList.remove('dark-theme');
    localStorage.setItem('theme', 'light');
  }
});

// Check local storage for theme preference on page load
if (localStorage.getItem('theme') === 'dark') {
  themeToggle.checked = true;
  body.classList.add('dark-theme');
}