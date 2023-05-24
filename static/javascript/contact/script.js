//------------------------------------------------------------------------------
// validacija za registrovanje korisnika

$(document).ready(function() {
    $('#contact-form').submit(function(event) {
    event.preventDefault();

    const email_regex = /^(?=.{1,255}$)\w+(\w|((?<!\.)\.))*\w+\@\w+(\w|((?<!\.)\.))*\.\w{2,4}$/;
    const basic_regex = /^(?=.{1,255}$)\w{2,}/;

    email = $('#contact-email');
    first_name = $('#contact-first-name');
    last_name = $('#contact-last-name');
    message = $('#contact-message');


    if(!basic_regex.test(first_name.val())){ first_name.addClass('is-invalid contact-stop'); }
    else{ first_name.removeClass('is-invalid contact-stop'); }

    if(!basic_regex.test(last_name.val())){ last_name.addClass('is-invalid contact-stop'); }
    else{ last_name.removeClass('is-invalid contact-stop'); }

    if(!basic_regex.test(email.val())){
      email.addClass('is-invalid contact-stop');
      $('#contact-email-msg').html('Unesite email adresu.');
    }else if(!email_regex.test(email.val())){
      email.addClass('is-invalid contact-stop');
      $('#contact-email-msg').html('Email adresa uneta u pogrešnom formatu.');
    }else{ email.removeClass('is-invalid contact-stop');  }

    if(!basic_regex.test(message.val())){ message.addClass('is-invalid contact-stop'); }
    else{ message.removeClass('is-invalid contact-stop'); }

    const validated = $('.contact-stop');
    if (validated.length != 0) return;

    let fd = new FormData(this);

    $.ajax({
        url: `/kontakt?first_name=${first_name.val()}&last_name=${last_name.val()}&email=${email.val()}&message=${message.val()}`,
        type: "get",
        data: fd,
        contentType: false,
        processData: false,
        success: response=>{
            if (response.status == '200') {
                successAlert("PORUKA JE USPEŠNO POSLATA!", "ODGOVOR MOŽETE DA OČEKUJETE U NAREDNIH 24H!", "", false);
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