(() => {
  const total = document.querySelectorAll('.total');
  const box = document.getElementById('total-amount');
  const totalAmount = document.createElement('h1');
  totalAmount.innerHTML = `<b><font color="#fc5c65">Total Amount: </font></b>$${[...total].reduce((acc, curr) => acc + +curr.innerText.slice(1), 0)}`;
  box.appendChild(totalAmount);

})()
