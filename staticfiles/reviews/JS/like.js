function PushLike(value) {
    id_user = document.querySelector("input[name = 'user_id']").value
    id_review = document.querySelector("input[name = 'review_id']").value
    sendLikeAjax(id_user, id_review)
}

function sendLikeAjax(id_user, id_review) {
    $.ajax({
        url:    "http://127.0.0.1:8000/reviews/like/" + id_user + ':' + id_review, //url страницы (action_ajax_form.php)
        type:    "GET", //метод отправки
        dataType: "html", //формат данных
        
        success: function(response) { //Данные отправлены успешно
            result = $.parseJSON(response);
            $('#like_value').html(result);
        },
        error: function(response) { // Данные не отправлены
            $('#like_value').html('Ошибка. Данные не отправлены.');
        }
    });
}