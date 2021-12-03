
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
    sendAjax(id_user, id_review, value)
}

function sendAjax(id_user, id_review, value) {
    $.ajax({
        url:    "http://127.0.0.1:8000/reviews/star/" + id_user + ':' + id_review + ':' + value, //url страницы (action_ajax_form.php)
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