let ws;

let vehicules = new Map();
let recommandations = new Map();

let locations = new Map([["linas",[48.624418, 2.243595,18]],
                                ["vigo",[42.102571, -8.614376,19]],
                                ["none",[0,0,3]]]);

let mapMetaDatas = [["bitmap/monthlery.jpg", 48.622197,2.235964,48.628130,2.251932],
                    ["bitmap/vigo.jpg", 42.100756, -8.616682,42.104132, -8.612138]];

let carIcon = L.icon({iconUrl: 'lib/img/car.png',iconSize: [15, 15]});
let projectionIcon = L.icon({iconUrl: 'lib/img/proj.png',iconSize: [25, 25]});

window.addEventListener('load',function(event) {

    selector = document.getElementById("locations");
    tuple = locations.get(selector[selector.selectedIndex].value);

    map = new L.Map('map');
    map.setView([tuple[0], tuple[1]],tuple[2]);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 19,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox.streets'
    }).addTo(map);

    marker = L.marker([48.624418, 2.243595],{icon: projectionIcon}).bindTooltip("PUTE",{
        permanent: true,
        direction: 'top',
        opacity: 0.5
    });
    marker.addTo(map);

    mapMetaDatas.forEach(function (elem) {
        L.imageOverlay(elem[0], [[elem[1],elem[2]],[elem[3],elem[4]]]).addTo(map);
    });


    selector.addEventListener('change',function () {
        tuple = locations.get(selector[selector.selectedIndex].value);
        map.setView([tuple[0], tuple[1]],tuple[2]);
    });

    document.getElementById("start-button").addEventListener('click', function(){
        button = this;
        if (button.id.includes("stop-button")) {
            button.id = "start-button";
            console.log("Track stopped !");
            notif.innerText = "Connection closed : "+window.location.hostname+":8081";
            ws.close();
        } else {
            button.id = "stop-button";
            ws = new WebSocket('ws://'+window.location.hostname+':8081');

            notif = document.getElementById("notif-entry");
            ws.onopen = function () {
                notif.className = "info";
                notif.innerText = "Connected on : "+window.location.hostname+":8081";
                setTimeout(function () {
                    notif.className = "";
                },5000);
            };

            ws.onmessage = function (message) {
                handleTelemetryPaquet(message.data);
            };

            ws.onclose = function(e) {
                console.log('Socket is closed.');
                notif.className = "error";
                button.id = "start-button";
                setTimeout(function () {
                    notif.className = "";
                },5000);
                button.innerText = window.getComputedStyle(button,null).getPropertyValue('content').split('"')[1];
            };

            ws.onerror = function(err) {
                console.error('Socket encountered error');
                notif.innerText = "Connection failed to : "+window.location.hostname+":8081";
                ws.close();
            };
        }
        this.innerText = window.getComputedStyle(this,null).getPropertyValue('content').split('"')[1];
    });

});

function handleTelemetryPaquet(str) {
    try {
        obj = JSON.parse(str);
        if (obj.type === "notify") {
            if (vehicules.get(obj.uuid) !== undefined) {
                vehicules.get(obj.uuid).setLatLng([obj.position.latitude,obj.position.longitude]).update();
            } else {
                marker = L.marker([obj.position.latitude,obj.position.longitude],{icon: carIcon}).bindTooltip(obj.uuid,{
                    permanent: true,
                    direction: 'top',
                    opacity: 0.5
                });
                marker.addTo(map);
                vehicules.set(obj.uuid,marker);
            }
        } else if (obj.type === "recommandation") {
            if (recommandations.get(obj.uuid) !== undefined) {
                recommandations.get(obj.uuid).setLatLng([obj.position.latitude,obj.position.longitude],{rotationAngle: obj.heading}).update();
            } else {
                marker = L.marker([obj.position.latitude,obj.position.longitude],{icon: projectionIcon,rotationAngle: obj.heading}).bindTooltip(obj.uuid,{
                    permanent: true,
                    direction: 'top',
                    opacity: 0.5
                });
                marker.addTo(map);
                recommandations.set(obj.uuid,marker);
            }
        }
    } catch (e) {
        console.error("Invalid JSON : ", e);
    }
}