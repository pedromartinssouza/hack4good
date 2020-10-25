const NAVBAR_HEIGHT = 51;
const SCROLLBAR_WIDTH = 15;
const PIN_SIZE = 32;
const CLICK_THRESHOLD_DISTANCE = 25;


const key = 'pk.eyJ1IjoiZnJpY2FyZGkiLCJhIjoiY2tnbXVtdTdiMnNkaDJxbDd4MWducDl4aSJ9.7yHPcpUHe1OygBNqz31AJw'

const options = {
    lat: 0,
    lng: 0,
    zoom: 8,
    studio: true,
    style: 'mapbox://styles/mapbox/traffic-night-v2',
};

const mappa = new Mappa('Mapbox', key);
let monitoringMap;

let canvas;
let meteorites;

let icons;

function setup() {

    // var windowHeight = window.innerHeight - NAVBAR_HEIGHT;
    // var windowWidth = window.innerWidth - SCROLLBAR_WIDTH;
    var windowHeight = window.innerHeight - NAVBAR_HEIGHT;
    var windowWidth = window.innerWidth - SCROLLBAR_WIDTH;
    canvas = createCanvas(windowWidth, windowHeight).parent('monitoring-map');


    var positive = loadImage('./../static/app/assets/icons/positive.png');
    var careful = loadImage('./../static/app/assets/icons/alert.png');
    var alert = loadImage('./../static/app/assets/icons/careful.png');
    
    icons = {
        positive,
        alert,
        careful
    };

    var coordinates = centerCoordinate();
    options.lat = coordinates.lat;
    options.lng = coordinates.lng;
    monitoringMap = mappa.tileMap(options,function () {
        monitoringMap.map.invalidateSize();
    });

    monitoringMap.overlay(canvas);
    monitoringMap.onChange(drawMeteorites);

    fill(109, 255, 0);
    stroke(100);
}

function centerCoordinate() {
    var lat = pins.reduce((acc, curr) => Number(acc) + Number(curr.lat), 0);
    var lng = pins.reduce((acc, curr) => Number(acc) + Number(curr.longit), 0);

    return { lat: lat / pins.length, lng: lng / pins.length };
}

function draw() { }

function drawMeteorites() {
    clear();

    for (var i = 0; i < pins.length; i++) {

        const latitude = Number(pins[i].lat);
        const longitude = Number(pins[i].longit);
        if (monitoringMap.map.getBounds().contains([latitude, longitude])) {
            const pos = monitoringMap.latLngToPixel(latitude, longitude);
            image(icons[pins[i].flag], pos.x - PIN_SIZE/2, pos.y - PIN_SIZE/2, PIN_SIZE, PIN_SIZE);
        }
    }

}

function mousePressed() {
    handlePinOnRangeWhenMousePressed();
}

function handlePinOnRangeWhenMousePressed(){
    var pinOnRange = pins.find((pin) => {
        const pinPos = monitoringMap.latLngToPixel(pin.lat, pin.longit);
        return (dist(mouseX, mouseY, pinPos.x, pinPos.y) < CLICK_THRESHOLD_DISTANCE);
    })
    if (pinOnRange) {
        populatePane(pinOnRange);
        toggleRightPane(true);
    }
}

function populatePane(pin) {
    var container = document.getElementById("localization-details");
    container.innerHTML = `<button type="button" class="btn btn-danger" onclick="toggleRightPane(false)">Close</button>`;
    var titleH2 = document.createElement("h2");
    titleH2.setAttribute("id", "loc-details-title")

    var titleText = document.createTextNode(pin.name);
    titleH2.appendChild(titleText);

    container.appendChild(titleH2);

    var detailsDataDiv = document.createElement("div")
    detailsDataDiv.setAttribute("id", "loc-details-data");

    detailsDataDiv.innerHTML = `Latitude: ${pin.lat}<br>Longitude: ${pin.longit}`
    container.appendChild(detailsDataDiv);

    var historicDataDiv = document.createElement("div")
    historicDataDiv.setAttribute("id", "loc-historical-data");

    for(var i = 0; i<pin.historical.length; i++) {
        var historyEntry = document.createElement('div');

        if(i == 0) {
            var currentData = document.createElement('div');
            currentData.innerHTML = "<h2>Today's data: </h2>";
            historicDataDiv.appendChild(currentData);
        }

        historyEntry.innerHTML = `<h5>Date: ${formatDate(pin.historical[i].date)}</h5>
                                    Temperature: ${pin.historical[i].temperature.temp}°C <br>
                                    Humidity: ${pin.historical[i].humidity} <br>
                                    Wind speed: ${pin.historical[i].wind.speed} m/s<br><br>`
        historicDataDiv.appendChild(historyEntry);

        if(i == 0) {
            currentData = document.createElement('div');
            currentData.innerHTML = "<h2>Historical data: </h2>";
            historicDataDiv.appendChild(currentData);
        }
    }

    container.appendChild(historicDataDiv);

}

function openCloseAddCity() {

    toggleRightPane(false);
    var rightPane = document.getElementById("localization-details");
    var isHidden = rightPane.classList.contains("hidden");
    if(isHidden) {
        toggleRightPane(true);
        populatePaneWithAddCity();
    } 
    else {
        toggleRightPane(false);
    }

}

function populatePaneWithAddCity() {

    var container = $("#localization-details").load("cities");;

}

function formatDate(unix_timestamp) {
    var date = new Date(unix_timestamp * 1000);

    var month = (parseInt(date.getMonth() + 1));
    var day = date.getDate();
    var year = date.getFullYear();
    
    return month + "-" + day  + "-" + year;

}

function toggleRightPane(show) {
    var rightPane = document.getElementById("localization-details");
    var isHidden = rightPane.classList.contains("hidden");
    if(show && isHidden) {
        rightPane.classList.remove("hidden");
    } else if (!show && !isHidden) {
        rightPane.classList.add("hidden");
    }
} 

function resizeMappa() {
    var windowHeight = window.innerHeight - NAVBAR_HEIGHT;
    var windowWidth = window.innerWidth - SCROLLBAR_WIDTH;
    resizeCanvas(windowWidth, windowHeight);
    monitoringMap.resize(canvas);
}