// Space where image will be dropped
const dragArea = document.querySelector('.drag-area');

// Change the text of Drag and drop
const dragText = document.querySelector('.header2'); 

let button = document.querySelector('.button');
let input = document.querySelector('#opener');

let file;

// When button is clicked open input
button.onclick = () => {
    input.click();
}

// When browse is clicked
input.addEventListener('change', function(){
    file = this.files[0];
    dragArea.classList.add('active');
    displayFile();
});

// When file is inside Drag Area
dragArea.addEventListener('dragover', (event) =>{
    event.preventDefault();
    console.log('File is inside the drag Area');
    dragText.textContent = 'Release to Upload';
    dragArea.classList.add('active');    
});

dragArea.addEventListener('dragleave', () =>{
    dragText.textContent = 'Drag and drop'; 
    console.log('File left the drag area');
    dragArea.classList.remove('active');   
});

// After file is dropped
dragArea.addEventListener('drop', (event)=>{
    event.preventDefault(); // Prevent to load the page from the submit button
    file = event.dataTransfer.files[0]; // Get the file uploaded
    displayFile();
    
});

// Savve and display image after it is dropped
function displayFile() {
    let fileType = file.type;

    let validExtensions = ['image/jpeg', 'image/jpg', 'image/png'];

    if (validExtensions.includes(fileType)){
        let fileReader = new FileReader();

        fileReader.onload = () =>{
            let fileURL = fileReader.result;
            //console.log(fileURL);
            let imgTag = `<img src = ${fileURL}>`;
            dragArea.innerHTML = imgTag;
            dragArea.classList.add('active2');
        };
        fileReader.readAsDataURL(file);
    }
    else{
        alert('This file is not an image');
        dragArea.classList.remove('active');
    }
}