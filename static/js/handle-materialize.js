document.addEventListener("DOMContentLoaded", function() {
    const elems = document.querySelectorAll(".materialboxed");
    const options = {};
    const instances = M.Materialbox.init(elems, options);
});
document.addEventListener("DOMContentLoaded", function() {
    const elems = document.querySelectorAll(".sidenav");
    const options = {
        edge: "right",
    };
    const instances = M.Sidenav.init(elems, options);
});