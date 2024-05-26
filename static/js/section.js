$(window).on('load', function() {
    const placeholder = $('#placeholder-right');
    const fixed = $('#fixed-right');
    var rect = placeholder[0].getBoundingClientRect();
    fixed.css({
        position: 'fixed',
        top: rect.top + 'px',
        left: rect.left + 'px',
        visibility: 'visible'
    });
})