//-------------------------------------------------------------------------------------------------------------------------
//funkcija za otkazivanje rezervacija

function deleteReservation(id){
    let fd = new FormData();
    fd.append('csrf_token', $('#csrf_token').val());

    $.ajax({
        url: `/reservation/${id}`,
        type: "delete",
        data: fd,
        contentType: false,
        processData: false,
        success: response=>{
            if (response.status == '200') {
                alert("Rezervacija je uspešno otkazana.");
                location.reload(true);
            }else{
                alert("Došlo je do greške prilikom otkazivanja rezervacije." + response.description);
                console.log(response);
            }
        },
        error: function(error) {
            alert("Došlo je do greške prilikom slanja zahteva.");
            console.error(error);
        }
    });
}
//-------------------------------------------------------------------------------------------------------------------------