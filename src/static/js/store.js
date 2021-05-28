const box = document.getElementById('box');
const deleteBtn = document.getElementById('delete');
const cartTotal = document.getElementById('cart-total');
const section = document.querySelector('section');

localStorage.clear();

const userProducts =  {products:[]};
let cart = 0;

function confirmDelete(event) {
  const deletePopUp = document.createElement('div');
  if (event.target.id === 'delete') {
    const prodId = event.target.getAttribute('data-product-id');
    deletePopUp.className = 'row'
    deletePopUp.innerHTML = `
    <div class="col-xs-10 offset-xs-1 col-sm-10 offset-sm-1 col-md-10 offset-md-1 col-lg-10 offset-lg-1 pop-up">
    <h2 class="text-danger">Are You Sure Of Deleting this Product?</h2>
    <hr>
    <a id="confirm-delete" data-prod-id="${prodId}" class="btn btn-danger" href="/store/delete-product/${prodId}">Yes, Delete</a>
    <a id="return" class="btn btn-secondary">No, Return</a>
    </div>
    `;
    section.classList.add('body-background');
    document.body.insertAdjacentElement('afterbegin', deletePopUp);
  } else if (event.target.id === 'return') {
    document.body.querySelector('div').firstElementChild.classList.add('invisible');
    section.classList.remove('body-background');
  };

};

box.addEventListener('click', event => {
  const elementId = event.target.id;
  if (elementId === 'add')  {
    event.preventDefault();
    cartTotal.classList.remove('hidden');

    const productId = event.target.getAttribute('data-product-id');
    const productName= event.target.getAttribute('data-product-name');
    const productImageURL= event.target.getAttribute('data-product-imageURL');
    const productQuantity = event.target.getAttribute('data-product-quantity');
    const productPrice = event.target.getAttribute('data-product-price');

    loop1:for (const key in userProducts) {
      for (const obj of userProducts[key]) {
        if (obj['productId'] === productId) {
          obj['quantity']++;
          cart++;
          break loop1;
        };
      };
      userProducts['products'].push({productId, productName, productImageURL, productPrice, productQuantity, quantity: 1});
      cart++;
      break;
    };
    localStorage.setItem('userProducts', JSON.stringify(userProducts));
    cartTotal.innerText = String(cart);
  };

});

document.body.addEventListener('click', confirmDelete);
