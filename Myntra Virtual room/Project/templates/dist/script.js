const $btn = document.querySelector(".button__text");
const text_mobile = "Añadir";
const text_desktop = "Añadir al carrito";

function changeText(node, mobile, desktop) {
  node.innerText = window.innerWidth < 430 ? mobile : desktop;
}

window.addEventListener("resize", () => {
  changeText($btn, text_mobile, text_desktop);
});

changeText($btn, text_mobile, text_desktop);