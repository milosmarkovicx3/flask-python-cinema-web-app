//------------------------------------------------------------------------------
//prikaz naziva fajla usled custom file inputa u glumac formi
$(document).ready(function() {
    $('#choose-actor-image').click(function() {
      $('#actor-image').click();
    });

    $("#actor-image").change(()=>{
        $("#actor-image-input-msg").val($("#actor-image").val());
    })
  });
  //------------------------------------------------------------------------------
//validacija i slanje glumac forme

$(document).ready(function() {
    $('#actor-form').submit(function(event) {        
    event.preventDefault(); 

    const basic_regex = /^(?=.{1,255}$)\w{2,}/;

    actor_name = $('#actor-name');
    actor_image = $('#actor-image');

    if(!basic_regex.test(actor_name.val())){
      actor_name.addClass('is-invalid actor-form-stop'); 
    }else{ 
        actor_name.removeClass('is-invalid actor-form-stop');  
    }   

    if(!actor_image.val()){
        actor_image.addClass('is-invalid actor-form-stop');
        $('#actor-image-msg').html("Izaberite sliku glumca.");
    }else if(!(actor_image.val().endsWith(".png") || actor_image.val().endsWith(".jpg") || actor_image.val().endsWith(".jpeg"))){
        actor_image.addClass('is-invalid actor-form-stop');
        $('#actor-image-msg').html("Dozvoljene ekstenzije: .png/.jpg/.jpeg.");
    }else if((actor_image[0].files[0].size/1024/1024).toFixed(1) >=3){ 
        let size = (actor_image[0].files[0].size/1024/1024).toFixed(1);
        actor_image.addClass('is-invalid actor-form-stop');
        $('#actor-image-msg').html(`Veličina slike prelazi 3MB (${size}MB).`);
    }else{
        actor_image.removeClass('is-invalid actor-form-stop');
    }

    const validated = $('.actor-form-stop');
    if (validated.length != 0) return;  
    
    let fd = new FormData(this);
    $.ajax({        
        url: "/actor",
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
                }
              }, false);
            }
            return xhr;
          },
        success: response=>{
            $('#loader').css({'display':'none'});
            if (response.status == '200') {
                successAlert("GLUMAC JE USPEŠNO KREIRAN!", "", "", false);
                $(this)[0].reset();
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