import "leaflet";
import "leaflet/dist/leaflet.css";
import markerIcon from 'leaflet/dist/images/marker-icon.png';
import markerIcon2x from 'leaflet/dist/images/marker-icon-2x.png';
import markerShadow from 'leaflet/dist/images/marker-shadow.png';
import "./Leaflet.AccuratePosition.js";
import "leaflet-control-custom";

document.addEventListener("DOMContentLoaded", function(){
    
    var map;
    var marker = "";
    var tipoBoton;
    const icon = L.icon({
        iconUrl: markerIcon,
        iconRetinaUrl: markerIcon2x,
        shadowUrl: markerShadow,
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });


    function onMapClick(e) {
        if (marker != "") {
          map.removeLayer(marker);
        } else {
        //   contratanos.classList.remove("invisible");
        //   ttubicacion.classList.remove("animate-bounce-bottom");
        }
        marker = L.marker(e.latlng, {
          icon: icon
        }).addTo(map);
        console.log(e.latlng);
      }
    
      function LoadOverlay(status) {
        overlay.classList.toggle("invisible");
        spinner.classList.toggle("invisible");
        status ? map.off('click', onMapClick) : map.on('click', onMapClick);
      }



    function initLeaflet() {
        // Solo inicializar el mapa una vez
        if (!map) {

            map = L.map('map', {
                center: [-34.160000, -70.840000],
                zoom: 5,
                zoomControl: true
              });

// Definir capas de mapas
var openStreetMap_Mapnik = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 20,
    attribution: '© OpenStreetMap contributors'
});

var esri_WorldImagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
    maxZoom: 19,
    attribution: 'Tiles © Esri — Source: Esri, i-cubed, USDA, USGS, AEX, GeoEye, Getmapping, Aerogrid, IGN, IGP, UPR-EGP, and the GIS User Community'
});

// Agregar una capa al mapa por defecto
esri_WorldImagery.addTo(map);

// Opciones de capas base
var baseMaps = {
    "OpenStreetMap": openStreetMap_Mapnik,
    "Esri WorldImagery": esri_WorldImagery
};

// Agregar control de capas al mapa
L.control.layers(baseMaps).addTo(map);
            L.control.custom({
                position: 'topright',
                content: `    
                        <svg class="sombra" fill="none" stroke="currentColor" stroke-linecap="round" stroke-width="2" viewBox="0 0 24 24">
                          <path  d="M2 12h3m14 0h3M12 2v3m0 14v3" />
                          <circle cx="12" cy="12" r="7" />
                          <circle cx="12" cy="12" r="3" />
                        </svg>`,
                classes: 'block  ml-auto h-12 w-12 bg-white rounded-md border border-black',
                id: 'ubicando',
                title: "Encuentra tu ubicación",
                style: {
                  cursor: 'pointer',
                },
                events: {
                  click: () => {
                    LoadOverlay(true);
                    map.findAccuratePosition({
                      maxWait: 10000,
                      desiredAccuracy: 20
                    });
                  },
                }
              }).addTo(map);
              function onAccuratePositionProgress(e) {
                console.log(e.accuracy);
                console.log(e.latlng);
              }
              function onAccuratePositionFound(e) {
                LoadOverlay(false);
                console.log(e.accuracy);
                console.log(e.latlng);
                map.flyTo(e.latlng, 19);
                (marker != "") ? map.removeLayer(marker) : null;
                marker = L.marker(e.latlng, {
                  icon: icon
                }).addTo(map);
              }

              function onAccuratePositionError(e) {
                LoadOverlay(false);
                alert("error");
                }
              
              map.on('accuratepositionprogress', onAccuratePositionProgress);
              map.on('accuratepositionfound', onAccuratePositionFound);
              map.on('accuratepositionerror', onAccuratePositionError);
              map.on('click', onMapClick);
        }

    }

     // Manejar la apertura del modal
    document.getElementById('ubicar-btn').addEventListener('click', function () {
        tipoBoton="ubicar";
        document.getElementById('mapModal').classList.remove('hidden');
        setTimeout(initLeaflet, 10); // Retraso para asegurar que el mapa se inicialice correctamente en el modal visible
    });

    document.getElementById('ubicarEmpalme-btn').addEventListener('click', function () {
        tipoBoton="ubicarEmpalme";
        document.getElementById('mapModal').classList.remove('hidden');
        setTimeout(initLeaflet, 10); // Retraso para asegurar que el mapa se inicialice correctamente en el modal visible
    });

    // Manejar el cierre del modal
    document.getElementById('closeModal').addEventListener('click', function () {
        document.getElementById('mapModal').classList.add('hidden');
    });

    document.getElementById('confirmarUbicacion-btn').addEventListener('click', function () {
        if (tipoBoton == "ubicar") {
            document.getElementById('lat').value = marker.getLatLng().lat.toFixed(7);
            document.getElementById('lon').value = marker.getLatLng().lng.toFixed(7);
        } else if (tipoBoton == "ubicarEmpalme") {
            document.getElementById('id_lat_energia').value = marker.getLatLng().lat.toFixed(7);
            document.getElementById('id_lon_energia').value = marker.getLatLng().lng.toFixed(7);
        }
        document.getElementById('mapModal').classList.add('hidden');
    });

    



});
