const telefone = document.getElementById("telefone");

telefone.addEventListener("input", function () {

    let valor = telefone.value.replace(/\D/g, "");

    valor = valor.replace(/^(\d{2})(\d)/g, "($1) $2");

    valor = valor.replace(/(\d{5})(\d)/, "$1-$2");

    telefone.value = valor;

});