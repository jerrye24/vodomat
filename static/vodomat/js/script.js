// Сортировка таблицы
$(".tablesorter").tablesorter();

// Фиксированные th таблицы
var tbl = $('.tablesorter');
var title = $('thead');
var titleClone = title.clone(true, true);
titleClone.prependTo(tbl).css({
    position: 'fixed',
    top: 0,
    backgroundColor: '#79aec8'
}).hide();
title.find('th').each(function(i,el){
    titleClone.find('th:eq('+i+')').width($(el).width());
});
$(document).scroll(function(){
    if($(this).scrollTop() > title.offset().top + title.height()){
        titleClone.show();
    } else {
        titleClone.hide();
    }
});

//Удаление маршрута
$('#deleteRoute').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget);
    var car_number = button.data('car_number');
    var delete_href = button.data('delete_href');
    var modal = $(this);
    modal.find('.modal-body h4').text('Вы действительно хотите удалить маршрут ' + car_number + ' ?');
    modal.find('.modal-footer a').attr('href', delete_href);
});

//Выбор периода datepicker
$("#id_period").datepicker({
    dateFormat: 'ddmmyy',
    firstDay: 1,
    dayNamesMin: [ 'Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
    monthNames: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
    onSelect: function( selectedDate ) {
        if(!$(this).data().datepicker.first){
            $(this).data().datepicker.inline = true;
            $(this).data().datepicker.first = selectedDate;
        }else{
            if(selectedDate > $(this).data().datepicker.first){
                $(this).val($(this).data().datepicker.first+"-"+selectedDate);
            }else{
                $(this).val(selectedDate+"-"+$(this).data().datepicker.first);
            }
            $(this).data().datepicker.inline = false;
        }
    },
    onClose:function(){
        delete $(this).data().datepicker.first;
        $(this).data().datepicker.inline = false;
    }
});

// Фокус на первое поле формы
document.forms[0].elements[1].focus();


// Часы
// function Clock() {
//     var id_period = new Date();
//     var hours = id_period.getHours();
//     var minutes = id_period.getMinutes();
//     var seconds = id_period.getSeconds();
//     if (hours < 10) hours = "0" + hours;
//     if (minutes < 10) minutes = "0" + minutes;
//     if (seconds < 10) seconds = "0" + seconds;
//     document.getElementById("clock").innerHTML = hours + ":" + minutes + ":" + seconds;
// }
// $(document).ready(function () {
//     setInterval(Clock, 1000);
// });

