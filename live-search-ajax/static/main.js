console.log("Hello World");


const url = window.location.href;
console.log("url", url);

const searchForm = document.getElementById("search-form");
const searchInput = document.getElementById("search-input");
const resultsBox = document.getElementById("results-box");

const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value;

searchInput.addEventListener("keyup", function(e) {
    if(resultsBox.classList.contains("not-visible")) {
        resultsBox.classList.remove("not-visible");
    }
    else if(e.target.value === "") {
        resultsBox.classList.add("not-visible");
    }

    let value = e.target.value;

    if(value.length > 0) {
        $.ajax({
            url: "search/",
            type: "POST",
            data: {
                'csrfmiddlewaretoken': csrf,
                'search': value
            },
            success: function(response) {
                const games = response.games;
                let html = "";

                if(games.length > 0) {
                    games.forEach(function(game) {
                        html += `
                            <a href="${game.url}" class="item">
                                <div class="row mt-2 mb-2">
                                    <div class="col-2">
                                        <img src="${game.image}"
                                             class="game-img"
                                        />
                                    </div>

                                    <div class="col-10">
                                        <h5>${game.name}</h5>
                                        <p>${game.studio}</p>
                                    </div>
                                </div>
                            </a>
                        `;
                    });
                }
                else {
                    html = "No games found...";
                }

                resultsBox.innerHTML = html;

            },
            error: function(response) {
                console.log(response);
            },
        })
    }
});