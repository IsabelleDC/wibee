wibeeApp.factory('PlaceFactory', function($http){
   return{
       placeList: [],
       getPlaces: function(callback) {
           $http.get('/api/places/')
               .success(function(places){
                   callback(places);
               }).error(function(error) {
                   console.log('error');
                   console.log(error);
               });
       },

        deletePlace: function(place, callback) {
            console.log('place id: ' + place);
            $http.delete('/api/places/' + place + '').success(function(response) {
                callback(response)
            }).error(function(error){
                console.log(error)
            })
        },

        updatePlace: function(place, data, callback) {
            console.log('place id: ' + place );
            $http.patch('/api/places/' + place, data).success(function(response) {
                callback(response)
            }).error(function(error){
                console.log(error)
            })
        }

   }
});