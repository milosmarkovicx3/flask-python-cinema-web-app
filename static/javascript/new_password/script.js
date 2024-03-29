//------------------------------------------------------------------------------
//logika za prikazivanje(toggle) ikonice pored inputa za lozinke u formama

$(document).ready(function() {
    $('#new-passwd-show').click(function() {
        $('#new-passwd').prop('type', function(index, value) {
            return value === 'password' ? 'text' : 'password';
        });
        $('#new-passwd-show').toggleClass('fi-rs-eye fi-rs-crossed-eye');
    });
});
//------------------------------------------------------------------------------
// validacija za promenu lozinke

$(document).ready(function() {
    $('#new-passwd-form').submit(function(event) {
    event.preventDefault();

    const passwd_regex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W]).{5,50}$/;
    const basic_regex = /^(?=.{1,255}$)\w{2,}/;
    passwd = $('#new-passwd');

    if(!basic_regex.test(passwd.val())){
      passwd.addClass('is-invalid new-stop');
      $('#new-passwd-msg').html('Izaberite lozinku.');
    }else if(!passwd_regex.test(passwd.val())){
      passwd.addClass('is-invalid new-stop');
      $('#new-passwd-msg').html('Lozinka mora sadržati minimum 5 karaktera, slovo, broj i specijalan znak.');
    }else{ passwd.removeClass('is-invalid new-stop');  }

    const validated = $('.new-stop');
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
                successAlert("LOZINKA JE USPEŠNO PROMENJENA!", "", "", false);
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