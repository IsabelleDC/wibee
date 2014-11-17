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
       }

   }

});