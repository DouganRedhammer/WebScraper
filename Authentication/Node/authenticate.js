var request = require('request');
var cheerio = require('cheerio');

var username= process.argv[2] ;
var password= process.argv[3] ;

var auth = "Basic " + new Buffer(username + ":" + password).toString("base64");

request.post({
  	uri: 'https://github.com/login',
            "Authorization" : auth,

}, function(err, res, body){
	if(err) {
        console.log("There was an Error" + err)
		return;
	}

	request('https://github.com/'+username, function(err, res, body) {
		if(err) {
            console.log("There was an Error" + err)
			return;
		}
    var $ = cheerio.load(body);

		var text = $('.vcard-fullname').text();
		console.log(text)

	});
});