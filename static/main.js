
  function updateTable() {
    $.ajax({
        url: 'http://10.40.9.25:8001/api/v2/get/all/plant',
        method: 'GET',
        success: function(data) {
            // Update table rows
            var tbody = $('#plantTable tbody');
            tbody.empty();
            data.forEach(function(item) {
                var row = '<tr>' +
                    '<td>' + item.plant_id + '</td>' +
                    '<td>' + item.name + '</td>' +
                    '<td>' + item.pin_soil.pin_value + '</td>' +
                    '<td>' + item.capacity + '</td>' +
                    '</tr>';
                tbody.append(row);
            });
        }
    });
}

// Call updateTable function every second
setInterval(updateTable, 300);