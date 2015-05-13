(function() {
  var MojioClient, config, mojio_client;
  MojioClient = this.MojioClient;
  // Create configurations with your app information.
  config = {
    application: '[bf316366-b86a-4b09-8137-1c9657b2daba]', // Fill in your app id here!
    redirect_uri: '[http://localhost:5000/]', // Fill in you redirect uri here! (Ex. 'http://localhost:4093/index.html')
    hostname: 'api.moj.io',
    version: 'v1',
    port: '443',
    scheme: 'https',
    live: false // This will connect your app to the sandbox environment, change it to true to go live.
  };
  // Create a new client with your configurations.
  mojio_client = new MojioClient(config);
});