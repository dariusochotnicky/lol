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
                    <span class="text-xl font-bold tracking-wide">Včelnica u dvoch bratov</span>
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
                <h1 class="text-3xl font-bold text-amber-900 mb-2">Naše včelie produkty</h1>
                <p class="text-amber-700 mb-6">100% čistý domáci med a produkty priamo od dvoch bratov včelárov.</p>
                
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

                <div class="border-t border-amber-200 pt-4 mb-6">
                    <div class="flex justify-between text-lg font-bold text-slate-900">
                        <span>Celkom:</span>
                        <span id="cart-total" class="text-amber-600">0.00 €</span>
                    </div>
                </div>

                <div id="checkout-section" class="hidden">
                    <h3 class="font-semibold text-slate-700 mb-3">Doručovacie údaje</h3>
                    <div class="space-y-3 mb-4">
                        <input type="text" id="name" placeholder="Meno a priezvisko" class="w-full p-2.5 border border-slate-200 rounded-xl text-sm focus:outline-none focus:border-amber-500">
                        <input type="text" id="address" placeholder="Ulica, Mesto, PSČ" class="w-full p-2.5 border border-slate-200 rounded-xl text-sm focus:outline-none focus:border-amber-500">
                    </div>
                    <button onclick="checkout()" class="w-full bg-amber-600 hover:bg-amber-700 text-white font-semibold py-3 rounded-xl transition shadow">
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

        <!-- ADMIN PANEL (skrytý, kým sa neprihlási) -->
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
                    <input type="number" step="0.01" id="new-price" placeholder="Cena v €" class="p-2.5 border border-slate-200 rounded-xl text-sm">
                    <input type="text" id="new-icon" placeholder="Ikona (napr. 🍯)" class="p-2.5 border border-slate-200 rounded-xl text-sm">
                    <input type="text" id="new-desc" placeholder="Krátky popis" class="p-2.5 border border-slate-200 rounded-xl text-sm">
                </div>
                <button onclick="addProduct()" class="bg-amber-600 hover:bg-amber-700 text-white font-semibold px-6 py-2.5 rounded-xl text-sm shadow transition">Pridať do ponuky</button>
            </div>

            <!-- Zoznam existujúcich produktov na správu -->
            <div class="bg-white p-6 rounded-2xl shadow-md border border-amber-100">
                <h2 class="text-lg font-bold text-slate-800 mb-4">Aktuálne produkty v ponuke</h2>
                <div id="admin-product-list" class="divide-y divide-amber-100">
                    <!-- Načíta sa cez JS -->
                </div>
            </div>
        </main>

        <!-- PÄTIČKA -->
        <footer class="bg-amber-900 text-amber-100 py-6 text-center text-sm mt-auto">
            <p>&copy; 2026 Včelnica u dvoch bratov. Všetky práva vyhradené. Vyrábané s láskou k prírode 🐝</p>
        </footer>

        <!-- JAVASCRIPT -->
        <script>
            let products = [
                { id: 1, name: "Kvetový med 950g", price: 8.50, icon: "🍯", desc: "Jemný krémový kvetový med z jarných lúk." },
                { id: 2, name: "Lesný med 950g", price: 10.00, icon: "🌲", desc: "Tmavý, aromatický lesný med plný minerálov." },
                { id: 3, name: "Med s vlašskými orechmi", price: 7.00, icon: "🥜", desc: "Kombinácia lahodného medu a chrumkavých orechov." },
                { id: 4, name: "Včelí propolis (tinktúra)", price: 6.50, icon: "🌿", desc: "Prírodné antibiotikum na posilnenie imunity." }
            ];

            let cart = [];

            function renderProducts() {
                const grid = document.getElementById("product-grid");
                grid.innerHTML = products.map(p => `
                    <div class="bg-white p-5 rounded-2xl shadow-sm border border-amber-100 flex flex-col justify-between hover:shadow-md transition">
                        <div>
                            <div class="text-4xl mb-3">${p.icon}</div>
                            <h3 class="font-bold text-lg text-slate-900">${p.name}</h3>
                            <p class="text-slate-500 text-xs mt-1 mb-4">${p.desc}</p>
                        </div>
                        <div class="flex items-center justify-between mt-4">
                            <span class="text-xl font-extrabold text-amber-700">${p.price.toFixed(2)} €</span>
                            <button onclick="addToCart(${p.id})" class="bg-amber-500 hover:bg-amber-600 text-white text-sm font-semibold px-4 py-2 rounded-xl transition shadow-sm">
                                Do košíka
                            </button>
                        </div>
                    </div>
                `).join('');
            }

            function renderAdminList() {
                const list = document.getElementById("admin-product-list");
                list.innerHTML = products.map(p => `
                    py-3 flex justify-between items-center text-sm
                    <div class="py-3 flex justify-between items-center w-full">
                        <div class="flex items-center space-x-3">
                            <span class="text-2xl">${p.icon}</span>
                            <div>
                                <span class="font-bold text-slate-800">${p.name}</span>
                                <span class="text-xs text-amber-700 ml-2 font-semibold">${p.price.toFixed(2)} €</span>
                            </div>
                        </div>
                        <button onclick="deleteProduct(${p.id})" class="bg-red-100 hover:bg-red-200 text-red-600 text-xs font-bold px-3 py-1.5 rounded-lg transition">Odstrániť</button>
                    </div>
                `).join('');
            }

            function openAdminLogin() {
                const password = prompt("Zadajte admin heslo:");
                if (password === "tatik") {
                    document.getElementById("store-section").classList.add("hidden");
                    document.getElementById("admin-section").classList.remove("hidden");
                    renderAdminList();
                } else if (password !== null) {
                    alert("Nesprávne heslo!");
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
                const icon = document.getElementById("new-icon").value || "🍯";
                const desc = document.getElementById("new-desc").value;

                if (!name || isNaN(price)) {
                    alert("Zadajte platný názov a cenu produktu.");
                    return;
                }

                const newId = products.length > 0 ? Math.max(...products.map(p => p.id)) + 1 : 1;
                products.push({ id: newId, name, price, icon, desc });

                document.getElementById("new-name").value = "";
                document.getElementById("new-price").value = "";
                document.getElementById("new-icon").value = "";
                document.getElementById("new-desc").value = "";

                renderAdminList();
                alert("Produkt bol úspešne pridaný!");
            }

            function deleteProduct(id) {
                products = products.filter(p => p.id !== id);
                renderAdminList();
            }

            function addToCart(id) {
                const product = products.find(p => p.id === id);
                const existing = cart.find(item => item.id === id);
                if (existing) {
                    existing.qty++;
                } else {
                    cart.push({ ...product, qty: 1 });
                }
                updateCartUI();
            }

            function removeFromCart(id) {
                cart = cart.filter(item => item.id !== id);
                updateCartUI();
            }

            function updateCartUI() {
                const cartContainer = document.getElementById("cart-items");
                const countBadge = document.getElementById("cart-count");
                const totalSpan = document.getElementById("cart-total");
                const checkoutSection = document.getElementById("checkout-section");

                let totalCount = cart.reduce((sum, item) => sum + item.qty, 0);
                let totalPrice = cart.reduce((sum, item) => sum + (item.price * item.qty), 0);

                countBadge.innerText = totalCount;
                totalSpan.innerText = totalPrice.toFixed(2) + " €";

                if (cart.length === 0) {
                    cartContainer.innerHTML = `<p class="text-slate-400 text-sm py-4 text-center">Košík je zatiaľ prázdny.</p>`;
                    checkoutSection.classList.add("hidden");
                } else {
                    cartContainer.innerHTML = cart.map(item => `
                        <div class="py-2 flex justify-between items-center w-full text-sm">
                            <div>
                                <span class="font-medium">${item.icon} ${item.name}</span>
                                <div class="text-xs text-slate-400">${item.qty} ks × ${item.price.toFixed(2)} €</div>
                            </div>
                            <button onclick="removeFromCart(${item.id})" class="text-red-400 hover:text-red-600 text-xs font-bold px-2 py-1">✕</button>
                        </div>
                    `).join('');
                    checkoutSection.classList.remove("hidden");
                }
            }

            function checkout() {
                const name = document.getElementById("name").value;
                const address = document.getElementById("address").value;

                if (!name || !address) {
                    alert("Prosím, vyplňte meno a doručovaciu adresu.");
                    return;
                }

                document.getElementById("checkout-section").classList.add("hidden");
                document.getElementById("cart-items").innerHTML = "";
                document.getElementById("success-msg").classList.remove("hidden");
                cart = [];
                updateCartUI();
            }

            function resetCart() {
                document.getElementById("success-msg").classList.add("hidden");
                document.getElementById("name").value = "";
                document.getElementById("address").value = "";
            }

            // Štartovacie načítanie
            renderProducts();
        </script>
    </body>
    </html>
    """