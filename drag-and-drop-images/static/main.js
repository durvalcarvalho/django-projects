Dropzone.autoDiscover = false;

const myDropZone = new Dropzone("#my-dropzone", {
    url: "upload/",
    maxFiles: 2,
    maxFilesize: 2,
    acceptedFiles: ".jpg,.png,.gif",
});