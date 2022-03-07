const fileInput = document.getElementById('pdf_file')

fileInput.addEventListener('change', (e) => {
    let label = fileInput.nextElementSibling
    let fileName = e.target.files[0].name
    label.innerHTML = `${fileName.slice(0, 20)}...${fileName.slice(-10, )}`

})

