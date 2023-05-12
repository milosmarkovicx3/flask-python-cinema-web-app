//-------------------------------------------------------------------------------------------------------------------------
//menjanje ikonica pri odabiru sedišta i pamćenje lokacije
let selected = [];

function selectSeat(element, id, type, image){
    if (type == 3 || type == 4 || type == 6) return;

    if (selected[0]) $(`#${selected[0]}`).attr('src', `${$('#root_path').val()}${selected[2]}`);

    $(element).attr('src', `${$('#root_path').val()}${type == 5 ? 'love_selected.png' : 'selected.png'}`);

    selected = [id, type, image];

    if(type == 2){
        $('#ticket-info').text('1x600rsd')
    }else if(type == 5){
        $('#ticket-info').text('2x400rsd')
    }else{
        $('#ticket-info').text('1x400rsd')
    }
}
//-------------------------------------------------------------------------------------------------------------------------
//funkcija za rezervaciju izabranih sedišta

$(document).ready(function() {
    $('#reservation-form').submit(function(event) {
    event.preventDefault();

    let fd = new FormData(this);
    fd.append('seat_id', selected[0]);

    $.ajax({        
        url: "/reservation",
        type: "post",
        data: fd,
        contentType: false,
        processData: false,
        success: response=>{
            if (response.status == '200') {
                alert("Rezervacija je uneta u sistem.");
                location.reload(true);
            }else{
                alert("Došlo je do greške prilikom kreiranja rezervacije." + response.description);
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
//-------------------------------------------------------------------------------------------------------------------------