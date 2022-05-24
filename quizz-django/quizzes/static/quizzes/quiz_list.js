const modalBtns = [...document.getElementsByClassName('modal-button')];
const modalBody = document.getElementById('modal-body-confirm');
const startBtn = document.getElementById('start-button');
const current_url = window.location.href;


modalBtns.forEach(
    modalBtn => modalBtn.addEventListener('click', () => {
        const pk = modalBtn.getAttribute('data-pk');
        const quiz_name = modalBtn.getAttribute('data-quiz');
        const question_count = modalBtn.getAttribute('data-question_count');
        const difficulty = modalBtn.getAttribute('data-difficulty');
        const duration = modalBtn.getAttribute('data-duration');
        const required_score = modalBtn.getAttribute('data-required_score');

        modalBody.innerHTML = `
            <div class="h5 mb-3">
                Are you sure you want to start the quiz <b>${quiz_name}</b> ?
                <div class="text-muted">
                    <ul>
                        <li>Number of questions:
                            <b>${question_count}</b>
                        </li>

                        <li>
                            Difficulty:
                            <b>${difficulty}</b>
                        </li>

                        <li>
                            Duration:
                            <b>${duration} minutes</b>
                        </li>

                        <li>
                            Required score to pass (percentage):
                            <b>${required_score}%</b>
                        </li>
                    </ul>
                </div>
            </div>
        `;


        startBtn.addEventListener('click', () => {
            window.location.href += `quizzes/${pk}`;
        });

    })
);