# Taka Fisch Haus - Çalışma Alanı Kuralları

- **Proje Dizini:** Taka Fisch Haus ile ilgili görevlerde, IDE'de başka bir sekme/dosya açık olsa bile işlemleri daima `c:\Users\oarsl\Desktop\Is Dosyasi\Taka Fisch Haus` dizini altında gerçekleştir.
- **Terminal Kısıtlaması:** Bu ortamda terminal (PowerShell) üzerinden komut çalıştırma (`run_command` / ACL write NUL) hatası vermektedir. Komut çalıştırmaktan kaçın.
- **HTML Okuma Kısıtlaması:** `.html` dosyaları `view_file` aracıyla (mimetype hatası yüzünden) okunamayabilir. Bunun yerine dosyaları okumak için alternatif stratejiler (ör. `grep_search`) kullan.
- **HTML Reading Workaround:** When instructed to read or modify an `.html` file, and after confirming that `view_file` and `grep_search` fail due to environment restrictions:
  1. DO NOT attempt to use terminal commands (`run_command`) as they are blocked.
  2. DO NOT write python scripts to read the file, as you cannot execute them.
  3. INSTEAD, immediately ask the user to either:
     a) Temporarily rename the file to `.txt` so it bypasses the mimetype filter, OR
     b) Copy and paste the contents of the file directly into the chat.
- **Vercel CLI Workaround:** When running Vercel deployment or CLI commands on this machine, NEVER use the bare `vercel` command (it will fail with CommandNotFoundException). ALWAYS use `npx vercel` instead (e.g., `npx vercel --prod`).
- **Mobile First Override Protection:** When implementing mobile-specific designs (like sticky navs, single columns, transparent cards) based on videos or mobile screenshots, ALWAYS wrap the CSS overrides in `@media (max-width: 768px)` or similar. Do NOT apply mobile layout CSS globally, as it destroys the desktop grid/card layouts.
- **Light Theme Color Guard:** Bu projede iki tema çalışıyor: koyu (dark) ve açık (light, `dl-bg-white` class). `menu-page.css` içindeki hard-coded renk değerleri (`#1a1a1a`, `#fff`, vb.) tema değişkenlerini geçersiz kılabiliyor. Açık tema için CSS değişikliği yaparken her zaman `body.dl-bg-white` scope'uyla override yaz. Metin renklerini her iki temada da test etmeden deploy etme.
- **Pre-Deploy Checklist:** CSS/JS değişikliği deploy etmeden önce şunları kontrol et:
  1. JSON-LD alanları (telefon: `+493026349486`, adres: `Kottbusser Damm 35, 10967 Berlin`) doğru mu?
  2. Font Awesome veya CDN kaynakları kullanıldıysa, ilgili HTML'de `<link>` veya `<script>` etiketi var mı?
  3. Rezervasyon formu gibi kritik formlarda çift `<input>` oluşmadı mı? (`index.html` satır 463'te önceden oluştu)
  4. Ana sayfada (`index.html`) JSON-LD yapısal verisi mevcut mu? (Henüz yok — eklenecek)

