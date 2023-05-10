//------------------------------------------------------------------------------
//logika za prikazivanje(toggle) ikonice pored inputa za lozinke u formama

$(document).ready(function() {
    $('#register-show-passwd').click(function() {
        $('#register-passwd').prop('type', function(index, value) {
            return value === 'password' ? 'text' : 'password';
        });
        $('#register-show-passwd').toggleClass('fi-rs-eye fi-rs-crossed-eye');
    });

    $('#login-show-passwd').on('click', function() {
        $('#login-passwd').prop('type', function(_, type) {
            return type === 'password' ? 'text' : 'password';
        });
        $(this).toggleClass('fi-rs-crossed-eye fi-rs-eye');
    });
});
//------------------------------------------------------------------------------
// validacija za registrovanje korisnika

$(document).ready(function() {
    $('#register-form').submit(function(event) {
    event.preventDefault();

    const email_regex = /^(?=.{1,255}$)\w+(\w|((?<!\.)\.))*\w+\@\w+(\w|((?<!\.)\.))*\.\w{2,4}$/;
    const passwd_regex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W]).{5,50}$/;
    const basic_regex = /^(?=.{1,255}$)\w{2,}/;

    username = $('#register-username');
    email = $('#register-email');
    passwd = $('#register-passwd');
    first_name = $('#register-first-name');
    last_name = $('#register-last-name');
    conditions = $('#register-conditions');

    if(!$username_exist)
    if(!basic_regex.test(username.val())){
      username.addClass('is-invalid register-stop');
      $('#register-username-msg').html('Izarerite korisničko ime.');
    }else{ username.removeClass('is-invalid register-stop');  }

    if(!$email_exist)
    if(!basic_regex.test(email.val())){
      email.addClass('is-invalid register-stop');
      $('#register-email-msg').html('Unesite email adresu.');
    }else if(!email_regex.test(email.val())){
      email.addClass('is-invalid register-stop');
      $('#register-email-msg').html('Email adresa uneta u pogrešnom formatu.');
    }else{ email.removeClass('is-invalid register-stop');  }

    if(!basic_regex.test(passwd.val())){
      passwd.addClass('is-invalid register-stop');
      $('#register-passwd-msg').html('Izaberite lozinku.');
    }else if(!passwd_regex.test(passwd.val())){
      passwd.addClass('is-invalid register-stop');
      $('#register-passwd-msg').html('Vaša lozinka mora sadržati minimum 5 karaktera, slovo, broj i specijalan znak.');
    }else{ passwd.removeClass('is-invalid register-stop');  }

    if(!basic_regex.test(first_name.val())){ first_name.addClass('is-invalid register-stop'); }
    else{ first_name.removeClass('is-invalid register-stop'); }

    if(!basic_regex.test(last_name.val())){ last_name.addClass('is-invalid register-stop'); }
    else{ last_name.removeClass('is-invalid register-stop'); }

    if(!conditions.is(':checked')){ conditions.addClass('is-invalid register-stop'); }
    else{ conditions.removeClass('is-invalid register-stop');  }

    const validated = $('.register-stop');
    if (validated.length != 0) return;

    let fd = new FormData(this);

    $.ajax({
        url: "/user",
        type: "post",
        data: fd,
        contentType: false,
        processData: false,
        success: response=>{
            if (response.status == '200') {
                alert("Nalog je uspešno kreiran.\nMail za konfirmaciju vam je poslat.");
                $(this)[0].reset();
                $('#staticBackdropRegistation').modal('hide');
            }else{
                alert("Došlo je greške prilikom pravljenja naloga." + response.description);
                console.log(response);
            }
        },
        error: function(error) {
            alert("Došlo je do greške prilikom slanja zahteva.");
            console.error(error);
        }
    });

    });
  });
//------------------------------------------------------------------------------
// provera za već postojeće korisničko ime tokom registracije

var $username_exist = false;

$(document).ready(function() {
    const $username_input = $('#register-username');
    const $username_msg = $('#register-username-msg'); 
    
    $username_input.on('input', function() {
      const username = $username_input.val();      
      
      $.ajax({
        url: `/user/${username}/username`,
        method: 'get',
        success: function(response) {
          if (response.status == '200') {
            $username_msg.html('Izabrano korisničko ime već postoji u sistemu.'); 
            $username_input.addClass('is-invalid register-stop'); 
            $username_exist = true    
          }else if ($username_exist){
            $username_msg.html('Izarerite korisničko ime.'); 
            $username_input.removeClass('is-invalid register-stop'); 
            $username_exist = false
          }
        },
        error: function(error) {
          console.error(error);
        }
      });
    });
  });
//------------------------------------------------------------------------------
// provera za već postojeću email adresu tokom registracije

var $email_exist = false;

$(document).ready(function() {
    const $email_input = $('#register-email');
    const $email_msg = $('#register-email-msg');  
    
    
    $email_input.on('input', function() {
      const email = $email_input.val();      
      
      $.ajax({
        url: `/user/${email}/email`,
        method: 'get',
        success: function(response) {
          if (response.status == '200') {
            $email_msg.html('Uneta email adresa već postoji u sistemu.');
            $email_input.addClass('is-invalid register-stop'); 
            $email_exist = true;    
          }else if ($email_exist){
            $email_msg.html('Unesite email adresu.');
            $email_input.removeClass('is-invalid register-stop'); 
            $email_exist = false;
          }
        },
        error: function(error) {
          console.error(error);
        }
      });
    });
  });
//------------------------------------------------------------------------------
