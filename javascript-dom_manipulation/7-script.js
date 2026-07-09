const listMovies = document.querySelector('#list_movies')
const url = 'https://swapi-api.hbtn.io/api/films/?format=json'

fetch(url)
  .then(function (response) {
    return response.json()
  })
  .then(function (data) {
    data.results.forEach(function (movie) {
      const newLi = document.createElement('li')
      newLi.textContent = movie.title
      listMovies.appendChild(newLi)
    })
  })