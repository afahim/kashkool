// This snippet of was found at
// https://developer.mozilla.org/en/Using_files_from_web_applications

function createDragNDropZone(){
    var dropbox = $("#uploaderFile")[0];
    dropbox.addEventListener("dragenter", dragenter, false);
    dropbox.addEventListener("dragover", dragover, false);
    dropbox.addEventListener("drop", drop, false);
}

function handleFiles(files) {
  for (var i = 0; i < files.length; i++) {
    var file = files[i];
    var imageType = /image.*/;
    
    if (!file.type.match(imageType)) {
      continue;
    }
    // what to do when the file is dropped
    var img = $("<img/>")[0];
    img.file = file;
    img.alt = file.name;   
    img.src = window.URL.createObjectURL(files[i]);
        img.onload = function(e) {
           window.URL.revokeObjectURL(this.src);
        }
    $("#imagePreview").html($(img));
  }
}

function dragenter(e) {
  e.stopPropagation();
  e.preventDefault();
}

function dragover(e) {
  e.stopPropagation();
  e.preventDefault();
}
function drop(e) {
  e.stopPropagation();
  e.preventDefault();
  var dt = e.dataTransfer;
  var files = dt.files;
  handleFiles(files);
}

