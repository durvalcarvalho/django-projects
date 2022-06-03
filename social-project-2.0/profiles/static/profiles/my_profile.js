const tableModalBody = document.getElementById('table-modal-body');
const tableModal = document.getElementById('modal-table');
const searchFriendBtn = document.getElementById('search-friend-btn');
const spinnerBox = document.getElementById('spinner-box');

searchFriendBtn.addEventListener('click', () => {
    $.ajax({
        url: '/profiles/unfollowed',
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            const profiles = response.profiles;
            console.log(profiles);
            profiles.forEach(profile => {
                tableModalBody.innerHTML += `
                    <tr>
                        <td>${profile.username}</td>
                        <td>
                            <button class="btn btn-primary"
                                    data-id="${profile.id}"
                            >Follow</button>
                        </td>
                    </tr>
                `;
            });

            spinnerBox.classList.add('d-none');
            tableModal.classList.remove('d-none');
        },
        error: function (response) {
            console.log("Error", response);
        }
    });
});
