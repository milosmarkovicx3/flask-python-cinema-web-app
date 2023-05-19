//-------------------------------------------------------------------------------------------------------------------------
//menjanje ikonica pri odabiru sedišta i pamćenje lokacije
let selected = [];

function selectSeat(element, id, type, image, ticket_price){
    if (type == 3 || type == 4 || type == 6) return;

    if (selected[0]) $(`#${selected[0]}`).attr('src', `${$('#root_path').val()}${selected[2]}`);

    $(element).attr('src', `${$('#root_path').val()}${type == 5 ? 'love_selected.png' : 'selected.png'}`);

    selected = [id, type, image];

    $('#ticket-info').text(ticket_price)

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
                successAlert("REZERVACIJA JE UNETA U SISTEM!", "NA MAIL VAM JE POSLATA POTVRDA O REZERVACIJI!",
                             "Ako ne vidite email odmah, molimo Vas da proverite vašu spam poštu.", true);
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
//-------------------------------------------------------------------------------------------------------------------------