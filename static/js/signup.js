$(function () {
    $('#signUpAvatar').on('change', function () {
        if (this.files.length > 0) {
            $('.file-icon').html('<i class="fas fa-check-circle"></i>');
        }
    });
})