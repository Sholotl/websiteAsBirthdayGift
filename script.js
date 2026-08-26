const map = L.map('map').setView([19.062556, -98.306361], 100)

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map)

L.marker([19.062556, -98.306361]).addTo(map).bindPopup('Chama mi amol').openPopup();