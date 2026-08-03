export function initMenu() {
    if (typeof menuData !== 'undefined' && document.getElementById('menuTabsWrapper')) {
        const tabsWrapper = document.getElementById('menuTabsWrapper');
        const contentContainer = document.getElementById('menuContentContainer');

        menuData.forEach((category, index) => {
            const isActive = index === 0 ? 'active' : '';

            // Tab
            const tabHTML = `<div class="swiper-slide tab-btn ${isActive}" data-target="${category.categoryId}">${category.categoryNameTR}</div>`;
            tabsWrapper.insertAdjacentHTML('beforeend', tabHTML);

            // Content Panel
            let itemsHTML = '';
            category.items.forEach(item => {
                const imageSrc = item.image || '';
                const imageHtml = imageSrc
                    ? `<img src="${imageSrc}" alt="${item.nameTR}" loading="lazy" style="width:100%;height:100%;object-fit:cover;">`
                    : `<span style="font-size:0.8rem;letter-spacing:1px;opacity:0.4;">✦</span>`;

                itemsHTML += `
                    <div class="swiper-slide menu-card glass-card">
                        <div class="img-placeholder" style="${imageSrc ? 'background:none;border-bottom:none;padding:0;' : ''}">
                            ${imageHtml}
                        </div>
                        <div class="menu-info">
                            <div class="menu-header">
                                <h3 class="tr-name">${item.nameTR}</h3>
                                <span class="price">${item.price} €</span>
                            </div>
                            <p class="de-name">${item.nameDE}</p>
                        </div>
                    </div>
                `;
            });

            const panelHTML = `
                <div class="menu-category-panel ${isActive}" id="${category.categoryId}" style="display:${isActive ? 'block' : 'none'};opacity:${isActive ? '1' : '0'};transition:opacity 0.4s ease;">
                    <div class="swiper category-swiper">
                        <div class="swiper-wrapper">${itemsHTML}</div>
                        <div class="swiper-pagination"></div>
                    </div>
                </div>
            `;
            contentContainer.insertAdjacentHTML('beforeend', panelHTML);
        });

        // Init Swipers
        const tabsSwiper = new Swiper('.menu-tabs-swiper', {
            slidesPerView: 'auto',
            spaceBetween: 10,
            freeMode: true,
            watchSlidesProgress: true,
        });

        const categorySwipers = {};
        document.querySelectorAll('.category-swiper').forEach(swiperEl => {
            const categoryId = swiperEl.closest('.menu-category-panel').id;
            categorySwipers[categoryId] = new Swiper(swiperEl, {
                slidesPerView: 1.15,
                spaceBetween: 20,
                grabCursor: true,
                pagination: {
                    el: swiperEl.querySelector('.swiper-pagination'),
                    clickable: true,
                    dynamicBullets: true,
                },
                breakpoints: {
                    640: { slidesPerView: 2.2, spaceBetween: 20 },
                    1024: { slidesPerView: 3.2, spaceBetween: 30 }
                }
            });
        });

        // Tab click logic
        const tabBtns = document.querySelectorAll('.tab-btn');
        const panels = document.querySelectorAll('.menu-category-panel');

        tabBtns.forEach((btn, index) => {
            btn.addEventListener('click', () => {

                tabBtns.forEach(t => t.classList.remove('active'));
                btn.classList.add('active');

                const targetId = btn.getAttribute('data-target');
                panels.forEach(p => {
                    p.classList.remove('active');
                    p.style.display = 'none';
                    p.style.opacity = '0';
                });

                const targetPanel = document.getElementById(targetId);
                targetPanel.style.display = 'block';
                void targetPanel.offsetWidth;
                targetPanel.classList.add('active');
                targetPanel.style.opacity = '1';

                if (categorySwipers[targetId]) {
                    categorySwipers[targetId].update();
                }

                tabsSwiper.slideTo(index > 0 ? index - 1 : 0);
            });
        });
    }
}
