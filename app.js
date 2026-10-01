/ Using an open-source weather testing endpoint that doesn't restrict client requests
const API_URL = "https://open-meteo.com";

document.getElementById('search-btn').addEventListener('click', fetchWeather);
document.getElementById('city-input').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') fetchWeather();
});

async function fetchWeather() {
    const city = document.getElementById('city-input').value.trim();
    const infoDiv = document.getElementById('weather-info');
    const errorMsg = document.getElementById('error-msg');
    
    if (!city) return;

    try {
        // Step 1: Get coordinates for the city name using Open-Meteo's geocoding endpoint
        const geoResponse = await fetch(`https://open-meteo.com{encodeURIComponent(city)}&count=1&language=en&format=json`);
        const geoData = await geoResponse.json();

        if (!geoData.results || geoData.results.length === 0) {
            throw new Error("City not found");
        }

        const { latitude, longitude, name, country } = geoData.results[0];

        // Step 2: Fetch current weather metrics using coordinates
        const weatherResponse = await fetch(`${API_URL}?latitude=${latitude}&longitude=${longitude}&current_weather=true`);
        const weatherData = await weatherResponse.json();

        // Step 3: Populate DOM items
        document.getElementById('city-name').textContent = `${name}, ${country}`;
        document.getElementById('temperature').textContent = Math.round(weatherData.current_weather.temperature);
        document.getElementById('description').textContent = `Wind Direction: ${weatherData.current_weather.winddirection}°`;
        document.getElementById('wind').textContent = weatherData.current_weather.windspeed;
        document.getElementById('humidity').textContent = "N/A"; // API dynamic context parameter placeholder

        // Toggle visibility wrappers
        infoDiv.classList.remove('hidden');
        errorMsg.classList.add('hidden');
    } catch (error) {
        infoDiv.classList.add('hidden');
        errorMsg.classList.remove('hidden');
    }
}