const swiper = new Swiper('.swiper-container', {
    pagination: '.swiper-pagination',
    nextButton: '.swiper-button-next',
    prevButton: '.swiper-button-prev',
    centeredSlides: true,
    autoplay: 2500,
    autoplayDisableOnInteraction: false
});

$(function () {
    initShowAll();
})

function initShowAll() {
    $('#showAllOrganizers').on('click', function () {
        $('#organizersList').toggle();
        if ($(this).html() === '<strong>Show All</strong>') {
            $(this).html('<strong>Hide List</strong>');
        } else {
            $(this).html('<strong>Show All</strong>');
        }
    });
}
