let url = window.location.href;

$('#quiz-alert').hide();

const quizBox = document.getElementById('quiz-box');
const div_alert_container = document.getElementById('quiz-alert-container');
const quizTimer = document.getElementById('quiz-timer');


const activateTimer = (time_in_minutes) => {
    let seconds = time_in_minutes * 60;

    const interval = setInterval(function() {
        seconds--;

        const minutes = Math.floor(seconds / 60);
        const remaining_seconds = seconds % 60;

        minutes_str = `${minutes}`
        if(minutes < 10) {
            minutes_str = `0${minutes}`
        }

        remaining_seconds_str = `${remaining_seconds}`

        if(remaining_seconds < 10) {
            remaining_seconds_str = `0${remaining_seconds}`
        }


        quizTimer.innerHTML = `${minutes_str}:${remaining_seconds_str}`;

        if(seconds === 0) {
            clearInterval(interval);
            sendData();
        }
    }, 1000);

};

if(url.includes('?format=json') === false) {
    url += '?format=json';
}

$.getJSON({
    type: 'GET',
    url: url,
    success: function(response) {
        console.log('response', response);

        const questions = response['questions'];

        questions.forEach(el => {
            const question_title = el['title'];
            const question_id = el['id'];
            const answers = el['answers'];

            quizBox.innerHTML += `
                <hr>
                <div class="mb-2" id="question-${question_id}">
                    <b>${question_title}</b>
                </div>
            `
            answers.forEach(answer => {
                const answer_id = answer['id'];
                const answer_title = answer['title'];

                quizBox.innerHTML += `
                    <div>
                        <input class="ans"
                               type="radio"
                               id="${answer_id}"
                               value="${answer_title}"
                               name="${question_id}"
                        >
                        <label for="${answer_id}" name="input-label" id="label-${answer_id}">
                            ${answer_title}
                        </label>
                    </div>
                `
            });
        });

        activateTimer(response['duration']);
    },
    error: function(response) {
        console.log('error response', response);
    },
});


const quizForm = document.getElementById('quiz-form');
const csrf = document.getElementsByName('csrfmiddlewaretoken');

const elements = document.getElementsByClassName('ans');

const insertAlertDiv = () => {
    let div_content = `
        <div class="alert alert-warning alert-dismissible fade show"
                role="alert"
                id="quiz-alert"
            >
            <div id="quiz-alert-message">
            </div>

            <button
                type="button"
                class="close"
                data-dismiss="alert"
                aria-label="Close"
                id="save-button"
            >
                <span aria-hidden="true">&times;</span>
            </button>
        </div>
    `;

    div_alert_container.innerHTML = div_content;
};

const sendData = () => {
    const data = {};
    data['csrfmiddlewaretoken'] = csrf[0].value;

    for (let element of elements) {
        if(element.checked) {
            data[element.name] = element.id;
        }
        else {
            if(!data[element.name]) {
                data[element.name] = null;
            }
        }
    }

    console.log(data);

    $.ajax({
        type: 'POST',
        url: url,
        data: data,
        success: function(response) {
            insertAlertDiv();

            const quiz_message_div = document.getElementById('quiz-alert-message');
            quiz_message_div.innerHTML = `
                Sua nota no quiz foi <strong> ${response['score']}%</strong>
            `
            const quiz_alert_div = $('#quiz-alert');

            if(quiz_alert_div.hasClass('alert-warning')) {
                quiz_alert_div.removeClass('alert-warning');
            }

            if(quiz_alert_div.hasClass('alert-success') === false) {
                quiz_alert_div.addClass('alert-success');
            }

            inputs_labels = document.getElementsByName('input-label');

            right_answers_ids = new Set();

            for(let right_answers_id of response.right_answers_ids) {
                right_answers_ids.add(`label-${right_answers_id}`);
            }

            console.log('right_answers_ids', right_answers_ids);

            for (let input_label of inputs_labels) {
                console.log('input_label.id', input_label.id);

                if(right_answers_ids.has(input_label.id)) {

                    if(input_label.classList.contains('text-danger')) {
                        input_label.classList.remove('text-danger');
                    }

                    input_label.classList.add('text-success');
                }
                else {
                    if(input_label.classList.contains('text-success')) {
                        input_label.classList.remove('text-success');
                    }
                    input_label.classList.add('text-danger');
                }
            }

            $('#quiz-alert').show();
            $('#save-button').hide();
        },
        error: function(response) {
            console.log(response);

            insertAlertDiv();

            const quiz_message_div = document.getElementById('quiz-alert-message');
            quiz_message_div.innerHTML = `
                Houve um erro ao enviar a resposta:
                <strong>
                    ${response['responseJSON']['error']}
                </strong>
            `
            const quiz_alert_div = $('#quiz-alert');

            if(quiz_alert_div.hasClass('alert-success')) {
                quiz_alert_div.removeClass('alert-success');
            }

            if(quiz_alert_div.hasClass('alert-warning') === false) {
                quiz_alert_div.addClass('alert-warning');
            }

            $('#quiz-alert').show();
            $('#save-button').hide();
        },
    });

    // Array.prototype.forEach.call(elements, function(el) {
    //     console.log(typeof el)

    //     if(el.checked)  {
    //         data[el.name] = el.value;
    //     } else {

    //     }
    // });
};


quizForm.addEventListener('submit', (e) => {
    e.preventDefault();
    sendData();
});
