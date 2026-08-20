const searchInput = document.getElementById("strategy-search");
const strategyList = document.getElementById("strategy-list")
const strategies = document.querySelectorAll("#strategy-list li");
const strategyValue = document.getElementById("strategy-value")
const strategyCombobox = document.getElementById("strategy-combobox")
const sourceDropzone = document.getElementById("source-dropzone")
const fileInput = document.getElementById("source-file")
const sourceDropzoneText = document.getElementById("source-dropzone-text")
const form = document.getElementById("input-form")

document.addEventListener('click', (e) => {
    const clickedElement = e.target;
});

document.addEventListener('click', (e) => {
    if (!strategyCombobox.contains(e.target)) {
        strategyList.classList.add('hidden');
    }
});

searchInput.addEventListener('focus', () => {
    strategyList.classList.remove('hidden');
});

searchInput.addEventListener('input', (e) => {
    const query = searchInput.value;
    strategies.forEach((strategy) => {
        const text = strategy.textContent;
        const matches = text.toLowerCase().includes(query.toLowerCase());
        if (matches) {
            strategy.classList.remove('hidden');
        } else {
            strategy.classList.add('hidden');
        }
    });
});

strategies.forEach((strategy) => {
    strategy.addEventListener('click', () => {
        searchInput.value = strategy.textContent;
        strategyValue.value = strategy.dataset.value;
    });
});


sourceDropzone.addEventListener('click', (e) => {
    fileInput.click();
});

fileInput.addEventListener('change', () => {
    if (fileInput.files.length === 1) {
        sourceDropzoneText.textContent = fileInput.files[0].name;
    }
});

sourceDropzone.addEventListener('dragover', (e) => {
    e.preventDefault();
    sourceDropzone.classList.add('border-sky-500');
});

sourceDropzone.addEventListener('dragleave', (e) => {
    sourceDropzone.classList.remove('border-sky-500');
});

sourceDropzone.addEventListener('drop', (e) => {
    e.preventDefault();
    sourceDropzone.classList.remove('border-sky-500');
    fileInput.files = e.dataTransfer.files;
    sourceDropzoneText.textContent = fileInput.files[0].name;
});

form.addEventListener('reset', () => {
    sourceDropzoneText.textContent = "Drag & drop a file here, or click to select"
});