// graph data specification: {'x_labels' : [label1, label2, ...], 'y_data' : [10, 20, 30, ...]}

var current_chart = ""

$('#teleop').click(()=> {
    if (current_chart != "teleop") {
        current_chart = "teleop"
        make_graph(['a', 'b', 'c'], [30, 20, 10])
    }
})

$('#auto').click(()=> {
    if (current_chart != "auto") {
        current_chart = "auto"
        make_graph(['a', 'b', 'c'], [20, 10, 30])
    }
})

$('#climb').click(()=> {
    if (current_chart != "climb") {
        current_chart = "climb"
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