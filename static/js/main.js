// controls photo slides on homepage / portfolio page
let slideIndex = 0;
showSlides();

function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides() {
  let slides = document.getElementsByClassName("slider-img");
  let dots = document.getElementsByClassName("dot");

  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}

  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
  setTimeout(showSlides, 6000);
}

// Toggle between adding and removing the "responsive" class to navmenu when the user clicks on the icon
function toggleResponsiveness() {
  let navMenu = document.getElementById("myNavMenu");
  if (navMenu.className === "nav-menu") {
    navMenu.className += " responsive";
  } else {
    navMenu.className = "nav-menu";
  }
}