let title = document.getElementById("header");
let paragraph = document.getElementById("paragraph");

title.style.color = "blue";
title.style.fontSize = "32px";
title.style.fontFamily = "Georgia";

paragraph.style.color = "green";
paragraph.style.fontSize = "20px";
paragraph.style.fontFamily = "Arial";

console.log("სათაური:", title);
console.dir(title); 

console.log("პარაგრაფი:", paragraph);
console.dir(paragraph);

// document - წარმოადგენს მთელ HTML დოკუმენტს JavaScript-ში
// DOM (Document Object Model) - არის HTML დოკუმენტის სტრუქტურა, რომელთანაც შეგვიძლია ურთიერთობა ჯავასკრიპტით
// getElementById - მეთოდი რომელიც პოულობს HTML ელემენტს მისი id-ით
