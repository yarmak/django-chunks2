(function($) {
    $(document).ready(function(){
        $('.edit_chunk').on(
            'click',
            'a',
            function() {
                var key = $(this).parent().data('key');
                var chunk = $(this).parent();
                chunk.empty();
                $.get('/chunks/edit/' + key + '/',
                      {},
                      function(data) {
                          chunk.html(data)
                          $('form', chunk).ajaxForm({
                              dataType: 'text',
                              beforeSubmit: function() { $('input', chunk).attr('disabled', 'disabled'); },
                              success: function(d, s, x) {
                                  console.log('SUCCESS: ' + x.status);
                                  $('form', chunk).css({
                                      'border': '10px solid green',
                                  }).animate(
                                      {'opacity': 'hide',},
                                      1000, 'linear',
                                      function() {
                                          var txt = $('.edit_chunk form textarea').val();
                                          chunk.empty();
                                          chunk.html(txt + '<a href="#">редактировать</a>')
                                      }
                                  );
                              },
                              error: function(d, s, x) { console.log('ERROR: ' + x.status); }
                          });
                      });
                return false;
            });
    });
})(jQuery);
