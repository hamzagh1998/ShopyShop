const box = document.getElementById('box');
const total = document.querySelectorAll('.total');

const h1 = document.createElement('h1');
h1.innerText = `Total: $${[...total].reduce((acc, curr) => acc + +curr.innerText.slice(1), 0)}`;

box.insertAdjacentElement('beforeend', h1);
