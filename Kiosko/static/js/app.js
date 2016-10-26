var cantidad = 1;
var btncantidad = document.getElementsByTagName("buttonproduct") ;


function addListProduct(name) {
    
    for (var i = 0; i < btncantidad.length; i++) {

        var nameproduct = btncantidad[i].children[0].textContent;
        var listproduct = btncantidad[i].children[4].textContent;
        var table = document.getElementById("tableproduct");
        var len=table.length;
        var newRow = table.insertRow(len);
        if(nameproduct==name){
          var cell = newRow.insertCell(0);
          cell.innerHTML="<td>"+nameproduct+"</td>";

          var cell = newRow.insertCell(1);
          cell.innerHTML="<td>"+cantidad+"</td>";

          var cell = newRow.insertCell(2);
          cell.innerHTML="<td>"+listproduct+"</td>";

          var cell = newRow.insertCell(3);
          cell.innerHTML="<td>"+'<input type="button" onclick="delListProduct(this)"/>'+"</td>";
          
        }

    }
    // sumaPrecioProducto(table);
  }

// function sumaPrecioProducto(table){
//   var total=0;
//   var iva =1.16;

//   for(var i = 0;i<table.rows.length;i++){
//     total += parseInt(table[i].value);
//   }

// }

function delListProduct(row){
  var i=row.parentNode.parentNode.rowIndex;
  document.getElementById('tableproduct').deleteRow(i);
}


