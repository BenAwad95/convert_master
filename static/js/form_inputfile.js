const fileInput = document.querySelectorAll('input')[1]

fileInput.addEventListener('change', (e) => {
    let label = fileInput.nextElementSibling
    let fileName = e.target.files[0].name
    label.innerHTML = `${fileName.slice(0, 20)}...${fileName.slice(-10, )}`

})

