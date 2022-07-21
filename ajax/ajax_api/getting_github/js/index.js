async function handleGitRequest(event) {
    event.preventDefault();
    
    const gitUser = document.querySelector("#gitUser").value;
    const URL = `https://api.github.com/users/${gitUser}`;


    const settings = {
        method:"GET"
    };

    const response = await fetch(URL, settings);
    const data = await response.json();

    // console.log(data)
    const results = document.querySelector(".results");
    results.innerHTML = "";

    results.innerHTML +=
    `<div class = "gitUser">
        <img src="${data.avatar_url}" alt="Img"/>
        <h3>Git User Name: ${data.name}</h3>
        <h5>Followers: ${data.followers}</h5>
    </div>`;
}