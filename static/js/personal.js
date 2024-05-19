$(function() {
    initTabs();
})

function initTabs() {
    $('#reviewPart').on('click', function() {
        $('#reviewPart').addClass('is-active');
        $('#submissionPart').removeClass('is-active');
        $('#messagePart').removeClass('is-active');
        $('#reviews').show();
        $('#submissions').hide();
        $('#messages').hide();
    });

    $('#submissionPart').on('click', function() {
        $('#reviewPart').removeClass('is-active');
        $('#submissionPart').addClass('is-active');
        $('#messagePart').removeClass('is-active');
        $('#reviews').hide();
        $('#submissions').show();
        $('#messages').hide();
    });

    $('#messagePart').on('click', function() {
        $('#reviewPart').removeClass('is-active');
        $('#submissionPart').removeClass('is-active');
        $('#messagePart').addClass('is-active');
        $('#reviews').hide();
        $('#submissions').hide();
        $('#messages').show();
    });
}
