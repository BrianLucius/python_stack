
const API_KEY = config.API_KEY

async function handleNewsRequest(event) {
    event.preventDefault();
    
    const searchTerm = document.querySelector("#searchTerm").value;
    const pageSize = document.querySelector("#pageSize").value;
    const URL = `https://newsapi.org/v2/everything?q=${searchTerm}&language=en&pageSize=${pageSize}`;

    console.log(URL);

    const settings = {
        method:"GET",
        headers: {
            "x-api-key" :  API_KEY
            // Authorization: `Bearer ${API_KEY}`
        }
    };

    const response = await fetch(URL, settings);
    const data = await response.json();

    const results = document.querySelector(".results");
    results.innerHTML = "";

    for (const article of data.articles) {
        results.innerHTML +=
        `<div class = "article">
            <h2>
                <a href=${article.url}>${article.title}</a>
            </h2>
            <div class="imageContainer">
                <img src="${article.urlToImage}" alt="Img"/>
                <h5>
                    ${article.author}
                </h5>
                <p>
                    ${article.description}
                </p>
            </div>
        </div>`
    };
}