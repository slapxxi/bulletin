$(document).ready(function() {
    // var source = document.getElementById('elm-lang');
    // Elm.embed(Elm.Main, source);
    $('[data-confirm]').on('click', require_confirmation);

    $('[data-validate]')
      .addClass('valid')
      .on('keydown', function(e) {
        $input = $(e.currentTarget);
        $input.removeClass('valid');
        $input.addClass('invalid');
      })

    $('.site-header a[href]').each(function(_, link) {
        make_link_active(link);
    });
})


function require_confirmation(event) {
    $link = $(event.currentTarget);
    result = confirm($link.attr('data-confirm'));
    if (result) return true
    return event.preventDefault();
}


function make_link_active(link) {
    $link = $(link);
    if ($link.attr('href') == current_url()) {
        $link.attr('href', '#')
        $link.addClass('active');
    }
}


function current_url() {
    return window.location.pathname;
}
