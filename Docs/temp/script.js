 // Fetch metadata from the URL
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const metadata = data[1][0]; // Assuming metadata is present at the first index
                const metadataDiv = document.getElementById("metadata");
                // Display metadata in the HTML
                metadataDiv.innerHTML = `<h3>Metadata</h3><pre>${JSON.stringify(metadata, null, 2)}</pre>`;
            })
            .catch(error => {
                console.error("Error fetching metadata:", error);
            });
    