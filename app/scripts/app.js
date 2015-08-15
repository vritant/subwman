'use strict';

/**
 * @ngdoc overview
 * @name subwmanApp
 * @description
 * # subwmanApp
 *
 * Main module of the application.
 */
angular
  .module('subwmanApp', [
    'ngAnimate',
    'ngCookies',
    'ngMessages',
    'ngResource',
    'ngRoute',
    'ngSanitize',
    'ngTouch'
  ])
  .config(function ($routeProvider) {
    $routeProvider
      .when('/installedProducts', {
        templateUrl: 'views/installedProducts.html',
        controller: 'InstalledProductsCtrl',
        controllerAs: 'installedProducts'
      })
      .when('/mySubscriptions', {
        templateUrl: 'views/mySubscriptions.html',
        controller: 'MySubscriptionsCtrl',
        controllerAs: 'mySubscriptions'
      })
      .when('/availableSubscriptions', {
        templateUrl: 'views/availableSubscriptions.html',
        controller: 'AvailableSubscriptionsCtrl',
        controllerAs: 'availableSubscriptions'
      })
      .otherwise({
        redirectTo: '/installedProducts'
      });
  });
