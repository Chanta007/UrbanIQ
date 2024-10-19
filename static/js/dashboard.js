async function startTrafficSimulation() {
    const response = await fetch('/simulate/traffic', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ duration: 30 })  // 30 seconds simulation
    });
    const result = await response.json();
    console.log(result);
}

async function simulateWeather() {
    const response = await fetch('/simulate/weather', { method: 'POST' });
    const result = await response.json();
    console.log(result);
}

async function renderMap() {
    const response = await fetch('/map/render');
    const result = await response.json();
    console.log(result);
    document.getElementById('map').innerText = JSON.stringify(result, null, 2);  // Display map data
}

async function stopSimulation() {
    const response = await fetch('/simulation/stop', { method: 'POST' });
    const result = await response.json();
    console.log(result);
}
