function main() {
    var prompt = document.getElementById("prompt").value;
    var imgSize = document.getElementById("img_size").value;

    if (prompt && imgSize) {
        var data = {
            prompt: prompt,
            size: imgSize
        };

        fetch('/generate-image/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            displayImages(data.images);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    } else {
        alert('Please enter a prompt and select an image size.');
    }
}

function reset() {
    console.log("reset");
    document.getElementById("Image_1").src = "";
    document.getElementById("Image_2").src = "";
    document.getElementById("bot_input").value = "";
    document.getElementById("img_size").value = "";
}

function displayImages(imageUrls) {
    var image1 = document.getElementById("Image_1");
    var image2 = document.getElementById("Image_2");

    if (imageUrls && imageUrls.length >= 2) {
        image1.src = imageUrls[0];
        image2.src = imageUrls[1];
    } else {
        alert('Error: Unexpected response from the server.');
    }
}
