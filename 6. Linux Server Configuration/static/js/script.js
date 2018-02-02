function start() {
        gapi.load('auth2', function () {
            auth2 = gapi.auth2.init({
                client_id: '652796629988-4878v3rgdjckh6si2056ma0qre03q283.apps.googleusercontent.com'
            });
        });
    }

    $('#signinButton').click(function () {
        auth2.grantOfflineAccess().then(signInCallback);
    });

    function signInCallback(authResult) {
        if (authResult['code']) {
            $('#signinButton').attr('style', 'display: none');

            $.ajax({
                type: 'POST',
                url: '/connect',
                processData: false,
                data: authResult['code'],
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                },
                contentType: 'application/octet-stream; charset=utf-8',
                success: function (result) {
                    if (result) {
                        location.reload();
                    }
                    else if (authResult['error']) {
                        console.log('There was an error: ' + authResult['error']);
                    }
                }
            });
        }
    }