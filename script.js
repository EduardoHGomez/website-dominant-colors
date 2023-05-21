const dragArea = document.querySelector('.drag-area');

// When file is inside Drag Area
dragArea.addEventListener('dragover', (event) =>{
    console.log('File is inside the drag Area');
})