const characterDiv = document.querySelector('#character')
const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json'

fetch(url)
  .then(function (response) {
    return response.json()
  })
  .then(function (data) {
    characterDiv.textContent = data.name
  })