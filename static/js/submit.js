var authorCount = 1;

$(function () {
    initAddAuthor();
    initFileUpload();
})

function initAddAuthor() {
    $('#addAuthor').on('click', function () {
        authorCount += 1;

        let div = document.createElement('div');
        div.classList.add('level');

        let input = document.createElement('input');
        input.classList.add('input');
        input.type = 'email';
        input.id = 'author' + authorCount;
        input.name = 'author' + authorCount;
        input.required = true;

        let button = document.createElement('button');
        button.classList.add('button');
        button.classList.add('is-danger');
        button.style.marginLeft = '10px';
        button.textContent = 'Remove';

        button.addEventListener('click', function () {
            div.remove();
        });

        div.appendChild(input);
        div.appendChild(button);

        $('#authors').append(div);
    });
}

function initFileUpload() {
    $('#submitContent').on('change', function () {
        if (this.files.length > 0) {
            $('.file-icon').html('<i class="fas fa-check-circle"></i>');
        }
    });
}
