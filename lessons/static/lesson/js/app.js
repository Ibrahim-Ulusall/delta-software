let slides = document.querySelectorAll('.slider-content');
let index = 0;

//next function

function next(){
    slides[index].classList.remove('active');
    index= (index + 1) % slides.length;
    slides[index].classList.add('active');
}

// prev function

function prev(){
    slides[index].classList.remove('active');
    index= (index - 1 + slides.length) % slides.length;
    slides[index].classList.add('active');
}
setInterval(next,5000);