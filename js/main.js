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
    initModal();
    initSignin();
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

function initModal() {
    function openModal($el) {
        $el.classList.add('is-active');
    }

    function closeModal($el) {
        $el.classList.remove('is-active');
    }

    function closeAllModals() {
        (document.querySelectorAll('.modal') || []).forEach(($modal) => {
            closeModal($modal);
        });
    }

    (document.querySelectorAll('.js-modal-trigger') || []).forEach(($trigger) => {
        const modal = $trigger.dataset.target;
        const $target = document.getElementById(modal);

        $trigger.addEventListener('click', () => {
            openModal($target);
        });
    });

    (document.querySelectorAll('.modal-background, .modal-close, .modal-card-head .delete, .modal-card-foot') || []).forEach(($close) => {
        const $target = $close.closest('.modal');

        $close.addEventListener('click', () => {
            closeModal($target);
        });
    });

    document.addEventListener('keydown', (event) => {
        if(event.key === "Escape") {
            closeAllModals();
        }
    });
}

function initSignin() {
    $('#signinButton').on('click', function () {
        const email = $('#signInEmail').val();
        const password = $('#signInPassword').val();
        console.log('Email:', email);
        console.log('Password:', password);
    });
}
