
document.getElementById('btn-register').addEventListener("click", register);

function register(){

    var password = document.getElementById('user-password').value;
    var repeatPassword = document.getElementById('user-confirm-password').value;

    if (password != repeatPassword) {
        alert("Las password no coinciden")
        return;

        //sweetalert2
    }

    
    const data = {
        name : document.getElementById('user-name').value,
        email : document.getElementById('user-email').value,
        password : document.getElementById('user-password').value,
    };

    //endpoint
    fetch('api/users', {
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify(data)
    }).then(response => response.json())
    .then(result => {
        if(result.success){
            alert("El usuario se guardo correctamente")
        } else{
            alert(result.message)
        }
    })
    .catch(error => {
        console.error(error);
    })

}