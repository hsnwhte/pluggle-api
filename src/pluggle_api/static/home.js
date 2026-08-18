const strategies = JSON.parse(document.getElementById("strategy-data").textContent);

const input = document.getElementById("strategy-input");
const hidden = document.getElementById("strategy-value");
const list = document.getElementById("strategy-list");

function render(items) {
    list.innerHTML = "";
    if (items.length === 0) {
        list.classList.add("hidden");
        return;
    }
    for (const name of items) {
        const li = document.createElement("li");
        li.textContent = name;
        li.className = "cursor-pointer px-3 py-2 hover:bg-slate-100";
        li.addEventListener("click", () => {
            input.value = name;
            hidden.value = name;
            list.classList.add("hidden");
        });
        list.appendChild(li);
    }
    list.classList.remove("hidden");
}

input.addEventListener("input", () => {
    hidden.value = "";                       // seçim bozuldu
    const q = input.value.trim().toLowerCase();
    render(strategies.filter(s => s.toLowerCase().includes(q)));
});

input.addEventListener("focus", () => render(strategies));

document.addEventListener("click", (e) => {
    if (!e.target.closest("#strategy-picker")) list.classList.add("hidden");
});