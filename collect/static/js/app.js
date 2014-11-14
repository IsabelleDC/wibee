var wibeeApp = angular.module('wibeeApp', ['ngRoute']);

wibeeApp.config(['$routeProvider', function($routeProvider) {
    $routeProvider.
        when('/', {
            templateUrl: '/static/js/views/home.html',
            controller: homeController
        }).
        otherwise({redirectTo:'/'});
}]);