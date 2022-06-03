
const copyBtns = [...document.getElementsByClassName('copy-btn')];

copyBtns.forEach(
    btn => btn.addEventListener('click', () => {
        const hexcode = btn.getAttribute('data-hexcode');
        navigator.clipboard.writeText(hexcode);

        btn.textContent = 'Copied!';
        setTimeout(() => { btn.textContent = 'Copy'; }, 1500);
    })
);
