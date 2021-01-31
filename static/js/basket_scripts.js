window.onload = function () {
    // добавляем ajax-обработчик для обновления количества товара
    $('.cart-list').on('click', 'input[type="number"]', function () {
        var target_href = event.target;
        
        if (target_href) {
            $.ajax({
                url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",

                success: function (data) {
                    $('.cart-list').html(data.result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });
}