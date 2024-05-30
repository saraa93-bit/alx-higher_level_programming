$(document).ready(function(){
    $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data){
        const movies = data.results;
        const listElement = $('#list_movies');
        
        $.each(movies, function(index, movie){
            listElement.append('<li>' + movie.title + '</li>');
        });
    });
});
