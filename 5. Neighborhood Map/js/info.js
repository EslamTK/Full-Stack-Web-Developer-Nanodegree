/**
 * @description Sets the wiki info link of the location in the infos object
 * @param {String} title
 */
function setInfo(title) {
    var wikiUrl = "https://en.wikipedia.org/w/api.php?action=query&titles=" +
        title + "&prop=revisions&rvprop=content&format=json";
    $.ajax({
        url: wikiUrl,
        dataType: "jsonp",
        success: function (response) {
            infos[title] = "https://en.wikipedia.org/?curid=" + Object.keys(response.query.pages)[0];
        },
        error : function () {
            infos[title] = "error";
        }
    });
}
