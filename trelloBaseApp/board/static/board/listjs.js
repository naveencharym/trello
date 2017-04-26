/**
 * Created by mmvb45 on 4/24/2017.
 */
$('body').css('background-color', '#0079BF');

$( "#taskCreate" ).click(function() {
  $( "#board-creation-form" ).show( "slow" );
  $("#create-board-link").hide("slow")
});

$('#create_card-form').click(function () {
    alert("clckikk")
    $("#card-creation-form").show("slow")
})

$('#task-create-cancel').click(function () {
    $( "#board-creation-form" ).hide( "slow" );
    $("#create-board-link").show("slow")

})

$("#card-create-close").click(function () {
    $("#card-creation-form").hide("slow")
})

$("#task-create").click(function () {

    if($("#taskName").val().length>0)
    {
        var taskName = $("#taskName").val().replace(/\s/g, '');

        url="/board/createtask";
        $.ajax({
            type: "GET",
            data: ({task_name:taskName,board_name:$("#boardName").text()}),
            dataType: 'json',
            url: url,
            success: function (data) {
              if(data.statusCode == 200)
                    location.reload();
                else if(data.statusCode == 204)
                    alert("List name already in use ")
            }
        });
    }
    else
    {
        alert("Please enter List name")
    }

})



function saveCard(id) {
     taskInfo =id.split('--');
     if($("#"+taskInfo[0]+"--text").val().length>0)
    {

        url="/board/cardsave";
        $.ajax({
            type: "GET",
            data: ({card_name:$("#"+taskInfo[0]+"--text").val(),task_name:taskInfo[0]}),
            dataType: 'json',
            url: url,
            success: function (data) {
                 if(data.statusCode == 200){
                    $("#card-creation-form").hide("slow")
                    location.reload();
                 }
                 else if(data.statusCode == 204)
                    alert("Card name already in use ")

            }
        });
    }
    else
    {
        alert("Please enter card name")
    }

}

function  displayCardForm(name) {
    id = "#"+name+"form";
    $(id).show("slow")
}

function cardCreationclose(name) {
    info = name.split("--")
    id = "#"+info[0]+"form";
    $(id).hide("slow")
}
function deletTask(taskName) {
    taskName = taskName.split('--');
    url="/board/deleteTask";
    $.ajax({
        type: "GET",
        data: ({task_name:taskName[0]}),
        dataType: 'json',
        url: url,
        success: function (data) {
            location.reload();
        }
    });

}

function deleteCard(cardName) {

    url="/board/deleteCard";
    $.ajax({
        type: "GET",
        data: ({card_name:cardName}),
        dataType: 'json',
        url: url,
        success: function (data) {
            location.reload();
        }
    });
}