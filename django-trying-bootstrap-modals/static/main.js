const spinner = document.getElementById('spinner');
const tableBody = document.getElementById('table-body-box');
const modalBody = document.getElementById('modal-body');
const mediaUrl = window.location.href + 'media';


$.ajax({
    url: '/data-json/',
    type: 'GET',
    success: function(response) {
        data = JSON.parse(response.data);

        data.forEach(el => {
            tableBody.innerHTML += `
                <tr>
                    <td>${el.pk}</td>
                    <td>
                        <div data-toggle="modal"
                             data-target="#previewPictureModal"
                             class="my-img"
                             data-pic="${mediaUrl}/${el.fields.picture}"
                        >
                             <img src="${mediaUrl}/${el.fields.image}/"
                                  height="40px"
                                  class="img-photo"
                                  data-pic="${mediaUrl}/${el.fields.image}"
                            >
                        </div>

                    </td>
                    <td>${el.fields.info}</td>
            `;
        });

        spinner.classList.add('not-visible');


        const imgPhotos = [...document.getElementsByClassName('img-photo')]

        imgPhotos.forEach(el => {
            el.addEventListener('click', e => {
                const imgURL = el.getAttribute('data-pic');
                modalBody.innerHTML = `
                    <div class="text-center">
                        <img src="${imgURL}">
                    </div>
                `;
            })
        });


    },
    error: function(response) {
        console.log(response);
    },
});