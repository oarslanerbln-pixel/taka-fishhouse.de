import codecs

path = 'index.html'
content = codecs.open(path, 'r', 'utf8').read()

old_logo = '''<a href="#" class="brand-logo">
            <span class="logo-taka">TAKA</span>
            <span class="logo-fishhouse">Fish House</span>
        </a>'''
new_logo = '''<a href="#" class="brand-logo">
            <img src="assets/taka_logo.png" alt="TAKA Fish House Logo" class="brand-logo-img" style="height: 50px; width: auto; object-fit: contain; filter: drop-shadow(0px 2px 4px rgba(0,0,0,0.5));">
        </a>'''
content = content.replace(old_logo, new_logo)

old_footer_info = '''<div class="footer-info">
            <h4 data-i18n="footer-contact-title">Iletisim</h4>
            <p>?? Kottbusser Damm 35, 10967 Berlin</p>
            <p>?? <a href="tel:+493026349486">+49 30 26349486</a></p>
            <p>?? <span data-i18n="footer-hours">Her Gün: 11:00 – 22:00</span></p>
        </div>'''
        
new_footer_info = '''<div class="footer-info">
            <h4 data-i18n="footer-contact-title">Iletisim & Impressum</h4>
            <p><strong>Taka Fish House GmbH</strong><br>?? Kottbusser Damm 35, 10967 Berlin</p>
            <p>?? <a href="tel:+493026349486">+49 30 26349486</a><br>?? Fax: 0800 202 07 702</p>
            <p>?? <span data-i18n="footer-hours">Her Gün: 11:00 – 22:00</span></p>
            <div style="font-size: 0.8rem; color: var(--text-muted); margin-top: 15px;">
                Vertretungsberechtigt: Ufuk Sentürk<br>
                Amtsgericht Charlottenburg: HRB 280084 B<br>
                MwSt-Nummer: DE457770945
            </div>
        </div>'''
content = content.replace(old_footer_info, new_footer_info)

old_map = '''<div class="contact-map">
                <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2428.468202356502!2d13.41724217696238!3d52.50153833715421!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47a84e311a2f960f%3A0xb3551532fcd0c732!2sKottbusser%20Damm%2035%2C%2010967%20Berlin!5e0!3m2!1str!2sde!4v1709210000000!5m2!1str!2sde" 
                    width="100%" 
                    height="100%" 
                    style="border:0;" 
                    allowfullscreen="" 
                    loading="lazy" 
                    referrerpolicy="no-referrer-when-downgrade">
                </iframe>
            </div>'''
new_map = '''<div class="contact-map" style="filter: invert(90%) hue-rotate(180deg) brightness(95%) contrast(100%); border-radius: 12px; overflow: hidden; border: 1px solid rgba(212,175,55,0.2);">
                <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2428.468202356502!2d13.41724217696238!3d52.50153833715421!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x47a84e311a2f960f%3A0xb3551532fcd0c732!2sKottbusser%20Damm%2035%2C%2010967%20Berlin!5e0!3m2!1str!2sde!4v1709210000000!5m2!1str!2sde" 
                    width="100%" 
                    height="100%" 
                    style="border:0;" 
                    allowfullscreen="" 
                    loading="lazy" 
                    referrerpolicy="no-referrer-when-downgrade">
                </iframe>
            </div>'''
content = content.replace(old_map, new_map)

old_reservation = '''<div class="res-actions">
                <a href="tel:+493026349486" class="btn btn-primary btn-large">
                    <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M6.62 10.79c1.44 2.83 3.76 5.14 6.59 6.59l2.2-2.2c.27-.27.67-.36 1.02-.24 1.12.37 2.33.57 3.57.57.55 0 1 .45 1 1V20c0 .55-.45 1-1 1-9.39 0-17-7.61-17-17 0-.55.45-1 1-1h3.5c.55 0 1 .45 1 1 0 1.25.2 2.45.57 3.57.11.35.03.74-.25 1.02l-2.2 2.2z"/></svg>
                    <span data-i18n="res-call">Hemen Ara</span>: +49 30 26349486
                </a>
                <span class="res-subtext" data-i18n="res-soon">Online rezervasyon sistemi yakinda!</span>
            </div>'''
            
new_reservation = '''<form class="res-form" style="margin-top: 30px; display: grid; gap: 15px; grid-template-columns: 1fr 1fr; text-align: left;">
                <input type="text" placeholder="Isim Soyisim" style="padding: 12px; border-radius: 8px; border: 1px solid rgba(212,175,55,0.3); background: rgba(0,0,0,0.5); color: #fff;">
                <input type="tel" placeholder="Telefon Numarasi" style="padding: 12px; border-radius: 8px; border: 1px solid rgba(212,175,55,0.3); background: rgba(0,0,0,0.5); color: #fff;">
                <input type="date" style="padding: 12px; border-radius: 8px; border: 1px solid rgba(212,175,55,0.3); background: rgba(0,0,0,0.5); color: #fff; grid-column: 1 / 2;">
                <select style="padding: 12px; border-radius: 8px; border: 1px solid rgba(212,175,55,0.3); background: rgba(0,0,0,0.5); color: #fff; grid-column: 2 / 3;">
                    <option value="2">2 Kisi</option>
                    <option value="3">3 Kisi</option>
                    <option value="4">4 Kisi</option>
                    <option value="5">5+ Kisi</option>
                </select>
                <button type="button" onclick="window.location.href='tel:+493026349486'" class="btn btn-primary" style="grid-column: 1 / -1; justify-content: center; font-size: 1.1rem; border: none; cursor: pointer;">Hizli Rezervasyon Yap</button>
            </form>'''
content = content.replace(old_reservation, new_reservation)

codecs.open(path, 'w', 'utf8').write(content)
print('Done updating index.html')
