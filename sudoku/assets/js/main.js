var cells = buildGrid();
console.log(cells);
var data = JSON.parse('../grid.json');
var grid = bGrid();
document.body.appendChild(grid);

function buildGrid() {
    var counter = 3;
    var cells = [];


    for (r = 0; r < 9; r++) {
        for (c = 0; c < 9; c++) {

            if (r < counter && c < counter) {
                cells.push((1, r + 1, c + 1))
            }

            if (r < counter && counter <= c < counter * 2) {
                cells.push((2, r + 1, c + 1))
            }

            if (r < counter && counter * 2 <= c < counter * 3) {
                cells.push((3, r + 1, c + 1))
            }

            if (counter <= r < counter * 2 && c < counter) {
                cells.push((4, r + 1, c + 1))
            }

            if (counter <= r < counter * 2 && counter <= c < counter * 2) {
                cells.push((5, r + 1, c + 1))
            }

            if (counter <= r < counter * 2 && counter * 2 <= c < counter * 3) {
                cells.push((6, r + 1, c + 1))
            }

            if (counter * 2 <= r < counter * 3 && c < counter) {
                cells.push((7, r + 1, c + 1))
            }

            if (counter * 2 <= r < counter * 3 && counter <= c < counter * 2) {
                cells.push((8, r + 1, c + 1))
            }

            if (counter * 2 <= r < counter * 3 && counter * 2 <= c < counter * 3) {
                cells.push([9, r + 1, c + 1])
            }
        }

    }
    console.log(cells);
    return cells;
}

function createElement() {
    var grid = document.createElement('div');
    grid.className = 'frame';
    for (i = 0; i < cells.length; i++) {
        arrItem = cells[i];
        var cell = grid.appendChild(document.createElement('div'));

        for (e = 0; e < arrItem.length; e++) {
            cell.className += e.toString();
            console.log(arrItem);

        }
    }

}



function loadJSON(callback) {

    var xobj = new XMLHttpRequest();
    xobj.overrideMimeType("application/json");
    xobj.open('GET', '../grid.json', true); // Replace 'my_data' with the path to your file
    xobj.onreadystatechange = function() {
        if (xobj.readyState == 4 && xobj.status == "200") {
            // Required use of an anonymous callback as .open will NOT return a value but simply returns undefined in asynchronous mode
            callback(xobj.responseText);
        }
    };
    xobj.send(null);
}


function init() {
    loadJSON(function(response) {
        // Parse JSON string into object
        var actual_JSON = JSON.parse(response);
        return actual_JSON;
    });
}

function bGrid() {
    for (i = 0; i < data.length; i++) {
        var cell = grid.appendChild(document.createElement('div'));

        for (e = 0; e < i.length; i++) {
            cell.className += e.toString();
        }
    }
}
console.log(grid);