async function getWeather() {
    const city = document.getElementById("city").value;

    const response = await fetch(`/get-weather/?city=${city}`);
    const data = await response.json();

    const result = document.getElementById("result");

    if (data.error) {
        result.innerHTML = "City not found";
    } else {
        result.innerHTML = `
            <h2>${data.city}</h2>
            <p>${data.temperature} °C</p>
            <p>${data.description}</p>
            <img src="http://openweathermap.org/img/wn/${data.icon}.png">
        `;
    }
}
