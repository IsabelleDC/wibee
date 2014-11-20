function homeController($scope, $http, PlaceFactory) {


    //Get places

    PlaceFactory.getPlaces(function(response) {
        $scope.places = response;
        PlaceFactory.placeList = $scope.places;
    });


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

    console.log()

    $scope.savePlace = function() {
        console.log('clicked');
        console.log($scope.place);

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

        console.log(data);

        $http.post('/api/places/', data)
            .success(function (place) {
                console.log('success');
                console.log(place);
                PlaceFactory.placeList.push(place);
                $scope.newPlace = false;
            })
            .error(function (error) {
                console.log('error');
                console.log(error);
            })
    };

    $scope.setCategory = function (newCategory) {
        console.log(newCategory);
        $scope.currentCategory = newCategory;
    };

}


