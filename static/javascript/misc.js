//------------------------------------------------------------------------------
//logika za menjanje sadrzaja paragrafa

const quotes = [  [`"You either die a hero or you live long enough to see yourself become the villain."`, `- The Dark Knight`],
                  [`"Let's just say I'm Frankenstein's monster...and I'm looking for my creator."`, `- X-Men: First Class`],
                  [`"Somewhere along the way, I lost a step. I got sloppy. dulled my own edge. maybe I went and did the worst crime of all... I got civilized."`, `- Riddick`],
                  [`"I had strings, but now I'm free..."`, `- Avengers: Age of Ultron`],
                  [`"I am the master of my fate, I am the captain of my soul."`, `- Invictus`],
                  [`"I weep for those who stand in my way, cos they are beyond mercy of god."`, `- xxxy4`],
                  [`"Dread it? run from it? destiny arrives all the same, and now it's here. or should I say: I am."`, `- Avengers: Infinity War`],
                  [`"Walk like a king or walk like you don't give f*ck, who's the king."`, `- Peaky Blinders`],
                  [`"When you pray for rain, you gotta deal with the mud too."`, `- The Equalizer`],
                  [`"Laugh like no one's listening, dance like you're standing on the corpses of your enemies."`, `- Lucifer`],
                  [`"Remember today, little brother. today, life is good."`, `- The Lord of the Rings`]
                ];
  
  const quote = $('#quote');
  const quote_from = $('#quote-from-hover');
  let counter = 0;
  
  setInterval(() => {
    if (++counter >= quotes.length) counter = 0;
    quote.removeClass('active');
    quote_from.removeClass('active');
    setTimeout(() => {
      quote.html(quotes[counter][0]);
      quote_from.html(quotes[counter][1]);      
      quote.addClass('active');
      quote_from.addClass('active');
    }, 500);
  }, 7000);
//------------------------------------------------------------------------------
//Logika za informativne modale

$(document).ready(function() {
    $('#refresh-page').click(function() {
        location.reload(true);
    });
    $('#cancel-page').click(function() {
        location.href = "/";
    });
});

function errorAlert(response){
        let modal = $('#staticBackdropErrorAlert');
        let modalTrigger = new bootstrap.Modal(modal);
        modalTrigger.show();
        console.error(response);
}
function successAlert(header, message, additional_message, refresh){
        let modal = $('#staticBackdropSuccessAlert');
        let modalTrigger = new bootstrap.Modal(modal);
        modalTrigger.show();
        $('#message-header').text(header);
        $('#message-text').text(message);
        $('#additional-message-text').text(additional_message);
        if(refresh){
            $('#success-confirm').click(function() {
                location.reload(true);
            });
        }else{
            $('#success-confirm').off('click');
        }
}
//------------------------------------------------------------------------------
//Iz nekog razloga mora da se doda ovaj kod.?
$(document).ready(function() {
    $(function () {
      $('[data-bs-toggle="tooltip"]').tooltip()
    })
});
//------------------------------------------------------------------------------