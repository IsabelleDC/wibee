function homeController($scope, $http, PlaceFactory) {

    //Get places

    PlaceFactory.getPlaces(function(response) {
        $scope.places = response;
        PlaceFactory.placeList = $scope.places;
    });


    $http.get('/api/categories/')
        .success(function (data) {
            $scope.categories = data;
        }).error(function (error) {
            console.log(error);
        });

    //Create new place
    $scope.newPlace = false;
    $scope.createPlace = function () {
        $scope.newPlace = true;
    };

    $scope.savePlace = function() {

        var data = {
            "name": $scope.name,
            "description": $scope.description,
            "category": $scope.category,
            "street":$scope.street,
            "city": $scope.city,
            "country": $scope.country,
            "image": $scope.image,
            "owner": 1,
            "status": $scope.visited
        };

        $http.post('/api/places/', data)
            .success(function (place) {
                PlaceFactory.placeList.push(place);
                $scope.newPlace = false;
                $scope.name = '';
                $scope.description = '';
                $scope.category = null;
                $scope.street = '';
                $scope.city = '';
                $scope.country = '';
                $scope.image = '';
                $scope.visited = false;
            })
            .error(function (error) {
                console.log(error);
            })
    };

    $scope.setCategory = function (newCategory) {
        $scope.currentCategory = newCategory;
    };

}


