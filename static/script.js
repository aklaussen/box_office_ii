//Anna Klaussen
//2014-07-22

$(document).ready(function() {
    $( "#title" ).blur(function() {
        console.log("About to call $.ajax()");
        console.log($("#title").val());
        $.ajax("http://omdbapi.com/",{
            data: {t: $("#title").val(), plot: "full"}, //read the form
            dataType: "jsonp"})
            .done(function(data,status,xhr){
                console.log(data);
                $("#title").val(data.Title);
                $("#plot").val(data.Plot);
                $("#rating").val(data.imdbRating);
                $("#year").val(data.Year);
                $("#imdb_id").val(data.imdbID);
                $("#poster").val(data.Poster);
                $("#runtime").val(data.Runtime.match("\\d*")); //not "142 min"
            });
    })    
})
