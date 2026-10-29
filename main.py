from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return """
    <!DOCTYPE html>
    <html lang="sk">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Včelnica u dvoch bratov</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">
        <style>
            body { font-family: 'Poppins', sans-serif; }
        </style>
    </head>
    <body class="bg-amber-50 text-slate-800 min-h-screen flex flex-col">

        <!-- HLAVIČKA -->
        <header class="bg-amber-600 text-white shadow-md sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
                <div class="flex items-center space-x-2 cursor-pointer" onclick="showStore()">
                    <span class="text-3xl">🐝</span>
                    <span class="text-xl font-bold tracking-wide">Včelnica U 2 bratov</span>
                </div>
                <div class="flex items-center space-x-3">
                    <button onclick="openAdminLogin()" class="bg-amber-800 hover:bg-amber-900 text-xs px-3 py-2 rounded-xl transition shadow">
                        ⚙️ Admin Panel
                    </button>
                    <button onclick="toggleCart()" class="bg-amber-700 hover:bg-amber-800 px-4 py-2 rounded-xl flex items-center space-x-2 transition shadow">
                        <span>🛒 Košík</span>
                        <span id="cart-count" class="bg-white text-amber-800 text-xs font-bold px-2 py-0.5 rounded-full">0</span>
                    </button>
                </div>
            </div>
        </header>

        <!-- HLAVNÝ OBSAH (OBCHOD) -->
        <main id="store-section" class="max-w-7xl mx-auto px-4 py-8 flex-grow w-full grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div class="lg:col-span-2">
                <h1 class="text-3xl font-bold text-amber-900 mb-2">Naše produkty</h1>
                <p class="text-amber-700 mb-4">Rodinné včelárstvo na úpätí Tribečských vrchov.</p>
                
                <!-- REÁLNY OBRÁZOK VČELNICE -->
                <div class="mb-6 rounded-2xl overflow-hidden shadow-md border border-amber-200">
                    <img src="data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEASABIAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAH0AlgBAREA/8QAHwAAAQEBAQEBAQEBAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD9K1v0VfvHqe9H2+P++34VTjs0ZclP8AJpfsEf8Ac/SrsmSzRjvEY/fJ+lWVvFb+I/jWctiufkXFTrYp/dx9KbgkK5aW8H8TH8qsbwvRjWctig7D8asJYx8/L+tQ0NFr7YD/E1WY23KCOhqp9ijx939aZ9gaNsqT+tTylXL1FVIoJEP3qsiuOS1EFFFFSUFFFFABQA0dTWfLbeYc/wCf8+tXBRW1GfI7mFWnzrUzfsP+/VpLUBfvVvUj4H8X51tzq2py+xc3e5VWyX1NXlsVAHzVcih3H+VX/sUf8Ad/Ws7sqxhPYp2aqz2S+hrqJNOjYZK1Xl0iJh90f55rWNRmbofmYH2JP7lMNguP4f0rfuPDkfXn86z5fDyjtXTGp2MHRZkT2i+hFUG07d/CtdTNotvjv6f1qA6TGO9bpvoYuh5mHNYDHw1kzaezHhf511s2mr6Vny6b7VouY5pUjnpdNd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" alt="Včelnica u dvoch bratov" class="w-full h-64 sm:h-80 object-cover">
                </div>
                
                <div id="product-grid" class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                    <!-- Produkty -->
                </div>
            </div>

            <!-- KOŠÍK -->
            <div class="bg-white p-6 rounded-2xl shadow-md border border-amber-100 h-fit sticky top-24">
                <h2 class="text-xl font-bold text-amber-900 mb-4 flex items-center justify-between">
                    <span>Váš nákupný košík</span>
                    <span>🍯</span>
                </h2>
                
                <div id="cart-items" class="divide-y divide-amber-100 mb-4 max-h-60 overflow-y-auto">
                    <p class="text-slate-400 text-sm py-4 text-center">Košík je zatiaľ prázdny.</p>
                </div>

                <div class="border-t border-amber-200 pt-4 mb-4">
                    <div class="flex justify-between text-lg font-bold text-slate-900">
                        <span>Celkom:</span>
                        <span id="cart-total" class="text-amber-600">0.00 €</span>
                    </div>
                </div>

                <div id="checkout-section" class="hidden">
                    <!-- KLUBOVÁ KARTA -->
                    <div class="bg-amber-50 p-3.5 rounded-xl border border-amber-200 mb-4">
                        <label class="flex items-center space-x-2 cursor-pointer mb-2">
                            <input type="checkbox" id="has-club-card" onchange="toggleClubCard()" class="w-4 h-4 text-amber-600 rounded focus:ring-amber-500">
                            <span class="text-xs font-semibold text-amber-900">Mám klubovú kartu (zľava 10%)</span>
                        </label>
                        <div id="club-card-details" class="hidden space-y-2 mt-2 pt-2 border-t border-amber-200">
                            <input type="email" id="club-email" oninput="updateCartUI()" placeholder="Váš e-mail" class="w-full p-2 border border-slate-200 rounded-lg text-xs focus:outline-none focus:border-amber-500 bg-white">
                            <input type="text" id="club-number" maxlength="6" oninput="updateCartUI()" placeholder="6-ciferné číslo karty" class="w-full p-2 border border-slate-200 rounded-lg text-xs focus:outline-none focus:border-amber-500 bg-white">
                        </div>
                    </div>

                    <h3 class="font-semibold text-slate-700 mb-3 text-sm">Doručovacie údaje</h3>
                    <div class="space-y-3 mb-4">
                        <input type="text" id="name" placeholder="Meno a priezvisko" class="w-full p-2.5 border border-slate-200 rounded-xl text-sm focus:outline-none focus:border-amber-500">
                        <input type="text" id="address" placeholder="Ulica, Mesto, PSČ" class="w-full p-2.5 border border-slate-200 rounded-xl text-sm focus:outline-none focus:border-amber-500">
                    </div>
                    <button onclick="checkout()" class="w-full bg-amber-600 hover:bg-amber-700 text-white font-semibold py-3 rounded-xl transition shadow text-sm">
                        Dokončiť objednávku
                    </button>
                </div>

                <div id="success-msg" class="hidden text-center py-6">
                    <div class="text-4xl mb-2">🎉</div>
                    <h3 class="text-lg font-bold text-green-700">Objednávka bola prijatá!</h3>
                    <p class="text-xs text-slate-500 mt-1">Ďakujeme za nákup. Bratov včelárov už balík balí!</p>
                    <button onclick="resetCart()" class="mt-4 text-xs bg-amber-100 hover:bg-amber-200 text-amber-800 font-semibold px-4 py-2 rounded-lg">Nakupovať znova</button>
                </div>
            </div>
        </main>

        <!-- ADMIN PANEL -->
        <main id="admin-section" class="max-w-4xl mx-auto px-4 py-8 flex-grow w-full hidden">
            <div class="flex justify-between items-center mb-6">
                <h1 class="text-3xl font-bold text-amber-900">⚙️ Správa produktov (Admin)</h1>
                <button onclick="showStore()" class="bg-amber-200 hover:bg-amber-300 text-amber-900 text-sm font-semibold px-4 py-2 rounded-xl">← Späť do obchodu</button>
            </div>

            <!-- Formulár na pridanie produktu -->
            <div class="bg-white p-6 rounded-2xl shadow-md border border-amber-100 mb-8">
                <h2 class="text-lg font-bold text-slate-800 mb-4">Pridať nový produkt</h2>
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4">
                    <input type="text" id="new-name" placeholder="Názov produktu" class="p-2.5 border border-slate-200 rounded-xl text-sm">
                    <input type="number" step="0.01" id="new-price" placeholder="Základná cena v €" class="p-2.5 border border-slate-200 rounded-xl text-sm">
                    <input type="number" id="new-stock" placeholder="Počet kusov na sklade (napr. 25)" class="p-2.5 border border-slate-200 rounded-xl text-sm">
                    <input type="number" step="0.01" id="new-bulk-price" placeholder="Cena pri veľkom odbere v € (napr. 22)" class="p-2.5 border border-slate-200 rounded-xl text-sm">
                    <input type="number" id="new-bulk-min" placeholder="Min. počet kusov pre zľavu (napr. 3)" class="p-2.5 border border-slate-200 rounded-xl text-sm">
                    <input type="text" id="new-icon" placeholder="Ikona (napr. 🍯)" class="p-2.5 border border-slate-200 rounded-xl text-sm">
                    <input type="text" id="new-desc" placeholder="Krátky popis" class="p-2.5 border border-slate-200 rounded-xl sm:col-span-2 text-sm">
                </div>
                <button onclick="addProduct()" class="bg-amber-600 hover:bg-amber-700 text-white font-semibold px-6 py-2.5 rounded-xl text-sm shadow transition">Pridať do ponuky</button>
            </div>

            <!-- Zoznam existujúcich produktov -->
            <div class="bg-white p-6 rounded-2xl shadow-md border border-amber-100">
                <h2 class="text-lg font-bold text-slate-800 mb-4">Aktuálne produkty v ponuke</h2>
                <div id="admin-product-list" class="divide-y divide-amber-100">
                    <!-- Načíta sa cez JS -->
                </div>
            </div>
        </main>

        <!-- ADMIN LOGIN MODAL -->
        <div id="admin-login-modal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 hidden">
            <div class="bg-white p-6 rounded-2xl shadow-xl max-w-sm w-full mx-4 border border-amber-100">
                <h3 class="text-lg font-bold text-slate-800 mb-2">Admin prihlásenie</h3>
                <p class="text-xs text-slate-500 mb-4">Zadajte administrátorské heslo:</p>
                <input type="password" id="admin-password-input" placeholder="Heslo" class="w-full p-2.5 border border-slate-200 rounded-xl text-sm mb-4 focus:outline-none focus:border-amber-500">
                <div class="flex space-x-2">
                    <button onclick="submitAdminLogin()" class="flex-1 bg-amber-600 hover:bg-amber-700 text-white font-semibold py-2 rounded-xl text-sm transition">Prihlásiť</button>
                    <button onclick="closeAdminLogin()" class="flex-1 bg-slate-200 hover:bg-slate-300 text-slate-700 font-semibold py-2 rounded-xl text-sm transition">Zrušiť</button>
                </div>
            </div>
        </div>

        <!-- PÄTIČKA -->
        <footer class="bg-amber-900 text-amber-100 py-6 text-center text-sm mt-auto">
            <p>&copy; 2026 Včelnica u dvoch bratov. Všetky práva vyhradené. Vyrábané s láskou k prírode 🐝</p>
        </footer>

        <!-- JAVASCRIPT -->
        <script>
            const defaultProducts = [
                { id: 1, name: "Kvetový med 950g", price: 8.50, stock: 25, bulkPrice: 7.50, bulkMin: 3, icon: "🍯", desc: "Jemný krémový kvetový med z jarných lúk." },
                { id: 2, name: "Lesný med 950g", price: 10.00, stock: 20, bulkPrice: 9.00, bulkMin: 3, icon: "🌲", desc: "Tmavý, aromatický lesný med plný minerálov." },
                { id: 3, name: "Med s vlašskými orechmi", price: 7.00, stock: 15, bulkPrice: 6.00, bulkMin: 3, icon: "🥜", desc: "Kombinácia lahodného medu a chrumkavých orechov." },
                { id: 4, name: "Včelí propolis (tinktúra)", price: 5.50, stock: 30, bulkPrice: 4.50, bulkMin: 3, icon: "🌿", desc: "Prírodné antibiotikum na posilnenie imunity." }
            ];

            let products = JSON.parse(localStorage.getItem("vcelnica_products")) || defaultProducts;
            let cart = [];

            function saveProducts() {
                localStorage.setItem("vcelnica_products", JSON.stringify(products));
            }

            function renderProducts() {
                const grid = document.getElementById("product-grid");
                grid.innerHTML = products.map(p => `
                    <div class="bg-white p-5 rounded-2xl shadow-sm border border-amber-100 flex flex-col justify-between hover:shadow-md transition">
                        <div>
                            <div class="flex justify-between items-start">
                                <div class="text-4xl mb-3">${p.icon}</div>
                                <span class="text-xs font-semibold px-2.5 py-1 rounded-full ${p.stock > 0 ? 'bg-amber-100 text-amber-800' : 'bg-red-100 text-red-700'}">
                                    ${p.stock > 0 ? `Skladom: ${p.stock} ks` : 'Vypredané'}
                                </span>
                            </div>
                            <h3 class="font-bold text-lg text-slate-900">${p.name}</h3>
                            <p class="text-slate-500 text-xs mt-1 mb-2">${p.desc}</p>
                            ${p.bulkMin && p.bulkPrice ? `<p class="text-xs text-amber-700 font-medium mb-4">✨ Zľava od ${p.bulkMin} ks (${p.bulkPrice.toFixed(2)} €/ks)</p>` : '<div class="mb-4"></div>'}
                        </div>
                        <div class="flex items-center justify-between mt-2 pt-3 border-t border-amber-50">
                            <div>
                                <span class="text-xl font-extrabold text-amber-700">${p.price.toFixed(2)} €</span>
                            </div>
                            <button onclick="addToCart(${p.id})" ${p.stock <= 0 ? 'disabled' : ''} class="bg-amber-500 hover:bg-amber-600 disabled:bg-slate-300 text-white text-sm font-semibold px-4 py-2 rounded-xl transition shadow-sm">
                                Do košíka
                            </button>
                        </div>
                    </div>
                `).join('');
            }

            function renderAdminList() {
                const list = document.getElementById("admin-product-list");
                list.innerHTML = products.map(p => `
                    <div class="py-4 flex flex-col sm:flex-row justify-between items-start sm:items-center w-full text-sm gap-3">
                        <div class="flex items-center space-x-3">
                            <span class="text-2xl">${p.icon}</span>
                            <div>
                                <span class="font-bold text-slate-800">${p.name}</span>
                                <div class="text-xs text-slate-500">Cena: ${p.price.toFixed(2)} € | Zľava: ${p.bulkPrice ? p.bulkPrice.toFixed(2)+'€' : 'žiadna'} (od ${p.bulkMin}ks)</div>
                            </div>
                        </div>
                        <div class="flex items-center space-x-2 w-full sm:w-auto justify-end">
                            <div class="flex items-center space-x-1">
                                <span class="text-xs text-slate-500">Sklad:</span>
                                <input type="number" id="stock-input-${p.id}" value="${p.stock}" class="w-16 p-1.5 border border-slate-200 rounded-lg text-xs text-center font-bold">
                                <button onclick="updateStock(${p.id})" class="bg-amber-100 hover:bg-amber-200 text-amber-900 text-xs font-semibold px-2.5 py-1.5 rounded-lg transition">Uložiť</button>
                            </div>
                            <button onclick="deleteProduct(${p.id})" class="bg-red-100 hover:bg-red-200 text-red-600 text-xs font-bold px-3 py-1.5 rounded-lg transition">Odstrániť</button>
                        </div>
                    </div>
                `).join('');
            }

            function openAdminLogin() {
                document.getElementById("admin-password-input").value = "";
                document.getElementById("admin-login-modal").classList.remove("hidden");
                document.getElementById("admin-password-input").focus();
            }

            function closeAdminLogin() {
                document.getElementById("admin-login-modal").classList.add("hidden");
            }

            function submitAdminLogin() {
                const password = document.getElementById("admin-password-input").value;
                if (password === "tatik") {
                    closeAdminLogin();
                    document.getElementById("store-section").classList.add("hidden");
                    document.getElementById("admin-section").classList.remove("hidden");
                    renderAdminList();
                } else {
                    alert("Nesprávne heslo!");
                    document.getElementById("admin-password-input").value = "";
                }
            }

            function showStore() {
                document.getElementById("admin-section").classList.add("hidden");
                document.getElementById("store-section").classList.remove("hidden");
                renderProducts();
            }

            function addProduct() {
                const name = document.getElementById("new-name").value;
                const price = parseFloat(document.getElementById("new-price").value);
                const stock = parseInt(document.getElementById("new-stock").value) || 10;
                const bulkPrice = parseFloat(document.getElementById("new-bulk-price").value) || null;
                const bulkMin = parseInt(document.getElementById("new-bulk-min").value) || 3;
                const icon = document.getElementById("new-icon").value || "🍯";
                const desc = document.getElementById("new-desc").value;

                if (!name || isNaN(price)) {
                    alert("Zadajte platný názov a cenu produktu.");
                    return;
                }

                const newId = products.length > 0 ? Math.max(...products.map(p => p.id)) + 1 : 1;
                products.push({ id: newId, name, price, stock, bulkPrice, bulkMin, icon, desc });
                saveProducts();

                document.getElementById("new-name").value = "";
                document.getElementById("new-price").value = "";
                document.getElementById("new-stock").value = "";
                document.getElementById("new-bulk-price").value = "";
                document.getElementById("new-bulk-min").value = "";
                document.getElementById("new-icon").value = "";
                document.getElementById("new-desc").value = "";

                renderAdminList();
                alert("Produkt bol úspešne pridaný!");
            }

            function updateStock(id) {
                const inputVal = parseInt(document.getElementById(`stock-input-${id}`).value);
                if (isNaN(inputVal) || inputVal < 0) {
                    alert("Zadajte platné číslo pre sklad.");
                    return;
                }
                const product = products.find(p => p.id === id);
                if (product) {
                    product.stock = inputVal;
                    saveProducts();
                    alert(`Sklad pre "${product.name}" bol aktualizovaný na ${inputVal} ks.`);
                    renderAdminList();
                }
            }

            function deleteProduct(id) {
                products = products.filter(p => p.id !== id);
                saveProducts();
                renderAdminList();
            }

            function addToCart(id) {
                const product = products.find(p => p.id === id);
                if (product.stock <= 0) {
                    alert("Tento produkt už nie je na sklade.");
                    return;
                }

                const existing = cart.find(item => item.id === id);
                if (existing) {
                    if (existing.qty < product.stock) {
                        existing.qty++;
                    } else {
                        alert("Viac kusov tohto produktu nie je na sklade.");
                        return;
                    }
                } else {
                    cart.push({ ...product, qty: 1 });
                }
                updateCartUI();
            }

            function removeFromCart(id) {
                cart = cart.filter(item => item.id !== id);
                updateCartUI();
            }

            function toggleClubCard() {
                const details = document.getElementById("club-card-details");
                const checkbox = document.getElementById("has-club-card");
                if (checkbox.checked) {
                    details.classList.remove("hidden");
                } else {
                    details.classList.add("hidden");
                    document.getElementById("club-email").value = "";
                    document.getElementById("club-number").value = "";
                }
                updateCartUI();
            }

            function updateCartUI() {
                const cartContainer = document.getElementById("cart-items");
                const countBadge = document.getElementById("cart-count");
                const totalSpan = document.getElementById("cart-total");
                const checkoutSection = document.getElementById("checkout-section");
                const hasClubCard = document.getElementById("has-club-card").checked;
                const clubEmail = document.getElementById("club-email").value.trim();
                const clubNumber = document.getElementById("club-number").value.trim();

                let totalCount = cart.reduce((sum, item) => sum + item.qty, 0);
                let totalPrice = 0;

                cart.forEach(item => {
                    let currentItemPrice = item.price;
                    if (item.bulkPrice && item.bulkMin && item.qty >= item.bulkMin) {
                        currentItemPrice = item.bulkPrice;
                    }
                    totalPrice += currentItemPrice * item.qty;
                });

                const isClubCardValid = hasClubCard && clubEmail !== "" && clubNumber.length === 6;
                if (isClubCardValid) {
                    totalPrice = totalPrice * 0.9;
                }

                countBadge.innerText = totalCount;
                totalSpan.innerText = totalPrice.toFixed(2) + " €";

                if (cart.length === 0) {
                    cartContainer.innerHTML = `<p class="text-slate-400 text-sm py-4 text-center">Košík je zatiaľ prázdny.</p>`;
                    checkoutSection.classList.add("hidden");
                } else {
                    cartContainer.innerHTML = cart.map(item => {
                        let activePrice = (item.bulkPrice && item.bulkMin && item.qty >= item.bulkMin) ? item.bulkPrice : item.price;
                        return `
                            <div class="py-2.5 flex justify-between items-center w-full text-sm">
                                <div>
                                    <span class="font-medium">${item.icon} ${item.name}</span>
                                    <div class="text-xs text-slate-400">${item.qty} ks × ${activePrice.toFixed(2)} € ${activePrice < item.price ? '(množstevná zľava)' : ''}</div>
                                </div>
                                <button onclick="removeFromCart(${item.id})" class="text-red-400 hover:text-red-600 text-xs font-bold px-2 py-1">✕</button>
                            </div>
                        `;
                    }).join('');
                    checkoutSection.classList.remove("hidden");
                }
            }

            function checkout() {
                const name = document.getElementById("name").value;
                const address = document.getElementById("address").value;
                const hasClubCard = document.getElementById("has-club-card").checked;
                const clubEmail = document.getElementById("club-email").value.trim();
                const clubNumber = document.getElementById("club-number").value.trim();

                if (!name || !address) {
                    alert("Prosím, vyplňte meno a doručovaciu adresu.");
                    return;
                }

                if (hasClubCard) {
                    if (!clubEmail || !clubNumber || clubNumber.length !== 6) {
                        alert("Pre uplatnenie klubovej karty zadajte svoj e-mail a presne 6-ciferné číslo karty.");
                        return;
                    }
                }

                cart.forEach(cartItem => {
                    const prod = products.find(p => p.id === cartItem.id);
                    if (prod) {
                        prod.stock -= cartItem.qty;
                    }
                });
                saveProducts();

                document.getElementById("checkout-section").classList.add("hidden");
                document.getElementById("cart-items").innerHTML = "";
                document.getElementById("success-msg").classList.remove("hidden");
                cart = [];
                updateCartUI();
                renderProducts();
            }

            function resetCart() {
                document.getElementById("success-msg").classList.add("hidden");
                document.getElementById("name").value = "";
                document.getElementById("address").value = "";
                document.getElementById("has-club-card").checked = false;
                document.getElementById("club-email").value = "";
                document.getElementById("club-number").value = "";
                document.getElementById("club-card-details").classList.add("hidden");
            }

            renderProducts();
        </script>
    </body>
    </html>
    """
