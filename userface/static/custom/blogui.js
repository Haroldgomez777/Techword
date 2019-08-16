const site_url = 'http://localhost:8000';

$.ajaxSetup({ 
     beforeSend: function(xhr, settings) {
         function getCookie(name) {
             var cookieValue = null;
             if (document.cookie && document.cookie != '') {
                 var cookies = document.cookie.split(';');
                 for (var i = 0; i < cookies.length; i++) {
                     var cookie = jQuery.trim(cookies[i]);
                     // Does this cookie string begin with the name we want?
                     if (cookie.substring(0, name.length + 1) == (name + '=')) {
                         cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                         break;
                     }
                 }
             }
             return cookieValue;
         }
         if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
             // Only send the token to relative URLs i.e. locally.
             xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
         }
     } 
});





$(document).ready(function(){

    console.log('ready');

    $("#addnewcategory").submit(function(e) {
        e.preventDefault();
    });

$('#addcategorybutton').click(function(e) {
    e.preventDefault();
    var category = $('#name-form1-i').val();
    var form = $('#addnewcategory');
    var fordata = new FormData(form[0]);
    console.log(fordata);

        function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');
    $.ajax({
        url: site_url + "/artic/addcategory",
        type: "POST",
        dataType: 'json',
        data: fordata,
        cache: false,
        processData: false,
        contentType: false,
        success: function(result){
            console.log(result);
        }

    });
});

});


