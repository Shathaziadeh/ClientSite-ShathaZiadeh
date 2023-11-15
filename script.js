// script.js

function handleSectionClick(section) {
    console.log(`Button clicked: ${section}`);
    var container = document.getElementById('background-container');

    if (container) {
        var existingImage = container.querySelector('img');
        if (existingImage) {
            container.removeChild(existingImage);
        }

        var image = document.createElement('img');
        image.classList.add('section-image');

        switch (section) {
            case 'home':
                image.src = staticPath + 'images/home.jpg';
                break;
            case 'cassettes':
                image.src = staticPath + 'images/cassettes.jpg';
                break;
            case 'cds':
                image.src = staticPath + 'images/cds.jpg';
                break;
            case 'equipment':
                image.src = staticPath + 'images/equipment.jpg';
                break;
            case 'records':
                image.src = staticPath + 'images/records.jpg';
                break;
            
        }

        container.appendChild(image);
    } else {
        console.error('Container element not found.');
    }
}

var staticPath = '/static/recordrental/';
