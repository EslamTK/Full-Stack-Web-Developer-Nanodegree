var map;
var infos = {};
var markers = [];
var infowindow;

/*
 * @description Init the map and sets the markers from the points.js data and load the locations info
 */
function initMap() {

    try {

        map = new google.maps.Map(document.getElementById('map'), {
            center: {lat: 29.979207, lng: 31.134213},
            zoom: 8
        });
    } catch (e) {
        mapError();
    }

    infowindow = new google.maps.InfoWindow();
    var bounds = new google.maps.LatLngBounds();

    for (var i in data) {

        var marker = new google.maps.Marker({
            position: data[i].position,
            animation: google.maps.Animation.DROP,
            map: map,
            title: data[i].name
        });

        marker.addListener('click', function () {
            markerClicked(this);
        });

        setInfo(marker.title);
        markers.push(marker);
        bounds.extend(data[i].position);
        locations.push({index: i, title: data[i].name});
    }
    map.fitBounds(bounds);
    map.setCenter(bounds.getCenter());
}

/*
 * @description Animate the marker when clicked and opens the infowindow with the info link
 */
function markerClicked(marker) {

    map.setCenter(marker.position);
    marker.setAnimation(google.maps.Animation.BOUNCE);

    setTimeout(function () {
        marker.setAnimation(null);
    }, 1400);

    if (infos[marker.title] == "error") {
        infowindow.setContent("Sorry The Info Link For This Location<br>Can't Be Loaded");
    }
    else {
        infowindow.setContent("<a href=" + infos[marker.title] + " target=\"_blank\">" + marker.title + "</a>");
    }
    infowindow.open(map, marker);
}

function mapError() {
    alert("Sorry The Map Can't Be Loaded Please Refresh The Page");
}