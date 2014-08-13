// Cache selectors
var lastId,
    topMenu = $("#top-menu"),
    topMenuHeight = topMenu.outerHeight()+15,
    // All list items
    menuItems = topMenu.find("a"),
    // Anchors corresponding to menu items
    scrollItems = menuItems.map(function(){
      var item = $($(this).attr("href"));
      if (item.length) { return item; }
    });

// Bind click handler to menu items
// so we can get a fancy scroll animation
menuItems.click(function(e){
  var href = $(this).attr("href"),
      offsetTop = href === "#" ? 0 : $(href).offset().top-topMenuHeight+1;
  $('html, body').stop().animate({
      scrollTop: offsetTop
  }, 500);
  e.preventDefault();
});

// Bind to scroll

$(window).scroll(function(){
   // Get container scroll position
   var fromTop = $(this).scrollTop()+topMenuHeight;

   // Get id of current scroll item
   var cur = scrollItems.map(function(){
     if ($(this).offset().top < fromTop)
       return this;
   });
   // Get the id of the current element
   cur = cur[cur.length-1];
   var id = cur && cur.length ? cur[0].id : "";

   if (lastId !== id) {
       lastId = id;
       // Set/remove active class
       menuItems
         .parent().removeClass("active")
         .end().filter("[href=#"+id+"]").parent().addClass("active");
   }
});
//
////JQuery
//
//$(document).ready(function() {
//    var eventbriteApiKey = 'ZK2FA7QOSAKQ3UUKPC';
//    var eventbriteOAuth = 'Y6NQUIILSJKGNHSHJ3CH';
//    var pageDisplay = 15;
//    var city = $('.userCity').text();
//    var searchQuery;
//
//    var list;
//
//    var eventbriteFinal = {};
//
//
//    $('.userChoice').on('click', function () {
//        searchQuery = $(this).text();
//        console.log(searchQuery);
//        console.log(city);
//
//        $.ajax({
//            url: 'https://developer.eventbrite.com/json/event_search?app_key=' + eventbriteApiKey + '&city=' + 'San+Francisco' + '&keywords=' + searchQuery + '&page=' + pageDisplay,
//            type: "GET",
//            dataType: 'jsonp',
//
//            beforeSend: function(xhrObj){
//                xhrObj.setRequestHeader("Content-Type","application/json");
//                xhrObj.setRequestHeader("Accept","application/json");
//                if(eventbriteApiKey !== undefined){
//                  xhrObj.setRequestHeader("Authorization", "Bearer " + eventbriteApiKey);
//                }
//            },
//            success: function (resp) {
//                if(resp.contents !== undefined){
//                  console.log(resp.contents.events);
//                  console.log(resp);
//                  var list = resp.contents.events;
//                  eventbriteList = [];
//                  for (i = 1; i < list.length; i++) {
//                      list = list[i];
//                      console.log(list);
//                  }
//
////                  $('#accordion').append(
////                          "<h3 class='ui-accordion-header'>" + list[1].event.title + "</h3>" +
////                          "<div class='ui-accordion-content'>" +
////                              "<p> Description: " + list[1].event.description + "</p>" +
////                              "<p> Event Date: " + list[1].event.start_date + "</p>" +
////                              "<a href=" + list[1].event.url + "></a>" +
////                              "<p> Venue Address: " + list[1].event.venue.address + "</p>" +
////                          "</div>"
//
////                  )
//
//            } else{
//              console.log(resp);
//            }
//            },error: function (resp) {
//                console.log("Error connecting to Eventbrite API");
//            }
//
//        })
//        });
//    });


//.complete(function () {
//                 $('#accordion').accordion({active: 1});
//
//    })


//SEARCH

$(document).ready(function() {
	$('.setting-btn').on('click', function () {
		$('.toggle-settings').toggle()
	})

});

//$(function(){
//
//    $('#search').keyup(function() {
//		console.log('searching');
//        $.ajax({
//            type: "POST",
//            url: "/search/",
//            data: {
//                'search_text' : $('#search').val(),
//                'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
//            },
//            success: searchSuccess,
//            dataType: 'html'
//        });
//
//    });
//
//});
//
//function searchSuccess(data, textStatus, jqXHR)
//{
//	console.log('in search success!');
//    $('#search-results').html(data);
//}