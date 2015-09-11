$(document).ready(function() {
    // добавление класса active
    $(".trigger-button").on('ontouchstart' in window ? 'touchstart' : 'click', function() {
        $(".trigger-button").not(this).removeClass("active");
        $(this).toggleClass("active");
    });

    // скрытие пункта с active при нажатии на свободную область
    $(document).on( "click", function(event){
        if( $(event.target).closest(".trigger-button, .hidden-block").length ) 
        return;
          $(".trigger-button.active").removeClass("active");
          event.stopPropagation();
    });

    // Прокрутка страницы наверх
    var top_show = 150; // В каком положении полосы прокрутки начинать показ кнопки "Наверх"
    var delay = 1000; // Задержка прокрутки
    $(window).scroll(function () { // При прокрутке попадаем в эту функцию
        /* В зависимости от положения полосы прокрукти и значения top_show, скрываем или открываем кнопку "Наверх" */
        if ($(this).scrollTop() > top_show) $('#top').fadeIn();
        else $('#top').fadeOut();
    });
    $('#top').click(function () { // При клике по кнопке "Наверх" попадаем в эту функцию
        /* Плавная прокрутка наверх */
        $('body, html').animate({
        scrollTop: 0
        }, delay);
    });

})
