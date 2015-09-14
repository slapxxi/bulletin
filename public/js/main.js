$(document).ready(function() {
    $(".trigger-button").on('ontouchstart' in window ? 'touchstart' : 'click', function() {
        $(".trigger-button").not(this).removeClass("active");
        $(this).toggleClass("active");
    });


    $(document).on( "click", function(event){
        if( $(event.target).closest(".trigger-button, .hidden-block").length )
        return;
          $(".trigger-button.active").removeClass("active");
          event.stopPropagation();
    });

    const TOP_SHOW = 150;
    const DELAY = 1000;

    $(window).scroll(function () {
        if ($(this).scrollTop() > TOP_SHOW) $('#top').fadeIn();
        else $('#top').fadeOut();
    });

    $('#top').click(function () {
        $('body, html').animate({
        scrollTop: 0
      }, DELAY);
    });
})
