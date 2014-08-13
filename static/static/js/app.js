/**
 * Created by htm on 8/11/14.
 */
angular
	.module('surveyApp', [
		'ngRoute',
		'ngResource'
	])
	.config(function($routeProvider) {
    $routeProvider
	    .when('/getting-started', {
		    templateUrl: '../static/views/getting_started.html',
		    controller: 'startSurveyController' })
	    .when('/survey', {
		    templateUrl: '../static/views/survey.html',
		    controller: 'indexController' })
	    .otherwise({
		    redirectTo: '/getting-started'
	    });
});

