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

    const data = {
        email: email,
        password: password
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
        } else {
            alert("Algo salio mal");
        }
    })
    .catch(error => {
        console.error(error);
    })
}