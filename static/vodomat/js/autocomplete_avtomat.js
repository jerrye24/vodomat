$('#id_avtomat_label').autocomplete({
    minLength: 2,
    source: function(request, response) {
        $.ajax({
            url: '/avtomat/avtomat_json/',
            dataType: 'json',
            data: {term: request.term},
            success: function(data) {response(data)}
        })
    },
    select: function (event, ui) {
        $(this).val(ui.item.label);
        $('#id_id').val(ui.item.id)
    }
});