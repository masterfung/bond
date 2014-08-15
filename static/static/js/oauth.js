/**
 * Created by htm on 8/14/14.
 */

$(document).ready(function() {

	// OAuth

	var version  = OAuth.getVersion();

	console.log(version);
	OAuth.initialize('BeQb7JX0quMabtVeIKqrNXGsyZc');

	//Using popup (option 1)
	OAuth.popup('meetup').done(function(result) {
	  console.log(result);
	  console.log('Johnny');
	  data = JSON.stringify(result);
		$.ajax({
			url: '/meetup_oauth/',
			type: 'POST',
			data: data,
			success: function(response) {
				console.log(response);
				console.log("AJAX WORKED");
			},
			error: function (response) {
				console.log(response);
			}
		})
	});

	//Using redirection (option 2)
	OAuth.redirect('meetup', 'callback/url');

	result.me().done(function(data) {
		console.log(data);
//	  console.log(data);
//	  console.log('Johnny');
//	  result = JSON.stringify(data);
//		$.ajax({
//			url: '/meetup_oauth/',
//			type: 'POST',
//			data: result,
//			success: function(response) {
//				console.log(response);
//				console.log("AJAX WORKED");
//			},
//			error: function (response) {
//				console.log(response);
//			}
//		})
	});
});