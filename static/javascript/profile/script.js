//------------------------------------------------------------------------------
//logika za prikazivanje(toggle) ikonice pored inputa za lozinke u formi

$(document).ready(function() {
    $('#profile-show-passwd').click(function() {
        $('#profile-passwd').prop('type', function(index, value) {
            return value === 'password' ? 'text' : 'password';
        });
        $('#profile-show-passwd').toggleClass('fi-rs-eye fi-rs-crossed-eye');
    });
    $('#profile-show-passwd-new').click(function() {
        $('#profile-passwd-new').prop('type', function(index, value) {
            return value === 'password' ? 'text' : 'password';
        });
        $('#profile-show-passwd-new').toggleClass('fi-rs-eye fi-rs-crossed-eye');
    });
});

//------------------------------------------------------------------------------
//prikaz slike i njenog naziva

$(document).ready(function() {
    $('#choose-image').click(function() {
      $('#profile-image').click();
    });

    $('#profile-image').change((e)=>{
        $('#profile-image-input-msg').val($('#profile-image').val());
        var file = e.target.files[0];
        if (!file) return;
    
        var reader = new FileReader();
        reader.onload = function(e) {
          $('#profile-image-edit').attr('src', e.target.result);
        }
        reader.readAsDataURL(file);        
    })
  });
//------------------------------------------------------------------------------
// validacija za ažuliranje podataka korisnika

$(document).ready(function() {
    $('#profile-form').submit(function(event) {
    event.preventDefault();

    const email_regex = /^(?=.{1,255}$)\w+(\w|((?<!\.)\.))*\w+\@\w+(\w|((?<!\.)\.))*\.\w{2,4}$/;
    const passwd_regex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W]).{5,50}$/;
    const basic_regex = /^(?=.{1,255}$)\w{2,}/;

    username = $('#profile-username');
    email = $('#profile-email');
    passwd = $('#profile-passwd');
    passwd_new = $('#profile-passwd-new');
    first_name = $('#profile-first-name');
    last_name = $('#profile-last-name');
    image = $('#profile-image');

    if(!$username_exist)
    if(!basic_regex.test(username.val())){
      username.addClass('is-invalid profile-stop');
      $('#profile-username-msg').html('Izarerite korisničko ime.');
    }else{ username.removeClass('is-invalid profile-stop');  }

    if(!$email_exist)
    if(!basic_regex.test(email.val())){
      email.addClass('is-invalid profile-stop');
      $('#profile-email-msg').html('Unesite email adresu.');
    }else if(!email_regex.test(email.val())){
      email.addClass('is-invalid profile-stop');
      $('#profile-email-msg').html('Email adresa uneta u pogrešnom formatu.');
    }else{ email.removeClass('is-invalid profile-stop');  }

    if(!basic_regex.test(passwd.val())){
      passwd.addClass('is-invalid profile-stop');
      $('#profile-passwd-msg').html('Unesite lozinku.');
    }else if(!passwd_regex.test(passwd.val())){
      passwd.addClass('is-invalid profile-stop');
      $('#profile-passwd-msg').html('Lozinka mora sadržati minimum 5 karaktera, slovo, broj i specijalan znak.');
    }else{ passwd.removeClass('is-invalid profile-stop');  }

    if(passwd_new.val() && !passwd_regex.test(passwd_new.val())){
      passwd_new.addClass('is-invalid profile-stop');
      $('#profile-passwd-new-msg').html('Lozinka mora sadržati minimum 5 karaktera, slovo, broj i specijalan znak.');
    }else{ passwd_new.removeClass('is-invalid profile-stop'); }

    if(!basic_regex.test(first_name.val())){ first_name.addClass('is-invalid profile-stop'); }
    else{ first_name.removeClass('is-invalid profile-stop'); }

    if(!basic_regex.test(last_name.val())){ last_name.addClass('is-invalid profile-stop'); }
    else{ last_name.removeClass('is-invalid profile-stop'); }

    if(image.val() &&
      !(image.val().endsWith(".gif") ||
        image.val().endsWith(".png") || 
        image.val().endsWith(".jpg") || 
        image.val().endsWith(".jpeg"))) {
        image.addClass('is-invalid movie-form-stop');
        $('#profile-image-msg').html("Dozvoljene ekstenzije: .gif/.png/.jpg/.jpeg.");
    }else if(image.val() && (image[0].files[0].size/1024/1024).toFixed(1) >=3){
        let size = (image[0].files[0].size/1024/1024).toFixed(1);
        image.addClass('is-invalid movie-form-stop');
        $('#profile-image-msg').html(`Veličina slike prelazi 3MB (${size}MB).`);
    }else{
        image.removeClass('is-invalid movie-form-stop');
    }


    const validated = $('.profile-stop');
    if (validated.length != 0) return;

    let fd = new FormData(this);

    $.ajax({
        url: "/user",
        type: "put",
        data: fd,
        contentType: false,
        processData: false,        
        xhr: function() {
          var xhr = $.ajaxSettings.xhr();
          if (xhr.upload) {
            xhr.upload.addEventListener('progress', function(event) {
              if (event.lengthComputable) {
                var percentComplete = Math.round((event.loaded / event.total) * 100);
                $('#loader').css({'display':'flex'});
                $('#loader-text').text(percentComplete + '%')
                console.log(percentComplete);
              }
            }, false);
          }
          return xhr;
        },
        success: response=>{
          $('#loader').css({'display':'none'});
            if (response.status == '200') {
                successAlert("NALOG JE USPEŠNO AŽULIRAN!", "", "", true);
                $('#staticBackdropRegistation').modal('hide');
            }else{
                errorAlert(response);
            }
        },
        error: function(error) {
          $('#loader').css({'display':'none'});
            errorAlert(response);
        }
    });

    });
  });
//------------------------------------------------------------------------------
// provera za već postojeće korisničko ime

var $username_exist = false;

$(document).ready(function() {
    const $username_input = $('#profile-username');
    const $username_msg = $('#profile-username-msg');
    const original_username = $('#original_username').val();
    const basic_regex = /^(?=.{1,255}$)\w{2,}/;

    $username_input.on('input', function() {
      const username = $username_input.val();
      if(username == original_username) return;
      if(!basic_regex.test(username)) return;

      $.ajax({
        url: `/user/${username}/username`,
        method: 'get',
        success: function(response) {
          if (response.status == '200') {
            $username_msg.html('Izabrano korisničko ime već postoji u sistemu.');
            $username_input.addClass('is-invalid profile-stop');
            $username_exist = true
          }else if ($username_exist){
            $username_msg.html('Izarerite korisničko ime.');
            $username_input.removeClass('is-invalid profile-stop');
            $username_exist = false
          }
        },
        error: function(error) {

        }
      });
    });
  });
//------------------------------------------------------------------------------
// provera za već postojeću email adresu

var $email_exist = false;

$(document).ready(function() {
    const $email_input = $('#profile-email');
    const $email_msg = $('#profile-email-msg');
    const original_email = $('#original_email').val();
    const email_regex = /^(?=.{1,255}$)\w+(\w|((?<!\.)\.))*\w+\@\w+(\w|((?<!\.)\.))*\.\w{2,4}$/;

    $email_input.on('input', function() {
      const email = $email_input.val();
      if(email == original_email) return;
      if(!email_regex.test(email)) return;

      $.ajax({
        url: `/user/${email}/email`,
        method: 'get',
        success: function(response) {
          if (response.status == '200') {
            $email_msg.html('Uneta email adresa već postoji u sistemu.');
            $email_input.addClass('is-invalid profile-stop');
            $email_exist = true;
          }else if ($email_exist){
            $email_msg.html('Unesite email adresu.');
            $email_input.removeClass('is-invalid profile-stop');
            $email_exist = false;
          }
        },
        error: function(error) {

        }
      });
    });
  });
//------------------------------------------------------------------------------
