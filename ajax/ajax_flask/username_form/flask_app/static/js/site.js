function getUsers(){
    fetch('http://localhost:5001/users')
        .then(res =>  res.json())
        .then(data => {
            var users = document.getElementById('users');
            for( let i = 0; i < data.length; i++){
                let row = document.createElement('tr');

                let name = document.createElement('td');
                name.innerHTML = data[i].user_name;
                row.appendChild(name);
                
                let email = document.createElement('td');
                email.innerHTML = data[i].email;
                row.appendChild(email);
                users.appendChild(row);
            }
        })

}
getUsers();

var userForm = document.getElementById('userForm');

userForm.onsubmit = function(e) {
    e.preventDefault();
    var formData = new FormData(userForm);
    fetch('http://localhost:5001/users/create', {method:'POST', body : formData })
        .then(response => response.json())
        .then(function(data) {
            console.log(data);
            //update table
            let user_name = document.getElementById('user_name').value;
            let email_addr = document.getElementById('email').value;

            let row = document.createElement('tr');
            let name = document.createElement('td');
            name.innerHTML = user_name;
            row.appendChild(name);
            
            let email = document.createElement('td');
            email.innerHTML = email_addr;
            row.appendChild(email);
            users.appendChild(row);

            //clear form inputs
            document.getElementById('user_name').value = '';
            document.getElementById('email').value = '';
        })
    }



