document.getElementById("btnBuscarResultado").addEventListener("click",function(){
    var filtro = document.getElementById("valorCamara")
    var obtenerValorSelect = filtro.value.toLowerCase();
    
   $.ajax({ 
        //url: '/llamar_apod',
        url: '/llamar_apod/'+obtenerValorSelect,
        type: 'POST',
        //data: {camera: obtenerValorSelect.toLowerCase()},
        success: function(response){
            if (response.photos && response.photos.length > 0) {
                var contenido="";
                for (var index = 0; index < response.photos.length; index++) {
                    var imgsrc = response.photos[index].img_src;
                    contenido += "<div class='col mb-4' ><img src='"+imgsrc+"' class='img-fluid'></div>";
                } 
                document.getElementById("divFiltrarBusquedaFotosRover").innerHTML = contenido;
            }else{
                document.getElementById("divFiltrarBusquedaFotosRover").innerHTML = '<div class="alert alert-danger" role="alert">No se encontraron resultados</div>';
            }
        },
        error: function(error){
            console.log(error);
        }   
   });    

});