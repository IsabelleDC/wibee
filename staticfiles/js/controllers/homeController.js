function homeController($scope, $http, PlaceFactory, PlaceResource) {
    console.log('homeController');

    //Get projects
    if (PlaceFactory.placeList.length > 0) {
        $scope.places = PlaceFactory.placeList;
        $scope.totalItems = $scope.places.length;
    } else{
        PlaceFactory.getPlaces(function(placeResponse) {
            $scope.places = placeResponse;
            console.log(placeResponse);
            PlaceFactory.placeList = $scope.places;
        });

}

    $http.get('/api/categories/')
        .success(function (data) {
//            console.log(data);
            $scope.categories = data;
//            console.log($scope.categories);
        }).error(function (error) {
            console.log("didn't work");
            console.log(error);
        });

    //Create new place
    $scope.newPlace = false;
    $scope.createPlace = function () {
        console.log('newPlace clicked');
        $scope.newPlace = true;
    };

    $scope.savePlace = function() {
        console.log('clicked');

        var data = {
            "name": $scope.name,
            "description": $scope.description,
            "category":$scope.category,
            "city":$scope.city,
            "country": $scope.country,
            "owner":1
        };

        console.log(data);

        $http.post('/api/places/', data)
            .success(function (place) {
                console.log('success');
                console.log(place);
                PlaceFactory.placeList.push(place);
            })
            .error(function (error) {
                console.log('error');
                console.log(error);
            })
    };


}


