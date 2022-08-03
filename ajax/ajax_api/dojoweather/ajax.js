var weatherLocation = document.querySelector(".weather");
var cookieRemover = document.querySelector(".alert");


function removeMe(){
    cookieRemover.remove();
}


function newWeather(data){
    var res = `<div class="col-4">
                <div class="box">
                    <h5>Today</h5>
                    <img src="assets/some_sun.png" alt="weather">
                    <p>${data.daily[0].weather[0].main}</p>
                    <div class="flex-me">
                        <div class="red" id="temp3">${data.daily[0].temp.max}</div>
                        <div class="blue" id="temp4">${data.daily[0].temp.min}</div>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="box">
                    <h5>Tomorrow</h5>
                    <img src="assets/some_sun.png" alt="weather">
                    <p>${data.daily[1].weather[0].main}</p>
                    <div class="flex-me">
                        <div class="red" id="temp3">${data.daily[1].temp.max}</div>
                        <div class="blue" id="temp4">${data.daily[1].temp.min}</div>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="box">
                    <h5>Next Day</h5>
                    <img src="assets/some_sun.png" alt="weather">
                    <p>${data.daily[2].weather[0].main}</p>
                    <div class="flex-me">
                        <div class="red" id="temp3">${data.daily[2].temp.max}</div>
                        <div class="blue" id="temp4">${data.daily[2].temp.min}</div>
                    </div>
                </div>
            </div>
            <div class="col-4">
                <div class="box">
                    <h5>Next Day</h5>
                    <img src="assets/some_sun.png" alt="weather">
                    <p>${data.daily[3].weather[0].main}</p>
                    <div class="flex-me">
                        <div class="red" id="temp3">${data.daily[3].temp.max}</div>
                        <div class="blue" id="temp4">${data.daily[3].temp.min}</div>
                    </div>
                </div>
            </div>`
    return res;
}


async function getData1(){
    response = await fetch("https://api.openweathermap.org/data/2.5/onecall?lat=37.3394&lon=-121.895&units=imperial&appid=418b0eee4a0e174711509f7ee2779250");
    weatherData = await response.json();
    $("#loc1").click(function(){
        location.reload(weatherData);
    });
    console.log(weatherData);
    weatherLocation.innerHTML = newWeather(weatherData);
}


async function getData2(){
    response = await fetch("https://api.openweathermap.org/data/2.5/onecall?lat=34.0522&lon=-118.2437&units=imperial&appid=418b0eee4a0e174711509f7ee2779250");
    weatherData = await response.json();
    $("#loc1").click(function(){
        location.reload(weatherData);
    });
    console.log(weatherData);
    weatherLocation.innerHTML = newWeather(weatherData);
}

async function getData3(){
    response = await fetch("https://api.openweathermap.org/data/2.5/onecall?lat=41.85&lon=-87.65&units=imperial&appid=418b0eee4a0e174711509f7ee2779250");
    weatherData = await response.json();
    $("#loc1").click(function(){
        location.reload(weatherData);
    });
    console.log(weatherData);
    weatherLocation.innerHTML = newWeather(weatherData);
}

async function getData4(){
    response = await fetch("https://api.openweathermap.org/data/2.5/onecall?lat=43.0004&lon=-75.4999&units=imperial&appid=418b0eee4a0e174711509f7ee2779250");
    weatherData = await response.json();
    $("#loc1").click(function(){
        location.reload(weatherData);
    });
    console.log(weatherData);
    weatherLocation.innerHTML = newWeather(weatherData);
}



// https://api.openweathermap.org/data/2.5/weather?lat=37.3394&lon=-121.895&cnt=1&appid=418b0eee4a0e174711509f7ee2779250

// los angeles: [34.0522, -118.2437]
// chicago: [41.85, -87.65]
// new york: [43.0004, -75.4999]

