//------------------------------------------------------------------------------
//logika za menjanje sadrzaja paragrafa

const quotes = [
  `"You either die a hero or you live long enough to see yourself become the villain." - The Dark Knight`,
  `"You are the Moon of my Life. That is all I know and all I need to know. And if this is a dream, I will kill the man who tries to wake me." - Game of Thrones`,
  `"Let's just say I'm Frankenstein's monster...and I'm looking for my creator" - X-Men: First Class`,
  `"Somewhere along the way, I lost a step. I got sloppy. Dulled my own edge. Maybe I went and did the worst crime of all... I got civilized." - Riddick`,
  `"I had strings, but now I'm free..." - Avengers: Age of Ultron`,
  `"I am the master of my fate, I am the captain of my soul"<br>- Invictus`,
  `"I weep for those who stand in my way, cos they are beyond mercy of god" - M.M. 22.12.2020`,
  `"Dread it? Run from it? Destiny arrives all the same, and now it's here. Or should I say: I am." - Avengers: Infinity War`,
  `"Walk like a king or walk like you don't give f*ck, who's the king." - Peaky Blinders`,
  `"When you pray for rain, you gotta deal with the mud too."<br>- The Equalizer`,
  `"Laugh like no one's listening, dance like you're standing on the corpses of your enemies." - Lucifer`,
  `"Remember today, little brother. Today, life is good."<br>- The Lord of the Rings: The Fellowship of the Ring`
];

const quotesParagraph = $('#movie-quotes');
let counter = 0;

setInterval(() => {
  if (++counter >= quotes.length) counter = 0;
  quotesParagraph.removeClass('active');
  setTimeout(() => {
    quotesParagraph.html(quotes[counter]);
    quotesParagraph.addClass('active');
  }, 500);
}, 7000);
//------------------------------------------------------------------------------
//logika za prikazivanje(toggle) ikonice pored inputa za lozinke u formama

$(document).ready(function() {
    $('#register-show-passwd').click(function() {
        $('#register-passwd').prop('type', function(index, value) {
            return value === 'password' ? 'text' : 'password';
        });
        $('#register-show-passwd').toggleClass('fi-rs-eye fi-rs-crossed-eye');
    });

    $('#login-show-passwd').on('click', function() {
        $('#login-passwd').prop('type', function(_, type) {
            return type === 'password' ? 'text' : 'password';
        });
        $(this).toggleClass('fi-rs-crossed-eye fi-rs-eye');
    });
});
//------------------------------------------------------------------------------
// validacija za registrovanje korisnika

function validationRegister() {
    const email_regex = /^(?=.{1,255}$)\w+(\w|((?<!\.)\.))*\w+\@\w+(\w|((?<!\.)\.))*\.\w{2,4}$/;
    const passwd_regex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W]).{5,50}$/;
    const basic_regex = /^(?=.{1,255}$)\w{2,}/;

    if(!$username_exist)
    $('#register-username-lbl').html(basic_regex.test($('#register-username').val()) ? 'Korisničko ime' : `Korisničko ime<span class="text-danger float-end xyz">*pogrešan unos/format</span>`);
    if(!$email_exist)
    $('#register-email-lbl').html(email_regex.test($('#register-email').val()) ? 'Email adresa' : `Email adresa<span class="text-danger float-end xyz">*pogrešan unos/format</span>`);
    $('#register-passwd-lbl').html(passwd_regex.test($('#register-passwd').val()) ? 'Lozinka' : `Lozinka<span class="text-danger float-end xyz">*pogrešan unos/format</span>`);
    $('#register-first-name-lbl').html(basic_regex.test($('#register-first-name').val()) ? 'Ime' : `Ime<span class="text-danger float-end xyz">*pogrešan unos/format</span>`);
    $('#register-last-name-lbl').html(basic_regex.test($('#register-last-name').val()) ? 'Prezime' : `Prezime<span class="text-danger float-end xyz">*pogrešan unos/format</span>`);
    const lbl_text = `Prihvatam <a href="" class="text-danger-emphasis text-decoration-none">politiku privatnosti</a> i <a href="" class="text-danger-emphasis text-decoration-none">uslove korišćenja</a>`;
    $('#register-conditions-lbl').html($('#register-conditions').is(':checked') ? lbl_text : `${lbl_text}<span class="text-danger float-end xyz">*pogrešan unos/format</span>`);
  
    const success = $('.xyz');
    if (success.length == 0) return true;  
    return false;
  }
//------------------------------------------------------------------------------
// validacija za prijavu korisnika

  function validationLogin() {
    const basic_regex = /^(?=.{1,50}$)\w{1,}/;

    $('#login-username-lbl').html(basic_regex.test($('#login-username').val()) ? 'Korisničko ime' : `Korisničko ime<span class="text-danger float-end zyx">*pogrešan unos/format</span>`);    
    $('#login-passwd-lbl').html(basic_regex.test($('#login-passwd').val()) ? 'Lozinka' : `Lozinka<span class="text-danger float-end zyx">*pogrešan unos/format</span>`);
 
    const success = $('.zyx');
    if (success.length === 0) return true;
    return false;
  }
//------------------------------------------------------------------------------
// provera za već postojeće korisničko ime tokom registracije

var $username_exist = false;

$(document).ready(function() {
    const $username_input = $('#register-username');
    const $username_lbl = $('#register-username-lbl');  
    
    $username_input.on('input', function() {
      const username = $username_input.val();      
      
      $.ajax({
        url: `/user/${username}/username`,
        method: 'get',
        success: function(response) {
          if (response.status == '200') {
            $username_lbl.html('Korisničko ime<span class="text-danger float-end xyz">*već postoji u sistemu</span>');  
            $username_exist = true    
          }else if ($username_exist){
            $username_lbl.html('Korisničko ime'); 
            $username_exist = false
          }
        },
        error: function(error) {
          console.error(error);
        }
      });
    });
  });
//------------------------------------------------------------------------------
// provera za već postojeću email adresu tokom registracije

var $email_exist = false;

$(document).ready(function() {
    const $email_input = $('#register-email');
    const $email_lbl = $('#register-email-lbl');  
    
    
    $email_input.on('input', function() {
      const email = $email_input.val();      
      
      $.ajax({
        url: `/user/${email}/email`,
        method: 'get',
        success: function(response) {
          if (response.status == '200') {
            $email_lbl.html('Email adresa<span class="text-danger float-end xyz">*već postoji u sistemu</span>');  
            $email_exist = true    
          }else if ($email_exist){
            $email_lbl.html('Email adresa'); 
            $email_exist = false
          }
        },
        error: function(error) {
          console.error(error);
        }
      });
    });
  });
//------------------------------------------------------------------------------
