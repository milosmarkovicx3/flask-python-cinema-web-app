//------------------------------------------------------------------------------
//prikaz naziva fajla usled custom file inputa u film formi
$(document).ready(function() {
    $('#choose-poster').click(function() {
      $('#poster').click();
    });

    $("#poster").change(()=>{
        $("#poster-input-msg").val($("#poster").val());
    })
  });
//------------------------------------------------------------------------------
//validacija i slanje film forme

$(document).ready(function() {
    $('#movie-form').submit(function(event) {        
    event.preventDefault(); 

    const basic_regex = /^(?=.{1,255}$)\w{1,}/;

    title = $('#title');
    year = $('#year');
    duration = $('#duration');
    rating = $('#rating');
    votes = $('#votes');
    poster = $('#poster');
    trailer = $('#trailer');
    actor_search = $('#actor-search');
    genre_search = $('#genre-search');

    if(!title_exist)
    if(!basic_regex.test(title.val())){
      title.addClass('is-invalid movie-form-stop'); 
      $('#title-msg').html('Unesite naziv filma.');
    }else{ 
        title.removeClass('is-invalid movie-form-stop');  
    }   

    if(basic_regex.test(year.val())){
        year.removeClass('is-invalid movie-form-stop');
    }else{
        year.addClass('is-invalid movie-form-stop');
    }

    if(basic_regex.test(duration.val())){
        duration.removeClass('is-invalid movie-form-stop');
    }else{
        duration.addClass('is-invalid movie-form-stop');
    }

    if(basic_regex.test(rating.val())){
        rating.removeClass('is-invalid movie-form-stop');
    }else{
        rating.addClass('is-invalid movie-form-stop');
    }

    if(basic_regex.test(votes.val())){
        votes.removeClass('is-invalid movie-form-stop');
    }else{
        votes.addClass('is-invalid movie-form-stop');
    }

    if(basic_regex.test(trailer.val())){
        trailer.removeClass('is-invalid movie-form-stop');
    }else{
        trailer.addClass('is-invalid movie-form-stop');
    }    

    if(!poster.val()){
        poster.addClass('is-invalid movie-form-stop');
        $('#poster-msg').html("Izaberite poster filma.");
    }else if(!(poster.val().endsWith(".png") || poster.val().endsWith(".jpg") || poster.val().endsWith(".jpeg"))){
        poster.addClass('is-invalid movie-form-stop');
        $('#poster-msg').html("Dozvoljene ekstenzije: .png/.jpg/.jpeg.");
    }else if((poster[0].files[0].size/1024/1024).toFixed(1) >=3){ 
        let size = (poster[0].files[0].size/1024/1024).toFixed(1);
        poster.addClass('is-invalid movie-form-stop');
        $('#poster-msg').html(`Veličina postera prelazi 3MB (${size}MB).`);
    }else{
        poster.removeClass('is-invalid movie-form-stop');
    }

    if(actors_added_to_movie.size == 0){
        actor_search.addClass('is-invalid movie-form-stop');
        $('#actors-list-msg').html('Izaberite glumce za dati film.');        
    }else{ 
        actor_search.removeClass('is-invalid movie-form-stop'); 
    }
    for (let [key, value] of actors_added_to_movie) {
        if (value === '') {
            actor_search.addClass('is-invalid movie-form-stop');
            $('#actors-list-msg').html('Niste uneli sve uloge za glumce.');
        }
    }

    if(genres_added_to_movie.size == 0){
        genre_search.addClass('is-invalid movie-form-stop');       
    }else{ 
        genre_search.removeClass('is-invalid movie-form-stop'); 
    }    

    const validated = $('.movie-form-stop');
    if (validated.length != 0) return;  
    
    let fd = new FormData(this);
    fd.append('genres', JSON.stringify(Array.from(genres_added_to_movie)));
    fd.append('actors', JSON.stringify(Array.from(actors_added_to_movie)));
    $.ajax({        
        url: "/movie",
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
                alert("Film je uspešno kreiran.");
                $(this)[0].reset();
                actors_added_to_movie = new Map();
                genres_added_to_movie = new Map();
            }else{
                alert("Došlo je do greške prilikom kreiranja filma." + response.description);
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
// provera za već postojeći naziv filma tokom samog dodavanja

var title_exist = false;

$(document).ready(function() {
    const $title_input = $('#title');
    const title_msg = $('#title-msg');  
    
    
    $title_input.on('input', function() {
      const title = $title_input.val();      
      
      $.ajax({
        url: `/movie/${title}/title`,
        method: 'get',
        success: function(response) {
          if (response.status == '200') {
            title_msg.html('Unet naziv filma već postoji u sistemu.');
            $title_input.addClass('is-invalid movie-form-stop'); 
            title_exist = true;    
          }else if (title_exist){
            title_msg.html('Unesite naziv filma.');
            $title_input.removeClass('is-invalid movie-form-stop'); 
            title_exist = false;
          }
        },
        error: function(error) {
          console.error(error);
        }
      });
    });
  });
//------------------------------------------------------------------------------
// pretraga i dodavanje glumaca u formi film

var actors_added_to_movie = new Map();

$(document).ready(function() {
    const $actors_input = $('#actor-search');
    const actors_list  = $('#actors-list');
    
    $actors_input.on('input', function() {
      const actors_search = $actors_input.val();      
      if(actors_search == ''){
        actors_list.html('');
        return;
      }
      
      $.ajax({
        url: `actor/?column=name&value=${actors_search}&max=5`,
        method: 'get',
        success: function(response) {
            actors_list.html('');  
            if (response.status == '200') {   
                for (let i = 0; i < response.item.length; i++) {
                    actors_list.append(`
                        <div class="w-100 container row p-0 m-0 border-bottom border-black">
                            <div class="col-sm-1 p-0 border-start border-end border-black">                           
                                <img class="w-100" src="/resource/actor-images/${response.item[i].image}">
                            </div>
                            <div class="col-sm-10 p-0 d-flex align-items-center">                           
                                <label id="actor-name-${response.item[i].id}" for="actor-${response.item[i].id}" class="h5 m-0 ms-3">${response.item[i].name}</label>   
                                <input type="text" id="actor-${response.item[i].id}-role" class="bg-dark m-0 w-100 h-100" placeholder="npr. Obi-Wan-Kenobi" style="display: none;">                 
                            </div>    
                            <div class="col-sm-1 p-0  d-flex align-items-center justify-content-center border-start border-end border-black">                           
                                <input type="checkbox" id="actor-${response.item[i].id}" class="bg-secondary form-check-input m-0 w-50 h-50" value="${response.item[i].id}">
                            </div>
                        </div>
                        `);

                        $(`#actor-${response.item[i].id}`).change(()=>{
                            if($(`#actor-${response.item[i].id}`).is(":checked")){                
                                actors_added_to_movie.set(response.item[i].id, '');
                                $(`#actor-${response.item[i].id}-role`).css({"display": "flex"});
                                $(`#actor-name-${response.item[i].id}`).css({"display": "none"});
                            }else{
                                actors_added_to_movie.delete(response.item[i].id);
                                $(`#actor-${response.item[i].id}-role`).val('');
                                $(`#actor-${response.item[i].id}-role`).css({"display": "none"});
                                $(`#actor-name-${response.item[i].id}`).css({"display": "flex"});
                            }
                        })
                        $(`#actor-${response.item[i].id}-role`).change(()=>{
                            actors_added_to_movie.set(response.item[i].id, $(`#actor-${response.item[i].id}-role`).val());
                        })

                        if(actors_added_to_movie.has(response.item[i].id)){
                            $(`#actor-${response.item[i].id}`).prop("checked", true);
                            $(`#actor-${response.item[i].id}-role`).css({"display": "flex"});
                            $(`#actor-name-${response.item[i].id}`).css({"display": "none"});
                            $(`#actor-${response.item[i].id}-role`).val(actors_added_to_movie.get(response.item[i].id));
                        }
                }
            }
        },
        error: function(error) {
          console.error(error);
        }
      });
    });
  });
//------------------------------------------------------------------------------
// pretraga i dodavanje žanrova u formi film

var genres_added_to_movie= new Map();

$(document).ready(function() {
    const $genres_input = $('#genre-search');
    const genres_list  = $('#genres-list');
    
    $genres_input.on('input', function() {
      const genres_search = $genres_input.val();      
      if(genres_search == ''){
        genres_list.html('');
        return;
      }
      
      $.ajax({
        url: `genre/?column=name&value=${genres_search}&max=5`,
        method: 'get',
        success: function(response) {
            genres_list.html('');  
            if (response.status == '200') {   
                for (let i = 0; i < response.item.length; i++) {
                    genres_list.append(`
                        <div class="w-100 container row p-0 m-0 border-bottom border-black">
                            <div class="col-sm-1 p-0 border-start border-end border-black">                           
                                <img class="w-100" src="/resource/genre-images/${response.item[i].image}">
                            </div>
                            <div class="col-sm-10 p-0 d-flex align-items-center">                           
                                <label id="genre-name-${response.item[i].id}" for="genre-${response.item[i].id}" class="h5 m-0 ms-3">${response.item[i].name}</label>   
                            </div>    
                            <div class="col-sm-1 p-0  d-flex align-items-center justify-content-center border-start border-end border-black">                           
                                <input type="checkbox" id="genre-${response.item[i].id}" class="bg-secondary form-check-input m-0 w-50 h-50" value="${response.item[i].id}">
                            </div>
                        </div>
                        `);

                        $(`#genre-${response.item[i].id}`).change(()=>{
                            if($(`#genre-${response.item[i].id}`).is(":checked")){                
                                genres_added_to_movie.set(response.item[i].id, 'X');
                            }else{
                                genres_added_to_movie.delete(response.item[i].id);
                            }
                        })

                        if(genres_added_to_movie.has(response.item[i].id)){
                            $(`#genre-${response.item[i].id}`).prop("checked", true);
                        }
                }
            }
        },
        error: function(error) {
          console.error(error);
        }
      });
    });
  });
//------------------------------------------------------------------------------
//dopunjavanje nedostataka reset dugmentu na film formi

$(document).ready(function() {
    $('#reset-movie-form').click(function() {
        actors_added_to_movie = new Map();
        genres_added_to_movie = new Map();
        $('#actors-list').html('');
        $('#genres-list').html('');
      });
});
//------------------------------------------------------------------------------
