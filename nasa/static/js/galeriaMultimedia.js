document.getElementById("btnFiltrarBusquedaMultimedia").addEventListener("click", function() {
    var checkbox = document.getElementById("flexCheckImagenes");
    var checkedCombo = checkbox.checked;

    var buscarGaleria = document.getElementById("inputBuscarGaleriaMultimedia");
    var valorInput = buscarGaleria.value;


    //var parametroEnviar = checkedCombo ? buscarGaleria : "video";
  
    fetch('/galeriaMultimedia2/' + valorInput, {
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
          var enlaceImagenes = [];
          var contenido = "";
          items.forEach(function(item) {
            enlaceImagenes.push(item.links[0].href);
            contenido += "<div class='col mb-4' ><img src='" + item.links[0].href + "' class='img-fluid'></div>";
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
  