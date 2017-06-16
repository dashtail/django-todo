$(document).ready(function(){
    //drag and drop
    $("ul.list-group").sortable({
      group: 'no-drop',
      handle: '.glyphicon-move',
      onDrop: function  ($item, container, _super) {
        var $clonedItem = $('<li/>').css({height: 0});
        $item.before($clonedItem);
        $clonedItem.animate({'height': $item.height()});

        $item.animate($clonedItem.position(), function  () {
          $clonedItem.detach();
          _super($item, container);
        });

        //get new order
        var tasks_list = [];
        $.each($(container.el[0]).find('li'),function(i, item){
            var pk = $(item).data('id');
            if (pk != undefined){
                tasks_list.push(pk);
            }

        });

        //reorder tasks
        var status = $(container.el[0]).data('status');
        $.ajax({
            url:'/reorder/',
            dataType: 'json',
            method: 'POST',
            data: {tasks_list, status:status}
        });

      },

      //drag mouse/item style
      onDragStart: function ($item, container, _super) {
        var offset = $item.offset(),
            pointer = container.rootGroup.pointer;

        adjustment = {
          left: pointer.left - offset.left,
          top: pointer.top - offset.top
        };

        _super($item, container);
      },
      onDrag: function ($item, position) {
        $item.css({
          left: position.left - adjustment.left,
          top: position.top - adjustment.top
        });
      }
    });
});
