

const foto = document.getElementById("foto_contact");
//print(foto.src)
const afbeeldingen = ["/img/atelier1.jpg", "/img/atelier2.jpg", "/img/ateliers3.jpg"];
//const afbeeldingen = ["{% static 'img/atelier1.jpg' %}", "{% static 'img/atelier2.jpg' %}", "{% static 'img/atelier3.jpg' %}"];
let index = 0 ;
//alert ("start van interval")

setInterval (() =>{
    index = (index + 1 ) % afbeeldingen.length;
    foto.src = afbeeldingen[index];}
,4000); // elke 4 seconden wisselen 
alert(foto.src)

if (foto.src.includes("/img/atelier1.jpg")){
   // alert ("foto include")
    foto.src('/img/atelier2.jpg')
}else {
    foto.src('/img/atelier1.jpg')
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

///


const atelier1 = "{% static 'img/atelier1.jpg' %}";
const atelier2 = "{% static 'img/atelier2.jpg' %}";

document.getElementById("foto_contact").src = atelier1;
console.log("contact pagina")

foto.addEventListener('click', function(){
    console.log("op foto geklikt")
    if (foto.src.includes("atelier1.jpg")){
        console.log("foto atelier1 wordt weergegeven")
        //foto.src = atelier2;
        //foto.src = foto.dataset.src;
        foto.src = "{% static 'img/atelier2.jpg' %}";
        //alert(foto.src)
    }else{
        console.log("foto atelier2 wordt weergegeven")
        document.getElementById("foto_contact").src = atelier1;
        //foto.src = "{% static 'img/atelier1.jpg' %}";
       // alert(foto.src) }
 }})