$("#id_street_label").autocomplete({
    minLength: 2,
   source: function(request, response) {
       $.ajax({
           url: "/avtomat/street_json/",
           dataType: "json",
           data: {term: request.term, city: $('#id_city').val()},
           success: function(data) {response(data)}
       })
   },
   select: function(event, ui) {
       event.preventDefault();
       $(this).val(ui.item.label);
       $("#id_street").val(ui.item.value)
   }
});
