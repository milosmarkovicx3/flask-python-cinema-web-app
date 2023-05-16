//-------------------------------------------------------------------------------
//glasanje preko zvezdica za recenziju

let remember_position = 0;

$(".star-hover-effect").hover(
  function() {
      $(this).prevAll().addBack().css("color", "rgb(209, 209, 15)");
  },
  function() {
    if (!remember_position){
        $(this).prevAll().addBack().css("color", "");
    }else{
        if($(this).prevAll().length > remember_position)
            $(".not-selected").css("color", "");
    }
  }
).click(function() {
  remember_position = $(this).prevAll().length;
  $('#vote').text(remember_position + 1)
  $(this).prevAll().addBack().css("color", "rgb(209, 209, 15)");
  $(this).nextAll().css("color", "");  
  $(this).prevAll().addBack().removeClass("not-selected");
  $(this).prevAll().addBack().addClass("selected");
  $(this).nextAll().removeClass("selected");
  $(this).nextAll().addClass("not-selected");
});
//-------------------------------------------------------------------------------
//validacija i slanje forme za recenziju

$(document).ready(function() {
    $('#review-form').submit(function(event) {        
    event.preventDefault(); 

    const basic_regex = /^(?=.{1,2048}$)\w{2,}/;
    comment = $('#comment');
    review_msg = $('#review-msg');

    if(!basic_regex.test(comment.val())){
        review_msg.text('Unesite komentar.')
        comment.addClass('is-invalid review-form-stop');
    }else if(!remember_position){
        review_msg.text('Izaberite ocenu.')
        comment.addClass('is-invalid review-form-stop');
    }else{
        comment.removeClass('is-invalid review-form-stop'); 
    }
    
    const validated = $('.review-form-stop');
    if (validated.length != 0) return; 

    let fd = new FormData(this);
    fd.append("rating", remember_position + 1);

    $.ajax({        
        url: "/review",
        type: "post",
        data: fd,
        contentType: false,
        processData: false,
        success: response=>{
            if (response.status == '200') {
                successAlert("RECENZIJA JE USPEŠNO POSLATA!", "", "", true);
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