/**
 * Module dependencies.
 */

var express     = require('express'),
    http        = require('http'),
    path        = require('path'),
    _           = require('lodash-node/underscore'),
    moment      = require( 'moment'),
    expressJwt  = require('express-jwt'),
    request     = require('request'),
    io          = require('socket.io').listen(9001);

    app = express();

var allowCrossDomain = function(req, res, next) {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
    res.header('Access-Control-Allow-Headers', 'Accept, Content-Type, Authorization, Content-Length, X-Requested-With');
    // intercept OPTIONS method
    if ('OPTIONS' == req.method) {
      res.send(200);
    }
    else {
      next();
    }
};


app.set('port', 9000);
app.set('views', __dirname + '/views');
app.set('view engine', 'jade');
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.bodyParser());
app.use(express.methodOverride());
app.use(express.static(path.join(__dirname, 'public')));
app.use(express.cookieParser());
app.configure(function(){
  app.use(allowCrossDomain);
  //app.use('/api', expressJwt({secret: secret}));
})
app.use(app.router);

// development only
if ('development' == app.get('env')) {
  app.use(express.errorHandler());
}

process.on('uncaughtException', function (err) {
    console.error('Uncaught exception: ' + err);
    console.error(err.stack);
});

//app.post('/api/game', documents.getNews);
//app.get('/api/documents/top20news', documents.getTop20News);

app.get('/', function (req, res) {
  //res.render('index', {});
  res.send( "index!");
});


app.get('/car', function(req,res) {

res.send("car!");

});

app.post('/car/mojio', function(req,res) {

console.log(req.body);


});


http.createServer(app).listen(app.get('port'), function(){
  console.log('Stare Contest 2.0\'s Express Server is now Listening on Port [' + app.get('port')+']...');
});