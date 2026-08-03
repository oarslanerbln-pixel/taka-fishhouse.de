document.addEventListener('DOMContentLoaded', () => {

    const menuWrapper = document.getElementById('menuWrapper');
    
    function renderMenu() {
        if (!menuWrapper) return;
        
        // Clear existing content
        menuWrapper.innerHTML = '';
        
        const lang = typeof i18n !== 'undefined' ? i18n.currentLang : 'de';
        
        // ===== RENDER MENU DATA =====
        if(typeof menuData !== 'undefined') {
            menuData.forEach(category => {
                const section = document.createElement('div');
                section.className = 'menu-category-section';
                if (category.categoryId === 'spezialitaten' || category.categoryId === 'hauptgerichte') {
                    section.classList.add('swipeable-row');
                }
                section.dataset.category = category.categoryId;
                
                const catTitle = lang === 'tr' ? category.categoryNameTR : category.categoryNameDE;
                
                let html = `
                    <div class="category-header">
                        <h2>${catTitle}</h2>
                    </div>
                    <div class="menu-list">
                `;
                
                if (category.items && Array.isArray(category.items)) {
                    category.items.forEach(item => {
                        // Allergen mapping (simple check for vegetarian, gluten-free, etc., for filter demo)
                        let tags = '';
                        let badgeHtml = '';
                        if (item.id === 210 || item.id === 211 || category.categoryId === 'suppen-salate') {
                            tags = 'vegetarian';
                            badgeHtml = `<div class="diet-badges"><div class="badge-icon" title="Vegetarian">🍃</div></div>`;
                        }
                        
                        const priceHtml = item.price ? `<div class="menu-item-price">${item.price} €</div>` : '';
                        const itemName = lang === 'tr' ? item.nameTR : item.nameDE;
                        
                        html += `
                            <div class="menu-item ${item.image ? 'has-image' : ''}" data-tags="${tags}" data-id="${item.id}">
                                ${item.image ? `<div class="menu-item-image">${badgeHtml}<img src="${item.image}" alt="${itemName}" loading="lazy"><div class="skeleton"></div></div>` : ''}
                                <div class="menu-item-content">
                                    <div class="menu-item-header">
                                        <span class="menu-item-num">${item.id || ''}</span>
                                        <div class="menu-item-title">
                                            <h4>${itemName} ${item.allergens ? `<span class="allergens">(${item.allergens})</span>` : ''} ${heartHtml}</h4>
                                        </div>
                                        <div class="menu-item-dots"></div>
                                        ${priceHtml}
                                    </div>
                                </div>
                            </div>
                        `;
                    });
                }
                
                html += `</div>`; // end menu-list
                section.innerHTML = html;
                menuWrapper.appendChild(section);
            });
            // Add Allergenes Legend Section
            const allergenesData = {
                allergene: {
                    tr: ["A: Glüten", "B: Kabuklular", "C: Yumurta", "D: Balık", "E: Fıstık", "F: Soya", "G: Süt", "H: Kuruyemiş", "L: Kereviz", "M: Hardal", "N: Susam", "O: Sülfitler", "P: Acıbakla", "R: Yumuşakçalar"],
                    de: ["A: Gluten", "B: Krebstiere", "C: Eier", "D: Fisch", "E: Erdnüsse", "F: Soja", "G: Milch", "H: Schalenfrüchte", "L: Sellerie", "M: Senf", "N: Sesam", "O: Sulfite", "P: Lupinen", "R: Weichtiere"]
                },
                zusatzstoffe: {
                    tr: ["1: Renklendirici", "2: Koruyucu madde", "3: Antioksidan", "4: Lezzet artırıcı", "5: Kükürtlü", "6: Karartılmış", "7: Fosfat", "8: Süt proteini", "9: Kafeinli", "10: Kininli", "11: Tatlandırıcılı", "12: Fenilalanin kaynağı içerir", "13: Mumlanmış", "14: Taurin", "15: Nitrit tuzlu"],
                    de: ["1: mit Farbstoff", "2: mit Konservierungsstoff", "3: mit Antioxidationsmittel", "4: mit Geschmacksverstärker", "5: geschwefelt", "6: geschwärzt", "7: mit Phosphat", "8: mit Milcheiweiß", "9: koffeinhaltig", "10: chininhaltig", "11: mit Süßungsmittel", "12: enthält eine Phenylalaninquelle", "13: gewachst", "14: mit Taurin", "15: nitritpökelsalzig"]
                }
            };
            const allSection = document.createElement('div');
            allSection.className = 'menu-category-section hidden';
            allSection.dataset.category = 'all';
            allSection.style.display = 'none';
            
            const allergenTitle = translations[lang]['allergen-title'] || 'Allergen Information';
            const legendAll = translations[lang]['legend-allergene'] || 'Allergene';
            const legendZusatz = translations[lang]['legend-zusatz'] || 'Zusatzstoffe';
            const legLang = allergenesData.allergene[lang] ? lang : 'de';

            let allHtml = `
                <div class="category-header">
                    <h2>${allergenTitle}</h2>
                </div>
                <div class="menu-item-group">
                    <div class="menu-item-allergenes">
                        <h5>${legendAll}</h5>
                        <ul>
                            ${allergenesData.allergene[legLang].map(a => `<li>${a}</li>`).join('')}
                        </ul>
                    </div>
                    <div class="menu-item-allergenes" style="margin-top:30px;">
                        <h5>${legendZusatz}</h5>
                        <ul>
                            ${allergenesData.zusatzstoffe[legLang].map(a => `<li>${a}</li>`).join('')}
                        </ul>
                    </div>
                </div>
            `;
            allSection.innerHTML = allHtml;
            menuWrapper.appendChild(allSection);
        }
    }

    // Initial render
    renderMenu();

    // Listen for language changes
    document.addEventListener('languageChanged', () => {
        renderMenu();
        // Since we re-rendered everything, we might need to hide/show according to active filter
        const activeBtn = document.querySelector('.cat-btn.active');
        if(activeBtn) activeBtn.click(); 
    });


    // ===== CATEGORY FILTER =====
    const catBtns = document.querySelectorAll('.cat-btn');
    
    catBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Premium Mobile UX: Haptic feedback and auto-centering
            if (navigator.vibrate) navigator.vibrate(30);
            btn.scrollIntoView({ behavior: 'smooth', inline: 'center', block: 'nearest' });

            const sections = document.querySelectorAll('.menu-category-section');
            // Update active button
            catBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const filter = btn.dataset.filter;
            
            sections.forEach(section => {
                const category = section.dataset.category;
                
                let shouldShow = false;
                if(filter === 'all') {
                    shouldShow = (category !== 'all'); 
                } else {
                    shouldShow = (category === filter);
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
                 const legSection = Array.from(sections).find(s => s.dataset.category === 'all');
                 if(legSection) {
                     legSection.classList.remove('hidden');
                     legSection.style.display = 'block';
                     legSection.style.animation = 'none';
                     legSection.offsetHeight; 
                     legSection.style.animation = 'fadeIn 0.6s ease-out';
                 }
            }
        }, 2500);
    });

    // ===== PARALLAX & BACK TO TOP =====
    const backToTopBtn = document.getElementById('backToTopBtn');
    const heroVideo = document.querySelector('.hero-video-container');
    const heroContent = document.querySelector('.menu-hero-content');

    window.addEventListener('scroll', () => {
        let scrollY = window.scrollY;
        
        // Back to top visibility
        if (scrollY > 500) {
            backToTopBtn?.classList.add('visible');
        } else {
            backToTopBtn?.classList.remove('visible');
        }
        
        // Parallax and Blur for Hero
        if (heroVideo && scrollY < 600) {
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

});
