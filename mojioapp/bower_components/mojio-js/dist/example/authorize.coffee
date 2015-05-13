MojioClient = @MojioClient

###

    Below, fill in your application specific details to make this code work

config =
    application: 'Your-Application-Key-Here' # Fill in your application key here
    redirect_uri: 'Your-Logout-redirect_url-Here' # Fill in your redirect url here (Ex. 'http://localhost:63342/mojio-js/example/authorize.html')
    live: false # Set to true if using the live environment
###

config =
    application: 'Your-Application-Key-Here',
    hostname: 'api.moj.io'
    version: 'v1'
    port: '443'
    scheme: 'https'
    redirect_uri: 'Your-Logout-redirect_url-Here'
#    redirect_uri: 'http://localhost:63342/mojio-js/example/authorize.html'
    live: false

mojio_client = new MojioClient(config)
User = mojio_client.model('User')

(() ->
    if (config.application == 'Your-Application-Key-Here')
        div = document.getElementById('result')
        div.innerHTML += 'Mojio Error:: Set your application key in authorize_complete.js.  '
        return

    if (config.redirect_uri == 'Your-Logout-redirect_url-Here')
        div = document.getElementById('result')
        div.innerHTML += 'Mojio Error:: Set the logout redirect url in authorize_complete.js and register it in your application at the developer center.  '
        return

    mojio_client.token((error, result) ->
        if (error)
            if confirm("Authorize Redirect, token could not be retrieved, you are logged out. Try again?")
                mojio_client.authorize(config.redirect_uri)
        else
            alert("Authorization Successful.")

            div = document.getElementById('result')
            div.innerHTML += 'POST /login<br>'
            div.innerHTML += JSON.stringify(result)
            mojio_client.get(User, {}, (error, result) ->
                if (error)
                    div = document.getElementById('result2')
                    div.innerHTML += 'Get User Error'+error+'<br>'
                else
                    users = mojio_client.getResults(User, result)

                    user = users[0]
                    div = document.getElementById('result2')
                    div.innerHTML += 'Query /User<br>'
                    div.innerHTML += JSON.stringify(result)
                    if confirm('You are logged in, logout and try again?')
                        mojio_client.unauthorize(config.redirect_uri)
            )
    )
)()