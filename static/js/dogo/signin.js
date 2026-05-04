document.getElementById("btn-signin").addEventListener("click", login);

function login(){
    const email = document.getElementById("user-email").value;
    const password = document.getElementById("user-password").value;

    if(email === "") {
        alert("Pon un correo");
        return;
    }

    if(password === "") {
        alert("Pon una password");
        return;
    }

    const fecha = new Date();
    let signin_time = fecha.getHours();

    
    if (signin_time < 12){
        mensaje_bienvenida = 'Buenos dÍas'
    } else if (signin_time >= 12 && signin_time < 18){
        mensaje_bienvenida = 'Buenas tardes'
    } else{
        mensaje_bienvenida = 'Buenas noches'
    }

    const data = {
        email: email,
        password: password,
        mensaje_bienvenida:mensaje_bienvenida
    }



    fetch('api/login', {
        method:"POST",
        headers: { "Content-Type": "application/json"},
        credentials: "include", 
        body: JSON.stringify(data)
    }). then(response => response.json())
    .then(result =>  {
        if(result.success){
                window.location.href = "/welcome";
        } else if (result.message) {
            alert(result.message);
        } else {
            alert("Algo salio mal");
        }
    })
    .catch(error => {
        console.error(error);
    })
}