'use strict';

angular.module('subwman')
  .controller('InstalledProductsController', ['$scope', '$modal', 'resolvedInstalledProducts', 'InstalledProducts',
    function ($scope, $modal, resolvedInstalledProducts, InstalledProducts) {

      $scope.installedproducts = resolvedInstalledProducts;

      $scope.create = function () {
        $scope.clear();
        $scope.open();
      };

      $scope.update = function (id) {
        $scope.installedProducts = InstalledProducts.get({id: id});
        $scope.open(id);
      };

      $scope.delete = function (id) {
        InstalledProducts.delete({id: id},
          function () {
            $scope.installedproducts = InstalledProducts.query();
          });
      };

      $scope.save = function (id) {
        if (id) {
          InstalledProducts.update({id: id}, $scope.installedProducts,
            function () {
              $scope.installedproducts = InstalledProducts.query();
              $scope.clear();
            });
        } else {
          InstalledProducts.save($scope.installedProducts,
            function () {
              $scope.installedproducts = InstalledProducts.query();
              $scope.clear();
            });
        }
      };

      $scope.clear = function () {
        $scope.installedProducts = {
          
          "name": "",
          
          "id": ""
        };
      };

      $scope.open = function (id) {
        var installedProductsSave = $modal.open({
          templateUrl: 'installedProducts-save.html',
          controller: 'InstalledProductsSaveController',
          resolve: {
            installedProducts: function () {
              return $scope.installedProducts;
            }
          }
        });

        installedProductsSave.result.then(function (entity) {
          $scope.installedProducts = entity;
          $scope.save(id);
        });
      };
    }])
  .controller('InstalledProductsSaveController', ['$scope', '$modalInstance', 'installedProducts',
    function ($scope, $modalInstance, installedProducts) {
      $scope.installedProducts = installedProducts;

      

      $scope.ok = function () {
        $modalInstance.close($scope.installedProducts);
      };

      $scope.cancel = function () {
        $modalInstance.dismiss('cancel');
      };
    }]);
