$.getScript("js/aos.js", function () {
    AOS.init({
        offset: 0, // offset (in px) from the original trigger point
        delay: 0, // values from 0 to 3000, with step 50ms
        duration: 1000, // values from 0 to 3000, with step 50ms
        easing: 'ease', // default easing for AOS animations
        once: false, // whether animation should happen only once - while scrolling down
        mirror: true, // whether elements should animate out while scrolling past them
        anchorPlacement: 'top-bottom', // defines which position of the element regarding to window should trigger the animation
    });
});

function includeHTML() {
    var z, i, elmnt, file, xhttp;
    /* Loop through a collection of all HTML elements: */
    z = document.getElementsByTagName("*");
    for (i = 0; i < z.length; i++) {
        elmnt = z[i];
        /*search for elements with a certain atrribute:*/
        file = elmnt.getAttribute("w3-include-html");
        if (file) {
            /* Make an HTTP request using the attribute value as the file name: */
            xhttp = new XMLHttpRequest();
            xhttp.onreadystatechange = function () {
                if (this.readyState == 4) {
                    if (this.status == 200) { elmnt.innerHTML = this.responseText; }
                    if (this.status == 404) { elmnt.innerHTML = "Page not found."; }
                    /* Remove the attribute, and call this function once more: */
                    elmnt.removeAttribute("w3-include-html");
                    includeHTML();
                }
            }
            xhttp.open("GET", file, true);
            xhttp.send();
            /* Exit the function: */
            return;
        }
    }
}

$(function () {
    $('[data-toggle="tooltip"]').tooltip()
})



$(document).ready(function () {
    $("#otpBtn").click(function () {
        var otpInput = $('.otp-input');

        if (!otpInput.hasClass('active')) {
            otpInput.addClass('show').outerWidth();
            otpInput.addClass('active');
            $(".get-otp-section").hide();
        }
    });

    $("#loginBtn").click(function () {
        var loginCard = $('.login-card');

        if (!loginCard.hasClass('active')) {
            loginCard.addClass('show').outerWidth();
            loginCard.addClass('active');
            loginCard.show();
        }
    });

    $("#loginBtnsm").click(function () {
        var loginCard = $('.login-card');

        if (!loginCard.hasClass('active')) {
            loginCard.addClass('show').outerWidth();
            loginCard.addClass('active');
            loginCard.show();
        }
    });

    $(document).mouseup(function (e) {
        var loginCardd = $(".login-card");

        // if the target of the click isn't the container nor a descendant of the container
        if (loginCardd.hasClass('active')) {
            if (!loginCardd.is(e.target) && loginCardd.has(e.target).length === 0) {
                loginCardd.hide();
                loginCardd.removeClass('show');
                loginCardd.removeClass('active');
            }
        }
    });

});

var timeoutHandle;
function countdown(minutes, seconds) {
    function tick() {
        var counter = document.getElementById("otpTimer");
        counter.innerHTML = "OTP will expire in " +
            minutes.toString() + ":" + (seconds < 10 ? "0" : "") + String(seconds);
        seconds--;
        if (seconds >= 0) {
            document.getElementById("otpTimer").style.display = "block";
            document.getElementById("resetBtn").style.display = "none";
            timeoutHandle = setTimeout(tick, 1000);
        } else {
            document.getElementById("otpTimer").style.display = "none";
            document.getElementById("resetBtn").style.display = "block";
            if (minutes >= 1) {
                // countdown(mins-1);   never reach “00″ issue solved:Contributed by Victor Streithorst
                setTimeout(function () {
                    countdown(minutes - 1, 59);
                }, 1000);
            }
        }
    }
    tick();
}