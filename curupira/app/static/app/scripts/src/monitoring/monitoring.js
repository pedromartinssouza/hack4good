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

var pins = [
    {
        lat: -29.9189,
        lng: -51.1781,
        color: 'positive',
        name: 'Canoas'
    },
    {
        lat: -30.0884,
        lng: -51.0238,
        color: 'careful',
        name: 'Viamão'
    },
    {
        lat: -30.0277,
        lng: -51.2287,
        color: 'alert',
        name: 'Porto Alegre'
    },
    {
        lat: -29.7848,
        lng: -55.7757,
        color: 'positive',
        name: 'Alegrete'
    }
]

let icons;

function setup() {

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

    monitoringMap = mappa.tileMap(options);

    monitoringMap.overlay(canvas);
    monitoringMap.onChange(drawMeteorites);

    fill(109, 255, 0);
    stroke(100);
}

function centerCoordinate() {
    var lat = pins.reduce((acc, curr) => Number(acc) + Number(curr.lat), 0);
    var lng = pins.reduce((acc, curr) => Number(acc) + Number(curr.lng), 0);

    return { lat: lat / pins.length, lng: lng / pins.length };
}

function draw() { }

function drawMeteorites() {
    clear();

    for (var i = 0; i < pins.length; i++) {

        const latitude = Number(pins[i].lat);
        const longitude = Number(pins[i].lng);
        if (monitoringMap.map.getBounds().contains([latitude, longitude])) {
            const pos = monitoringMap.latLngToPixel(latitude, longitude);
            image(icons[pins[i].color], pos.x - PIN_SIZE/2, pos.y - PIN_SIZE/2, PIN_SIZE, PIN_SIZE);
        }
    }

}

function mousePressed() {
    handlePinOnRangeWhenMousePressed();
}

function handlePinOnRangeWhenMousePressed(){
    var pinOnRange = pins.find((pin) => {
        const pinPos = monitoringMap.latLngToPixel(pin.lat, pin.lng);
        return (dist(mouseX, mouseY, pinPos.x, pinPos.y) < CLICK_THRESHOLD_DISTANCE);
    })
    populatePane(pinOnRange);
    toggleRightPane(true);
}

function populatePane(pin) {
    var title = document.getElementById("loc-details-title");
    var lat = document.getElementById("loc-details-lat");
    var lng = document.getElementById("loc-details-lng");
    title.innerHTML = pin.name;
    lat.innerHTML = pin.lat;
    lng.innerHTML = pin.lng;
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
