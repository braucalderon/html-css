// Initialize and add the map

function initMap(){
    const loc = { lat: 42.361145, lng: -71.057083};

    // Centered map on location
    const map = new google.maps.Map(document.querySelector('.map')
    , {
        zoom: 14,
        center: loc
    });
    // The maker, position at location
    const maker = new google.maps.Marker({ position: loc,
        map: map});
    
}

// Opacity at the top bar
window.addEventListener('scroll', function(){
    if(window.scrollY > 150){
        document.querySelector('#navbar').style.opacity = 0.9;

    }else{
        document.querySelector('#navbar').style.opacity = 1;
    }
});
// Smooth Scrolling
// $('#navbar a, .btn').on('click', function(event){
  
//     if(this.hash !==''){
//         event.preventDefault();

//         const hash = this.hash;

//         $('html. body').animate(
//             {
//                 scrollTop: $(hash).offset().top -100
//             },
//             // speed on how the scroll will go
//             800
//         );
//     }
// });