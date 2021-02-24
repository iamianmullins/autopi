
// Create an instance of Wia
// Device secret key
var wia = require('wia')('x_xx_xxxxxxxxxxxxxxxxxxxxxxxx');

//Blynk credentials and v pin from smartphone app
var BlynkLib = require('blynk-library');
var blynk = new BlynkLib.Blynk('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx');
var v2 = new blynk.VirtualPin(2);


v2.on('write', function(param) {
  console.log('V2:', param);

 // Publish current location to wia iot platform
  wia.locations.publish({
    latitude: param[0],
    longitude: param[1]
  })

});

