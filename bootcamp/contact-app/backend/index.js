let express = require('express')
let app = express();

// install pg
// two ports for each, one for frontend and one for backend
//  app.get('/') //it is a path
app.get('/', function(request, response){
    console.log('Hellow there');
    response.send('Hello people')
    
});
app.post('/', function(request, response){
    console.log('Hellow there');
    response.send('Hello Post')
    
});
app.get('/contact', function(request, response){
    console.log('Hellow there');
    response.send('Contact Page')
    
});

// for forms
// < form action='action.page.js' metthod='get'
// <form admin=''  method= 'Get'>

app.listen(3003, function(){
    console.log('listening');
    
});

