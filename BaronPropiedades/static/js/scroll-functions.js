window.addEventListener("scroll", function () {
    var button = document.getElementById("contact-button-form");
    
    if(button){
        button.classList.add("jiggler-one");
        setTimeout(function () {
            button.classList.remove("jiggler-one");
        }, 1500);
    }
});

window.addEventListener("scroll", function () {
    var button = document.getElementById("catalogue-button-redirect");
    
    if(button){
        button.classList.add("jiggler-two");
        setTimeout(function () {
            button.classList.remove("jiggler-two");
        }, 1500);
    }
});

window.addEventListener("mouseover", function () {
    var button = document.getElementById("property-contact-btn");
    
    if(button){
        button.classList.add("jiggler-two");
        setTimeout(function () {
            button.classList.remove("jiggler-two");
        }, 1500);
    }
});

