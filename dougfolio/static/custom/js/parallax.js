function EasyPeasyParallax() {
	scrollPos = $(this).scrollTop();
	$('#banner').css({
		'background-position' : '50% ' + (-scrollPos/4)+"px"
	});
	$('#bannertext').css({
		'margin-top': (scrollPos/4)+"px",
		'opacity': 1-(scrollPos/250)
	});
}

$(document).ready(function(){
	$(window).scroll(function() {
		EasyPeasyParallax();
	});

	$('#sidebar').animate(
		{marginLeft: "0%", opacity: 0.6}, 300, 'swing'
	);

	$('#bannertext').animate(
		{opacity: 1}, 1000, 'linear'
	);

 // $('#bannertext').hover(
 //    function(){
 //        $(this).toggleClass('shadow');
 //    });

	$("#bannertext").click(function (){
            $('html, body').animate({
                scrollTop: $("#content").offset().top
			}, 1000, 'swing');
    });
});