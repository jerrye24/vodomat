// Сортировка таблицы
$(".tablesorter").tablesorter();

$('th')
    .mouseenter(function () {
        $(this).addClass('text-info')
    })
    .mouseleave(function () {
       $(this).removeClass('text-info')
    });

// Фиксированные th таблицы
var tbl = $('.table');
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



// Фокус на первое поле формы
// document.forms[0].elements[1].focus();


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

