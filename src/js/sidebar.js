import { map, markers, ready } from "../../map.js";
 
ready.then(({ locations, content }) => {
    const sidebarList = document.getElementById("sidebar-list");
 
    for (let location of locations) {
 
        const info = content.find(item => item.id === location.id);
        const li = document.createElement("li");
 
        li.classList.add("sidebar-item");
        li.textContent = info.titulo;
        
        li.addEventListener("click", () => {
            const zoom = 15;
            const offsetPoint = map.project([location.lat, location.lng], zoom).subtract([0, 300]);
            const offsetLatLng = map.unproject(offsetPoint, zoom);
 
            map.setView(offsetLatLng, zoom, {
                animate: true,
                duration: 1.5,
                easeLinearity: 0.25
            });
            map.once('moveend', () => {
                markers[location.id].openPopup();
            });
        });
 
        sidebarList.appendChild(li);
    }
});