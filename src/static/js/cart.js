const tableBody = document.getElementById('table-body');
const checkout = document.getElementById('checkout');

//fill the table with the products
(() => {
  let id = 0;

  for (const product of productObj['products']) {
    const total = (product.quantity * +product.productPrice).toFixed(2);
    tableBody.innerHTML += `
      <tr data-id="${id}" id="${product.productId}">
        <td><div id="img-card"><img src="${product.productImageURL}" alt="${product.productName}"></div></td>
        <td>${product.productName}</td>
        <td>${product.productQuantity}</td>
        <td><i id="up" class="ion-arrow-up-b"></i><span>${product.quantity}</span><i id="down" class="ion-arrow-down-b"></i></td>
        <td>$${product.productPrice}</td>
        <td class="total">$${total}</td>
        <td><i id="trash" class="ion-trash-b"></i></td>
      </tr>
    `;
    id++;
  };
})();

function getTotal() {
  const total = document.querySelector('.show-total-amount');
  const totalList = tableBody.querySelectorAll('.total');
  const list = [];
  totalList.forEach(cell => list.push(+cell.innerText.slice(1)));

  total.innerText = `$${(list.reduce((accumulator, currentValue) => accumulator + currentValue, 0)).toFixed(2)}`;
};
getTotal();

function onClick(event) {
  if (event.target.id === 'up') {
    const item = event.target.parentElement.parentElement;
    const product = productObj['products'][item.dataset.id];
    const quantity = event.target.nextElementSibling;
    const stock = +event.target.parentElement.previousElementSibling.innerText;

    if (+quantity.innerText < stock) {
      product['quantity']++;
      let count = +quantity.innerText++
      const q = count+1;
      item.querySelector('.total').innerText = `$${(q * +product['productPrice']).toFixed(2)}`;
    };
  } else if (event.target.id === 'down') {
    const item = event.target.parentElement.parentElement;
    const product = productObj['products'][item.dataset.id];
    const quantity = event.target.previousElementSibling;

    if (+quantity.innerText > 1) {
      product['quantity']--;
      let count = +quantity.innerText--;
      const q = count-1;
      item.querySelector('.total').innerText = `$${(q * +product['productPrice']).toFixed(2)}`;
    };
  } else if (event.target.id === 'trash') {
    const item = event.target.parentElement.parentElement;
    productObj['products'] = productObj['products'].filter(product => product.productId != item.id);
    if (productObj.products.length === 0) location.href = '/';
    localStorage.clear();
    localStorage.setItem('userProducts', JSON.stringify(productObj));
    item.remove();
  };
  getTotal();
}

function sendData(event) {
  event.preventDefault(); // prevent the refresh
  const userInputs = [];
  userInputs.push(textValidator(document.getElementById('inputName')));
  userInputs.push(numValidator(document.getElementById('phone')));
  userInputs.push(textValidator(document.getElementById('inputAddress')));
  userInputs.push(textValidator(document.getElementById('inputCity')));
  userInputs.push(textValidator(document.getElementById('inputState')));
  userInputs.push(zipValidator(document.getElementById('inputZip')));
  if (document.getElementById('inputName').value && document.getElementById('phone').value &&
      document.getElementById('inputAddress').value && document.getElementById('inputCity').value &&
      document.getElementById('inputState').value && document.getElementById('inputZip').value) {
    console.log("Done");
    const query = [userInputs, productObj.products];
    fetch("/store/get-validation/",{
      method:"POST",
      header: {"Contant-Type":"application/json"},
      body: JSON.stringify(query),
    })
    .then(resp => resp.json())
    .then(data => {
      document.querySelector('.show-total-amount').innerText = `$${data}`;
      location.href = '/store/shipping-data/';
    });
  };
};

// Event Listener
tableBody.addEventListener('click', onClick);
checkout.addEventListener('click', sendData);
