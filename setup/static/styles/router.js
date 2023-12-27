const route = (event) => {
    event.preventDefault();
    const path = event.target.getAttribute("href");
    handleLocation(path);
};

const routes = {
    404: "<h1>404 page not found</h1>",
    "admin_dashboard": "{% url 'admin_dashboard2' %}",
}

const handleLocation = (path) => {
    const route = routes[path] || routes[404];
    const html = fetch(route).then((data) => data.text());
    document.getElementById("main-page").innerHTML = html;
};

window.onpopstate = handleLocation;
window.route = route;

handleLocation();