wibeeApp.factory('Category', function($resource) {
    return $resource('/api/categories/', {
            // Parameter defaults
        }, {
            // Actions
            update: {method: 'PUT'}
        }
    );
});