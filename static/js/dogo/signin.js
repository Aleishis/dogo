document.getElementById('btn-signin').addEventListener('click', login);


function login(){
    const email = document.getElementById('user-email').value;
    const password = document.getElementById('user-password').value;

    if (email === ""){
        alert("Debe de ingresar un correo electronico") //TODO: PON EL SWEETALERT
    }

    if (password === ""){
        alert("Debe ingresar su contraseña") //TODO: PON EL SWEETALERT
    }

    const data = {
        email : email,
        password : password
    }

    //endpoint api/login
    fetch('api/login', {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(result => {
        if(result.success){
            window.location.href = "/welcome"
        } else{
            alert(result.message) //TODO: SWEETALERT
        }
    })
    .catch(error => {
        alert("No se pudo");
        console.error(error);
    })
}