document.getElementById('btn-register').addEventListener("click", register);

function register(){

    var password = document.getElementById('user-password').value;
    var repeatPassword = document.getElementById('user-repeat-password').value;

    if (password != repeatPassword) {
        alert("Las password no coinciden")
        return;

        // sweetalert
    }

    
    const data = {
        name : document.getElementById('user-name').value,
        email : document.getElementById('user-email').value,
        email : document.getElementById('user-email').value,
    };


}