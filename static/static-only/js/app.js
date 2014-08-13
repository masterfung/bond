/**
 * Created by htm on 8/11/14.
 */
var survey = angular.module('surveyApp', [
	'ngRoute',
	'ngResource'
]);

survey.config(['$routeProvider, $locationProvider', function($routeProvider) {
    $routeProvider
	    .when('/survey',
	    { templateUrl: '/static/views/survey.html',
		    controller: 'indexController' });
}]);

