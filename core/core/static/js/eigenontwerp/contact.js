

const afbeeldingen = ["img/atelier1.jpg", "img/atelier2.jpg", "img/ateliers3.jpg"];
//const afbeeldingen = ["{% static 'img/atelier1.jpg' %}", "{% static 'img/atelier2.jpg' %}", "{% static 'img/atelier3.jpg' %}"];
let index = 0 ;
//alert ("start van interval")

setInterval (() =>{
    index = (index + 1 ) % afbeeldingen.length;
    foto.src = afbeeldingen[index];}
,4000); // elke 4 seconden wisselen 

if (foto.src.includes("img/atelier1.jpg")){
    alert ("foto include")
}else {
    foto.src('img/atelier1.jpg')
}

//
// // const foto = document.getElementById("foto_contact");
// console.log("contact pagina")
// foto.addEventListener('click', function(){
//    if (foto.src.includes("atelier1.jpg")){
//        foto.src = "img/atelier2.jpg";
//    }else{
//        foto.src = "img/atelier1.jpg";
//   }
//  })