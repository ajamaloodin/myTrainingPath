function consulta() {

    let datosJSON;

    fetch('resumen.json')
    .then(res => res.json())
    .then((salida) => {
        datosJSON = salida;

        let elementBanco = document.getElementById("banco");
        elementBanco.textContent = `${datosJSON.banco}`;

        let elementdonde = document.getElementById("donde");
        elementdonde.textContent = `${datosJSON.sucursal}`;

        let elementCuenta = document.getElementById("cuenta");
        elementCuenta.textContent = `Nro de Cuenta: ${datosJSON.nro_cuenta}`;

        let elementSaldos = document.getElementById("saldos");

        moneyArray = datosJSON.saldo;
        for (money of moneyArray){
            let item = document.createElement('li');
            item.innerText = `${money.monto} ${money.moneda}`;
            elementSaldos.appendChild(item);
        }


        let elementCBU = document.getElementById("cbu");
        elementCBU.textContent = `CBU: ${datosJSON.cbu}`;

    })
    .catch((err) => {
        console.log(err);
    })

}