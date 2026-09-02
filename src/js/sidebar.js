import { map, markers, ready } from "../../map.js";

ready.then(({ locations, content }) => {
    const sidebarList = document.getElementById("sidebar-list");

    for (let location of locations) {

        const info = content.find(item => item.id === location.id);
        const li = document.createElement("li");

        li.classList.add("sidebar-item");
        li.textContent = info.titulo;
        
        li.addEventListener("click", () => {
            map.setView([location.lat, location.lng], 17);
            markers[location.id].openPopup();
        });

        sidebarList.appendChild(li);
    }
});