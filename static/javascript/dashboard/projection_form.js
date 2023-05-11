//------------------------------------------------------------------------------
//validacija i slanje projekcija forme

$(document).ready(function() {
    $('#projection-form').submit(function(event) {
    event.preventDefault();

    let movie_id = $('#projection-movie');
    let hall_id = $('#projection-hall');
    let date_from = $('#projection-from');
    let date_to = $('#projection-to');
    let time = $('#projection-time');

    movie_id.val() ? movie_id.removeClass('is-invalid projection-form-stop') : movie_id.addClass('is-invalid projection-form-stop');
    hall_id.val() ? hall_id.removeClass('is-invalid projection-form-stop') : hall_id.addClass('is-invalid projection-form-stop');
    date_from.val() ? date_from.removeClass('is-invalid projection-form-stop') : date_from.addClass('is-invalid projection-form-stop');
    date_to.val() ? date_to.removeClass('is-invalid projection-form-stop') : date_to.addClass('is-invalid projection-form-stop');
    time.val() ? time.removeClass('is-invalid projection-form-stop') : time.addClass('is-invalid projection-form-stop');

    if (date_from.val() && date_to.val() && date_from.val() < date_to.val() ) {
        date_to.removeClass('is-invalid projection-form-stop');
    }else{
        date_to.addClass('is-invalid projection-form-stop');
    }

    const validated = $('.projection-form-stop');
    if (validated.length != 0) return;

    let fd = new FormData(this);
    $.ajax({
        url: "/projection",
        type: "post",
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
                alert("Projekcija je uspešno kreirana.");
                $(this)[0].reset();
            }else{
                alert("Došlo je do greške prilikom kreiranja projekcije." + response.description);
                console.log(response);
            }
        },
        error: function(error) {
            $('#loader').css({'display':'none'});
            alert("Došlo je do greške prilikom slanja zahteva.");
            console.error(error);
        }
    });

    });
  });
//------------------------------------------------------------------------------