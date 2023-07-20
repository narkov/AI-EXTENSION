document.getElementById('submit').addEventListener('click', function() {
    var inputValue = document.getElementById('input').value;
    var data = { 'text': inputValue };
    fetch('/api/data', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').textContent = 'Result: ' + result.result;
    })
    .catch(error => {
        console.error('API request failed:', error);
    });
});