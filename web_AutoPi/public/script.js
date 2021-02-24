// Firebase configuration for the AutoPi web app
const firebaseConfig = {
  apiKey: "<APIKEY>",
  authDomain: "autopi-48de4.firebaseapp.com",
  databaseURL: "https://autopi-48de4-default-rtdb.firebaseio.com",
  projectId: "autopi-48de4",
  storageBucket: "autopi-48de4.appspot.com",
  messagingSenderId: "385747335470",
  appId: "1:385747335470:web:b227ab66d11a83777562bf"
};

firebase.initializeApp(firebaseConfig);

// Reference to the file storage service
const storage = firebase.storage();
// Reference to the database service
const database = firebase.database();

// Create camera database reference
const camRef = database.ref("photo");
const vidRef = database.ref("video");


// Sync on any updates to the DB. THIS CODE RUNS EVERY TIME AN UPDATE OCCURS ON THE DB.
camRef.limitToLast(1).on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    const image = childSnapshot.val()["image"];
    const time = childSnapshot.val()["timestampPic"];
    const lat = childSnapshot.val()["latPic"];
    const long = childSnapshot.val()["longPic"];
    const alt = childSnapshot.val()["altPic"];
    const speed = childSnapshot.val()["speedPic"];
    const description = childSnapshot.val()["descriptionPic"];
    const temperature = childSnapshot.val()["temperaturePic"];
    const coverage = childSnapshot.val()["coveragePic"];
    const storageRef = storage.ref(image);

    storageRef
    .getDownloadURL()
    .then(function(url) {
      console.log(url);
      document.getElementById("image").src = url;
      document.getElementById("timestampPic").innerText = time;
      document.getElementById("latitudePic").innerText = lat;
      document.getElementById("longitudePic").innerText = long;
      document.getElementById("altPic").innerText = alt;
      document.getElementById("speedPic").innerText = speed;
      document.getElementById("descriptionPic").innerText = description;
      document.getElementById("temperaturePic").innerText = temperature;
      document.getElementById("coveragePic").innerText = coverage;
      
      const longi = parseFloat(long);
      const lati = parseFloat(lat);  
              // Latest location of AutoPi
              const dataLoc = { lat: lati, lng: longi};
              // The map, centered at accident coordinates
              const map = new google.maps.Map(document.getElementById("map"), {
                zoom: 12,
                center: dataLoc,
              });
              // The marker, positioned at PiPic coordinates
              const marker = new google.maps.Marker({
                position: dataLoc,
                map: map,
              });
              map.setMapTypeId(google.maps.MapTypeId.HYBRID);
            })
    .catch(function(error) {
      console.log(error);
    });
  });
});



// Sync on any updates to the DB. THIS CODE RUNS EVERY TIME AN UPDATE OCCURS ON THE DB.
vidRef.limitToLast(1).on("value", function(snapshot) {
  snapshot.forEach(function(childSnapshot) {
    const vid = childSnapshot.val()["vid"];
    const time = childSnapshot.val()["timestampVid"];
    const lat = childSnapshot.val()["latVid"];
    const long = childSnapshot.val()["longVid"];
    const alt = childSnapshot.val()["altVid"];
    const speed = childSnapshot.val()["speedVid"];
    const description = childSnapshot.val()["descriptionVid"];
    const temperature = childSnapshot.val()["temperatureVid"];
    const coverage = childSnapshot.val()["coverageVid"];

    const storageRef = storage.ref(vid);

    storageRef
    .getDownloadURL()
    .then(function(url) {
      console.log(url);
      document.getElementById("image").src = url;
      document.getElementById("timestampVid").innerText = time;
      document.getElementById("latitudeVid").innerText = lat;
      document.getElementById("longitudeVid").innerText = long;
      document.getElementById("altVid").innerText = alt;
      document.getElementById("speedVid").innerText = speed;
      document.getElementById("descriptionVid").innerText = description;
      document.getElementById("temperatureVid").innerText = temperature;
      document.getElementById("coverageVid").innerText = coverage;
      
      const longi = parseFloat(long);
      const lati = parseFloat(lat);  
              // Latest location of AutoPi
              const dataLoc = { lat: lati, lng: longi};
              // The map, centered at accident coordinates
              const map = new google.maps.Map(document.getElementById("map2"), {
                zoom: 12,
                center: dataLoc,
              });
              // The marker, positioned at accident coordinates
              const marker = new google.maps.Marker({
                position: dataLoc,
                map: map,
              });
              map.setMapTypeId(google.maps.MapTypeId.HYBRID);
            })
    .catch(function(error) {
      console.log(error);
    });
  });
});
