//------------------------------------------------------------------------------
//prikaz naziva fajla usled custom file inputa u žanr formi
$(document).ready(function() {
    $('#choose-genre-image').click(function() {
      $('#genre-image').click();
    });

    $("#genre-image").change(()=>{
        $("#genre-image-input-msg").val($("#genre-image").val());
    })
  });
//------------------------------------------------------------------------------
//validacija i slanje žanr forme

$(document).ready(function() {
    $('#genre-form').submit(function(event) {        
    event.preventDefault(); 

    const basic_regex = /^(?=.{1,255}$)\w{2,}/;

    genre_name = $('#genre-name');
    genre_image = $('#genre-image');

    if(!basic_regex.test(genre_name.val())){
      genre_name.addClass('is-invalid genre-form-stop'); 
    }else{ 
        genre_name.removeClass('is-invalid genre-form-stop');  
    }   

    if(!genre_image.val()){
        genre_image.addClass('is-invalid genre-form-stop');
        $('#genre-image-msg').html("Izaberite sliku žanra.");
    }else if(!(genre_image.val().endsWith(".png") || genre_image.val().endsWith(".jpg") || genre_image.val().endsWith(".jpeg"))){
        genre_image.addClass('is-invalid genre-form-stop');
        $('#genre-image-msg').html("Dozvoljene ekstenzije: .png/.jpg/.jpeg.");
    }else if((genre_image[0].files[0].size/1024/1024).toFixed(1) >=3){ 
        let size = (genre_image[0].files[0].size/1024/1024).toFixed(1);
        genre_image.addClass('is-invalid genre-form-stop');
        $('#genre-image-msg').html(`Veličina slike prelazi 3MB (${size}MB).`);
    }else{
        genre_image.removeClass('is-invalid genre-form-stop');
    }

    const validated = $('.genre-form-stop');
    if (validated.length != 0) return;  
    
    let fd = new FormData(this);
    $.ajax({        
        url: "/genre",
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
                alert("Žanr je uspešno kreiran.");
                $(this)[0].reset();
            }else{
                alert("Došlo je do greške prilikom kreiranja žanra.");
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