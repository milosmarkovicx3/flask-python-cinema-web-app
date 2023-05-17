//------------------------------------------------------------------------------
// validacija za promenu lozinke

$(document).ready(function() {
    $('#forgotten-passwd-form').submit(function(event) {
    event.preventDefault();

    const email_regex = /^(?=.{1,255}$)\w+(\w|((?<!\.)\.))*\w+\@\w+(\w|((?<!\.)\.))*\.\w{2,4}$/;
    email = $('#forgotten-passwd-email');

    if(!basic_regex.test(email.val())){
      email.addClass('is-invalid forgotten-stop');
      $('#register-email-msg').html('Unesite email adresu.');
    }else if(!email_regex.test(email.val())){
      email.addClass('is-invalid forgotten-stop');
      $('#register-email-msg').html('Email adresa uneta u pogrešnom formatu.');
    }else{ email.removeClass('is-invalid forgotten-stop');  }

    const validated = $('.forgotten-stop');
    if (validated.length != 0) return;

    let fd = new FormData(this);

    $.ajax({
        url: "/forgotten-password",
        type: "post",
        data: fd,
        contentType: false,
        processData: false,
        success: response=>{
            if (response.status == '200') {
                successAlert("PROCEDURA ZA PROMENU LOZINKE JE POKRENUTA!","MOLIMO VAS DA PROVERITE SVOJ EMAIL ZA DALJE INSTRUKCIJE!",
                             "Ako ne vidite email odmah, molimo Vas da proverite vašu spam poštu.", false);
                $(this)[0].reset();
            }else{
                errorAlert(response);
            }
        },
        error: function(error) {
            errorAlert(response);
        }
    });

    });
  });
//------------------------------------------------------------------------------