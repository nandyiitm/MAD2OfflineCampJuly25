<template>
    <h2>Admin Summary</h2>

<div>
  <canvas id="myChart"></canvas>
</div>

<img src="http://127.0.0.1:5000/static/image.png" alt="">

</template>

<script>
import Chart from 'chart.js/auto';

export default {
    name: 'AdminSummary',
    data() {
        return {
           label: '',
           labels: [],
           noOfReser: []
        }
    },
    methods: {
        fetchData() {
            fetch('http://127.0.0.1:5000/graph', {
              method: 'GET', // Specify the HTTP method
            })
            .then(response => {
                if (!response.ok) {
                    alert(response.status)
                }
                console.log(response.status)
                return response.json()
            })
            .then(data => {
                console.log('Response from POST', data)
                this.label = data.label
                this.labels = data.labels
                this.noOfReser = data.noOfReservations
                this.populateGraph()
            })
            .catch( error => {
                console.log(error)
            })
        },
        populateGraph() {
            const ctx = document.getElementById('myChart');
                      new Chart(ctx, {
            type: 'bar',
            data: {
            labels: this.labels,
            datasets: [{
                label: this.label,
                data: this.noOfReser,
                borderWidth: 1
            }]
            },
            options: {
            scales: {
                y: {
                beginAtZero: true
                }
            }
            }
        });

        }
    },
    mounted() {

        this.fetchData()

    
    }
}
</script>