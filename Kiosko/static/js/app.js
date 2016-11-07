var nombres=JSON.parse(localStorage.getItem('nombres') || "[]");
var cantidades=JSON.parse(localStorage.getItem('cantidades') || "[]");
var precios=JSON.parse(localStorage.getItem('precios') || "[]");


function addListProduct(nombre,precio,indexCant) {
  
  var cantidad=document.getElementsByClassName('input-number');
  indexCant--;
  var valorcantidad = parseInt(cantidad[indexCant].defaultValue)
  nombres.push(nombre);
  cantidades.push(valorcantidad);
  precios.push(precio);
  
  localStorage.setItem('nombres',JSON.stringify(nombres));
  localStorage.setItem('cantidades',JSON.stringify(cantidades));
  localStorage.setItem('precios',JSON.stringify(precios));
  var table = document.getElementById("tableproduct");
  var len=table.length;
  var newRow = table.insertRow(len);

  var cell = newRow.insertCell(0);
  cell.innerHTML="<td>"+nombre+"</td>";
  
  var cell = newRow.insertCell(1);
  cell.innerHTML="<td>"+valorcantidad+"</td>";
  
  var cell = newRow.insertCell(2);
  cell.innerHTML="<td>"+precio+"</td>";

  var cell = newRow.insertCell(3);
  cell.innerHTML="<td>"+'<input type="button" onclick="delListProduct(this)"/>'+"</td>";

  SumaCantidad()
  
}

function clearStorage(){
  localStorage.clear();
}

function delListProduct(row){
  var j=row.parentNode.parentNode.rowIndex;
  document.getElementById('tableproduct').deleteRow(j);
  id=j-1;
  nombres.splice(id,1);
  cantidades.splice(id,1);
  precios.splice(id,1);
  localStorage.setItem('nombres',JSON.stringify(nombres));
  localStorage.setItem('cantidades',JSON.stringify(cantidades));
  localStorage.setItem('precios',JSON.stringify(precios));
  SumaCantidad()

}


function increaseValue(id) {
  var number = document.getElementsByClassName('input-number');
  id--;
  var value = parseInt(number[id].defaultValue);
  if(value==10){
    value=10;
    number[id].defaultValue = value;
  }else{
    value++;
    number[id].defaultValue = value;
  }
}

function decreaseValue(id) {
  var number = document.getElementsByClassName('input-number');
  id--;
  var value = parseInt(number[id].defaultValue);
  if(value==0){
    value=0;
    number[id].defaultValue = value;
  }else{
    value--;
    number[id].defaultValue = value;
  }
  number[id].defaultValue = value;
}


function loadTabla(){
  var table = document.getElementById("tableproduct");
  
  for(var i=0 ;i<nombres.length;i++){
    var len=table.length;
    var newRow = table.insertRow(len);
    var cell = newRow.insertCell(0);
    cell.innerHTML="<td>"+nombres[i]+"</td>";
  
    var cell = newRow.insertCell(1);
    cell.innerHTML="<td>"+cantidades[i]+"</td>";
    
    var cell = newRow.insertCell(2);
    cell.innerHTML="<td>"+precios[i]+"</td>";

    var cell = newRow.insertCell(3);
    cell.innerHTML="<td>"+'<input type="button" onclick="delListProduct(this)"/>'+"</td>";
          
  }
  SumaCantidad()
}
function SumaCantidad(){
  var iva= document.getElementById("IVA");
  var total= document.getElementById("Total");
  var sub=document.getElementById("SubTotal");
  var subtotal=0.00;
  var acomulador= 0.00;
  var ivacomulador=0.16;
  for(var i=0 ;i<nombres.length;i++){
    subtotal += parseFloat(precios[i])*parseFloat(cantidades[i]);
  }
  ivacomulador*=subtotal;
  acomulador=subtotal+ivacomulador;
  sub.innerHTML=subtotal;
  iva.innerHTML=ivacomulador
  total.innerHTML=acomulador
}