$('#add-test').on('click', () => {

});

$('#test-result').on('keyup', () => {

});

$('#test-name').on('change', () => {

});

$('#create-test').on('click', () => {

});


let tests =[
    {'name': 'Dislillation 50%',      'id':1, 'result': "43"},
    {'name': 'Flash Point',           'id':2, 'result': "61"},
    {'name': 'Water by Karl Fischer', 'id':3, 'result': "24"},
];

let current_action = '';

for(const test of tests) {
    addRow(test)
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
            >${obj.result}</td>

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

    const value = $(this).html();

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

        const value = input.val();
        test[input_type] = value;
        td.html(`${value}`);

        td.data('current-action', '');

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
        togglHiddenClass(testid);
        return;
    }

    // Remove record from list of records
    tests = tests.filter(test => test.id !== testid);

    // Remove row from table
    $(`.test-row-${testid}`).remove();
}