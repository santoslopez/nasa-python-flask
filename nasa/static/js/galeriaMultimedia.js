var EXTENSION_VIDEO_NASA = "~orig.mp4";
var EXTENSION_IMAGEN_NASA = "~thumb.jpg";

// array para almacenar los valores de los checkbox seleccionados
var valoresCheckbox = [];
function actualizarParametroArray() {
  valoresCheckbox = [];
  var checkboxImagenes = document.getElementById("flexCheckImagenes");
  var checkboxVideos = document.getElementById("flexCheckCheckedVideos");
  
  if (checkboxImagenes.checked) {
    valoresCheckbox.push(checkboxImagenes.value);
  }
  if (checkboxVideos.checked) {
    valoresCheckbox.push(checkboxVideos.value);
  }
}

// Desplegar error sino hay checkbox seleccionados
function validarCheckbox() {
  Swal.fire({
    icon: 'error',
    title: 'Error',
    text: 'Debes seleccionar al menos una opción del checkbox',
    footer: '<a href="">Why do I have this issue?</a>'
  })
}

// agregar eventos dependiendo de los checkbox seleccionados
document.getElementById("flexCheckImagenes").addEventListener('change',actualizarParametroArray);
document.getElementById("flexCheckCheckedVideos").addEventListener('change',actualizarParametroArray);

document.getElementById("btnFiltrarBusquedaMultimedia").addEventListener("click", function() {
    var buscarGaleria = document.getElementById("inputBuscarGaleriaMultimedia");
    // es lo que el usuario como busqueda
    var valorInput = buscarGaleria.value;
    
    actualizarParametroArray();
    // es lo que el usuario selecciona en los checkbox y se envia a python
    var parametroArregloCheckbox = valoresCheckbox;

    if (parametroArregloCheckbox==0) {
      validarCheckbox();
      return;
    }

    fetch(`/galeriaMultimediaFiltrarBusqueda/${valorInput}/${parametroArregloCheckbox}`, {
      method: 'POST'
    })
      .then(response => {
        if (response.status === 200) {
            return response.json();
        } else if (response.status === 400) {
            return response.json().then(data => { 
               throw new Error(data.error);  
            });
            //alert("error 400")
        } else {
            throw new Error('Error en la solicitud: Código de estado ' + response.status);
          }
        })
      .then(data => {
        if (data.error) {
            throw new Error(data.error);
        }

        if (data.collection && data.collection.items && data.collection.items.length > 0) {
          var items = data.collection.items;
         
          //var enlaceImagenes = [];
          
          var contenido = "";
          items.forEach(function(item) {
            if (item.data[0].media_type == "image") {
              //alert("es imagen");
              contenido += "<div class='col mb-4'><a href='"+item.links[0].href+"'><img src='"+item.links[0].href+"' class='img-fluid'></a></div>";
              
            }else if (item.data[0].media_type == "video") {
              // Si el enlace directo al video no está disponible, buscar enlaces alternativos
              var videoLinks = item.links.filter(link => link.rel === "preview" && link.href.includes("video")).map(link => link.href);               
              var videoURL = item.links[0].href.replace(EXTENSION_IMAGEN_NASA,EXTENSION_VIDEO_NASA);
              contenido += "<div class='col mb-4' style='background:orange'><a href='"+videoURL+"'>Ver vídeo<img src='" + videoLinks+ "' class='img-fluid'></a></div>";
            }else{  
              //alert("no es ni imagen ni video");
            }
          });
          document.getElementById("resultadosGaleriaMultimedia").innerHTML = contenido;
        }else{
            //throw new Error("No se encontraron resultados")
            document.getElementById("resultadosGaleriaMultimedia").innerHTML = "<div class='alert alert-danger' role='alert'>Based on your selections, no results were found.</div>";
        }
      })
      .catch(error => {
        // Manejar errores de la solicitud
        console.error(error);
        //alert("catch error: "+error.message)
      });
  });
  
