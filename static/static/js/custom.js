//SEARCH

$(document).ready(function() {
//	$('.setting-btn').on('click', function () {
//		$('.toggle-settings').toggle()
//	});

//    Toggle buttons for questions
    $('.questSetOneNext').on('click', function () {
        $('.questSetOne').hide('slow');
        $('.questSetTwo').show('slow');
    });

    $('.questSetTwoNext').on('click', function () {
        $('.questSetTwo').hide('slow');
        $('.questSetThree').show('slow');
    });
    $('.questSetThreeNext').on('click', function () {
        $('.questSetThree').hide('slow');
        $('.questSetFour').show('slow');
    });

});