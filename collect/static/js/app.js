var wibeeApp = angular.module('wibeeApp', ['ngRoute', 'ngResource', 'ui.bootstrap', 'angular-flip']);

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

        otherwise({redirectTo:'/'});
}]);