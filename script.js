const map = L.map('map').setView([19.0485386, -98.2166069], 15)

const Stadia_AlidadeSmooth = L.tileLayer('https://tiles.stadiamaps.com/tiles/alidade_smooth/{z}/{x}/{y}{r}.{ext}', {
	minZoom: 0,
	maxZoom: 20,
	attribution: '&copy; <a href="https://www.stadiamaps.com/" target="_blank">Stadia Maps</a> &copy; <a href="https://openmaptiles.org/" target="_blank">OpenMapTiles</a> &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
	ext: 'png'
}).addTo(map);

function createMarkers(locations, content) 
{
    for (let location of locations) 
		{
        let info = content.find(item => item.id === location.id);

        let popup = `
            <h2>${info.titulo}</h2>
            <p>${info.nota}</p>
            <img src="${info.foto}" alt="${info.titulo}">
        `;

        if (info.audio !== null) {
            popup += `
                <audio controls>
                    <source src="${info.audio}" type="audio/mpeg">
                    Tu navegador no soporta audio.
                </audio>
            `;
        }

        L.marker([location.lat, location.lng])
            .addTo(map)
            .bindPopup(popup);
    }
}

function loadLocations()
{
	return fetch("src/data/locations.json")
        .then(response => response.json());
}

function loadContent()
{
	return fetch("src/data/content.json")
        .then(response => response.json());
}

Promise.all([

		loadLocations(),
		loadContent()

	]).then(([locations, content]) => {

		createMarkers(locations, content)
});