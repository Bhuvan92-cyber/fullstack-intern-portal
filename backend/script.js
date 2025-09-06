// script.js - minimal usage: fetch and log the user json on page load (only for demo)
document.addEventListener('DOMContentLoaded', () => {
    fetch('data/user.json')
        .then(response => {
            if (!response.ok) throw new Error("HTTP error " + response.status);
            return response.json();
        })
        .then(data => {
            console.log("User data fetched from backend:", data);
        })
        .catch(err => {
            console.error("Failed to fetch user data:", err);
        });
});

