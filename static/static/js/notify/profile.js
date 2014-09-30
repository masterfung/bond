/**
 * Created by htm on 9/29/14.
 */

$(document).ready(function () {

	$.notify("Welcome!", "success");

	$(".current-city").notify(
		"If your city is not correct, please change it",
		{ position: "left" }
	)

});