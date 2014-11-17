wibeeApp.factory('PlaceResource', function($resource) {
    return $resource('/places/', {
            //paramDefaults
        }, {
            //Actions
            update: {method: 'PUT'}

        }
    );
});