$(document).ready(function(){
    // gallery script  
	$('.bxslider').bxSlider({
		auto: true
	});
	$("#lightgallery").lightGallery(); 
	
	$('.callback-img').click(function (e) {
		$('#content').toggle();

		e.stopPropagation();
	});
    // gallery script ends
    
    // callback form 
	$('#content').click(function (e) {
		e.stopPropagation();
	});

	$('.title img').click(function(e){
		$("#content").css("display","none");
	});

	$('input[type="submit"]').click(function(){
		var nameValue = $("#name").val();
		var phoneValue = $("#phone").val();
		if(nameValue != "" && phoneValue !=""){
			$("#content").css("display","none");	
			$(".success").delay(1000).fadeIn(1000);
			$(".success").delay(3000).fadeOut(500);
		}
	});
    // callback script ends
    
    // button-top 
    $(window).scroll(function () {
        if ($(this).scrollTop() > 500) {
            $('#scroller').fadeIn();
        } else {
            $('#scroller').fadeOut();
        }
        
    });
		$('#scroller').click(function () {
		    $('body,html').animate(
		        {scrollTop: 0}, 400); return false;
		    
		});
    // 	button-top ends
    
});

