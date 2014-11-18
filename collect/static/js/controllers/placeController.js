function placeController($scope, $http, $routeParams, $location, PlaceFactory) {
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

    $scope.deletePlace = function() {
        PlaceFactory.deletePlace($scope.placeId, function(response){
            $location.path('/home')})
    }
    var data = $scope.place ;
    $scope.updatePlace = function() {
        PlaceFactory.updatePlace($scope.placeId, data, function(response){
            $location.path('/place')})
    }
}