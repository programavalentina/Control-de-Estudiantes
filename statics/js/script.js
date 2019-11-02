$(document).ready(function() {
	$("#btn-menu").click(function() {
		$(this).toggleClass("open");
			$("nav").fadeToggle();
	});

	$("#options-home").click(function() {
		$(this).toggleClass("open");
			$(".options-sign").fadeOut();
			$(".options-log").fadeOut();	
	});

	$("#options-about").click(function() {
		$(this).toggleClass("open");
			$(".options-sign").fadeOut();
			$(".options-log").fadeOut();	
	});

	$("#options-sign").click(function() {
		$(this).toggleClass("open");
			$(".options-sign").fadeToggle();
			$(".options-log").fadeOut();	
	});

	$("#options-log").click(function() {
		$(this).toggleClass("open");
			$(".options-log").fadeToggle();
			$(".options-sign").fadeOut();	
	});
});