//-------------------------------------------------------------------------------------------------------------------------
//funkcija za otkazivanje rezervacija

function deleteReservation(id){
    let fd = new FormData();
    fd.append('csrf_token', $('#csrf_token').val());
    fd.append('value', id);

    $.ajax({
        url: '/reservation',
        type: "delete",
        data: fd,
        contentType: false,
        processData: false,
        success: response=>{
            if (response.status == '200') {
                successAlert("REZERVACIJA JE USPEŠNO OTKAZANA!", "", "", true);
            }else{
                errorAlert(response);
            }
        },
        error: function(error) {
            errorAlert(response);
        }
    });
}
//-------------------------------------------------------------------------------------------------------------------------