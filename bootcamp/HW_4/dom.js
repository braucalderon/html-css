document.querySelector('#color').addEventListener('change', function(e) {
    let color = document.getElementById('#color')
    if(color){
        
        console.log(e);
    }
    
})
// help me on how make the button to create copies 

let addSq = document.getElementById('#btn-duplicate');
console.log("it works");

addSq.addEventListener('click',function(){
    let sq = document.getElementById('#square')
    let clone = sq.firstElementChild.cloneNode(true)
    sq.appendChild(clone)

});
    
    
    // let cln = btn_1.cloneNode(true)

    // document.getElementById('#container').appendChild(cln)

    console.log('it works');
    
    
    


// const sq = document.ready(function(){
//     sq('#sq-duplicate').click(function(){
//         sq('#square').clone().appendTo('#container')
//     })
// })
