const scrollers = document.querySelectorAll(".scroller");

// If a user hasn't opted in for recuded motion, then we add the animation
if (!window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
  addAnimation();
}

function addAnimation() {
  scrollers.forEach((scroller) => {
    // add data-animated="true" to every `.scroller` on the page
    scroller.setAttribute("data-animated", true);

    // Make an array from the elements within `.scroller-inner`
    const scrollerInner = scroller.querySelector(".scroller__inner");
    const scrollerContent = Array.from(scrollerInner.children);

    // For each item in the array, clone it
    // add aria-hidden to it
    // add it into the `.scroller-inner`
    scrollerContent.forEach((item) => {
      const duplicatedItem = item.cloneNode(true);
      duplicatedItem.setAttribute("aria-hidden", true);
      scrollerInner.appendChild(duplicatedItem);
    });
  });
}


// script.js
let currentSlide = 0;
const slides = document.querySelectorAll("#carousel-slides > div");
const totalSlides = slides.length;

document.getElementById("next").addEventListener("click", moveToNextSlide);
document.getElementById("prev").addEventListener("click", moveToPrevSlide);

function updateSlidePosition() {
    const carouselSlides = document.getElementById("carousel-slides");
    carouselSlides.style.transform = `translateX(-${currentSlide * 100}%)`;
}

function moveToNextSlide() {
    currentSlide = (currentSlide + 1) % totalSlides;
    updateSlidePosition();
}

function moveToPrevSlide() {
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    updateSlidePosition();
}


let autoplay = setInterval(moveToNextSlide, 3000);

document.querySelector(".relative").addEventListener("mouseover", () => {
    clearInterval(autoplay);
});

document.querySelector(".relative").addEventListener("mouseout", () => {
    autoplay = setInterval(moveToNextSlide, 3000);
});
