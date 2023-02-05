let actors=[];
let actorsSelected=[];
let genres=[];
let genresSelected=[];
let movies=[];
function getActors(){$.post("/actors/",  response=>{actors=response;})}
function getGenres(){$.post("/genres/",  response=>{genres=response;})}
function getMovies(){$.post("/movies/",  response=>{movies=response;})}
getActors();
getGenres();
getMovies();
//--------------------------------------------------------------------------------------------------------------
$("#actorsSearch").keyup(()=>{
    $("#actorsDatabase").text('');
    let counter = 0;
    let val = $("#actorsSearch").val();
    for(let x of actors){        
        if(x[1].toLowerCase().includes(val)){
            if(counter++==4){break;}
            $("#actorsDatabase").append(`
                <div class="w-100 h-38px"> 
                    <img src="static/resources/actors-images/${x[2]}"  class="w-38px"/>
                    <label id="actor-name-${x[0]}" for="actor-${x[0]}" class="lbl-actor align-center">${x[1]}</label>
                    <input id="actor-${x[0]}-role" name="actor-${x[0]}-role" type="text" placeholder="npr. Obi-Wan-Kenobi"> 
                    <input id="actor-${x[0]}" type="checkbox" value="${x[0]}" class="w-38px">
                </div>
            `);
            $(`#actor-${x[0]}`).change(()=>{
                if($(`#actor-${x[0]}`).is(":checked")){                
                    actorsSelected.push(x);
                    $(`#actor-${x[0]}-role`).css({"display": "flex"});
                    $(`#actor-name-${x[0]}`).css({"display": "none"});
                }else{
                    actorsSelected=actorsSelected.filter(actor=>actor[0]!=x[0]);
                    $(`#actor-${x[0]}-role`).css({"display": "none"});
                    $(`#actor-name-${x[0]}`).css({"display": "flex"});
                }
            })
            $(`#actor-${x[0]}-role`).change(()=>{
                x[3]=$(`#actor-${x[0]}-role`).val();
            })
        }
    }
    for(let x of actorsSelected){
        $(`#actor-${x[0]}-role`).css({"display": "flex"});
        $(`#actor-name-${x[0]}`).css({"display": "none"});
        $(`#actor-${x[0]}-role`).val(x[3]);
        $(`#actor-${x[0]}`).prop("checked", true);
    }
});

$("#genresSearch").keyup(()=>{
    $("#genresDatabase").text('');
    let counter = 0;
    let val = $("#genresSearch").val();
    for(let x of genres){        
        if(x[1].toLowerCase().includes(val)){
            if(counter++==4){break;}
            $("#genresDatabase").append(`
                <div class="w-100 h-38px"> 
                    <img src="static/resources/genres-images/${x[2]}"  class="w-38px"/>
                    <label id="genre-name-${x[0]}" for="genre-${x[0]}" class="lbl-genre align-center">${x[1]}</label>
                    <input id="genre-${x[0]}" type="checkbox" value="${x[0]}" class="w-38px">
                </div>
            `);
            $(`#genre-${x[0]}`).change(()=>{
                if($(`#genre-${x[0]}`).is(":checked")){                
                    genresSelected.push(x);
                }else{
                    genresSelected=genresSelected.filter(genre=>genre[0]!=x[0])
                }
            })
        }
    }
    for(let x of genresSelected){
        $(`#genre-${x[0]}`).prop("checked", true);
    }
});
//--------------------------------------------------------------------------------------------------------------
$("#posterFile").change(()=>{ $("#poster").val($("#posterFile").val());})
$("#actorFile").change(()=>{ $("#actorImage").val($("#actorFile").val());})
$("#genreFile").change(()=>{ $("#genreImage").val($("#genreFile").val());})
//--------------------------------------------------------------------------------------------------------------
// if(2 < len){$('#title')[0].setCustomValidity('Morate uneti više od 2 karaktera!');}

function len(id, errorId, min, max){
    let val = $(`#${id}`).val().trim().length;
    if(val>=min && val<=max){$(`#${errorId}`).css({"display":"none"});}
    else{$(`#${errorId}`).css({"display":"inline"});return false;}
    return true;
}
function pic(id, errorId){
    let picture = $(`#${id}`).val();
    if(picture){
        $(`#${errorId}`).css({"display":"none"});
        if(!(picture.endsWith(".png") || picture.endsWith(".jpg") || picture.endsWith(".jpeg"))){
            $(`#${errorId}`).css({"display":"inline"}); bool=false;
            $(`#${errorId}`).text('*Loša ekstenzija postera!*');
            return false;
        }else{
            let size = ($(`#${id}`)[0].files[0].size/1024/1024).toFixed(1);
            if(size>2){
                $(`#${errorId}`).css({"display":"inline"}); 
                $(`#${errorId}`).text(`*Veličina postera (${size}MB) je veća od 2MB!*`);
                return false;
            }
        }
    }else{      
        $(`#${errorId}`).css({"display":"inline"}); 
        $(`#${errorId}`).text('*Loš unos, pokušajte opet*');
        return false;
    }
    return true;
}
function ajax(fd, path){
    return new Promise((resolve, reject)=>{
    $.ajax({
        type: "post", 
        url: path, 
        data: fd, 
        contentType: false, 
        processData: false,
        success: response=>{
            if(response=="Uspešan unos u bazu!"){   
                alert(response);             
            }else{
                alert("Došlo je do greške prilikom obrade zahteva na strani servera!\nZa detaljni opis greške pogledajte konzolni ispis!");
                console.log(response);
            }            
            resolve();
        },
        error: () => {
            alert("Došlo je do greške prilikom slanja zahteva!");
            reject();
        }
    });});
}
//--------------------------------------------------------------------------------------------------------------
$("#formMovie").on("submit", ev=>{
    ev.preventDefault();
    let bool = true;

    if(!len("title","error-title",2,100)) bool=false;
    if(!len("year","error-year",4,4)) bool=false;
    if(!len("duration","error-duration",2,6)) bool=false;
    if(!len("rating","error-rating",2,6)) bool=false;
    if(!len("votes","error-votes",2,6)) bool=false;
    
    if(!pic("posterFile","error-poster")) bool=false;
   
    if(genresSelected.length){$("#error-genresSearch").css({"display":"none"});}
    else{$("#error-genresSearch").css({"display":"inline"}); bool=false;}
    if(actorsSelected.length){$("#error-actorsSearch").css({"display":"none"});}
    else{$("#error-actorsSearch").css({"display":"inline"}); bool=false;}

    if(!bool)return false;
    
    let fd = new FormData($('#formMovie')[0]);
    let genresId;
    genresSelected.forEach(element => {genresId+=element[0]+":";});
    fd.append('genresId',genresId);
    let actorsId, actorsRoles;
    actorsSelected.forEach(element => {actorsId+=element[0]+":"; actorsRoles+=element[3]+":";});
    fd.append('actorsId',actorsId);
    fd.append('actorsRoles',actorsRoles);    
    ajax(fd, "/insertMovie").then(()=>{
        setTimeout(()=>{$('#formMovie')[0].reset()},1000);
    });
}) 
$("#formActor").on("submit", ev=>{
    ev.preventDefault();
    let bool = true;

    if(!len("name","error-name",6,100)) bool=false;
    if(!pic("actorFile","error-actorImage")) bool=false;
    if(!bool)return false;
    
    let fd = new FormData($('#formActor')[0]);
    ajax(fd, "/insertActor").then(()=>{
        getActors();
        setTimeout(()=>{$('#formActor')[0].reset()},1000);
    });
}) 
$("#formGenre").on("submit", ev=>{
    ev.preventDefault();
    let bool = true;

    if(!len("genre","error-genre",3,100)) bool=false;
    if(!pic("genreFile","error-genreImage")) bool=false;
    if(!bool)return false;
    
    let fd = new FormData($('#formGenre')[0]);
    ajax(fd, "/insertGenre").then(()=>{
        getGenres();
        setTimeout(()=>{$('#formGenre')[0].reset()},1000);
    });
}) 
//--------------------------------------------------------------------------------------------------------------
function loadInstances(){
    $(".field").css({"display":"none"});
    let option = $("#option").val();
    if(option=="delete"){
        $("#instances").css({"display":"inline"});
        $("#instances").text('');
        let category = $("#category").val();
        if(category=="Movie"){
            for(let x of movies){$("#instances").append(`<option value="${x[0]}">${x[1]}</option>`);}
        }else if(category=="Actor"){
            for(let x of actors){$("#instances").append(`<option value="${x[0]}">${x[1]}</option>`); if(x[1]=='formGenre')console.log("kurcina");}
        }else if(category=="Genre"){
            for(let x of genres){$("#instances").append(`<option value="${x[0]}">${x[1]}</option>`);}
        }
    }else{
        $("#instances").css({"display":"none"});
    }
}
$("#option").change(loadInstances);
$("#category").change(loadInstances);
//--------------------------------------------------------------------------------------------------------------
function request(){
    let option = $("#option").val();
    let category = $("#category").val();
    let instanceId = $("#instances").val();    

    if(option=="insert"){
        if(category=="Movie"){
            $("#fieldMovie").css({"display":"flex"}); 
        }else if(category=="Actor"){
            $("#fieldActor").css({"display":"flex"});
        }else if(category=="Genre"){
            $("#fieldGenre").css({"display":"flex"}); 
        }     
    }else if(option=="delete"){
        $.post(`/delete${category}`, {uuid: instanceId}).done(response=>{
            alert(response);
            if(category=="Movie"){getMovies();}
            else if(category=="Actor"){getActors();}
            else if(category=="Genre"){getGenres();} 
            setTimeout(loadInstances,500);
        }).fail(() => {alert("Došlo je do greške prilikom slanja zahteva!"); });
    }
}
//--------------------------------------------------------------------------------------------------------------
