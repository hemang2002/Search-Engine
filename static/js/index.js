const dropContainer = document.getElementById("dropcontainer")
const fileInput = document.getElementById("file")


dropContainer.addEventListener("dragover", (e) => {
    
    e.preventDefault()
}, false)


dropContainer.addEventListener("dragenter", () => {

    dropContainer.classList.add("drag-active")
})


dropContainer.addEventListener("dragleave", () => {

    dropContainer.classList.remove("drag-active")
})


dropContainer.addEventListener("drop", (e) => {

    e.preventDefault()
    dropContainer.classList.remove("drag-active")
    fileInput.files = e.dataTransfer.files
})


$(document).ready(function() {

    bsCustomFileInput.init();
});


document.getElementById('search-bar').addEventListener('keydown', function(event) {

    if (event.key === 'Enter') {
        performSearch();
    }
});


function performSearch(){

    const query = document.getElementById('search-bar').value;
    const top_k = document.getElementById('stop-bar').value;
    const fileInput = document.getElementById('file');

    const filename = fileInput.files.length > 0 ? fileInput.files[0].name : '';

    if (!query || !filename) {

        alert('Please provide a query and upload a file.');
        return;
    }
}