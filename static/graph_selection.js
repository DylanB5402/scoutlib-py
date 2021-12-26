// graph data specification: {'x_labels' : [label1, label2, ...], 'y_data' : [10, 20, 30, ...]}

var current_chart = ""
generate_graph('teleop')

$('#teleop').click(()=> {
    if (current_chart != "teleop") {
        current_chart = "teleop"
        generate_graph('teleop')
    }
})

$('#auto').click(()=> {
    if (current_chart != "auto") {
        current_chart = "auto"
        generate_graph('auto')
    }
})

$('#climb').click(()=> {
    if (current_chart != "climb") {
        current_chart = "climb"
        generate_graph('climb')
    }
})

function generate_graph(data_tag) {
    fetch(`/api/analyzed/${data_tag}`).then((response) => response.json()).then(
        (data) => {
            make_graph(data['x_labels'], data['y_data'])
        })
}

function make_graph(x_labels, y_data) {
    str_x_labels = []
    x_labels.forEach(element => {
        str_x_labels.push('team ' + String(element))
    });
    var data = [
        {
            x: str_x_labels,
            y: y_data,
            type: 'bar'
        }
    ];
    Plotly.newPlot('data_graph', data);
}