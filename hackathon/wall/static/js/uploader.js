function init(){
    $("#uploaderCaption > input").val("");
    $("uploader > input").removeAttr("checked");
    $("#uploaderUrl").css("visibility", "hidden");
    $("#uploaderFile").css("visibility", "hidden");
}

function add(){
    var tagString = $.trim($("input[name='tags']").val());
    var jsonVal = JSON.stringify(tagString.split(" "));
    alert(jsonVal);
    $("input[name='tags']").val(jsonVal);   
    $("#uploader > form").submit();
    alert("submtted");
}

function addJSON(){
    alert("jsoning");
    var tagString = $.trim($("input[name='tags']")).val();
    alert(tagString);
    $("#uploader > form").submit();
}


function showURLUploader(){
    $("#uploaderUrl").css("visibility", "visible");
    $("#uploaderFile").css("visibility", "hidden");
}

function showFileUploader(){
    $("#uploaderUrl").css("visibility", "hidden");
    $("#uploaderFile").css("visibility", "visible");
}

function previewUrl(){
    var img = $("<img/>")[0];
    img.src = $("#uploaderUrl > input").val();
    $("#imagePreview").html($(img));
}

