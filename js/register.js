$(function () {
    initSignup();
})

function initSignup() {
    $('#signupButton').on('click', function () {
        const name = $('#signupName').val();
        const gender = $('#signupGender').val();
        const email = $('#signupEmail').val();
        const password = $('#signupPassword').val();
        console.log('Name:', name);
        console.log('Gender', gender);
        console.log('Email:', email);
        console.log('Password:', password);
    })
}
