var nombres=JSON.parse(localStorage.getItem('nombres') || "[]");
var cantidades=JSON.parse(localStorage.getItem('cantidades') || "[]");
var precios=JSON.parse(localStorage.getItem('precios') || "[]");
var index = JSON.parse(localStorage.getItem('index') || "[]");

function SumaCantidad(){
   var valororden = document.getElementById('id_name').value
  var subtotal=0.00;
  var acomulador= 0.00;
  var ivacomulador=0.16;
  for(var i=0 ;i<nombres.length;i++){
    subtotal += parseFloat(precios[i])*parseFloat(cantidades[i]);
  }
  ivacomulador*=subtotal;
  acomulador=subtotal+ivacomulador;

    document.getElementById("id_nombreorder").innerHTML=valororden
    document.getElementById("id_amount_tax").value=ivacomulador.toFixed(2);
    document.getElementById("id_amount_untaxed").value=subtotal.toFixed(2);
    document.getElementById("id_amount_total").value=acomulador.toFixed(2);
    document.getElementById("id_sub_total").innerHTML=subtotal.toFixed(2);
    document.getElementById("id_iva").innerHTML=ivacomulador.toFixed(2);
    document.getElementById("id_total").innerHTML=acomulador.toFixed(2);
    TableProduct();
    addListProduct() ;

}

function TableProduct(){

    var cantidad = document.getElementsByClassName("cantidadformulario");
    var cantidaduom = document.getElementsByClassName("cantidad2formulario");
    var precio = document.getElementsByClassName("precioformulario");
    var idproduct = document.getElementsByClassName('product_idformulario');
    var idnombres=document.getElementsByClassName("nombreformulario");

    for(var i = 0; i<nombres.length; i++){
      cantidad[i].value=cantidades[i];
      cantidaduom[i].value=cantidades[i];
      precio[i].value=precios[i];
      idnombres[i].value=nombres[i];
      idproduct[i].value=index[i];
    }

}
function addListProduct() {

    var table = document.getElementById("tablebody");
    for(var i=0 ;i<nombres.length;i++){
        var len=table.length;
        var newRow = table.insertRow(len);
        var cell = newRow.insertCell(0);
        cell.innerHTML='<td>'+nombres[i]+'</td>';

        var cell = newRow.insertCell(1);
        cell.innerHTML='<td>'+cantidades[i]+'</td>';

        var cell = newRow.insertCell(2);
        cell.innerHTML='<td>'+precios[i]+'</td>';
    }
}
function clearStorage(){
  localStorage.clear();
}