

const jdenticons = [...document.getElementsByClassName('jdenticon')];
const modalBody = document.getElementById('modal-body');

jdenticons.forEach(
    element => element.addEventListener(
        'click', () => {
            const el = element.cloneNode(true);
            el.setAttribute('width', '100%');
            el.setAttribute('height', '100%');

            modalBody.innerHTML = "";
            modalBody.appendChild(el);
        }
    )
);

