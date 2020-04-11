let a = require('./nod.js') 

console.log(a.helloPerson('Norberto'));

let h = require('http');

h.createServer(function(req, res){
    res.write('hello Bruja !!!###');
    res.end();

}).listen(8080);