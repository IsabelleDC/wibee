var wibeeApp = angular.module('wibeeApp', ['ngRoute', 'ngResource', 'ui.bootstrap']);

wibeeApp.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: '/static/js/views/home.html',
            controller: homeController
        }).
        when('/places/:placeId', {
            templateUrl: '/static/js/views/place.html',
            controller: placeController
        }).
        when('/map', {
            templateUrl: '/static/js/views/map.html',
            controller: mapController
        }).

        otherwise({redirectTo:'/'});
}]);