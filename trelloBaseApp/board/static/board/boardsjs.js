/**
 * Created by mmvb45 on 4/23/2017.
 */
var selectedBoard ="";
$('body').css('background-color', '#ffffff');
$( "#one" ).click(function() {
  $( "#board-creation-form" ).show( "slow" );
  $("#create-board-link").hide("slow")
});


$("#board-create").click(function () {
    url="/board/createboard";
    var boardName = $("#bordName").val()
    if($("#bordName").val().length>0){
        $.ajax({
            type: "GET",
            data: ({name:boardName}),
            dataType: 'json',
            url: url,
            success: function (data) {
                if(data.statusCode == 200)
                    location.reload();
                else if(data.statusCode == 204)
                    alert("Board name already in use ")
            }
        });
    }
    else
    {
        alert("Please enter Board name")
    }

})

$("#close-board-create").click(function () {
    $( "#board-creation-form" ).hide( "slow" );
    $("#create-board-link").show("slow")
})

function deletBoard(boardName) {
    url="/board/deleteBoard";
    $.ajax({
        type: "GET",
        data: ({board_name:boardName}),
        dataType: 'json',
        url: url,
        success: function (data) {
            console.log(data);
            location.reload();
        }
    });
}