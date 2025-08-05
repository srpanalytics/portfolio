// Dark/Light mode toggle
document.getElementById('themeToggle').addEventListener('click', function () {
    document.body.classList.toggle('dark-theme');
    localStorage.setItem('theme', document.body.classList.contains('dark-theme') ? "dark" : "");
});

// Persist theme choice
if (localStorage.getItem('theme') === "dark") {
    document.body.classList.add('dark-theme');
}
