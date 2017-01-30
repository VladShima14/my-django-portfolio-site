$(document).ready(function(){
	$('.bxslider').bxSlider({
		auto: true
	});
	$("#lightgallery").lightGallery(); 
	document.getElementsByClassName("inputCompany")[0].setAttribute("placeholder", "Введите название компании");
	document.getElementsByClassName("inputEmail")[0].setAttribute("placeholder", "Введите электронный адрес");
	document.getElementsByClassName("inputPhone")[0].setAttribute("value", "+380");
	
	$(document).ready(function () {
	$('.callback').click(function (e) {
		$('#content').toggle();

		e.stopPropagation();
	});

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
    });

});

