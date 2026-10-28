const presets = [
//   L  B
    [3, 3],
    [3, 4],
    [4, 3],
    [4, 4],
    [5, 4],
    [5, 5],
    [5, 6]
];
const sfxLive = new Audio("./assets/sfx/live.wav");
const sfxBlank = new Audio("./assets/sfx/blank.wav");
let chamber = [];
let pane = "transition";

function get(id) {
    return document.getElementById(id);
}

function play(live) {
    if (live) {
        sfxLive.play();
    } else {
        sfxBlank.play();
    }
}

function trans(id) {
    get("transition").classList.add("active");
    get(pane).classList.remove("active");
    setTimeout(() => {
        get(id).classList.add("active");
        get("transition").classList.remove("active");
        pane = id;
    }, 250);
}

// https://stackoverflow.com/questions/2450954/how-to-randomize-shuffle-a-javascript-array
function shuffle(array) {
  let currentIndex = array.length;

  // While there remain elements to shuffle...
  while (currentIndex != 0) {

    // Pick a remaining element...
    let randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex--;

    // And swap it with the current element.
    [array[currentIndex], array[randomIndex]] = [
      array[randomIndex], array[currentIndex]];
  }
}

function initRound(newGame) {
    if (newGame) {
        let health = Math.floor(Math.random() * 3) + 3;
        get("info-health").textContent = `${health} HEALTH`;
    } else {
        get("info-health").textContent = "";
    }

    let draw = Math.floor(Math.random() * 3) + 2;
    get("info-items").textContent = `DRAW ${draw}`;

    const preset = presets[Math.floor(Math.random() * presets.length)];
    const live = preset[0];
    const blank = preset[1];
    chamber = [];
    for (let i = 0; i < live; i++) {
        chamber.push(true); 
    }
    for (let i = 0; i < blank; i++) {
        chamber.push(false);
    }
    shuffle(chamber);
}

function click(id) {
    switch(id) {
        case "round":
            trans("info-1");
            initRound(false);
            break;
        case "game":
            trans("info-1");
            initRound(true);
            break;
        case "info-1":
            trans("info-2");
            break;
        case "info-2":
            trans("select");
            break;
        case "fire":
            trans("fire-pane");
            break;
        case "eject":
            trans("eject-pane");
            break;
        case "invert":
            trans("invert-pane");
            break;
        case "glass":
            trans("glass-pane");
            break;
        case "phone":
            trans("phone-pane");
            break;
        case "med":
            trans("med-pane");
            break;
        case "fire-pane":
            let shot = true;
            play(shot);
            if (shot) { get("gun").classList.add("shot"); }

            setTimeout(() => {
                trans("select");
                get("gun").classList.remove("shot");
            }, 1500);
            break;
        case "eject-pane":
        case "invert-pane":
        case "glass-pane":
        case "phone-pane":
        case "med-pane":
            trans("select");
            break;
        case "end":
            trans("start");
            break;
    }
}

for (const button of document.getElementsByTagName("button")) {
    button.addEventListener("click", () => { click(button.id) });
};

for (const pane of document.getElementsByClassName("pane")) {
    pane.addEventListener("click", () => { click(pane.id) });
};

initRound(true);
trans("info-1");

