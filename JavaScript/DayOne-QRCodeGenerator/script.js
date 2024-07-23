let imgBox = document.getElementById('imgBox');
let qrImage = document.getElementById('qrImage');
let qrText = document.getElementById('qrText');
let qrX = document.getElementById('qrX');
let qrY = document.getElementById('qrY');
let format = document.getElementById('qrFormat').value;

function Generate() {
    if (qrText.value.length > 0) {
        // Generate QR code
        let size = qrX.value + "x" + qrY.value;
        qrImage.src = "https://api.qrserver.com/v1/create-qr-code/?size="+ size + "&format=" + format +"&data=" + qrText.value;
        imgBox.classList.add('show-img');
    } else {
        qrText.classList.add("error");
        setTimeout(()=> {
            qrText.classList.remove("error");
        }, 1000)
    }
}

