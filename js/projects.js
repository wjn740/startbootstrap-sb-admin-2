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
                t = t + "<li><a href=\"#\">Testing Plans</a></li>"
                t = t + "<li><a href=\"#\">Testing Machines</a></li>"
                t = t + "</ul>";//end third level
                t = t + d;
                $("#projects_list").append(t);
            });
        },
        async: false
    });
