document.addEventListener('DOMContentLoaded', function () {
    loadHouses();

    document.getElementById('addHouseForm').addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(this);
        const houseData = {
            address: formData.get('address'),
            occupants: formData.get('occupants'),
            poultry: formData.get('poultry') === 'on',
            vegetable_garden: formData.get('vegetableGarden') === 'on',
            fish_pond: formData.get('fishPond') === 'on'
        };

        fetch('/houses', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(houseData),
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);
            loadHouses();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});

function loadHouses() {
    fetch('/houses')
    .then(response => response.json())
    .then(data => {
        const housesContainer = document.getElementById('houses');
        housesContainer.innerHTML = '';
        data.forEach(house => {
            const houseElement = document.createElement('div');
            houseElement.innerHTML = `
                <p><strong>Address:</strong> ${house.address}</p>
                <p><strong>Occupants:</strong> ${house.occupants}</p>
                <p><strong>Poultry:</strong> ${house.poultry ? 'Yes' : 'No'}</p>
                <p><strong>Vegetable Garden:</strong> ${house.vegetable_garden ? 'Yes' : 'No'}</p>
                <p><strong>Fish Pond:</strong> ${house.fish_pond ? 'Yes' : 'No'}</p>
            `;
            housesContainer.appendChild(houseElement);
        });
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}