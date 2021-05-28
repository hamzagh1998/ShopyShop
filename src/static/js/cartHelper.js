function textValidator(input) {
  if (input.value.length === 0) {
    input.nextElementSibling.style.display = 'block';
    input.nextElementSibling.innerText = 'This fiels is required!';
    return;
  } else if (input.value.length > 0 && isNaN(input.value)) {
    input.nextElementSibling.style.display = 'none';
    return input.value;
  } else {
    input.nextElementSibling.innerText = 'Error, please enter a valid input!';
  };
};

function numValidator(input) {
  if (input.value.length === 0 || input.value.length > 8) {
    input.nextElementSibling.style.display = 'block';
    input.nextElementSibling.innerText = 'This fiels is required!';
    return;
  } else if (input.value.length === 8 && !isNaN(input.value)) {
    input.nextElementSibling.style.display = 'none';
    return input.value;
  } else {
    input.nextElementSibling.innerText = 'Error, please enter a valid input!';
  };
};

function zipValidator(input) {
  if (input.value.length === 4 && !isNaN(input.value)) return input.value;
  else if (input.value.length < 4 || isNaN(input.value)) input.nextElementSibling.innerText = 'Error, please enter a valid input!';
};
