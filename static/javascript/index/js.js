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