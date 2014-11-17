function placeController($scope, $http, $routeParams, PlaceFactory) {
    console.log('placeController');
    $scope.placeId = $routeParams.placeId;

    $http.get('/api/places/' + $scope.placeId)
        .success(function (place) {
            console.log(place);
            $scope.place = place;
        })
        .error(function (error) {
            console.log('error');
            console.log(error);
        });
}