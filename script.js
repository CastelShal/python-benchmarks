const data = {
    labels: ['n=500', 'n=1000', 'n=2500', 'n=5000', 'n=10000'],
    datasets: [
        {
            label: 'Cython',
            data: [0.000809, 0.003132, 0.019067, 0.075333, 0.298856],
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 2
        },
        {
            label: 'PyPy',
            data: [0.001621, 0.006762, 0.040198, 0.175724, 0.573305],
            backgroundColor: 'rgba(255, 159, 64, 0.2)',
            borderColor: 'rgba(255, 159, 64, 1)',
            borderWidth: 2
        },
        {
            label: 'CPython',
            data: [0.003045, 0.012379, 0.073211, 0.295603, 1.200937],
            backgroundColor: 'rgba(153, 102, 255, 0.2)',
            borderColor: 'rgba(153, 102, 255, 1)',
            borderWidth: 2
        },
        {
            label: 'Jython',
            data: [0.006935, 0.027754, 0.139924, 0.582739, 2.347894],
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            borderColor: 'rgba(255, 99, 132, 1)',
            borderWidth: 2
        }
    ]
};

const config = {
    type: 'line',
    data: data,
    options: {
        responsive: true,
        maintainAspectRatio: true,
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Number of Primes (n)'
                }
            },
            y: {
                title: {
                    display: true,
                    text: 'Execution Time (seconds)'
                },
                beginAtZero: true
            }
        },
        plugins: {
            legend: {
                position: 'top'
            }
        }
    }
};

const ctx = document.getElementById('benchmarkChart').getContext('2d');
new Chart(ctx, config);

// Scalability Chart
const scalabilityChartCtx = document.getElementById('scalabilityChart').getContext('2d');
new Chart(scalabilityChartCtx, {
  type: 'line',
  data: {
    labels: ['100', '500', '1000', '5000', '10000'],
    datasets: [
      {
        label: 'Without Parallelization',
        data: [0.5, 1.5, 3.2, 15.8, 30],
        borderColor: '#ff6384',
        fill: false
      },
      {
        label: 'With Parallelization',
        data: [0.4, 1.2, 2.8, 9.5, 18],
        borderColor: '#36a2eb',
        fill: false
      }
    ]
  },
  options: {
    responsive: true,
    plugins: {
      legend: { display: true }
    },
    scales: {
      x: { title: { display: true, text: 'Input Size' } },
      y: { title: { display: true, text: 'Execution Time (s)' } }
    }
  }
});
