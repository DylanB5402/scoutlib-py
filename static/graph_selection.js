var current_chart = "teleop"
        $('#auto').click(()=> {
            if (current_chart != "auto") {
                current_chart = "auto"
                console.log(687)
            }
        })

// var data = [
//         {
//             x: ['giraffes', 'orangutans', 'monkeys'],
//             y: [20, 14, 23],
//             type: 'bar'
//         }
//         ];

// Plotly.newPlot('data_graph', data);