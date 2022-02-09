$.get("https://swapi-api.hbtn.io/api/films/?format=json",  function (data) {
	const reqResults = data.results;
	for (i = 0; i < reqResults.length; i++) {
		$("ul#list_movies").append("<li>" + reqResults[i].title + "</li>");
	}
});
