/**
 * Created by htm on 7/27/14.
 */
$(document).ready(function () {
    var eventbriteApiKey = 'ZK2FA7QOSAKQ3UUKPC';
    var eventbriteOAuth = 'Y6NQUIILSJKGNHSHJ3CH';
    var pageDisplay;
    var searchQuery;
//    $.getJSON('https://www.eventbriteapi.com/v3/events/?token='+ eventbriteOAuth, function(result) {
//    console.log(result);
//    var jsonString = JSON.stringify(result);
//    var result = JSON.parse(jsonString);
//    console.log(result);
//    });

    $('.userChoice').on('click', function () {
        searchQuery = $(this).text();
        console.log(searchQuery);

        $.ajax({
            url: 'https://developer.eventbrite.com/json/event_search?app_key=' + eventbriteApiKey+'&city=San+Francisco',
            type: "GET",
            dataType: 'jsonp',

            beforeSend: function(xhrObj){
            xhrObj.setRequestHeader("Content-Type","application/json");
            xhrObj.setRequestHeader("Accept","application/json");
            if(eventbriteApiKey !== undefined){
              xhrObj.setRequestHeader("Authorization", "Bearer " + eventbriteApiKey);
            }
            },
            success: function (resp) {
            if(resp.contents !== undefined){
              console.log(resp.contents);
            }else{
              console.log(resp);
            }
            },
            error: function (err) {
            console.log("Error connecting to Eventbrite API");
            }
            })
        });
    });




//{
//        url: 'https://www.eventbriteapi.com/v3/events/?token='+ eventbriteOAuth,
//        type: "GET",
//        dataType: 'jsonp',
//        success: function (response) {
//            console.log(response);
//        }
