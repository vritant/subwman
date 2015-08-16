'use strict';

angular.module('subwman')
  .factory('InstalledProducts', ['$resource', function ($resource) {
    return $resource('subwman/installedproducts/:id', {}, {
      'query': { method: 'GET', isArray: true},
      'get': { method: 'GET'},
      'update': { method: 'PUT'}
    });
  }]);
