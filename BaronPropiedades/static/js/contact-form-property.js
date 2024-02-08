// Show contact form
function showCustomAlert(property_title) {

    // Add property values to the form - Tittle & ID
    var title = document.getElementById("form-property-title");
    title.innerHTML ="¿Te interesa "+property_title+ "? <br> Regístrate y te contactaremos!";
    

    // Show Overlay
    var overlay = document.getElementById('form-overlay');
    var customAlert = document.getElementById('form-alert');
    var body = document.body;

    overlay.style.display = 'block';
    customAlert.style.display = 'block';

    // Trigger reflow to enable the transition
    customAlert.offsetHeight;

    customAlert.classList.add('show');
    body.classList.add('no-scroll');
}


// Hide contact form
function hideCustomAlert() {
    var overlay = document.getElementById('form-overlay');
    var customAlert = document.getElementById('form-alert');
    var body = document.body;

    overlay.style.display = 'none';
    customAlert.classList.remove('show');
    body.classList.remove('no-scroll');

}






