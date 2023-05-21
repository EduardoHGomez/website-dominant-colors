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

// When browse
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
    event.preventDefault();
    file = event.dataTransfer.files[0];

    displayFile();
    console.log(file);
});

function displayFile() {
    let fileType = file.type;

    let validExtensions = ['image/jpeg', 'image/jpg', 'image/png'];

    if (validExtensions.includes(fileType)){
        let fileReader = new FileReader();

        fileReader.onload = () =>{
            let fileURL = fileReader.result;
            //console.log(fileURL);
            let imgTag = `<img src="${fileURL}" alt ="">`;
            dragArea.innerHTML = imgTag;
        };
        fileReader.readAsDataURL(file);
    }
    else{
        alert('This file is not an image');
        dragArea.classList.remove('active');
    }
}