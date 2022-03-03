// Modal Functionality
const openEls = document.querySelectorAll("[data-open]");
const closeEls = document.querySelectorAll("[data-close]");
const body = document.querySelector("body");
const isVisible = "is-visible";
var distanceToTopFromModal
const logoImageSource = document.querySelector(".header__logo-img").src
// Sets background image of the modal content
document.getElementById("drag-modal1").style.background =  `whitesmoke url('${logoImageSource}') no-repeat center center fixed`

// Open Modal
for(const el of openEls) {
    el.addEventListener("click", function() {
        const modalId = this.dataset.open;
        body.classList.add("hide-body-overflow")
        document.getElementById(modalId).classList.add(isVisible);
        distanceToTopFromModal = dragModal.getBoundingClientRect().top;
    });
}

// Close Modal when X is clicked
for (const el of closeEls) {
    el.addEventListener("click", function() {
        body.classList.remove("hide-body-overflow")
        document.querySelector(".modal.is-visible").classList.remove(isVisible);
    });
}

// Close Modal when outside the modal is clicked
document.addEventListener("click", e => {
    if (e.target === document.querySelector(".modal.is-visible")) {
        body.classList.remove("hide-body-overflow")
        document.querySelector(".modal.is-visible").classList.remove(isVisible);

    }
});

// Close Modal with Escape button
document.addEventListener("keyup", e => {
    if (e.key === "Escape" && document.querySelector(".modal.is-visible")) {
        body.classList.remove("hide-body-overflow")
        document.querySelector(".modal.is-visible").classList.remove(isVisible);
    }
});


// Drag Functionality
var modalContainer = document.querySelector("#modal1");
var dragModal = document.querySelector("#drag-modal1");

var active = false;
var currentX;
var currentY;
var initialX;
var initialY;
var xOffset = 0;
var yOffset = 0;

// For TouchScreen
modalContainer.addEventListener("touchstart", dragStart, false);
modalContainer.addEventListener("touchend", dragEnd, false);
modalContainer.addEventListener("touchmove", drag, false);

// For Mouse
modalContainer.addEventListener("mousedown", dragStart, false);
modalContainer.addEventListener("mouseup", dragEnd, false);
modalContainer.addEventListener("mousemove", drag, false);

function dragStart(e) {
    if (e.type === "touchstart") {
        initialX = e.touches[0].clientX - xOffset;
        initialY = e.touches[0].clientY - yOffset;
    } else {
        initialX = e.clientX - xOffset;
        initialY = e.clientY - yOffset;
    }
    if (e.target === dragModal) {
        active = true;
    }
}

function dragEnd(e) {
    initialX = 0;
    initialY = 0;

    // If modal is dragged up
    if (dragModal.getBoundingClientRect().top < distanceToTopFromModal){
        if (dragModal.getBoundingClientRect().top < distanceToTopFromModal/2){
            setTranslate("0", distanceToTopFromModal * 10, dragModal);
            setTimeout(function () {
                body.classList.remove("hide-body-overflow")
                modalContainer.classList.remove(isVisible)
                setTranslate("0", "0", dragModal);
            }, 300)
        }
        else {
            setTranslate("0", "0", dragModal);
        }
    }
    // If modal is dragged is down
    else if (dragModal.getBoundingClientRect().top > distanceToTopFromModal){
        if (dragModal.getBoundingClientRect().top > distanceToTopFromModal + distanceToTopFromModal/2){
            setTranslate("0", distanceToTopFromModal * -10, dragModal);
            setTimeout(function () {
                body.classList.remove("hide-body-overflow")
                modalContainer.classList.remove(isVisible)
                setTranslate("0", "0", dragModal);
            }, 300)
        }
        else {
            setTranslate("0", "0", dragModal);
        }
    }

    active = false;
}

function drag(e) {
    if (active) {

        // e.preventDefault();

        if (e.type === "touchmove") {
            currentX = e.touches[0].clientX - initialX;
            currentY = e.touches[0].clientY - initialY;
        } else {
            currentX = e.clientX - initialX;
            currentY = e.clientY - initialY;
        }

        xOffset = 0;
        yOffset = 0;

        setTranslate("0", currentY, dragModal);

    }
}


function setTranslate(xPos, yPos, el) {
    el.style.transform = "translate3d(" + xPos + "px, " + yPos + "px, 0)";
}
