function renderPie(labels, data) {
  new Chart(document.getElementById("pieChart"), {
    type: "pie",
    data: {
      labels: labels,
      datasets: [{
        data: data,
        backgroundColor: [
          "#0d6efd", "#20c997", "#ffc107",
          "#dc3545", "#6f42c1", "#198754"
        ]
      }]
    },
    options: {
      responsive: true,                  // ✅ responsive yoqilgan
      maintainAspectRatio: false,        // ✅ aspect ratio bo‘sh (divga moslashadi)
      plugins: { legend: { position: "right" } }
    }
  });
}





function renderBarLine(labels, rev, cost, profit){
  new Chart(document.getElementById("barLineChart"), {
    type: 'bar',
    data: {
      labels: labels,
      datasets: [
        {
          label: 'Tushum',
          data: rev,
          backgroundColor: '#0d6efd',
          barThickness: 50  // 👈 QALINLIK berildi
        },
        {
          label: 'Xarajat',
          data: cost,
          backgroundColor: '#dc3545',
          barThickness: 50
        },
        {
          label: 'Foyda',
          data: profit,
          backgroundColor: '#ffc107',
          barThickness: 50
        }
      ]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            callback: v => v.toLocaleString()
          }
        }
      },
      plugins: {
        legend: {
          position: 'top'
        }
      }
    }
  });
}