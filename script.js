document.getElementById('submit').addEventListener('click', function() {
    var inputValue = document.getElementById('input').value;
    var data = { 'prompt': inputValue };
    fetch('https://fathomless-escarpment-69401-466c2059570f.herokuapp.com/getimage', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        // Get the 'result' div element
        const resultDiv = document.getElementById('result');
        // Create an anchor tag to make the URL clickable
        const anchorTag = document.createElement('a');
        anchorTag.textContent = 'Result: ' + result.result;
        anchorTag.href = result.result; // Set the URL as the href attribute
        // Add the anchor tag to the 'result' div
        resultDiv.appendChild(anchorTag);
    })
    .catch(error => {
        console.error('API request failed:', error);
    });
});
