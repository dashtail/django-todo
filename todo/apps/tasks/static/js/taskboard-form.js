$(document).ready(function (){
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val();
    //Save the task on ToDo List
    $('#save-task').click(function (){
        var name = $('#task-name').val();
        $.ajax({
            url: '/',
            method: 'POST',
            data: {name: name, csrfmiddlewaretoken:csrftoken},
            success: function (pk){
                $('.todo').prepend('<li class="list-group-item" data-name="'+ name +
                '" data-id="'+pk+'"><span class="glyphicon glyphicon-move" ></span> ' +
                    name +
                    '<button class="pull-right"><span class="glyphicon glyphicon-trash" ></span></button>' +
                    '<button class="pull-right"><span class="glyphicon glyphicon-pencil" ></span></button>'+
                '</li>');
                $('#task-name').val('');
            }
        });
    });

    //Enable to edit a task / hide li item and show the form
    $('.edit-task').click(function(){
        var pk = $(this).data('id');
        $('.edit-form-task-'+pk).removeClass('hide');
        $('.item-task-'+pk).addClass('hide');
    });

    //update a task
    $('.update-task').click(function(){
        var pk = $(this).data('id');
        var name = $('.form-name-'+pk).val();
        $.ajax({
            url: '/update/',
            type: 'POST',
            data: {pk: pk, name: name, csrfmiddlewaretoken:csrftoken },
            success: function(){
                $('.edit-form-task-'+pk).addClass('hide');
                $('.item-task-'+pk).removeClass('hide');
                $('.task-name-'+pk).text(name);
            }
        });
    });

    //Remove a task
    $('.delete-task').click(function(){
        var pk = $(this).data('id');
        $.ajax({
            url: '/delete/',
            type: 'POST',
            data: {pk: pk, csrfmiddlewaretoken:csrftoken},
            success: function(){
                $("ul").find("[data-id='" + pk + "']").remove();
            }
        });
    });
});
