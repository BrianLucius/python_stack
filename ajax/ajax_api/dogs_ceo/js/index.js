
// async function handleDogFormRequest(event) {
//     event.preventDefault();

//     const numberOfDogs = document.querySelector("#numberOfDogs").value;
//     console.log(numberOfDogs);

//     const URL = `https://dog.ceo/api/breeds/image/random/${numberOfDogs}`
//     // const URL = "https://dog.ceo/api/breeds/image/random/"+ numberOfDogs

//     const settings = {
//         method : "GET"
//     }

//     const response = await fetch(URL, settings);
//     const data = await response.json();
    
//     const resultsDiv = document.querySelector(".results");
//     resultsDiv.innerHTML = "";

//     for (const image of data.message) {
//         resultsDiv.innerHTML+=`
//             <div class="dogImage">
//                 <img src="${image}" alt="Dog image" class="dogImage" />
//             </div>
//         `;
//     }
// }


function handleDogFormRequest(event) {
    event.preventDefault();
    
    const numberOfDogs = document.querySelector("#numberOfDogs").value;
    console.log(numberOfDogs);

    const URL = `https://dog.ceo/api/breeds/image/random/${numberOfDogs}`
    // const URL = "https://dog.ceo/api/breeds/image/random/"+ numberOfDogs

    const settings = {
        method : "GET"
    }

    fetch( URL, settings)
        .then(function(response){
            return response.json();
        })
        .then(function (data){
            console.log(data);
            const resultsDiv = document.querySelector(".results");
            resultsDiv.innerHTML = "";

            for (const image of data.message) {
                resultsDiv.innerHTML+=`
                    <div class="dogImageContainer">
                        <img src="${image}" alt="Dog image" class="dogImage" />
                    </div>
                `;
            }
        })
    }