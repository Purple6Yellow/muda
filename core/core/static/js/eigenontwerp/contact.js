
document.addEventListener("DOMContentLoaded", function() {
    const foto = document.getElementById("foto_contact");

    // Lees de waarde uit het data attribuut
    const nieuweUrl = foto.dataset.src;
    const oudeUrl = foto.dataset.original;

    foto.addEventListener('click', function(){
        console.log("op foto geklikt")
        if (foto.src.includes("atelier1.jpg")){
            console.log("foto atelier1 wordt weergegeven")
            // Zet de echte afbeelding als src
            foto.src = nieuweUrl;

            //foto.src = atelier2;
            //foto.src = foto.dataset.src;
            //foto.src = "{% static 'img/atelier2.jpg' %}";
            //alert(foto.src)
        }else{
            foto.src = oudeUrl;
            console.log("foto atelier2 wordt weergegeven")
            //document.getElementById("foto_contact").src = atelier1;
            //foto.src = "{% static 'img/atelier1.jpg' %}";
        // alert(foto.src) }
    }})    

let index = 0 ;
const afbeeldingen = [nieuweUrl, oudeUrl ];
setInterval (() =>{
    index = (index + 1 ) % afbeeldingen.length;
    foto.src = afbeeldingen[index];},3000); // elke 4 seconden wisselen 
    console.log("interval werkt")
});







