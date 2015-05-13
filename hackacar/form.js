'use strict';

$(function () {
    var customerInfo = {};
    
    // Google address auto complete
    var initializeSearch = function () {
        var cityInput,
            autocomplete,
            options = {
                types: [],
                componentRestrictions: { country: "us"}
            };
            
        $('#to-be-hidden').hide();
        
        cityInput = document.getElementById('destination');
        autocomplete = new google.maps.places.Autocomplete(cityInput, options);
        
        google.maps.event.addListener(autocomplete, 'place_changed', function () {
            var place = autocomplete.getPlace();
            customerInfo.lat = place.geometry.location.lat();
            customerInfo.long = place.geometry.location.lng();
        });
    };
    
     google.maps.event.addDomListener(window, 'load', initializeSearch);
    
    // showResults() - unhide result section and animate it up
    var showResults = function () {
        $("#to-be-hidden").show();
        $('html, body').animate({ scrollTop: $("#to-be-hidden").offset().top + 10 }, { duration: 1500 });
    };
    
    // my location map
 
});

