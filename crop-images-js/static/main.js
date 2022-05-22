var $image = $('#image');

const alertBox = document.getElementById('alert-box');
const imageBox = document.getElementById('image-box');
const imageForm = document.getElementById('image-form');
const confirmBtn = document.getElementById('confirm-button');

const input = document.getElementById('id_file');
const csrf = document.getElementsByName('csrfmiddlewaretoken');


input.addEventListener('change', () => {
    confirmBtn.classList.remove('not-visible');
    alertBox.innerHTML = "";


    const img_data = input.files[0];
    const url = URL.createObjectURL(img_data);

    imageBox.innerHTML = `<img src="${url}" id="image" width="500px">`;

    $image = $('#image');

    $image.cropper({
        aspectRatio: 1,
        crop: function (event) {
            // console.log('x', event.detail.x);
            // console.log('y', event.detail.y);

            // console.log('width', event.detail.width);
            // console.log('height', event.detail.height);

            // console.log('rotate', event.detail.rotate);

            // console.log('scaleX', event.detail.scaleX);
            // console.log('scaleY', event.detail.scaleY);

            // console.log('\n');
        }
    });

    var cropper = $image.data('cropper');









    confirmBtn.addEventListener('click', () => {
        cropper.getCroppedCanvas().toBlob(function (blob) {
            const fd = new FormData();
            fd.append('csrfmiddlewaretoken', csrf[0].value);

            fd.append('file', blob, 'image.png');

            const url = imageForm.action;
            console.log('url', url);

            $.ajax({
                type: 'POST',
                url: imageForm.action,
                enctype: 'multipart/form-data',
                data: fd,
                success: function (response) {
                    console.log(response);
                    alertBox.innerHTML = `<div class="alert alert-success" role="alert">
                                               ${response.message}
                                          </div>`;
                },
                error: function (error) {
                    console.log(error);
                    alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
                                                Ops! Something went wrong.
                                          </div>`;


                },
                cache: false,
                contentType: false,
                processData: false,
            });
        });

    });
});

