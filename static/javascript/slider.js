const slider = document.querySelector('#slider');
const images = document.querySelectorAll('#slider img');

let index = 0;

function slide() {
  for (let i = 0; i < images.length; i++) {
    images[i].classList.remove('active');
  }
  images[index].classList.add('active');
  index++;
  if (index >= images.length) {
    index = 0;
  }
}

slide();
setInterval(slide, 5000);
