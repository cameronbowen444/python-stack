var cardDiv = document.querySelector(".container");
var currentUsername = "";



function getUsername(element){
    console.log(element.value)
    currentUsername = element.value
}

function makeCoderCard(data){
    cardMade = `<div class="card">
                    <div>
                    <img src="${data.avatar_url}" alt="${data.login}">
                    </div>
                    <div>
                        <h3>${data.login} - ${data.name}</h3> 
                        <p>Location: ${data.location}</p>
                        <p>Respositories: ${data.public_repos}</p>
                    </div>
                </div>`;
    return cardMade;
}


async function getCoderData() {
    var response = await fetch("https://api.github.com/users/" + currentUsername);
    var coderData = await response.json();
    console.log(coderData);
    cardDiv.innerHTML = makeCoderCard(coderData) + cardDiv.innerHTML;
}





// http://api.openweathermap.org/data/2.5/forecast/daily?id=524901&APPID=418b0eee4a0e174711509f7ee2779250