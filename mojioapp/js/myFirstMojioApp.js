(function() {
  var MojioClient, config, mojio_client;
  MojioClient = this.MojioClient;
  // Create configurations with your app information.
  config = {
    application: '[YOUR APP ID GOES HERE]', // Fill in your app id here!
    redirect_uri: '[YOUR REDIRECT URI GOES HERE]', // Fill in you redirect uri here! (Ex. 'http://localhost:4093/index.html')
    hostname: 'api.moj.io',
    version: 'v1',
    port: '443',
    scheme: 'https',
    live: false // This will connect your app to the sandbox environment, change it to true to go live.
  };
  // Create a new client with your configurations.
  mojio_client = new MojioClient(config);

  // This will check if you have an API token already 
  mojio_client.token(function(error, result) {
  if (error) {
    // There is not a token so authorize navigates to the Mojio OAuth2 sign in page
    console.log("redirecting to login.");
    mojio_client.authorize(config.redirect_uri);
  }
  else {
    // Authorization is complete, the redirect has occurred and the token has been set!
    alert("Authorization Successful.");
    div = $("#welcome");
    div.html('Authorization Result:');
    div.append(JSON.stringify(result));
  }
}).call(this);
});