
function mapController($scope, $http, $routeParams, PlaceFactory) {
    console.log('mapController');
    $scope.places = $routeParams.places;

    $http.get('/api/places/' + $scope.places)
        .success(function (place) {
            console.log(place);
            $scope.place = place;
        })
        .error(function (error) {
            console.log('error');
            console.log(error);
        });
}
