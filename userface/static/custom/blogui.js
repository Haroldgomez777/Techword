const site_url = 'http://localhost:8000';
$(document).ready(function(){
    console.log('ready');
$('#addcategorybutton').click(function() {

    var category = $('#name-form1-i').val();
    $.ajax({
        url: site_url + "/artic/addcategory",
        method:'POST',
        dataType :'json',
        data: {title:category},
        success: function(result){
            console.log(result);
      }
    });
});

});