var request = require('request');
var cheerio = require('cheerio'); 
var fs      = require('fs');
var mkdirp = require('mkdirp');

var nextPage = '';
var numberOfPages = 0;
var mangaTitle = process.argv[2]; 
var chapterStart = process.argv[3];
var chapterEnd = process.argv[4]
  
var scrape = function(data) {
request('http://www.mangareader.net' + data, function (error, response, html) {
  if (!error && response.statusCode == 200) {
    var $ = cheerio.load(html);
	nextPage = $(".next a").attr('href')
	SaveImage( $('#img').attr('src'), $('#img').attr('alt'));

  scrape($(".next a").attr('href'));
  
  console.log(nextPage)
  }
});
}
scrape('/' + mangaTitle + '/' + chapterStart)

function GetNumberOfPages(){
		return $('#pageMenu option:last-child').text();
}

/*
	file naming conventions
	
	Title volume page
	Claymore_v06_028
	
	Title    Volume   Chapter  Page
	Claymore_v05_c022_-_011
*/

function SaveImage(imgUrl, fileName){
	request(imgUrl, {encoding: 'binary'}, function(error, response, body) {
  fs.writeFile(fileName + '.jpg', body, 'binary', function (err) {});
});
}
