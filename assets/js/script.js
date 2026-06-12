document.addEventListener('DOMContentLoaded', function () {
  // Mobile nav toggle
  const toggle = document.querySelector('.mobile-toggle');
  const nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      nav.classList.toggle('open');
    });
  }

  // Dropdowns on mobile
  document.querySelectorAll('.dropdown > a, .dropdown > .dropbtn').forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      if (window.innerWidth <= 768) {
        e.preventDefault();
        this.parentElement.classList.toggle('open');
      }
    });
  });

  // Hero carousel
  var slides = document.querySelectorAll('.hero-slide');
  var dotsContainer = document.querySelector('.hero-dots');
  if (slides.length && dotsContainer) {
    var dots = dotsContainer.querySelectorAll('button');
    var current = 0;
    var interval;

    function goTo(index) {
      slides.forEach(function (s) { s.classList.remove('active'); });
      dots.forEach(function (d) { d.classList.remove('active'); });
      slides[index].classList.add('active');
      dots[index].classList.add('active');
      current = index;
    }

    dots.forEach(function (dot, i) {
      dot.addEventListener('click', function () { goTo(i); resetInterval(); });
    });

    function next() { goTo((current + 1) % slides.length); }
    function resetInterval() { clearInterval(interval); interval = setInterval(next, 5000); }
    resetInterval();
  }
});
