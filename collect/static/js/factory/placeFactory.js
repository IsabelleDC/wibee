wibeeApp.factory('PlaceFactory', function($http){
   return{
       placeList: [],
       getPlaces: function(callback) {
           $http.get('/api/places/')
               .success(function(places){
                   callback(places);
               }).error(function(error) {
                   console.log(error);
               });
       },

        deletePlace: function(place, callback) {
            // I don't think you need the extra + '' here, or may want to add a trailing slash + '/'
            $http.delete('/api/places/' + place + '').success(function(response) {
                callback(response)
            }).error(function(error){
                console.log(error);
            });
        },

        updatePlace: function(place, data, callback) {
            $http.put('/api/places/' + place, data).success(function(response) {
                callback(response)
            }).error(function(error){
                console.log(error);
            });
        }

   }
});
