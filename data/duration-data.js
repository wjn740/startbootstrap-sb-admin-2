$(function() {

    $.ajax({
        type: "POST",
        url: "../data/duration-data.py",
        success: function(msg) {
            alert(msg);
            Morris.Bar({
                element: 'morris-bar-chart',
                data: msg,
                xkey: 'host',
                ykeys: ['test_time'],
                labels: ['testing duration'],
                hideHover: 'auto',
                resize: true
            });
        }

    });

    
});
