/**
 * Created by htm on 7/25/14.
 */
var geocoder;
var userInput;
var map;

$(document).ready(function () {

function initialize() {
    var mapOptions = {
      center: new google.maps.LatLng(37.7833, -122.4167),
      zoom: 15,
	  mapTypeId: google.maps.MapTypeId.ROADMAP

    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        mapOptions);

//    map.setCenter({lat: 37.7833, lng: -122.4167});

    geocoder = new google.maps.Geocoder();

	getData();
    }

     // Try HTML5 geolocation
  if(navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var pos = new google.maps.LatLng(position.coords.latitude,
                                       position.coords.longitude);

      var infowindow = new google.maps.InfoWindow({
        map: map,
        position: pos,
        content: 'You are located around here'
      });

      map.setCenter(pos);
        }, function() {
          handleNoGeolocation(true);
        });
      } else {
        // Browser doesn't support Geolocation
        handleNoGeolocation(false);
      }


    function handleNoGeolocation(errorFlag) {
      if (errorFlag) {
        var content = 'Error: The Geolocation service failed.';
      } else {
        var content = 'Error: Your browser doesn\'t support geolocation.';
      }

      var options = {
        map: map,
        position: new google.maps.LatLng(60, 105),
        content: content
      };

      var infowindow = new google.maps.InfoWindow(options);
      map.setCenter(options.position);
    }
	google.maps.event.addDomListener(window, 'load', initialize);

	var getData = function() {

		$.ajax({
			url: '/get-events/',
			type: "GET",
			success: function (data) {
				console.log(data[0].fields.lat);
				console.log('success');
			},
			error: function (data) {
				console.log('error');
				console.log(data.response);
				console.log(data);
			}
		})
	};

    $(".maps").on('click', function () {
        userInput = $('#inputTextAddress').val();
        console.log(userInput);
        geocoder.geocode( { 'address': userInput }, function(results, status) {
            console.log(results);
            if (status == google.maps.GeocoderStatus.OK) {
            map.setCenter(results[0].geometry.location);

            var marker = new google.maps.Marker({
            map: map,
            position: results[0].geometry.location
        });
        } else {
            alert("Geocode was not successful for the following reason: " + status);
        }
        })
    });

});