const foto = document.getElementById("foto_contact");
console.log("contact pagina")

foto.addEventListener('click', function(){
    if (foto.src.includes("atelier1.jpg")){
        foto.src = "{% static 'img/atelier2.jpg' %}";
        //alert(foto.src)
    }else{
        foto.src = "{% static 'img/atelier1.jpg' %}";
       // alert(foto.src) }
 }})

