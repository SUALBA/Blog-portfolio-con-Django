// static/blog/js/buho.js
const frasesBuho = [
  "“La seguridad no es un producto, es un proceso.” — Bruce Schneier",
  "“La ciberseguridad es responsabilidad de todos, no solo del departamento de TI.”",
  "“El mejor firewall es una persona bien entrenada.”",
  "“La confianza es la base de la seguridad, pero debe ser verificada.”",
  "“Proteger datos es proteger personas.”",
  "“La información es poder, pero la información segura es libertad.”"
];

function hablaBuho() {
  const frase = frasesBuho[Math.floor(Math.random() * frasesBuho.length)];
  const div = document.getElementById('frase-buho');
  div.innerText = '💬 ' + frase;
  div.hidden = false;
  setTimeout(() => div.hidden = true, 5000);
}