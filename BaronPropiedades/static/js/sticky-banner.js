onscroll = function () {
    stickyBanner();
};

var banner = document.getElementById("banner-container");
var sticky = banner.offsetTop + 250;

function stickyBanner() {
    if (window.scrollY >= sticky) {
        banner.classList.add("is-sticky");
    }
    else {
        banner.classList.remove("is-sticky");
    }
}
