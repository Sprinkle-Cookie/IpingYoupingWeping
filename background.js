

mysocket = new WebSocket("ws://linus.casa:8000/");
mysocket.onopen = function(evt) { console.log('opened!');}

// printout out the lags measured from linus
mysocket.onmessage = function(evt) {
    data = JSON.parse(evt.data);
    console.log('received message from Linus!');
    console.log(data);
}


    
browser.browserAction.onClicked.addListener(function() {
    console.log("button clicked! sending lag-measure request to Linus!");
    
    // send message to Linus

});
