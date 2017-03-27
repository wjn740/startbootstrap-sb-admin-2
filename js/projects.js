    $.ajax({
        url: '../data/projects.py',
        dataType: 'json',
        success: function(data) {
        var a;
        var b;
        var c;
        var d;
        var third_level;
        var t;
        a="<li>";
        b="<a href=\"#\">";
        c="<span class=\"fa arrow\"></span></a>";
        d="</li>";
        third_level="<ul class=\"nav nav-third-level\">";
            $.each(data, function(i, e){
                t = a+ b + e.project + c;
                //insert next level menu 
                t = t + third_level;
                t = t + "<li><a href=\"#\" class=\"testing_plans\" pid=\"" + e.project + "\">Testing Plans</a></li>";
                t = t + "<li><a href=\"#\" class=\"testing_machines\" pid=\"" + e.project + "\">Testing Machines</a></li>";
                if (e.baselines.length>0) {
                    t = t + "<li><a href=\"#\" class=\"baseline_status\" pid=\"" + e.project + "\">Baseline status" + c;
                    t = t + third_level;
                    $.each(e.baselines, function(i,a){
                        t = t + "<li><a href=\"#\" class=\"baseline\" r_run_id=\"" + a.r_run_id + "\"pid=\"" + e.project + "\">"+ a.r_release +"</a>";
                    });
                }else{
                    t = t + "<li><a href=\"#\" class=\"baseline_status\" pid=\"" + e.project + "\">Baseline status</a>";
                }
                t = t + "</ul>";//end baseline level
                t = t + "</li>";//end baseline_status
                t = t + "</ul>";//end third level
                t = t + d;
                $("#projects_list").append(t);
            });
        },
        async: false
    });


$(function(){
    var table = null;
    $("#baseline_status").hide();
    $(".baseline").on('click', function() {
        var me;
        me=$(this)
        if (table) {
            table.destroy();
        }
        $("#page-wrapper > div").fadeOut("slow", function(){
            $("#baseline_status").fadeIn("fast", function(){

            });
        });
        table=$("#dataTables-baseline_status").DataTable({
            ajax: {
                url: '../data/baseline_status.py',
                type: 'POST',
                data: {'r_release': me.text(), 'r_run_id': me.attr("r_run_id")},
                dataSrc: '',
            },
            columns: [
            {data: "host"},
            {data: "testcase"},
            {data: "testsuite"},
            {data: "Count"},
            ],
        });
        
    });
});
