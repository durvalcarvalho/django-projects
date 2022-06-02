const alertBox = document.getElementById('alert-box');
const imgBox = document.getElementById('img-box');
const form = document.getElementById('p-form');
const image = document.getElementById('id_image');
const btnBox = document.getElementById('btn-box');

const btns = [...btnBox.children];

const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value;

const url = "";

const handleAlerts = (type, message) => {
    alertBox.innerHTML = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            <strong>${message}</strong>

            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
    `;
}

image.addEventListener('change', () => {
    const img_data = image.files[0];
    const url = URL.createObjectURL(img_data);
    console.log(url);
    imgBox.innerHTML = `<img src="${url}" width="100%">`;

    btnBox.classList.remove('not-visible');
});

let filter = null;

btns.forEach(btn => {
    btn.addEventListener('click', (event) => {
        event.preventDefault();

        filter = btn.getAttribute('data-filter');

        // const data = new FormData();
        // data.append('image', image.files[0]);
        // data.append('csrfmiddlewaretoken', csrf);
        // data.append('btn', btn.id);

        // fetch(url, {
        //     method: 'POST',
        //     body: data
        // })
        // .then(response => response.json())
        // .then(data => {
        //     if (data.status === 'success') {
        //         handleAlerts('success', data.message);
        //     } else {
        //         handleAlerts('danger', data.message);
        //     }
        // })
        // .catch(error => {
        //     handleAlerts('danger', error);
        // });
    });
});

let id = null;

form.addEventListener('submit', e => {
    e.preventDefault();

    const fd = new FormData();

    fd.append('image', image.files[0]);
    fd.append('csrfmiddlewaretoken', csrf);
    fd.append('filter', filter);

    $.ajax({
        url: url,
        type: 'POST',
        enctype: 'multipart/form-data',
        data: fd,
        success: function(data) {
            const sText = `Successfully uploaded image`;
            handleAlerts('success', sText);

            setTimeout(()=> {
                alertBox.innerHTML = '';
                imgBox.innerHTML = '';
                image.value = '';
            }, 3000);
        },

        error: function(error) {
            handleAlerts('danger', 'Ups... Something went wrong');
        },
        cache: false,
        contentType: false,
        processData: false,
    });
});