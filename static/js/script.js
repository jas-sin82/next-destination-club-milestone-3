/*
Functions which will open/show the overlay navigation menu
*/

function openMenu() {
    document.getElementById("menu_bar").style.width = "100%";
}

function closeMenu() {
    document.getElementById("menu_bar").style.width = "0%";
}

/* 
Call function to intialise emailjs
*/

(function () {
    emailjs.init("user_ogk8J5XmQvETaxv1fZva0");
})();

function sendMail(contactForm) {
    emailjs.send("gmail", "template_i3671bf", {
            "from_name": contactForm.name.value,
            "from_email": contactForm.emailaddress.value,
            "message": contactForm.message.value
        })

        .then(
            function () {
                document.getElementById("contact-form").reset();
            })

        .then(
            function (response) {
                console.log("SUCCESS", response);
                emailSuccess();
            },
            function (error) {

                console.log("FAILED", error);
                unsuccess();

            }
        );
    return false;

}

function emailSuccess() {
    swal({
        title: "Great!",
        text: "Your message has been sent successfully!",
        icon: "success",
        button: "ok!",
    });
}