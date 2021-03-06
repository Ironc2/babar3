'use strict';

/**
 * @ngdoc service
 * @name BabarApp.auth
 * @description
 * # Auth
 * Service in the BabarApp.
 */
angular.module('BabarApp')
.controller('AuthCtrl', function ($location, $scope, $mdDialog, API, why) {
	this.why = why;

	this.cancel = function() {
		$mdDialog.cancel();
	};
	this.submit = function() {
		/* Try an authentication
		 * If it fails, demand another password or a cancellation
		 * It it succeeds, resolve the dialog;
		 * this will retrigger the previous request.
		 *
		 * Note that other dialogs are different: they close
		 * and only then submit. And this is precisely because
		 * of this one (can't have two dialogs at the same time).
		 */
		API.login(this.username, this.password)
		.then(function(res)  {
			// Auth successful, exit
			$mdDialog.hide(res.data.token);
		}, function(res) {
			// Auth unsuccessful, tell the user
			var wrongStatuses = [400, 401, 403];
			if(wrongStatuses.indexOf(res.status) >= 0) {
				$scope.authForm.password.$setValidity('wrong', false);
			}
			else {
				$location.url('error');
			}
		});
	};
})
.service('auth', function ($q, $mdDialog, $mdToast) {
	var header = '';
	var setHeader = function(val) {
		header = 'Token ' + val;
	};
	this.clearHeader = function() {
		header = '';
	};
	this.getHeader = function() {
		if(header === '') {
			return prompt('Please log in')
			.then(function(token) {
				setHeader(token);
				return $q.resolve(header);
			}, function() {
				return $q.reject();
			});
		}
		else {
			return $q.resolve(header);
		}
	};
	var prompt = function(why) {
		return $mdDialog.show({
			templateUrl: 'views/auth-dialog.html',
			openFrom: '#left',
			closeTo: '#right',
			clickOutsideToClose: true,
			escapeToClose: true,
			controller: 'AuthCtrl',
			controllerAs: 'auth',
			locals: {why: why},
		}).then(function(token) {
			// OK
			return $q.resolve(token);
		}, function() {
			// Cancelled
			$mdToast.showSimple('Cancelled');
			return $q.reject();
		});
	};
});
