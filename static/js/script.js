document.getElementById('scraper-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const urls = document.getElementById('urls').value;
    const outputFormat = document.getElementById('output-format').value;
    
    fetch('/scrape', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ urls, outputFormat })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '';

        if (outputFormat === 'html') {
            data.forEach(result => {
                const div = document.createElement('div');
                div.className = 'result-container p-4 mb-4 bg-white rounded shadow';
                const pre = document.createElement('pre');
                pre.textContent = result;
                div.appendChild(pre);
                resultsDiv.appendChild(div);
            });
        } else if (outputFormat === 'json') {
            data.forEach(result => {
                const div = document.createElement('div');
                div.className = 'result-container p-4 mb-4 bg-white rounded shadow';
                const pre = document.createElement('pre');
                pre.textContent = JSON.stringify(result, null, 2);
                div.appendChild(pre);
                resultsDiv.appendChild(div);
            });
        }
    })
    .catch(error => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = `<div class="alert alert-danger">Error: ${error}</div>`;
    });
});
