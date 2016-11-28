var nombres=JSON.parse(localStorage.getItem('nombres') || "[]");
var cantidades=JSON.parse(localStorage.getItem('cantidades') || "[]");
var precios=JSON.parse(localStorage.getItem('precios') || "[]");
var index = JSON.parse(localStorage.getItem('index') || "[]");

function addListProduct(producto,precio,indexCant,productid) {
  var cantidad = document.getElementsByClassName("id_cantidad");
  var valorcantidad = 1;
  

  if(valorcantidad!=0){

     if(findproduct(producto)){
        for(i=0;i<=nombres.length;i++){
            if(nombres[i]==producto && nombres[i] !=null){
                var valornuevo = cantidades[i] + valorcantidad;
                cantidades[i]=valornuevo;
                localStorage.setItem('cantidades',JSON.stringify(cantidades));
                break;
            }
         }
      }else{
        nombres.push(producto);
        cantidades.push(valorcantidad);
        precios.push(precio);
        index.push(productid);
        localStorage.setItem('index',JSON.stringify(index));
        localStorage.setItem('nombres',JSON.stringify(nombres));
        localStorage.setItem('cantidades',JSON.stringify(cantidades));
        localStorage.setItem('precios',JSON.stringify(precios));


      }


    Vaciartabla();
  }else{
    sweetAlert("Oops...", "Por favor agregar cantidad", "error");
  }
  
  
}

function findproduct(producto){
    for(i=0;i<=nombres.length;i++){
            if(nombres[i]==producto && nombres[i] !=null){
                return true;
            }
    }
}

function clearStorage(){
  localStorage.clear();
}

function delListProduct(row){
  var j=row.parentNode.parentNode.rowIndex;
  document.getElementById('tableproduct').deleteRow(j);
  id=j-1;
  if(cantidades[id]>0){
    cantidades[id]-=1;
    localStorage.setItem('cantidades',JSON.stringify(cantidades));
    if(cantidades[id]==0){
      nombres.splice(id,1);
      cantidades.splice(id,1);
      precios.splice(id,1);
      index.splice(id,1);
      localStorage.setItem('nombres',JSON.stringify(nombres));
      localStorage.setItem('cantidades',JSON.stringify(cantidades));
      localStorage.setItem('precios',JSON.stringify(precios));
      localStorage.setItem('index',JSON.stringify(index));
    }
  }
  Vaciartabla();

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
    var cantidad = document.getElementsByClassName("id_cantidad");
    var idnombre = document.getElementsByClassName("id_nombre");
    var table = document.getElementById("tablebody");

  
    for(var i=0 ;i<nombres.length;i++){
        var len=table.childElementCount;
        var newRow = table.insertRow(len);
        var cell1 = newRow.insertCell(0);
        var cell2 = newRow.insertCell(1);
        var cell3 = newRow.insertCell(2);
        var cell4 = newRow.insertCell(3);

        cell1.innerHTML='<td>'+nombres[i]+'</td>';
        cell2.innerHTML='<td>'+cantidades[i]+'</td>';
        cell3.innerHTML='<td>'+precios[i]+'</td>';
        cell4.innerHTML='<td>'+'<button onclick="delListProduct(this)"><img src="/static/img/del.png" width="10px" height="10px" ></button>'+'</td>';
    }
    for(var j=0 ;j<idnombre.length;j++ ){
    cantidad[j].innerText=0;
     for(var i=0 ;i<nombres.length;i++){
        if(idnombre[j].textContent==nombres[i]){
            cantidad[j].innerHTML=cantidades[i];
        }
     }
    }


  SumaCantidad()

}
function Vaciartabla(){

    $("#tablebody").empty();
    $(".id_cantidad").empty();
    loadTabla();

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
      sub.innerHTML=subtotal.toFixed(2);
      iva.innerHTML=ivacomulador.toFixed(2);
      total.innerHTML=acomulador.toFixed(2);

}

