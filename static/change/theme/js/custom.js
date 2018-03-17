// $(window).ready(function() {
// 	$('#loading').fadeOut(3000)
// });

$('.hastip').tooltipsy({
offset: [1,1],
css: {
'padding': '2px',
'max-width': '200px',
'color': '#1c7025',
'background-color': '#ffffff',
'border': '1px solid #1a701d',
'font-size' : '12px',
'font-family' : '"Yantramanav", sans-serif',
'-moz-box-shadow': '0 0 1px rgba(0, 0, 0, .5)',
'-webkit-box-shadow': '0 0 1px rgba(0, 0, 0, .5)',
'box-shadow': '0 0 1px rgba(0, 0, 0, .5)',
'text-shadow': 'none'
}
});
function htmlbodyHeightUpdate(){
var height3 = $( window ).height()
var height1 = $('.nav').height()+50
height2 = $('.main').height()
if(height2 > height3){
$('html').height(Math.max(height1,height3,height2)+10);
$('body').height(Math.max(height1,height3,height2)+10);
}
else
{
$('html').height(Math.max(height1,height3,height2));
$('body').height(Math.max(height1,height3,height2));
}

}
$(document).ready(function () {
htmlbodyHeightUpdate()
$( window ).resize(function() {
htmlbodyHeightUpdate()
});
$( window ).scroll(function() {
height2 = $('.container').height()
htmlbodyHeightUpdate()
});
});
$("#menu-toggle").click(function(e) {
e.preventDefault();
});
$("#wrapper").toggleClass("toggled");

$(document).ready(function(){
$(window).scroll(function(){
if ($(this).scrollTop() > 100) {
$('#scroll').fadeIn();
} else {
$('#scroll').fadeOut();
}
});
$('#scroll').click(function(){
$("html, body").animate({ scrollTop: 0 }, 600);
return false;
});
});
$(document).ready(function(){
$("#hide").click(function(){
$("#hide>a").toggle();
});
});

	$(document).ready(function(){

		$('.d_1287').on('click',function(){

			var txt1 = " <i>&#x2714</i>";

			$(this).css("color","green");
			$(this).append(txt1);
			$(this).off('click');

		});

		$('.C1232_2').on('click',function(){

			var txt1 = " <i>&#x2716</i>";

			$(this).css("color","red");
			$(this).append(txt1);
			$(this).off('click');

		});
	});




// dragElement(document.getElementById(("mydiv")));

// function dragElement(elmnt) {
//   var pos1 = 0, pos2 = 0, pos3 = 0, pos4 = 0;
//   if (document.getElementById(elmnt.id + "header")) {
//     /* if present, the header is where you move the DIV from:*/
//     document.getElementById(elmnt.id + "header").onmousedown = dragMouseDown;
//   } else {
//     /* otherwise, move the DIV from anywhere inside the DIV:*/
//     elmnt.onmousedown = dragMouseDown;
//   }

//   function dragMouseDown(e) {
//     e = e || window.event;
//     // get the mouse cursor position at startup:
//     pos3 = e.clientX;
//     pos4 = e.clientY;
//     document.onmouseup = closeDragElement;
//     // call a function whenever the cursor moves:
//     document.onmousemove = elementDrag;
//   }

//   function elementDrag(e) {
//     e = e || window.event;
//     // calculate the new cursor position:
//     pos1 = pos3 - e.clientX;
//     pos2 = pos4 - e.clientY;
//     pos3 = e.clientX;
//     pos4 = e.clientY;
//     // set the element's new position:
//     elmnt.style.top = (elmnt.offsetTop - pos2) + "px";
//     elmnt.style.left = (elmnt.offsetLeft - pos1) + "px";
//   }

//   function closeDragElement() {
//     /* stop moving when mouse button is released:*/
//     document.onmouseup = null;
//     document.onmousemove = null;
//   }
// }