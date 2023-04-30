//------------------------------------------------------------------------------
//logika za menjanje sadrzaja paragrafa namenjenom za citate
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

const quotesParagraph = document.querySelector('#movie-quotes');
let counter = 0;

setInterval(() => {
  if (++counter >= quotes.length) counter = 0;
  quotesParagraph.classList.remove('active');
  setTimeout(() => {
    quotesParagraph.innerHTML = quotes[counter];
    quotesParagraph.classList.add('active');
  }, 500);
}, 7000);
//------------------------------------------------------------------------------

//------------------------------------------------------------------------------
//logika za prikazivanje(toggle) lozinke u formi za registraciju i prijavu
const registerIcon = document.querySelector('#register-show-passwd');
const registerPasswd = document.querySelector('#register-passwd');

registerIcon.addEventListener('click', () => {
	registerPasswd.type = registerPasswd.type === 'password' ? 'text' : 'password';
	if (registerIcon.classList.contains('fi-rs-crossed-eye')){
	    registerIcon.classList.remove('fi-rs-crossed-eye');
	    registerIcon.classList.add('fi-rs-eye');
	}else{
        registerIcon.classList.remove('fi-rs-eye');
	    registerIcon.classList.add('fi-rs-crossed-eye');
	}
})

const loginIcon = document.querySelector('#login-show-passwd');
const loginPasswd = document.querySelector('#login-passwd');

loginIcon.addEventListener('click', () => {
	loginPasswd.type = loginPasswd.type === 'password' ? 'text' : 'password';
	if (loginIcon.classList.contains('fi-rs-crossed-eye')){
	    loginIcon.classList.remove('fi-rs-crossed-eye');
	    loginIcon.classList.add('fi-rs-eye');
	}else{
        loginIcon.classList.remove('fi-rs-eye');
	    loginIcon.classList.add('fi-rs-crossed-eye');
	}
})
//------------------------------------------------------------------------------


//------------------------------------------------------------------------------
function validationRegister(){

    let username = document.getElementById("register-username").value;
    let email = document.getElementById("register-email").value;
    let passwd = document.getElementById("register-passwd").value;
    let first_name = document.getElementById("register-first-name").value;
    let last_name = document.getElementById("register-last-name").value;
    let conditions = document.getElementById("register-conditions").checked;
    const email_regex = /^(?=.{1,255}$)\w+(\w|((?<!\.)\.))*\w+\@\w+(\w|((?<!\.)\.))*\.\w{2,4}$/;
    const passwd_regex = /^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W]).{5,50}$/;
    const basic_regex = /^(?=.{1,255}$)\w{2,}/;

    if(basic_regex.test(username)){ document.getElementById("register-username-lbl").innerHTML="Korisničko ime"; }
    else{ document.getElementById("register-username-lbl").innerHTML="Korisničko ime<span class='text-danger float-end xyz'>*pogrešan unos<span>"; }
    console.log(basic_regex.lastIndex);
    if(email_regex.test(email)){ document.getElementById("register-email-lbl").innerHTML="Email adresa"; }
    else{ document.getElementById("register-email-lbl").innerHTML="Email adresa<span class='text-danger float-end xyz'>*pogrešan unos<span>"; }

    if(passwd_regex.test(passwd)){ document.getElementById("register-passwd-lbl").innerHTML="Lozinka"; }
    else{ document.getElementById("register-passwd-lbl").innerHTML="Lozinka<span class='text-danger float-end xyz'>*pogrešan unos<span>"; }

    if(basic_regex.test(first_name)){ document.getElementById("register-first-name-lbl").innerHTML="Ime"; }        
    else{ document.getElementById("register-first-name-lbl").innerHTML="Ime<span class='text-danger float-end xyz'>*pogrešan unos<span>"; }
    console.log(basic_regex.lastIndex);
    if(basic_regex.test(last_name)){ document.getElementById("register-last-name-lbl").innerHTML="Prezime"; }        
    else{ document.getElementById("register-last-name-lbl").innerHTML="Prezime<span class='text-danger float-end xyz'>*pogrešan unos<span>"; }
    console.log(basic_regex.lastIndex);
    let lbl_text = `Prihvatam <a href="" class="text-danger-emphasis text-decoration-none">politiku privatnosti</a> i
                    <a href="" class="text-danger-emphasis text-decoration-none">uslove korišćenja</a>`; 
    if(conditions){
        document.getElementById("register-conditions-lbl").innerHTML= lbl_text;        
    }else{ document.getElementById("register-conditions-lbl").innerHTML= lbl_text+"<span class='text-danger float-end xyz'>*pogrešan unos<span>"; }

    let success = document.querySelectorAll('.xyz');

    if(success.length == 0){
        document.getElementById('register-close').click();
        return true;
    } 
    return false;
}
//------------------------------------------------------------------------------