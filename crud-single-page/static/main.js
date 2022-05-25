let new_id = 4;
let new_test = { 'name': '', 'result': '', 'id': new_id };

const zeroPad = (num, places) => String(num).padStart(places, '0')


function handleButtonForm() {
    const form_elem = $('.form-wrapper')

    if(form_elem.hasClass('hidden') === false) {
        $('#add-test').html('Close form');
        $('#add-test').toggleClass('btn-success');
        $('#add-test').toggleClass('btn-danger');
    }

    else {
        $('#add-test').html('Add test');

        $('#add-test').toggleClass('btn-success');
        $('#add-test').toggleClass('btn-danger');
    }
}

$('#add-test').on('click', () => {
    const form_elem = $('.form-wrapper')
    form_elem.toggleClass('hidden');

    handleButtonForm();

    $('#test-name').val('');
    $('#test-result').val('');
});

$('#test-name').on('change', () => {
    const elem = $('#test-name');
    new_test.name = elem.val();
});

function formatResultInput(value) {
    // Remove spaces and %
    value = value.replace(/\s/g, '');

    // Convert to int
    value = parseInt(value);

    // If not a number, set to 0
    if(isNaN(value) || value > 100) {
        alert('Please enter a number between 0 and 100');
        value = 0
    };

    value = zeroPad(value, 2)
    value = `${value}%`;
    return value;
}

$('#test-result').on('change', () => {
    const elem = $('#test-result');
    let value = elem.val();

    // Convert to int
    value = formatResultInput(value);

    $('#test-result').val(value);
    new_test.result = value;
});

$('#create-test').on('click', () => {
    if(new_test.name == '' || new_test.result == '') {
        alert('Please fill in all the fields');
        return;
    }

    for(const test of tests) {
        if(test.id >= new_id) {
            new_test.id = test.id + 1;
        }
    }

    $.ajax({
        url: `/tasks/create/`,
        type: 'POST',
        dataType: 'json',
        data: {
            'name': new_test.name,
            'percentage_completed': new_test.result,
        },
        success: function(response) {
            $('#test-table').html('');
            tests = fetch_all_tests();
        },
        error: function(response) {
            console.log(response);
        },
    });

    tests.push(new_test);

    addRow(new_test);

    $('.form-wrapper').addClass('hidden');

    handleButtonForm();
});

let tests = fetch_all_tests();

function fetch_all_tests() {
    var host = window.location.protocol + "//" + window.location.host;

    $.ajax({
        url: `${host}/tasks/`,
        type: 'GET',
        dataType: 'json',
        success: function(response) {
            tests = response['tasks'];
            for(const test of tests) {
                addRow(test)
            }
        },
        error: function(response) {
        }
    });
}

function addRow(obj) {
    const row = `
        <tr scope="row" class="test-row-${obj.id}">
            <td id="input-name-${obj.id}"
                data-testid="${obj.id}"
                class="input-name"
            >${obj.name}</td>

            <td id="input-result-${obj.id}"
                data-testid="${obj.id}"
                class="input-result"
            >${obj.percentage_completed}</td>

            <td>
                <button class="btn btn-sm btn-danger"
                        data-testid="${obj.id}"
                        id="delete-btn-${obj.id}"
                > Delete </button>

                <!--
                <button class="btn btn-sm btn-info"
                        disabled
                        data-testid="${obj.id}"
                        id="save-btn-${obj.id}"
                > Save </button>
                -->

                <button class="btn btn-sm btn-danger hidden"
                        data-testid="${obj.id}"
                        id="cancel-btn-${obj.id}"
                > Cancel </button>

                <button class="btn btn-sm btn-primary hidden"
                        data-testid="${obj.id}"
                        id="confirm-btn-${obj.id}"
                > Confirm </button>
            </td>
        </tr>
    `;

    $('#test-table').append(row);


    $(`#delete-btn-${obj.id}`).on('click', deleteTest);
    // $(`#save-btn-${obj.id}`).on('click', saveUpdate);
    $(`#cancel-btn-${obj.id}`).on('click', cancelAction);
    $(`#confirm-btn-${obj.id}`).on('click', confirmAction);

    $(`#input-result-${obj.id}`).on('dblclick', editResult);
    $(`#input-name-${obj.id}`).on('dblclick', editResult);
}

function togglHiddenClass(id) {
    const delete_btn = $(`#delete-btn-${id}`);
    const save_btn = $(`#save-btn-${id}`);
    const cancel_btn = $(`#cancel-btn-${id}`);
    const confirm_btn = $(`#confirm-btn-${id}`);

    // Toggle hidden class
    for(let btn of [delete_btn, save_btn, cancel_btn, confirm_btn]) {
        btn.toggleClass('hidden');
    }
}

function editResult() {
    // If has input child, return
    if($(this).children().length > 0) return;

    const testid = $(this).data('testid');

    const input_name = $(`#input-name-${testid}`);
    const input_result = $(`#input-result-${testid}`);

    // Set current element action to edit
    const elem_id = $(this)[0].id
    const elem_selector = `#${elem_id}`;
    $(elem_selector).data('current-action', 'edit');

    let value = $(this).html();

    // If at least one of the inputs is being edit, dont switch the buttons
    if(input_name.children().length == 0 && input_result.children().length == 0) {
        togglHiddenClass(testid);
    }

    $(this).html(`
        <input type="text"
               class="result form-control"
               data-test="${testid}"
               value="${value}"
        >
    `);
}

// function saveUpdate() {
//     const testid = $(this).data('testid');
// }

function deleteTest() {
    const testid = $(this).data('testid');

    const input_name = $(`#input-name-${testid}`);
    const input_result = $(`#input-result-${testid}`);

    input_name.data('current-action', 'delete');
    input_result.data('current-action', 'delete');

    togglHiddenClass(testid);
}

function undoEditInput(id, input_type) {
    const input = $(`#input-${input_type}-${id}`);

    let test = tests.find(test => test.id === id);

    if (input.data('current-action') == 'edit') {
        let value = test[input_type];
        input.html(`${value}`);
    }

    input.data('current-action', '');
}

function cancelAction() {
    const testid = $(this).data('testid');

    togglHiddenClass(testid);

    for(let input_type of ['name', 'result']) {
        undoEditInput(testid, input_type);
    }
}

function confirmEditInput(id, input_type) {
    let test = tests.find(test => test.id === id);

    const td = $(`#input-${input_type}-${id}`);

    if (td.data('current-action') == 'edit') {
        const input = $(`#input-${input_type}-${id} > input`);

        let value = input.val();

        if(input_type === 'result') {
            value = formatResultInput(value);
        }

        test[input_type] = value;
        td.html(`${value}`);

        td.data('current-action', '');

        const row = $(`.test-row-${id}`);

        row.css('opacity', '0.5');

        setTimeout(() => {
            row.css('opacity', '1');
        }, 1000);

        return true;
    }

    return false;
}

function confirmAction() {
    const testid = $(this).data('testid');

    let made_changes = false;

    made_changes |= confirmEditInput(testid, 'name');
    made_changes |= confirmEditInput(testid, 'result');

    if(made_changes) {
        let test = tests.find(test => test.id === testid);

        let td_name = $(`#input-name-${testid}`);
        let td_result = $(`#input-result-${testid}`);

        const new_name = td_name.html();
        const new_result = td_result.html();

        $.ajax({
            url: `/tasks/${testid}/update/`,
            type: 'PUT',
            data: {
                'name': new_name,
                'percentage_completed': new_result,
            },
            success: function(response) {
                $('#test-table').html('');
                tests = fetch_all_tests();
            },
            error: function(response) {
                console.log('error');
                console.log(response);
            },
        });

        togglHiddenClass(testid);
        return;
    }

    // Remove record from list of records
    tests = tests.filter(test => test.id !== testid);

    $.ajax({
        url: `/tasks/${testid}/delete/`,
        type: 'DELETE',
        success: function(response) {
            console.log('success');
            console.log(response);
            // Remove row from table

            $(`.test-row-${testid}`).remove();
            // tests = fetch_all_tests
        },
        error: function(response) {
            console.log('error');
            console.log(response);
        },
    });
}
