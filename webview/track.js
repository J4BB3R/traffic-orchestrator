window.addEventListener("load", function(event) {

    locations = new Map([["linas",[48.624418, 2.243595,18]],
                                ["vigo",[42.102571, -8.614376,19]],
                                ["none",[0,0,3]]]);

    mapMetaDatas = [["bitmap/monthlery.jpg", 48.622197,2.235964,48.628130,2.251932],
                    ["bitmap/vigo.jpg", 42.100756, -8.616682,42.104132, -8.612138]];

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

    mapMetaDatas.forEach(function (elem) {
        L.imageOverlay(elem[0], [[elem[1],elem[2]],[elem[3],elem[4]]]).addTo(map);
    });


    selector.addEventListener("change",function () {
        tuple = locations.get(selector[selector.selectedIndex].value);
        map.setView([tuple[0], tuple[1]],tuple[2]);
    });

    document.getElementById("start-button").addEventListener("click", function(){
        if (this.id.includes("stop-button")) {
            this.id = "start-button";
        } else {
            this.id = "stop-button"
        }
        this.innerText = window.getComputedStyle(this,null).getPropertyValue('content').split('"')[1];
    });

});