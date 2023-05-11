//-------------------------------------------------------------------------------------------------------------------------
let selected_seat_id = '';
let selected_seat_type = '';
let additional_selected_seat_id = '';
let additional_selected_seat_type = '';
let seat_type = {
    1: 'normal.png',
    2: 'vip.png',
    3: 'unavailable.png',
    4: 'disabled.png',
    5: 'love_left.png',
    6: 'love_right.png',
    7: 'reserved.png'
}
//-------------------------------------------------------------------------------------------------------------------------
//menjanje ikonica pri odabiru sedišta i pamćenje lokacije
//root_path promenljiva sačuvana unutar html script taga

function selectSeat(img, id, type){
    if (type == 3 || type == 4 || type == 7)
        return;
    if (selected_seat_id){
        $(`#${selected_seat_id}`).attr('src', `${root_path}${seat_type[selected_seat_type]}`);
        if(additional_selected_seat_id){
            $(`#${additional_selected_seat_id}`).attr('src', `${root_path}${seat_type[additional_selected_seat_type]}`);
            additional_selected_seat_id = 0
        }
    }
    if(type == 5){
        $(img).attr('src', `${root_path}selected_left.png`);
        $(`#${id+1}`).attr('src', `${root_path}selected_right.png`);
        additional_selected_seat_id = id+1;
        additional_selected_seat_type = 6
        $('#ticket-info').text('(2x400rsd)')
    }else if (type == 6){
        $(img).attr('src', `${root_path}selected_right.png`);
        $(`#${id-1}`).attr('src', `${root_path}selected_left.png`);
        additional_selected_seat_id = id-1;
        additional_selected_seat_type = 5;
        $('#ticket-info').text('(2x400rsd)')
    }else{        
        $(img).attr('src', `${root_path}selected.png`);
        $('#ticket-info').text('(1x400rsd)')
    }
    selected_seat_id = id;
    selected_seat_type = type;
}
//-------------------------------------------------------------------------------------------------------------------------
//funkcija za rezervaciju izabranih sedišta

$(document).ready(function() {
    $('#reserve-button').click(function(event) { 

    let fd = new FormData();
    fd.append('csrf_token', csrf);
    fd.append('selected_seat_id', selected_seat_id);
    fd.append('additinal_selected_seat_id', additional_selected_seat_id);
    fd.append('projection_id', projection_id);

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