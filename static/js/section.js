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

$(function () {
    document.querySelectorAll('.post-content').forEach((element) => {
        truncateText(element, 2);
    });
})

function truncateText(element, lineCount) {
    const lineHeight = parseFloat(getComputedStyle(element).lineHeight);
    const maxHeight = lineHeight * lineCount;

    let text = element.innerText;
    while (element.scrollHeight > maxHeight) {
        text = text.slice(0, -1);
        element.innerText = text + '...';
    }
}