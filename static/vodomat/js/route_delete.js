//Удаление маршрута
$('#deleteRoute').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var car_number = button.data('car_number');
    var delete_href = button.data('delete_href');
    var modal = $(this);
    modal.find('.modal-body h4').text('Вы действительно хотите удалить маршрут ' + car_number + ' ?');
    modal.find('.modal-footer a').attr('href', delete_href);
});