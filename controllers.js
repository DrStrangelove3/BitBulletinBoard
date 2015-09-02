angular.module('BulletinBoardApp.controllers', []).
    controller('mainFeedCtrl', function($scope, $http) {
    
        $scope.vote = function(index, updown){
            $http({
                method: 'POST',
                url: "/cgi-bin/sendVote.py",
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                data: "updown=" + encodeURIComponent(updown) + "&parent=" + encodeURIComponent($scope.posts[index].msgid) + "&to=" + encodeURIComponent($scope.posts[index].chanAddress) + "&address=" + encodeURIComponent($scope.addressSelect)
            }).success(function () {});
        };
    
        $scope.post = function(){
            $http({
                method: 'POST',
                url: "/cgi-bin/sendPost.py",
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                data: "from=" + encodeURIComponent($scope.addressSelect) + "&to=" + encodeURIComponent($scope.chanSelect) + "&title=" + encodeURIComponent($scope.title) + "&url=" + encodeURIComponent($scope.url)
            }).success(function (response) {
                window.alert("Post submitted: " + response);
            }).error(function(){
                window.alert("Error: Is BitBulletinBoard and PyBitmessage running?");
            });
            
            $scope.clearInputs();
        };
    
        $scope.refresh = function(){
            $http.post("/cgi-bin/refreshPosts.py"); //TODO: Check to see is it was successfull 
            $http.post("/cgi-bin/getUpVotes.py");
            $http.post("/cgi-bin/getDownVotes.py");
            $http.get("/cgi-bin/getAddresses.py").success(function (response) {$scope.addresses = response.addresses; $scope.addressSelect = $scope.addresses[0].address;}); //TODO: Handle failure
            $http.get("/cgi-bin/getChans.py").success(function (response) {$scope.chans = response.chans; $scope.chanSelect = $scope.chans[0].address;}); //TODO: Handle failure
            $http.get("/cgi-bin/getPosts.py").success(function (response) {$scope.posts = response.posts;}); //TODO: Handle failure
        };
    
        $scope.selectPost = function(selected){
            for (n in $scope.posts){
                $scope.posts[n].active = false;
            }
            
            selected.active = true;
        };
    
        $scope.uploadImage = function(){
            var fd = new FormData();
            fd.append('file', $scope.imageFile);
            fd.append('title', $scope.title);
            fd.append('from', $scope.addressSelect);
            fd.append('to', $scope.chanSelect);
            $http.post('/cgi-bin/uploadImage.py', fd, {
            transformRequest: angular.identity,
            headers: {'Content-Type': undefined}
            })
            .success(function(response){
                window.alert("Image Submitted: " + response);
            })
            .error(function(){
                window.alert("Error: Is BitBulletinBoard and PyBitmessage running?");
            });
            
            $scope.clearInputs();
        }
        
        $scope.clearInputs = function(){
            $scope.title = "";
            $scope.url = "";
        }
        
        $scope.postTypeSelect = 'link';
        $scope.refresh();
    });