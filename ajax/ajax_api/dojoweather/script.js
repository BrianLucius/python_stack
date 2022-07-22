async function getWeatherByCity(event, city) {
    event.preventDefault();

    // const API_EXCLUSIONS = "minutely,hourly,alerts";
    const API_KEY = config.API_KEY;
    const locations = {
        "sanjose" : {"lat": "37.33", "lon": "-121.88"},
        "burbank" : {"lat": "34.18", "lon": "-118.30"},
        "chicago" : {"lat": "41.87", "lon": "-87.62"},
        "dallas"  : {"lat": "32.77", "lon": "-96.79"},
        "denver"  : {"lat": "39.74", "lon": "-104.99"}
    };
    const settings = {
        method: "GET"
    };

    // const URL = `https://api.openweathermap.org/data/2.5/forecast?lat=${locations[city].lat}&lon=${locations[city].lon}&units=imperial&exclude=${API_EXCLUSIONS}&appid=${API_KEY}`;
    const URL = `http://api.weatherapi.com/v1/forecast.json?q=${locations[city].lat},${locations[city].lon}&days=4&key=${API_KEY}`
    console.log(city, URL);

    fetch(URL, settings)
        .then(function(response){
            return response.json();
        })
        .then(function (data) {
            console.log(data);
            dayNum=1;
            var units = document.querySelector(`#temperature`).value;
            console.log("Units:", units);

            var city=document.getElementById('city');
            city.innerText=data.location.name+' - Last Updated: '+data.current.last_updated;

            for (dailyWeather of data.forecast.forecastday) {
                var dh=document.querySelector(`#day${dayNum} .ht`);
                var dl=document.querySelector(`#day${dayNum} .lt`);
                var cond=document.querySelector(`#day${dayNum} .condition`);
                var icon=document.querySelector(`#day${dayNum} .icon`);
                var dow=document.querySelector(`#day${dayNum} .dow`);
                
                cond.innerText=dailyWeather.day.condition.text;
                icon.src=dailyWeather.day.condition.icon;

                if (document.querySelector(`#temperature`).value = 'C') {
                    dh.innerText=Math.round(dailyWeather.day.maxtemp_c);
                    dl.innerText=Math.round(dailyWeather.day.mintemp_c);
                } else {
                    dh.innerText=Math.round(dailyWeather.day.maxtemp_f);
                    dl.innerText=Math.round(dailyWeather.day.mintemp_f);
                }
                dayNum++;
            }
        });
    
}


function acceptCookies() {
    var element = document.querySelector("#cookie-time");
    element.remove();
}

function setTemperatures(element) {
    var d1h=document.querySelector("#day1 .ht");
    var d1l=document.querySelector("#day1 .lt");
    var d2h=document.querySelector("#day2 .ht");
    var d2l=document.querySelector("#day2 .lt");
    var d3h=document.querySelector("#day3 .ht");
    var d3l=document.querySelector("#day3 .lt");
    var d4h=document.querySelector("#day4 .ht");
    var d4l=document.querySelector("#day4 .lt");

    if (element.value == "F") {
        d1h.innerText=Math.round((parseInt(d1h.innerText)*(9/5))+32);
        d1l.innerText=Math.round((parseInt(d1l.innerText)*(9/5))+32);
        d2h.innerText=Math.round((parseInt(d2h.innerText)*(9/5))+32);
        d2l.innerText=Math.round((parseInt(d2l.innerText)*(9/5))+32);
        d3h.innerText=Math.round((parseInt(d3h.innerText)*(9/5))+32);
        d3l.innerText=Math.round((parseInt(d3l.innerText)*(9/5))+32);
        d4h.innerText=Math.round((parseInt(d4h.innerText)*(9/5))+32);
        d4l.innerText=Math.round((parseInt(d4l.innerText)*(9/5))+32);
    }
    if (element.value == "C") {
        d1h.innerText=Math.round((parseInt(d1h.innerText)-32)*(5/9));
        d1l.innerText=Math.round((parseInt(d1l.innerText)-32)*(5/9));
        d2h.innerText=Math.round((parseInt(d2h.innerText)-32)*(5/9));
        d2l.innerText=Math.round((parseInt(d2l.innerText)-32)*(5/9));
        d3h.innerText=Math.round((parseInt(d3h.innerText)-32)*(5/9));
        d3l.innerText=Math.round((parseInt(d3l.innerText)-32)*(5/9));
        d4h.innerText=Math.round((parseInt(d4h.innerText)-32)*(5/9));
        d4l.innerText=Math.round((parseInt(d4l.innerText)-32)*(5/9));
    }
}