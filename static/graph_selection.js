var current_chart = ""

$('#teleop').click(()=> {
    if (current_chart != "teleop") {
        current_chart = "teleop"
        make_graph(['a', 'b', 'c'], [30, 20, 10])
        // console.log(987)
    }
})

$('#auto').click(()=> {
    if (current_chart != "auto") {
        current_chart = "auto"
        make_graph(['a', 'b', 'c'], [20, 10, 30])
        // console.log(687)
    }
})

$('#climb').click(()=> {
    if (current_chart != "climb") {
        current_chart = "climb"
        // console.log(1323)
        make_graph(['a', 'b', 'c'], [10, 20, 30])
    }
})



function make_graph(x_labels, y_data) {
    var data = [
        {
            x: x_labels,
            y: y_data,
            type: 'bar'
        }
    ];
    Plotly.newPlot('data_graph', data);
}