function EasyPeasyParallax() {
	scrollPos = $(this).scrollTop();
	$('.first').css({
		'background-position' : '50% ' + (-scrollPos/4)+"px"
	});
}

$(document).ready(function(){
	$(window).scroll(function() {
		EasyPeasyParallax();
	});

	var controller = $.superscrollorama();
	controller.addTween(
	  '.second',
	  (new TimelineLite())
	    .append([
	      TweenMax.to($('.first'), 1, 
	        {css:{backgroundPosition: 1000}, immediateRender:true} 
	        ),
	    ]),
	  200 // scroll duration of tween
	);
	// $('.sidebar').animate(
	// 	{marginLeft: "0%", opacity: 0.6}, 300, 'swing'
	// );

	// $('.bannertext').animate(
	// 	{opacity: 1}, 1000, 'linear'
	// );

 // $('.bannertext').hover(
 //    function(){
 //        $(this).toggleClass('shadow');
 //    });

	// $(".bannertext").click(function (){
 //            $('html, body').animate({
 //                scrollTop: $(".content").offset().top
	// 		}, 1000, 'swing');
 //    });

    $(".bannertext").click(function (){
        $('.banner').animate({
            marginLeft: '-100%'
		}, 600, 'swing');
		$('.content').css("display", "inline");
    });
});