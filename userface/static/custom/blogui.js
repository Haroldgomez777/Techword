const site_url = 'http://localhost:8000';


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$(document).ready(function(){

    console.log('ready');

    $("#addnewcategory").submit(function(e) {
        e.preventDefault();
    });

$('#addcategorybutton').click(function(e) {
    e.preventDefault();
    var category = $('#name-form1-i').val();
    $.ajax({

        url: site_url + "/artic/addcategory",
        method:'POST',
        data: {
            'title':category,
            'csrftoken' : getCookie('csrftoken')
        },
        success: function(result){
            console.log(result);
        }

    });
});

});