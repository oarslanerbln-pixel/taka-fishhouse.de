// Bir ürün görseli var gibi görünüp (yol yazılı) gerçekte yüklenemezse
// (eksik dosya, ölü link) tarayıcının çirkin kırık-resim ikonu yerine
// menünün kendi "Görsel Hazırlanıyor" rozetini göster. renderMenu()
// tarafından her <img>'in onerror'unda çağrılır.
window.__takaImgFallback = function (imgEl, text) {
    const wrap = imgEl.closest('.menu-item-image');
    const item = imgEl.closest('.menu-item');
    const content = item ? item.querySelector('.menu-item-content') : null;
    if (!wrap || !item) return;
    wrap.remove(); // görsel çerçevesini tamamen kaldır — kırık ikon kalmasın
    item.classList.remove('has-image');
    // Rozeti, gerçekten görselsiz ürünlerdeki AYNI konuma (içerik bloğunun
    // sonuna) ekle — böylece iki durum da birebir aynı görünür.
    if (content) {
        const badge = document.createElement('div');
        badge.className = 'no-image-badge';
        badge.innerHTML = `<span class="icon">✨</span><span class="text"></span>`;
        badge.querySelector('.text').textContent = text; // XSS'e kapalı: metin innerHTML değil textContent ile yazılır
        content.appendChild(badge);
    }
};

document.addEventListener('DOMContentLoaded', () => {

    // "Perde açılma" giriş animasyonu (.menu-hero.reveal-active) — artık
    // hem menu.html hem qr-menu/index.html'de var, ikisi de bu ortak
    // dosyayı paylaşıyor. .menu-hero bulunamazsa (video hiç yoksa) no-op
    // geçilir. CSS tarafı .reveal-active eklenene kadar videoyu kapalı
    // (clip-path: inset 50%, opacity 0) tutuyor.
    (function revealMenuHero() {
        const hero = document.querySelector('.menu-hero');
        const video = document.getElementById('menuHeroVideo');
        if (!hero) return;
        const reveal = () => hero.classList.add('reveal-active');
        if (!video) { reveal(); return; }
        if (video.readyState >= 2) {
            reveal();
        } else {
            video.addEventListener('loadeddata', reveal, { once: true });
            // Video hiç yüklenmezse (ağ hatası vb.) perde sonsuza kadar kapalı kalmasın.
            setTimeout(reveal, 2500);
        }
    })();

    // Sabit (sticky) header, arama kutusu ve kategori çubuğu üst üste
    // dizilirken CSS üç ayrı yerde header/arama yüksekliğini elle tahmin
    // ediyordu (157px / 149px / 92px / 84px / 64px gibi). Logo metni dar
    // ekranlarda iki satıra sarınca gerçek yükseklik bunların hiçbiriyle
    // eşleşmiyor ve kategori sekmeleri header'ın ARKASINDA kalıp görünmez
    // oluyordu. Artık gerçek yükseklikler ölçülüp CSS değişkenine yazılıyor.
    (function syncStickyOffsets() {
        const header = document.getElementById('header');
        const search = document.querySelector('.search-container');
        if (!header) return;
        const apply = () => {
            const root = document.documentElement.style;
            root.setProperty('--header-h', header.getBoundingClientRect().height + 'px');
            if (search) root.setProperty('--search-h', search.getBoundingClientRect().height + 'px');
        };
        apply();
        window.addEventListener('resize', apply);
        window.addEventListener('load', apply);
        if (document.fonts && document.fonts.ready) document.fonts.ready.then(apply);
        if (window.ResizeObserver) {
            const ro = new ResizeObserver(apply);
            ro.observe(header);
            if (search) ro.observe(search);
        }
    })();

    function getCorrectImageUrl(imagePath) {
        if (!imagePath || imagePath.startsWith('http') || imagePath.includes('placeholder') || imagePath.startsWith('data:')) return imagePath;

        let newPath = imagePath;

        // NOT: Burada eskiden "uskumru.jpg" ve "kizarmis_dondurma_tek_top.jpg"
        // için elle dosya adı düzeltmeleri vardı. Veri artık doğru dosya
        // adlarını (uskumru.jpg.jpg) doğrudan kullanıyor, o yüzden bu iki kural
        // hiçbir zaman eşleşmiyordu (ölü kod) — ikincisi ayrıca var olmayan bir
        // dosyaya (kizarmis_dondurma.jpg) işaret ediyordu, yani bir gün veri
        // yeniden eşleşirse sessizce 404 verecekti (Rotbarbe'de daha önce
        // yaşanan hatayla — bkz. commit cda3848 — aynı kalıp). İkisi de
        // kaldırıldı.

        // Vercel root directory'ye çıkmak için ../ kullanıyoruz
        if (!newPath.startsWith('../') && !newPath.startsWith('/') && !newPath.startsWith('http')) {
            newPath = '../' + newPath;
        }
        
        return newPath;
    }

    // ===== ASMR AUDIO SYSTEM =====
    const AudioContext = window.AudioContext || window.webkitAudioContext;
    let audioCtx;

    function playAsmrSound(type) {
        if(!audioCtx) {
            try { audioCtx = new AudioContext(); } catch(e) { return; }
        }
        if(audioCtx.state === 'suspended') audioCtx.resume();
        
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        
        osc.connect(gain);
        gain.connect(audioCtx.destination);
        
        const now = audioCtx.currentTime;
        
        if(type === 'click') {
            // Soft click
            osc.type = 'sine';
            osc.frequency.setValueAtTime(800, now);
            osc.frequency.exponentialRampToValueAtTime(200, now + 0.04);
            gain.gain.setValueAtTime(0, now);
            gain.gain.linearRampToValueAtTime(0.2, now + 0.01);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.04);
            osc.start(now);
            osc.stop(now + 0.05);
        } else if(type === 'pop') {
            // Heart pop / water drop
            osc.type = 'sine';
            osc.frequency.setValueAtTime(400, now);
            osc.frequency.linearRampToValueAtTime(1000, now + 0.06);
            gain.gain.setValueAtTime(0, now);
            gain.gain.linearRampToValueAtTime(0.4, now + 0.02);
            gain.gain.exponentialRampToValueAtTime(0.001, now + 0.1);
            osc.start(now);
            osc.stop(now + 0.1);
        }
    }

    const menuWrapper = document.getElementById('menuWrapper');
    
    function renderMenu() {
        if (!menuWrapper) return;
        
        // Clear existing content
        menuWrapper.innerHTML = '';
        
        const lang = typeof i18n !== 'undefined' ? i18n.currentLang : 'de';
        
        // ===== RENDER MENU DATA =====
        if(typeof menuData !== 'undefined') {
            
            // Hack to prevent duplicate 'Kızarmış Dondurma' rendering based on user feedback
            let seenIceCream = false;
            menuData.forEach(category => {
                if(category.items && Array.isArray(category.items)) {
                    category.items = category.items.filter(item => {
                        if (item.nameTR && item.nameTR.toLowerCase().includes('kızarmış dondurma')) {
                            if (seenIceCream) return false;
                            seenIceCream = true;
                        }
                        return true;
                    });
                }
            });

            menuData.forEach(category => {
                const section = document.createElement('div');
                section.className = 'menu-category-section';
                section.dataset.category = category.categoryId;
                
                let catTitle = category.categoryNameDE || category.categoryDE;
                if (lang === 'tr') catTitle = category.categoryNameTR || category.categoryTR;
                if (lang === 'en' && (category.categoryNameEN || category.categoryEN)) catTitle = category.categoryNameEN || category.categoryEN;
                if (lang === 'ru' && (category.categoryNameRU || category.categoryRU)) catTitle = category.categoryNameRU || category.categoryRU;
                if (lang === 'es' && (category.categoryNameES || category.categoryES)) catTitle = category.categoryNameES || category.categoryES;
                if (lang === 'ar' && (category.categoryNameAR || category.categoryAR)) catTitle = category.categoryNameAR || category.categoryAR;
                
                // Premium micro-interactions: add favorite heart
                const heartHtml = `<button class="fav-btn" aria-label="Favorite"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path></svg></button>`;

                let html = `
                    <div class="category-header">
                        <h2>${catTitle}</h2>
                    </div>
                    <div class="menu-list">
                `;
                
                if (category.items && Array.isArray(category.items)) {
                    category.items.forEach(item => {
                        let priceHtml = '';
                        if (item.price) {
                            if (item.price.includes('/')) {
                                const portionTexts = {
                                    'tr': 'Küçük / Büyük Porsiyon',
                                    'de': 'Kleine / Große Portion',
                                    'en': 'Small / Large Portion',
                                    'ru': 'Маленькая / Большая порция',
                                    'es': 'Porción Pequeña / Grande',
                                    'ar': 'حصة صغيرة / كبيرة'
                                };
                                const pText = portionTexts[lang] || portionTexts['de'];
                                priceHtml = `<div class="menu-item-price-container" style="display: flex; flex-direction: column; align-items: flex-end;">
                                                <div class="menu-item-price">${item.price} €</div>
                                                <div class="portion-info" style="font-size: 0.75rem; color: var(--text-muted); opacity: 0.8; margin-top: 2px;">${pText}</div>
                                             </div>`;
                            } else {
                                priceHtml = `<div class="menu-item-price">${item.price} €</div>`;
                            }
                        }
                        let itemName = item.nameDE;
                        if (lang === 'tr') itemName = item.nameTR;
                        if (lang === 'en' && item.nameEN) itemName = item.nameEN;
                        if (lang === 'ru' && item.nameRU) itemName = item.nameRU;
                        if (lang === 'es' && item.nameES) itemName = item.nameES;
                        if (lang === 'ar' && item.nameAR) itemName = item.nameAR;
                        
                        // Alerjen & diyet etiketleri
                        let tags = [];
                        let badgeHtml = '';

                        // Product Badges
                        if (item.badge) {
                            if (item.badge === 'popular') {
                                badgeHtml += `<div class="product-badge badge-popular"><i class="fa-solid fa-fire"></i> <span data-i18n="badge-popular">Popüler</span></div>`;
                            } else if (item.badge === 'chef') {
                                badgeHtml += `<div class="product-badge badge-chef"><i class="fa-solid fa-star"></i> <span data-i18n="badge-chef">Şefin Seçimi</span></div>`;
                            }
                        }

                        // Vejetaryen/glutensiz durumu artık assets/js/menu-data.js içindeki
                        // item.diet alanından geliyor (scripts/migrate-diet-flags.js ile
                        // ürünün kendi alerjen kodlarından ve adından üretildi).
                        // Eskiden burada "item.id >= 130" gibi rastgele bir sayı eşiği
                        // ve veride hiç var olmayan kategori ID'leri ("desserts",
                        // "getranke", "alkohol") kullanılıyordu — 130+ ID'li HER ürün,
                        // ne olduğuna bakılmaksızın otomatik "vejetaryen + glutensiz"
                        // damgası yiyordu.
                        let isVeg = !!(item.diet && item.diet.vegetarian);
                        let isGf = !!(item.diet && item.diet.glutenFree);

                        if (isVeg) {
                            tags.push('vegetarian');
                            badgeHtml += `<div class="badge-icon" title="Vegetarian">🍃</div>`;
                        }
                        if (isGf) {
                            tags.push('gluten-free');
                            badgeHtml += `<div class="badge-icon" title="Gluten-Free">🌾</div>`;
                        }
                        
                        if (badgeHtml !== '') {
                            badgeHtml = `<div class="diet-badges">${badgeHtml}</div>`;
                        }
                        
                        const tagsString = tags.join(' ');
                        
                        const noImageText = (typeof translations !== 'undefined' && translations[lang] && translations[lang]['coming-soon']) ? translations[lang]['coming-soon'] : 'Görsel Hazırlanıyor';
                        
                        let imageSrc = getCorrectImageUrl(item.image);

                        const noImageHtml = imageSrc ? '' : `<div class="no-image-badge"><span class="icon">✨</span><span class="text">${noImageText}</span></div>`;
                        // "imageSrc var" demek "dosya gerçekten yükleniyor" demek değil.
                        // Yol yazılı ama dosya eksikse (örn. citir_karides.png) tarayıcının
                        // çirkin kırık-resim ikonu yerine aynı "Görsel Hazırlanıyor" rozetini
                        // göstermek için onerror'da kartı zarifçe düşürüyoruz.
                        const noImageTextEsc = noImageText.replace(/'/g, "\\'");

                        let story = '';
                        if (lang === 'tr') story = item.storyTR || item.storyDE || '';
                        else if (lang === 'en') story = item.storyEN || item.storyDE || '';
                        else story = item.storyDE || '';

                        const viewDetailsText = (typeof translations !== 'undefined' && translations[lang] && translations[lang]['view-details']) ? translations[lang]['view-details'] : (lang === 'tr' ? 'DETAYLARI GÖR' : (lang === 'de' ? 'DETAILS ANSEHEN' : 'VIEW DETAILS'));
                        const storyHtml = (story ? `<p class="menu-item-desc-inline">${story}</p>` : '') + `<div class="view-details-wrapper"><span class="view-details-btn">${viewDetailsText}</span></div>`;

                        html += `
                            <div class="menu-item ${imageSrc ? 'has-image' : ''}" data-tags="${tagsString}" data-id="${item.id}">
                                ${imageSrc ? `
                                <div class="menu-item-image">
                                    ${badgeHtml}
                                    <img src="${imageSrc}" alt="${itemName}" loading="lazy" onerror="window.__takaImgFallback(this, '${noImageTextEsc}')">
                                    <div class="skeleton"></div>
                                </div>` : ''}
                                <div class="menu-item-content">
                                    <div class="menu-item-header">
                                        <div class="menu-item-title-row">
                                            <h4>${itemName} ${item.allergens ? `<span class="allergens">(${item.allergens})</span>` : ''} ${heartHtml}</h4>
                                            ${priceHtml}
                                        </div>
                                    </div>
                                    ${storyHtml}
                                    ${noImageHtml}
                                </div>
                            </div>
                        `;
                    });
                }
                
                html += `</div>`; // end menu-list
                section.innerHTML = html;
                menuWrapper.appendChild(section);
            });
            
            // ===== ALERJEN / EK MADDE LEJANDI =====
            // Yemek ürünleri item.allergens'te SAYISAL AB alerjen kodları
            // taşıyor (1,2,4,7,11,14 — Gluten/Krebstiere/Fisch/Milch/
            // Sesam/Weichtiere). İçecekler ise TAMAMEN AYRI bir HARF
            // tabanlı ek madde (Zusatzstoffe) kodlaması taşıyor (A,B,C,
            // E,F,H,I,J). Eskiden burada TEK bir tablo vardı ve o tablo
            // harfleri "D: Fisch, G: Milch" gibi ALERJEN isimleriyle
            // açıklıyordu — yani balık alerjisi olan bir müşteri yemeğin
            // yanında "(4)" görüp lejantta "4" değil sadece "D: Fisch"
            // bulabiliyordu; veride hiç kullanılmayan D/G harfleri
            // listedeyken, gerçekten kullanılan I/J harfleri hiç yoktu.
            // Artık iki ayrı tablo var ve kodlar veriden DİNAMİK olarak
            // toplanıyor — yeni bir kod eklenirse lejant kendiliğinden
            // güncellenir, elle senkron tutmaya gerek kalmaz.
            const usedAllergenCodes = new Set();
            const usedAdditiveCodes = new Set();
            menuData.forEach(cat => (cat.items || []).forEach(it => {
                (it.allergens || '').split(',').map(s => s.trim()).filter(Boolean).forEach(code => {
                    (/^[0-9]+$/.test(code) ? usedAllergenCodes : usedAdditiveCodes).add(code);
                });
            }));

            // Resmi AB Gıda Bilgilendirme Yönetmeliği (1169/2011) Ek II — 14 alerjen.
            const ALLERGEN_NAMES = {
                1: { tr: 'Gluten içeren tahıllar', de: 'Glutenhaltiges Getreide', en: 'Cereals containing gluten', ru: 'Злаки, содержащие глютен', es: 'Cereales con gluten', ar: 'الحبوب التي تحتوي على الغلوتين' },
                2: { tr: 'Kabuklu deniz ürünleri', de: 'Krebstiere', en: 'Crustaceans', ru: 'Ракообразные', es: 'Crustáceos', ar: 'القشريات' },
                3: { tr: 'Yumurta', de: 'Eier', en: 'Eggs', ru: 'Яйца', es: 'Huevos', ar: 'البيض' },
                4: { tr: 'Balık', de: 'Fisch', en: 'Fish', ru: 'Рыба', es: 'Pescado', ar: 'السمك' },
                5: { tr: 'Yer fıstığı', de: 'Erdnüsse', en: 'Peanuts', ru: 'Арахис', es: 'Cacahuetes', ar: 'الفول السوداني' },
                6: { tr: 'Soya', de: 'Sojabohnen', en: 'Soybeans', ru: 'Соя', es: 'Soja', ar: 'فول الصويا' },
                7: { tr: 'Süt / Laktoz', de: 'Milch/Laktose', en: 'Milk/Lactose', ru: 'Молоко/лактоза', es: 'Leche/Lactosa', ar: 'الحليب/اللاكتوز' },
                8: { tr: 'Sert kabuklu yemişler', de: 'Schalenfrüchte', en: 'Tree nuts', ru: 'Орехи', es: 'Frutos de cáscara', ar: 'المكسرات' },
                9: { tr: 'Kereviz', de: 'Sellerie', en: 'Celery', ru: 'Сельдерей', es: 'Apio', ar: 'الكرفس' },
                10: { tr: 'Hardal', de: 'Senf', en: 'Mustard', ru: 'Горчица', es: 'Mostaza', ar: 'الخردل' },
                11: { tr: 'Susam', de: 'Sesamsamen', en: 'Sesame seeds', ru: 'Кунжут', es: 'Sésamo', ar: 'السمسم' },
                12: { tr: 'Kükürt dioksit/Sülfitler', de: 'Schwefeldioxid/Sulfite', en: 'Sulphur dioxide/Sulphites', ru: 'Диоксид серы/сульфиты', es: 'Dióxido de azufre/Sulfitos', ar: 'ثاني أكسيد الكبريت/الكبريتات' },
                13: { tr: 'Acı bakla (lupin)', de: 'Lupinen', en: 'Lupin', ru: 'Люпин', es: 'Altramuces', ar: 'الترمس' },
                14: { tr: 'Yumuşakçalar', de: 'Weichtiere', en: 'Molluscs', ru: 'Моллюски', es: 'Moluscos', ar: 'الرخويات' },
            };
            // Standart Alman gastronomi ek madde (Zusatzstoffe) harf kodlaması.
            const ADDITIVE_NAMES = {
                A: { tr: 'Renklendirici içerir', de: 'mit Farbstoff', en: 'Contains coloring', ru: 'Содержит краситель', es: 'Contiene colorante', ar: 'يحتوي على ملون' },
                B: { tr: 'Koruyucu içerir', de: 'mit Konservierungsstoff', en: 'Contains preservative', ru: 'Содержит консервант', es: 'Contiene conservante', ar: 'يحتوي على مادة حافظة' },
                C: { tr: 'Antioksidan içerir', de: 'mit Antioxidationsmittel', en: 'Contains antioxidant', ru: 'Содержит антиоксидант', es: 'Contiene antioxidante', ar: 'يحتوي على مضاد أكسدة' },
                D: { tr: 'Tat güçlendirici içerir', de: 'mit Geschmacksverstärker', en: 'Contains flavor enhancer', ru: 'Содержит усилитель вкуса', es: 'Contiene potenciador del sabor', ar: 'يحتوي على معزز نكهة' },
                E: { tr: 'Kükürtlenmiş', de: 'geschwefelt', en: 'Sulphured', ru: 'Сульфитировано', es: 'Sulfurado', ar: 'مكبرت' },
                F: { tr: 'Kararmış (siyahlaştırılmış)', de: 'geschwärzt', en: 'Blackened (darkened)', ru: 'Затемнено', es: 'Ennegrecido', ar: 'مُسوّد' },
                G: { tr: 'Mumlanmış', de: 'gewachst', en: 'Waxed', ru: 'Вощеный', es: 'Encerado', ar: 'مشمّع' },
                H: { tr: 'Fosfat içerir', de: 'mit Phosphat', en: 'Contains phosphate', ru: 'Содержит фосфат', es: 'Contiene fosfato', ar: 'يحتوي على فوسفات' },
                I: { tr: 'Kafein içerir', de: 'koffeinhaltig', en: 'Contains caffeine', ru: 'Содержит кофеин', es: 'Contiene cafeína', ar: 'يحتوي على كافيين' },
                J: { tr: 'Kinin içerir', de: 'chininhaltig', en: 'Contains quinine', ru: 'Содержит хинин', es: 'Contiene quinina', ar: 'يحتوي على الكينين' },
                K: { tr: 'Tatlandırıcı içerir', de: 'mit Süßungsmitteln', en: 'Contains sweeteners', ru: 'Содержит подсластители', es: 'Contiene edulcorantes', ar: 'يحتوي على محليات' },
                L: { tr: 'Fenilalanin kaynağı içerir', de: 'enthält eine Phenylalaninquelle', en: 'Contains a source of phenylalanine', ru: 'Содержит источник фенилаланина', es: 'Contiene una fuente de fenilalanina', ar: 'يحتوي على مصدر فينيل ألانين' },
            };

            const nameFor = (map, code) => (map[code] && (map[code][lang] || map[code].de)) || code;
            const allergenRows = [...usedAllergenCodes].sort((a, b) => +a - +b)
                .map(code => `<li><strong>${code}</strong> — ${nameFor(ALLERGEN_NAMES, code)}</li>`).join('');
            const additiveRows = [...usedAdditiveCodes].sort()
                .map(code => `<li><strong>${code}</strong> — ${nameFor(ADDITIVE_NAMES, code)}</li>`).join('');

            const allSection = document.createElement('div');
            allSection.className = 'menu-category-section';
            allSection.dataset.category = 'all_legend';

            const allergenTitle = translations[lang]['allergen-title'] || 'Allergen Information';
            const legendAllergens = translations[lang]['legend-allergene'] || 'Allergene';
            const legendAdditives = translations[lang]['legend-zusatz'] || 'Zusatzstoffe';

            allSection.innerHTML = `
                <div class="category-header">
                    <h2>${allergenTitle}</h2>
                </div>
                <div class="menu-item-group menu-item-group--legend">
                    ${allergenRows ? `<div class="menu-item-allergenes">
                        <h5>${legendAllergens}</h5>
                        <ul>${allergenRows}</ul>
                    </div>` : ''}
                    ${additiveRows ? `<div class="menu-item-allergenes">
                        <h5>${legendAdditives}</h5>
                        <ul>${additiveRows}</ul>
                    </div>` : ''}
                </div>
            `;
            menuWrapper.appendChild(allSection);

            initInteractions();

            // i18n.updateUI() sayfa ilk açılırken (i18n.js'nin kendi
            // DOMContentLoaded'ı) BU fonksiyondan ÖNCE bir kere çalışıyor —
            // yani "Popüler"/"Şefin Seçimi" rozeti gibi renderMenu()'nun
            // kendisinin oluşturduğu data-i18n elemanları o an DOM'da hiç
            // yoktu ve hiçbir zaman çevrilmiyordu. Her render'dan sonra
            // burada tekrar çağırarak yeni oluşturulan elemanların da
            // güncel dile göre dolmasını sağlıyoruz.
            if (typeof i18n !== 'undefined') i18n.updateUI();
        }
    }

    // Initial render
    renderMenu();

    // ===== DIET FILTER LOGIC =====
    const dietFilterBtns = document.querySelectorAll('.diet-filter-btn');
    
    function applyDietFilters() {
        const activeFilters = Array.from(dietFilterBtns)
            .filter(btn => btn.classList.contains('active'))
            .map(btn => btn.dataset.type);
            
        const allItems = document.querySelectorAll('.menu-item');
        const allSections = document.querySelectorAll('.menu-category-section:not([data-category="all_legend"])');
        
        if (activeFilters.length === 0) {
            allItems.forEach(item => item.style.display = '');
            allSections.forEach(sec => sec.style.display = '');
            return;
        }
        
        allItems.forEach(item => {
            const itemTags = item.dataset.tags ? item.dataset.tags.split(' ') : [];
            const matchesAll = activeFilters.every(filter => itemTags.includes(filter));
            
            if (matchesAll) {
                item.style.display = 'flex';
            } else {
                item.style.display = 'none';
            }
        });
        
        // Hide sections that have no visible items, but respect active category filter
        const activeCategoryBtn = document.querySelector('.cat-btn.active');
        const activeCategory = activeCategoryBtn ? activeCategoryBtn.dataset.filter : 'all';

        allSections.forEach(sec => {
            const category = sec.dataset.category;
            let categoryMatch = false;
            if (activeCategory === 'all') {
                categoryMatch = (category !== 'all_legend');
            } else {
                categoryMatch = (category === activeCategory);
            }

            const visibleItems = Array.from(sec.querySelectorAll('.menu-item')).filter(i => i.style.display !== 'none');
            
            if (visibleItems.length === 0 || !categoryMatch) {
                sec.style.display = 'none';
            } else {
                sec.style.display = 'block';
            }
        });
    }

    dietFilterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            btn.classList.toggle('active');
            playAsmrSound('pop');
            if(navigator.vibrate) navigator.vibrate(15);
            applyDietFilters();
        });
    });

    document.addEventListener('languageChanged', () => {
        renderMenu();
        applyDietFilters(); // Re-apply diet filters when language changes

        // Modal (#storyModalOverlay) menuWrapper'ın DIŞINDA yaşıyor, bu yüzden
        // renderMenu() ona hiç dokunmaz. Popup açıkken dil değiştirilirse
        // içerik (başlık/fiyat/açıklama/alerjen) eski dilde donuk kalıyordu —
        // açıksa güncel dile göre yeniden dolduruyoruz.
        const openModal = document.getElementById('storyModalOverlay');
        if (openModal && openModal.classList.contains('active') && currentOpenItemId) {
            populateStoryModal(currentOpenItemId);
        }
    });

    // Şu an popup'ta açık olan ürünün id'si (kapalıyken null). languageChanged
    // handler'ının hangi ürünü yeniden dolduracağını bilmesi için tutuluyor.
    let currentOpenItemId = null;

    // Modal içeriğini (başlık/fiyat/açıklama/alerjen/eşleşen ürün) doldurur.
    // Hem ürün kartına tıklanınca hem de modal AÇIKKEN dil değiştirilince
    // (yukarıdaki languageChanged handler'ı) çağrılabilsin diye ayrı bir
    // fonksiyona çıkarıldı. itemId bulunamazsa false döner.
    function populateStoryModal(itemId) {
        const sImg = document.getElementById('storyModalImg');
        const sTitle = document.getElementById('storyModalTitle');
        const sPrice = document.getElementById('storyModalPrice');
        const sDesc = document.getElementById('storyModalDesc');
        const sPairing = document.getElementById('storyModalPairing');
        if (!sTitle || typeof menuData === 'undefined') return false;

        let foundItem = null;
        for (let cat of menuData) {
            const f = cat.items?.find(i => i.id === itemId);
            if (f) { foundItem = f; break; }
        }
        if (!foundItem) return false;

        const lang = typeof i18n !== 'undefined' ? i18n.currentLang : 'de';

        let itemName = foundItem.nameDE;
        if (lang === 'tr') itemName = foundItem.nameTR;
        if (lang === 'en' && foundItem.nameEN) itemName = foundItem.nameEN;
        if (lang === 'ru' && foundItem.nameRU) itemName = foundItem.nameRU;
        if (lang === 'es' && foundItem.nameES) itemName = foundItem.nameES;
        if (lang === 'ar' && foundItem.nameAR) itemName = foundItem.nameAR;

        sTitle.textContent = itemName;
        sPrice.textContent = foundItem.price ? foundItem.price + ' €' : '';

        let modalImgSrc = getCorrectImageUrl(foundItem.image || 'assets/placeholder.jpg');
        sImg.src = modalImgSrc;

        // Story logic without fallback leaking to other languages.
        // storyRU/ES/AR veri setinde yok — bu diller için İngilizce'ye,
        // o da yoksa Almanca/Türkçe'ye düşülür (boş açıklama modalı yerine).
        let story = foundItem['story' + lang.toUpperCase()]
            || foundItem.storyEN || foundItem.storyDE || foundItem.storyTR;
        sDesc.textContent = story || '';
        sDesc.style.display = story ? '' : 'none';

        // Allergen Logic
        let sAllergens = document.getElementById('storyModalAllergens');
        if (!sAllergens) {
            sAllergens = document.createElement('div');
            sAllergens.id = 'storyModalAllergens';
            sAllergens.className = 'modal-allergens';
            const descContainer = document.querySelector('.story-modal-desc-container');
            if (descContainer) descContainer.appendChild(sAllergens);
        }

        if (foundItem.allergens) {
            // "Alerjen:" etiketi dil ne olursa olsun hep Türkçe sabitti —
            // Almanca/İngilizce modda bile değişmiyordu.
            const allergenLabel = (typeof translations !== 'undefined' && translations[lang] && translations[lang]['modal-allergen-label']) || 'Allergen';
            const algArray = foundItem.allergens.split(',');
            let algHtml = '';
            algArray.forEach(alg => {
                algHtml += `<span class="modal-allergen-badge">${allergenLabel}: ${alg.trim()}</span>`;
            });
            sAllergens.innerHTML = algHtml;
            sAllergens.style.display = 'flex';
        } else {
            sAllergens.style.display = 'none';
        }

        // Smart Pairing Logic
        if (foundItem.pairingId) {
            let pairingItem = null;
            for (let cat of menuData) {
                const p = cat.items?.find(i => i.id === foundItem.pairingId);
                if (p) { pairingItem = p; break; }
            }
            if (pairingItem) {
                let pName = pairingItem.nameDE;
                if (lang === 'tr') pName = pairingItem.nameTR;
                if (lang === 'en' && pairingItem.nameEN) pName = pairingItem.nameEN;
                if (lang === 'ru' && pairingItem.nameRU) pName = pairingItem.nameRU;
                if (lang === 'es' && pairingItem.nameES) pName = pairingItem.nameES;
                if (lang === 'ar' && pairingItem.nameAR) pName = pairingItem.nameAR;
                document.getElementById('pairingTitle').textContent = pName;
                document.getElementById('pairingPrice').textContent = pairingItem.price ? pairingItem.price + ' €' : '';

                let pImgSrc = getCorrectImageUrl(pairingItem.image || 'assets/placeholder.jpg');
                document.getElementById('pairingImg').src = pImgSrc;

                sPairing.classList.remove('hidden');
            } else {
                sPairing.classList.add('hidden');
            }
        } else {
            sPairing.classList.add('hidden');
        }

        return true;
    }

    // ===== INTERACTION LOGIC (ScrollSpy, Lightbox, Hearts) =====
    function initInteractions() {
        // Image Load Skeleton removal
        document.querySelectorAll('.menu-item-image img').forEach(img => {
            img.onload = () => {
                const skeleton = img.parentElement.querySelector('.skeleton');
                if (skeleton) skeleton.style.opacity = '0';
            }
        });

        // Storytelling Modal & Lightbox Logic
        const storyModal = document.getElementById('storyModalOverlay');
        const sClose = document.getElementById('storyModalClose');

        if (storyModal) {
            document.querySelectorAll('.menu-item').forEach(itemCard => {
                itemCard.addEventListener('click', (e) => {
                    // Ignore clicks on fav btn
                    if (e.target.closest('.fav-btn')) return;

                    // ASMR & Haptics
                    if (navigator.vibrate) navigator.vibrate(15);
                    playAsmrSound('click');

                    const itemId = parseInt(itemCard.dataset.id);
                    if (!itemId) return;
                    if (!populateStoryModal(itemId)) return;

                    currentOpenItemId = itemId;
                    storyModal.classList.add('active');
                    // overflow:hidden yerine class kullanıyoruz: menu-page.css'te
                    // sticky pozisyon düzeltmesi html/body'e "overflow-y: visible
                    // !important" veriyor ve bu, inline style'ı (JS'in eski hali)
                    // eziyordu — modal açıkken arka plan telefonlarda kayabiliyordu.
                    document.body.classList.add('modal-open');
                });
            });

            // sClose/storyModal statik elemanlar — menuWrapper'ın dışında,
            // hiç yeniden oluşturulmuyor. initInteractions() her dil
            // değişiminde (renderMenu() ile) tekrar çalıştığı için, bu
            // dinleyicileri korumasız her seferinde eklemek üst üste
            // yığılan "duplicate listener" birikimine yol açıyordu.
            if (!storyModal.dataset.chromeBound) {
                storyModal.dataset.chromeBound = 'true';

                const closeStoryModal = () => {
                    storyModal.classList.remove('active');
                    document.body.classList.remove('modal-open');
                    currentOpenItemId = null;
                };

                sClose.addEventListener('click', closeStoryModal);
                storyModal.addEventListener('click', (e) => {
                    if (e.target === storyModal) closeStoryModal();
                });
            }
        }

        // Heart/Favorite Toggle
        document.querySelectorAll('.fav-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                btn.classList.toggle('active');
                if(navigator.vibrate) navigator.vibrate(20);
                playAsmrSound('pop');
                
                // Add pop animation
                btn.style.transform = 'scale(1.3)';
                setTimeout(() => btn.style.transform = 'scale(1)', 200);
            });
        });
    }

    // ===== CATEGORY FILTER (Tab-Based) =====
    const catBtns = document.querySelectorAll('.cat-btn');
    
    catBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Haptic feedback & ASMR
            if (navigator.vibrate) navigator.vibrate(30);
            playAsmrSound('click');
            
            // Center the clicked button in the scroll track (sabit Alerjenler
            // simgesi artık şeridin dışında bir kardeş öğe, bu mantığın dışında)
            const track = document.querySelector('.categories-track');
            if(track && btn.closest('.categories-track')) {
                const trackRect = track.getBoundingClientRect();
                const btnRect = btn.getBoundingClientRect();
                const scrollLeft = track.scrollLeft + (btnRect.left - trackRect.left) - (trackRect.width / 2) + (btnRect.width / 2);
                track.scrollTo({ left: scrollLeft, behavior: 'smooth' });
            }

            const sections = document.querySelectorAll('.menu-category-section');
            // Update active button
            catBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.filter;
            // 13 sekme 6'ya indirilirken bazı sekmeler artık birden fazla
            // categoryId'yi birden gösteriyor (örn. "hauptgerichte,deniz-mahsulleri").
            // Menü verisi (menuData'daki categoryId'ler) hiç değişmedi —
            // sadece hangi sekmenin hangi kategorileri görünür kıldığı değişti.
            const filterList = filter.split(',');

            sections.forEach(section => {
                const category = section.dataset.category;

                let shouldShow = false;
                if(filter === 'all') {
                    shouldShow = (category !== 'all'); // Show all except the hidden legend base
                } else {
                    shouldShow = filterList.includes(category);
                }

                if (shouldShow) {
                    section.classList.remove('hidden');
                    section.style.display = 'block';
                    // Re-trigger animation
                    section.style.animation = 'none';
                    section.offsetHeight; 
                    section.style.animation = 'fadeIn 0.6s ease-out';
                } else {
                    section.classList.add('hidden');
                    section.style.display = 'none';
                }
            });
            
            if(filter === 'all_legend') {
                 const legSection = Array.from(sections).find(s => s.dataset.category === 'all_legend');
                 if(legSection) {
                     legSection.classList.remove('hidden');
                     legSection.style.display = 'block';
                     legSection.style.animation = 'none';
                     legSection.offsetHeight; 
                     legSection.style.animation = 'fadeIn 0.6s ease-out';
                 }
            }
        });
    });

    // ===== LIVE SEARCH =====
    const menuSearch = document.getElementById('menuSearch');
    const clearSearch = document.getElementById('clearSearch');
    
    if (menuSearch) {
        let isSearching = false;
        menuSearch.addEventListener('input', (e) => {
            const searchTerm = e.target.value.toLowerCase().trim();
            const allItems = document.querySelectorAll('.menu-item');
            const allSections = document.querySelectorAll('.menu-category-section');
            
            if (searchTerm.length > 0) {
                if (clearSearch) clearSearch.style.display = 'block';
                if (!isSearching) {
                    isSearching = true;
                    // Reset to "all" category when starting a search
                    const allBtn = document.querySelector('.cat-btn[data-filter="all"]');
                    if(allBtn) allBtn.click();
                }
            } else {
                if (clearSearch) clearSearch.style.display = 'none';
                isSearching = false;
            }
            
            allItems.forEach(item => {
                const title = item.querySelector('h4') ? item.querySelector('h4').textContent.toLowerCase() : '';
                const desc = item.querySelector('.menu-item-desc-inline') ? item.querySelector('.menu-item-desc-inline').textContent.toLowerCase() : '';
                
                if (title.includes(searchTerm) || desc.includes(searchTerm)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
            
            allSections.forEach(section => {
                if (section.dataset.category === 'all_legend') return;
                
                const visibleItems = Array.from(section.querySelectorAll('.menu-item')).filter(item => item.style.display !== 'none');
                
                if (searchTerm.length > 0) {
                    if (visibleItems.length === 0) {
                        section.style.display = 'none';
                    } else {
                        section.style.display = 'block';
                    }
                } else {
                    section.style.display = 'block';
                }
            });
        });
        
        if (clearSearch) {
            clearSearch.addEventListener('click', () => {
                menuSearch.value = '';
                menuSearch.dispatchEvent(new Event('input'));
            });
        }
    }

    // ===== CINEMATIC REVEAL REMOVED FOR SMOOTH PARALLAX =====

    // ===== PARALLAX & BACK TO TOP =====
    const backToTopBtn = document.getElementById('backToTopBtn');
    const heroVideo = document.querySelector('.hero-video-container');
    const heroContent = document.querySelector('.menu-hero-content');

    window.addEventListener('scroll', () => {
        let scrollY = window.scrollY;
        const header = document.getElementById('header');
        
        // Add subtle shadow to header when scrolling
        if (scrollY > 10) {
            header?.classList.add('has-shadow');
        } else {
            header?.classList.remove('has-shadow');
        }

        // Back to top visibility
        if (scrollY > 500) {
            backToTopBtn?.classList.add('visible');
        } else {
            backToTopBtn?.classList.remove('visible');
        }
        
        // Parallax and Blur for Hero
        if (heroVideo && scrollY < 400) {
            let blurValue = Math.min(scrollY / 40, 10);
            let opacityValue = Math.max(1 - (scrollY / 400), 0.3);
            heroVideo.style.filter = `blur(${blurValue}px)`;
            heroVideo.style.opacity = opacityValue;
            heroVideo.style.transform = `translateY(${scrollY * 0.4}px)`;
        }
        
        if (heroContent && scrollY < 400) {
            let opacityValue = Math.max(1 - (scrollY / 200), 0);
            heroContent.style.opacity = opacityValue;
            heroContent.style.transform = `translateY(${scrollY * 0.2}px)`;
        }
    });

    if (backToTopBtn) {
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
            if(navigator.vibrate) navigator.vibrate(10);
        });
    }

    // ===== Premium Splash Screen Logic =====
    const premiumSplash = document.getElementById('premium-splash');
    if (premiumSplash) {
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
            premiumSplash.remove();
        } else {
            // Prevent scrolling during splash
            document.body.style.overflow = 'hidden';

            // ~1.8 saniyelik kısa bir karşılama — sonra kayboluyor
            setTimeout(() => {
                premiumSplash.classList.add('is-exiting');

                // Allow scrolling again
                document.body.style.overflow = '';

                // Remove from DOM to keep things clean
                setTimeout(() => {
                    premiumSplash.remove();
                }, 1200);
            }, 1800);
        }
    }
});
