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

/* form validation form Validation code taken from https://stackoverflow.com/questions/24128659/contact-form-validation-javascript */

function validateName() {

    var name = document.getElementById('fullname').value;
  
    if(name.length == 0) {
  
      producePrompt('Name is required', 'name-error' , 'red')
      return false;
  
    }
  
    if (!name.match(/^[A-Za-z]*\s{1}[A-Za-z]*$/)) {
  
      producePrompt('Full Name, please.','name-error', 'red');
      return false;
  
    }
  
    producePrompt('Valid', 'name-error', 'green');
    return true;
  
  }

  function validateEmail () {

    var email = document.getElementById('emailaddress').value;
  
    if(email.length == 0) {
  
      producePrompt('Email Invalid','email-error', 'red');
      return false;
  
    }
  
    if(!email.match(/^[A-Za-z\._\-[0-9]*[@][A-Za-z]*[\.][a-z]{2,4}$/)) {
  
      producePrompt('Email Invalid', 'email-error', 'red');
      return false;
  
    }
  
    producePrompt('Valid', 'email-error', 'green');
    return true;
  
  }
  
  function validateMessage() {
    var message = document.getElementById('message').value;
    var required = 10;
    var left = required - message.length;
  
    if (left > 0) {
      producePrompt(left + ' more characters required','message-error','red');
      return false;
    }
  
    producePrompt('Valid', 'message-error', 'green');
    return true;
  
  }
  
  function validateForm() {
    if (!validateName() || !validatePhone() || !validateEmail() || !validateMessage()) {
      jsShow('submit-error');
      producePrompt('Please fix errors to submit.', 'submit-error', 'red');
      setTimeout(function(){jsHide('submit-error');}, 2000);
    }
    else {
  
    }
  }
  
  function jsShow(id) {
    document.getElementById(id).style.display = 'block';
  }
  
  function jsHide(id) {
    document.getElementById(id).style.display = 'none';
  }
  
  
  
  
  function producePrompt(message, promptLocation, color) {
  
    document.getElementById(promptLocation).innerHTML = message;
    document.getElementById(promptLocation).style.color = color;
  
  
  }

