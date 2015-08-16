'use strict';

angular.module('subwman')
  .config(['$routeProvider', function ($routeProvider) {
    $routeProvider
      .when('/installedproducts', {
        templateUrl: 'views/installedProducts/installedproducts.html',
        controller: 'InstalledProductsController',
        resolve:{
          resolvedInstalledProducts: ['InstalledProducts', function (InstalledProducts) {
            return InstalledProducts.query();
          }]
        }
      })
    }]);
