async function predictAQI() {
  const data = {
    PM2_5: parseFloat(document.getElementById("pm25").value),
    PM10: parseFloat(document.getElementById("pm10").value),
    NO2: parseFloat(document.getElementById("no2").value),
    CO: parseFloat(document.getElementById("co").value),
    O3: parseFloat(document.getElementById("o3").value)
    
  };

  const resultBox = document.getElementById("result");

  try {
    const response = await fetch("http://127.0.0.1:8000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    });

    const result = await response.json();
    const category = result.AQI_Category;

    // Reset styles
    resultBox.className = "result";
    resultBox.style.display = "block";

    // Apply category-based style
    if (category.toLowerCase().includes("good")) {
      resultBox.classList.add("good");
    } else if (category.toLowerCase().includes("moderate")) {
      resultBox.classList.add("moderate");
    } else {
      resultBox.classList.add("unhealthy");
    }

    resultBox.innerHTML = "Predicted AQI Category: " + category;
  } catch (error) {
    resultBox.className = "result unhealthy";
    resultBox.style.display = "block";
    resultBox.innerHTML = "Error: " + error.message;
  }
}

