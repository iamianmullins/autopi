// Create an instance of Wia
// Device secret key
var wia = require('wia')('d_sk_HolYFwZ6E3J3cjfiEp8gBsmS');

var BlynkLib = require('blynk-library');

var blynk = new BlynkLib.Blynk('ca4QwEA0UPvvkfS1988T6A9UHBE0FuVU');
var v2 = new blynk.VirtualPin(2);


v2.on('write', function(param) {
  console.log('V2:', param);
 console.log(param[0]);

// Listen for a successful connection to the MQTT API
wia.stream.on('connect', function() {
  // Publish a location
  wia.locations.publish({
    latitude: param[0],
    longitude: param[1]
  });
});

// Connect to the MQTT API
wia.stream.connect();
});



