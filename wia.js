
// Create an instance of Wia
// Device secret key
var wia = require('wia')('d_sk_HolYFwZ6E3J3cjfiEp8gBsmS');

//Blynk credentials and v pin from smartphone app
var BlynkLib = require('blynk-library');
var blynk = new BlynkLib.Blynk('ca4QwEA0UPvvkfS1988T6A9UHBE0FuVU');
var v2 = new blynk.VirtualPin(2);


v2.on('write', function(param) {
  console.log('V2:', param);

 // Publish current location to wia iot platform
  wia.locations.publish({
    latitude: param[0],
    longitude: param[1]
  })

});

