
start_raiting();

function start_raiting() {
    const rating = document.getElementById("rating_value").innerHTML
    initRatings(rating)
}

function initRatings(rating) {
    document.getElementsByClassName('raiting_active')[0].style.width = rating / 0.05 + '%';
}

function PushRait(value) {
    id_user = document.querySelector("input[name = 'user_id']").value
    id_review = document.querySelector("input[name = 'review_id']").value
    sendRaitAjax(id_user, id_review, value)
}

function sendRaitAjax(id_user, id_review, value) {
    $.ajax({
        url:    "https://glacial-dusk-64788.herokuapp.com/reviews/star/" + id_user + ':' + id_review + ':' + value, //url страницы (action_ajax_form.php)
        type:    "GET", //метод отправки
        dataType: "html", //формат данных
        
        success: function(response) { //Данные отправлены успешно
            result = $.parseJSON(response);
            $('#rating_value').html(result);
            initRatings(result)
        },
        error: function(response) { // Данные не отправлены
            $('#rating_value').html('Ошибка. Данные не отправлены.');
        }
    });
}