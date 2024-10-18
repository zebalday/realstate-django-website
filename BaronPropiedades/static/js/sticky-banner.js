onscroll = function () {
    stickyBanner();
};

var banner = document.getElementById("social-media-container");
var sticky = banner.offsetTop + 250;

function stickyBanner() {
    if (window.scrollY >= sticky) {
        banner.classList.add("is-sticky");
        banner.classList.add("banner-container");
    }
    else {
        banner.classList.remove("banner-container");
        banner.classList.remove("is-sticky");
    }
}
