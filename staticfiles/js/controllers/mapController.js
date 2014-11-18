
function mapController($scope, $http, $routeParams, PlaceFactory) {
    console.log('mapController');
    $scope.places = $routeParams.places;

    PlaceFactory.getPlaces(function(response) {
        $scope.places = response;
        PlaceFactory.placeList = $scope.places;
    });

}
