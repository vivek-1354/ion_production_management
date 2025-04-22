// filepath: dashboard-project/dashboard-project/dashboard/static/js/charts.js
console.log("charts.js loaded");
document.addEventListener('DOMContentLoaded', function() {
    // Fetch data for line production
    const lineLabels = JSON.parse(document.getElementById('lineLabels').textContent);
    const lineData = JSON.parse(document.getElementById('lineData').textContent);
    console.log(lineLabels, lineData);

    const ctxLine = document.getElementById('lineChart').getContext('2d');
    new Chart(ctxLine, {
        type: 'bar',
        data: {
            labels: lineLabels,
            datasets: [{
                label: 'Units Produced',
                data: lineData,
                backgroundColor: '#42A5F5'
            }]
        },
        // options: {
        //     responsive: true,
        //     scales: {
        //         y: {
        //             beginAtZero: true
        //         }
        //     }
        // }
    });

    // Fetch data for shift production
    const shiftLabels = JSON.parse(document.getElementById('shiftLabels').textContent);
    const shiftData = JSON.parse(document.getElementById('shiftData').textContent);

    const ctxShift = document.getElementById('shiftChart').getContext('2d');
    new Chart(ctxShift, {
        type: 'bar',
        data: {
            labels: shiftLabels,
            datasets: [{
                label: 'Units per Shift',
                data: shiftData,
                backgroundColor: '#66BB6A'
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    const productLabels = JSON.parse(document.getElementById('productLabels').textContent);
    const productData = JSON.parse(document.getElementById('productData').textContent);

    const ctxProduct = document.getElementById('productChart').getContext('2d');
    new Chart(ctxProduct, {
        type: 'bar',
        data: {
            labels: productLabels,
            datasets: [{
                label: 'Units per Product',
                data: productData,
                backgroundColor: '#FFA726'
            }]
        },
        options: {
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });

    // Fetch data for energy consumption
    const energyToday = document.getElementById('energyToday').textContent;
    const energyMonth = document.getElementById('energyMonth').textContent;
    console.log(energyToday, energyMonth);

    document.getElementById('energyTodayDisplay').textContent = `Today: ${energyToday} kWh`;
    document.getElementById('energyMonthDisplay').textContent = `This Month: ${energyMonth} kWh`;
});