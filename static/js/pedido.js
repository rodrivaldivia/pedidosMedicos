      $(document).ready(function(){
        var date_input=$('input[name="pedido_date"]'); //our date input has the name "date"
        var container=$('.bootstrap-iso form').length>0 ? $('.bootstrap-iso form').parent() : "body";
        var options={
          format: 'dd/mm/yyyy',
          todayHighlight: true,
          autoclose: true,
          language: "es"
        };
        date_input.datepicker(options);
      })

      $("#id_pedido_provincia").change(function () {
      var url = $("#PedidosForm").attr("data-loc-url");  // get the url of the `load_cities` view
      var provinciaId = $(this).val();  // get the selected country ID from the HTML input


      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'provincia': provinciaId       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_cities` view function
          $("#id_pedido_localidad").html(data);  // replace the contents of the city input with the data that came from the server
        }
      });

      });



      $("#id_pedido_nro_afiliado").change(function () {
      var url = $("#PedidosForm").attr("data-pac-url");  // get the url of the `load_cities` view
      var afiliadoID = $(this).val();  // get the selected nro_afiliado ID from the HTML input

      $.ajax({                       // initialize an AJAX request
        url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
        data: {
          'nro_afiliado': afiliadoID       // add the country id to the GET parameters
        },
        success: function (data) {   // `data` is the return of the `load_cities` view function
          alert("Se cargo al paciente " + data["nombre"])
          document.getElementById('id_pedido_paciente').value= data["nombre"];
          document.getElementById('id_pedido_dni').value= data["dni"];
          document.getElementById('id_pedido_direccion').value= data["direccion"];
          document.getElementById('id_pedido_telefono').value= data["telefono"];

          document.getElementById('id_pedido_provincia').value = data["provincia"];

          var loc = data["localidad"];
                        alert(loc);
          var url = $("#PedidosForm").attr("data-loc-url");  // get the url of the `load_cities` view
          var provinciaId = $("#id_pedido_provincia").val();  // get the selected country ID from the HTML input

            $.ajax({                       // initialize an AJAX request
                    url: url,                    // set the url of the request (= localhost:8000/hr/ajax/load-cities/)
                    data: {
                      'provincia': provinciaId       // add the country id to the GET parameters
                    },
                    success: function (data) {   // `data` is the return of the `load_cities` view function
                      $("#id_pedido_localidad").html(data);  // replace the contents of the city input with the data that came from the server
                        alert(loc);
                        document.getElementById('id_pedido_localidad').value= loc;
                    }
             });



        }
      });




      });
