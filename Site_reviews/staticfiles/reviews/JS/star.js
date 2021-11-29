start_raiting();

function start_raiting() {
    const rating = document.getElementById("rating_value").innerHTML
    initRatings(rating)
}

function initRatings(rating) {
    document.getElementsByClassName('raiting_active')[0].style.width = rating / 0.05 + '%';
}