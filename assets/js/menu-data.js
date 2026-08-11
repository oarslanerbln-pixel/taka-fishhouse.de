const menuData = [
    {
        "categoryId": "hauptgerichte",
        "categoryTR": "Ana Yemekler",
        "categoryDE": "Hauptgerichte",
        "categoryNameEN": "Main Courses",
        "categoryNameRU": "Основные блюда",
        "categoryNameES": "Platos principales",
        "categoryNameAR": "الأطباق الرئيسية",
        "icon": "fa-fish-fins",
        "items": [
            {
                "id": 61,
                "badge": "popular",
                "nameTR": "Çipura (Izgara veya Tava)",
                "nameDE": "Dorade (gegrillt oder gebraten)",
                "nameEN": "Sea Bream (Grilled or Fried)",
                "nameRU": "Дорадо (Гриль или Жареная)",
                "nameES": "Dorada (A la plancha o frita)",
                "nameAR": "دنيس (مشوي أو مقلي)",
                "price": "24,50",
                "image": "assets/img/products/dorade.jpg",
                "pairingId": 22,
                "storyTR": "Ege'nin serin sularından özenle seçilmiş, şefimizin özel zeytinyağı marinasyonu ile hazırlanan taptaze Çipura. Izgara ateşinde mühürlenerek sululuğunu ve o eşsiz deniz aromasını kaybetmeden masanıza gelir.",
                "storyDE": "Sorgfältig aus den kühlen Gewässern der Ägäis ausgewählt, wird diese frische Dorade mit einer speziellen Olivenöl-Marinade unseres Küchenchefs zubereitet. Auf dem Grill versiegelt, um ihre Saftigkeit und das unvergleichliche Meeresaroma zu bewahren.",
                "storyEN": "Carefully selected from the cool waters of the Aegean, this fresh Sea Bream is prepared with our chef's special olive oil marinade. Seared on the grill to retain its juiciness and that incomparable sea aroma.",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 62,
                "nameTR": "Levrek (Izgara veya Tava)",
                "nameDE": "Wolfsbarsch (gegrillt oder gebraten)",
                "nameEN": "Sea Bass (Grilled or Fried)",
                "nameRU": "Сибас (Гриль или Жареный)",
                "nameES": "Lubina (A la plancha o frita)",
                "nameAR": "قاروص (مشوي أو مقلي)",
                "price": "24,50",
                "image": "assets/img/products/levrek.jpg",
                "pairingId": 20,
                "storyTR": "Günün en taze avlarından... Kar beyazı eti ve pürüzsüz dokusuyla Levrek, deniz ürünleri tutkunları için bir başyapıt. Özel baharat harmanımızla marine edilerek dışı çıtır, içi pamuk gibi servis edilir.",
                "storyDE": "Einer der frischesten Fänge des Tages... Mit seinem schneeweißen Fleisch und der geschmeidigen Textur ist der Wolfsbarsch ein Meisterwerk für Liebhaber von Meeresfrüchten. Mit unserer speziellen Gewürzmischung mariniert, wird er außen knusprig und innen butterweich serviert.",
                "storyEN": "One of the freshest catches of the day... With its snow-white meat and smooth texture, the Sea Bass is a masterpiece for seafood lovers. Marinated with our special spice blend, it is served crispy on the outside and buttery soft on the inside.",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 63,
                "nameTR": "Hamsi Tava",
                "nameDE": "Hamsi – gebraten",
                "nameEN": "Hamsi (Fried Anchovies)",
                "nameRU": "Жареная хамса",
                "nameES": "Anchoas fritas",
                "nameAR": "أنشوجة مقلية",
                "price": "20,00",
                "image": "assets/img/products/hamsi_gebraten.jpg",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 65,
                "nameTR": "Barbun",
                "nameDE": "Rotbarbe",
                "nameEN": "Red Mullet",
                "nameRU": "Барабулька",
                "nameES": "Salmonete",
                "nameAR": "سلطان إبراهيم",
                "price": "25,00",
                "image": "assets/img/products/rotbarbe_ai2.jpg",
                "pairingId": 22,
                "storyTR": "Taze avlanmış barbun balığı, ustalıkla temizlenip hafifçe unlanarak altın sarısı olana dek kızartılır. Çıtır dokusu ve nefis lezzetiyle Karadeniz esintisini sofranıza taşır.",
                "storyDE": "Frisch gefangene Rotbarbe, fachmännisch gesäubert, leicht mehliert und goldbraun gebraten. Mit ihrer knusprigen Textur und dem köstlichen Geschmack bringt sie eine Brise des Schwarzen Meeres auf Ihren Tisch.",
                "storyEN": "Freshly caught red mullet, expertly cleaned, lightly floured, and fried until golden brown. With its crispy texture and delicious flavor, it brings a breeze of the Black Sea to your table.",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 66,
                "nameTR": "Uskumru",
                "nameDE": "Makrele",
                "nameEN": "Mackerel",
                "nameRU": "Скумбрия",
                "nameES": "Caballa",
                "nameAR": "إسقمري",
                "price": "22,00",
                "image": "assets/img/products/makrele.jpg",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 67,
                "nameTR": "Somon File",
                "nameDE": "Lachsfilet",
                "nameEN": "Salmon Filet",
                "nameRU": "Филе лосося",
                "nameES": "Filete de salmón",
                "nameAR": "فيليه سلمون",
                "price": "26,00",
                "image": "assets/img/products/lachsfilet.jpg",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 68,
                "nameTR": "Alabalık",
                "nameDE": "Forelle",
                "nameEN": "Trout",
                "nameRU": "Форель",
                "nameES": "Trucha",
                "nameAR": "تروتة",
                "price": "23,00",
                "image": "assets/img/products/forelle_ai.jpg",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 71,
                "nameTR": "Mezgit",
                "nameDE": "Merlan",
                "nameEN": "Whiting (Merlan)",
                "nameRU": "Мерланг",
                "nameES": "Merlán",
                "nameAR": "بياض",
                "price": "22,00",
                "image": "assets/img/products/merlan.jpg",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 72,
                "nameTR": "İstavrit",
                "nameDE": "Stöcker",
                "nameEN": "Horse Mackerel",
                "nameRU": "Ставрида",
                "nameES": "Jurel",
                "nameAR": "شيم",
                "price": "22,00",
                "image": "assets/img/products/istavrit.jpg",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 74,
                "badge": "chef",
                "nameTR": "Karışık Taka Spesiyal Izgara",
                "nameDE": "Gemischter Taka Spezial Teller",
                "nameEN": "Taka Special Mixed Grill",
                "nameRU": "Тарелка смешанного гриля Taka",
                "nameES": "Parrillada mixta especial Taka",
                "nameAR": "مشاوي مشكلة تاكا سبيشال",
                "price": "29,50",
                "image": "assets/img/products/gemischter_taka_spezial_teller_ai.jpg",
                "allergens": "2,4,14",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 80,
                "nameTR": "Dil Balığı",
                "nameDE": "Seezunge",
                "nameEN": "Sole Fish",
                "nameRU": "Морской язык",
                "nameES": "Lenguado",
                "nameAR": "سمك موسى",
                "price": "32,00",
                "image": "assets/img/products/dil_baligi.jpg",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 81,
                "nameTR": "2 Kişilik Taka Özel Menü Tabağı",
                "nameDE": "Taka Spezial Menü Teller für 2 Personen",
                "nameEN": "Taka Special Menu Platter for 2 Persons",
                "nameRU": "Специальное меню Taka на 2 персоны",
                "nameES": "Menú Especial Taka para 2 personas",
                "nameAR": "طبق قائمة تاكا الخاصة لشخصين",
                "price": "75,00",
                "image": "assets/img/products/taka_spezial_2_personen.jpg",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            }
        ]
    },
    {
        "categoryId": "corbalar",
        "categoryTR": "Çorbalar",
        "categoryDE": "Suppen",
        "categoryNameEN": "Soups",
        "categoryNameRU": "Супы",
        "categoryNameES": "Sopas",
        "categoryNameAR": "الشوربات",
        "icon": "fa-bowl-food",
        "items": [
            {
                "id": 1,
                "nameTR": "Balık Çorbası",
                "nameDE": "Lachssuppe",
                "nameEN": "Fish Soup (Salmon)",
                "nameRU": "Рыбный суп (Лосось)",
                "nameES": "Sopa de pescado (Salmón)",
                "nameAR": "شوربة سمك (سلمون)",
                "price": "8,50",
                "image": "assets/img/products/lachssuppe.jpg",
                "allergens": "4,7",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            }
        ]
    },
    {
        "categoryId": "salatalar",
        "categoryTR": "Salatalar",
        "categoryDE": "Salate",
        "categoryNameEN": "Salads",
        "categoryNameRU": "Салаты",
        "categoryNameES": "Ensaladas",
        "categoryNameAR": "السلطات",
        "icon": "fa-leaf",
        "items": [
            {
                "id": 4,
                "nameTR": "Karışık Yeşil Salata",
                "nameDE": "Gemischter grüner Salat",
                "nameEN": "Mixed Green Salad",
                "nameRU": "Смешанный зеленый салат",
                "nameES": "Ensalada verde mixta",
                "nameAR": "سلطة خضراء مشكلة",
                "price": "6,00 / 8,00",
                "image": "assets/img/products/gemischter_gruener_salat.jpg",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 5,
                "nameTR": "Çoban Salatası",
                "nameDE": "Bauernsalat",
                "nameEN": "Shepherd's Salad",
                "nameRU": "Салат Чобан",
                "nameES": "Ensalada del pastor",
                "nameAR": "سلطة الراعي",
                "price": "6,50 / 8,50",
                "image": "assets/img/products/bauernsalat.jpg",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 6,
                "nameTR": "Roka Salatası",
                "nameDE": "Ruccolasalat",
                "image": "assets/img/products/rucolasalat.jpg",
                "nameEN": "Arugula Salad",
                "nameRU": "Салат с рукколой",
                "nameES": "Ensalada de rúcula",
                "nameAR": "سلطة جرجير",
                "price": "6,00 / 8,00",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 7,
                "nameTR": "Somon Salatası",
                "nameDE": "Lachssalat",
                "image": "assets/img/products/lachssalat.jpg",
                "nameEN": "Salmon Salad",
                "nameRU": "Салат с лососем",
                "nameES": "Ensalada de salmón",
                "nameAR": "سلطة سلمون",
                "price": "17,50",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 8,
                "nameTR": "Karides Salatası",
                "nameDE": "Garnelensalat",
                "image": "assets/img/products/garnelensalat.jpg",
                "nameEN": "Shrimp Salad",
                "nameRU": "Салат с креветками",
                "nameES": "Ensalada de camarones",
                "nameAR": "سلطة جمبري",
                "price": "17,50",
                "allergens": "2",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 9,
                "nameTR": "Hamsi Salatası",
                "nameDE": "Hamsisalat",
                "image": "assets/img/products/hamsisalat.jpg",
                "nameEN": "Anchovy Salad",
                "nameRU": "Салат с хамсой",
                "nameES": "Ensalada de anchoas",
                "nameAR": "سلطة أنشوجة",
                "price": "15,50",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            }
        ]
    },
    {
        "categoryId": "soguk-mezeler",
        "categoryTR": "Soğuk Mezeler",
        "categoryDE": "Kalte Vorspeisen",
        "categoryNameEN": "Cold Appetizers",
        "categoryNameRU": "Холодные закуски",
        "categoryNameES": "Aperitivos fríos",
        "categoryNameAR": "المقبلات الباردة",
        "icon": "fa-plate-wheat",
        "items": [
            {
                "id": 10,
                "nameTR": "Karışık Meze Tabağı",
                "nameDE": "Gemischter Vorspeisenteller",
                "nameEN": "Mixed Appetizer Platter",
                "nameRU": "Смешанная Тарелка Закусок",
                "nameES": "Plato de Aperitivos Mixtos",
                "nameAR": "مقبلات مشكلة",
                "price": "13,50 / 22,50",
                "image": "assets/img/products/karisik_meze_tabagi.jpg",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            },
            {
                "id": 13,
                "nameTR": "Havuç Tarator",
                "nameDE": "Tarator – Joghurt, Möhren",
                "nameEN": "Carrot Tarator (Yogurt & Carrots)",
                "nameRU": "Морковный таратор",
                "nameES": "Tarator de zanahoria",
                "nameAR": "طرطور جزر",
                "price": "4,50 / 7,50",
                "image": "assets/img/products/havuc_tarator.jpg",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 14,
                "nameTR": "Acı Antep Ezmesi",
                "nameDE": "Scharfes Paprikapüree",
                "nameEN": "Spicy Pepper Paste (Antep Ezme)",
                "nameRU": "Острая паста (Антеп Эзме)",
                "nameES": "Pasta picante (Antep Ezme)",
                "nameAR": "معجون حار (عنتاب إزمي)",
                "price": "4,50 / 7,50",
                "image": "assets/img/products/acili_ezme.jpg",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            },
            {
                "id": 15,
                "nameTR": "Humus",
                "nameDE": "Humus",
                "nameEN": "Hummus",
                "nameRU": "Хумус",
                "nameES": "Hummus",
                "nameAR": "حمص",
                "price": "4,50 / 7,50",
                "allergens": "11",
                "image": "assets/img/products/humus.jpg",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 16,
                "nameTR": "Levrek Marin",
                "nameDE": "Wolfsbarsch Marin",
                "nameEN": "Marinated Sea Bass",
                "nameRU": "Маринованный сибас",
                "nameES": "Lubina marinada",
                "nameAR": "قاروص متبل",
                "price": "8,50 / 12,50",
                "image": "assets/img/products/wolfsbarsch_marin_ai.jpg",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 17,
                "nameTR": "Deniz Mahsülleri",
                "nameDE": "Meeresfrüchte",
                "nameEN": "Seafood",
                "nameRU": "Морепродукты",
                "nameES": "Mariscos",
                "nameAR": "مأكولات بحرية",
                "price": "8,50 / 12,50",
                "image": "assets/img/products/meeresfruechte_meze.jpg",
                "allergens": "2,4,14",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 18,
                "nameTR": "Şakşuka",
                "nameDE": "Şakşuka",
                "image": "assets/img/products/saksuka.jpg",
                "nameEN": "Şakşuka",
                "nameRU": "Шакшука",
                "nameES": "Shakshuka",
                "nameAR": "شكشوكة",
                "price": "4,50 / 7,50",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            },
            {
                "id": 19,
                "nameTR": "Girit Ezmesi",
                "nameDE": "Kretische Käsepaste",
                "nameEN": "Cretan Cheese Paste",
                "nameRU": "Критская сырная паста",
                "nameES": "Pasta de queso cretense",
                "nameAR": "معجون جبن كريتي",
                "price": "4,50 / 7,50",
                "image": "assets/img/products/girit_ezmesi_ai.jpg",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 21,
                "nameTR": "Köpoğlu",
                "nameDE": "Geröstete Aubergine, Paprika, Joghurt mit Knoblauch",
                "nameEN": "Köpoğlu (Roasted Eggplant, Pepper & Yogurt)",
                "nameRU": "Кёпоглу (Запеченные баклажаны с йогуртом)",
                "nameES": "Köpoğlu (Berenjena asada y yogur)",
                "nameAR": "كوبوغلو (باذنجان مشوي مع زبادي)",
                "price": "4,50 / 7,50",
                "image": "assets/img/products/kopoglu.jpg",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 22,
                "nameTR": "Ahtapot Salatası",
                "nameDE": "Oktopussalat",
                "nameEN": "Octopus Salad",
                "nameRU": "Салат с осьминогом",
                "nameES": "Ensalada de pulpo",
                "nameAR": "سلطة أخطبوط",
                "price": "9,50 / 14,50",
                "image": "assets/img/products/oktopussalat.jpg",
                "allergens": "14",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 23,
                "nameTR": "Narlı Dibariye",
                "nameDE": "Grüner Salat mit Granatapfel, Petersilie, Frühlingszwiebel",
                "nameEN": "Dibariye Salad (Greens, Pomegranate, Parsley)",
                "nameRU": "Салат с гранатом (Дибарие)",
                "nameES": "Ensalada Dibariye (Verduras y Granada)",
                "nameAR": "سلطة ديبريه (خضار ورمان)",
                "price": "4,50 / 7,50",
                "image": "https://imageproxy.wolt.com/assets/69a80cc67d25f60394a12f6c",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            },
            {
                "id": 27,
                "nameTR": "Urla Meze",
                "nameDE": "Urla Meze",
                "image": "assets/img/products/urla_meze.jpg",
                "nameEN": "Urla Meze",
                "nameRU": "Урла Мезе",
                "nameES": "Urla Meze",
                "nameAR": "أورلا ميزي",
                "price": "4,50 / 7,50",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 30,
                "nameTR": "Yoğurtlu Patlıcan",
                "nameDE": "Aubergine mit Joghurt",
                "image": "assets/img/products/aubergine_mit_joghurt.jpg",
                "nameEN": "Eggplant with Yogurt",
                "nameRU": "Баклажаны с йогуртом",
                "nameES": "Berenjena con yogur",
                "nameAR": "باذنجان مع زبادي",
                "price": "4,50 / 7,50",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 31,
                "nameTR": "Kuru Cacık",
                "nameDE": "Kuru Cacik (traditioneller türkischer Joghurt Gurken-Dip)",
                "nameEN": "Dry Tzatziki (Traditional Yogurt Dip)",
                "nameRU": "Сухой дзадзики",
                "nameES": "Tzatziki seco",
                "nameAR": "تزاتزيكي جاف",
                "price": "4,50 / 7,50",
                "image": "assets/img/products/kuru_cacik_ai.jpg",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            },
            {
                "id": 32,
                "nameTR": "Pembe Sultan",
                "nameDE": "Rote Beete mit Joghurt und Knoblauch",
                "nameEN": "Beetroot with Yogurt and Garlic",
                "nameRU": "Свекла с йогуртом и чесноком",
                "nameES": "Remolacha con yogur y ajo",
                "nameAR": "شمندر مع زبادي وثوم",
                "image": "assets/img/products/pembe_sultan.jpg",
                "price": "4,50 / 7,50",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 35,
                "nameTR": "Deniz Börülcesi",
                "nameDE": "Seespargel",
                "nameEN": "Sea Asparagus (Samphire)",
                "nameRU": "Морская спаржа",
                "nameES": "Espárrago de mar",
                "nameAR": "هليون البحر",
                "price": "9,50 / 12,50",
                "image": "assets/img/products/deniz_borulcesi.jpg",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            }
        ]
    },
    {
        "categoryId": "ara-sicaklar",
        "categoryTR": "Ara Sıcaklar",
        "categoryDE": "Warme Zwischengerichte",
        "categoryNameEN": "Warm Appetizers",
        "categoryNameRU": "Тёплые закуски",
        "categoryNameES": "Aperitivos calientes",
        "categoryNameAR": "المقبلات الساخنة",
        "icon": "fa-fire-burner",
        "items": [
            {
                "id": 42,
                "nameTR": "Patlıcanlı Balık",
                "nameDE": "Fisch auf Augerberginenpüreebett",
                "nameEN": "Fish on Eggplant Puree Bed",
                "nameRU": "Рыба на пюре из баклажанов",
                "nameES": "Pescado sobre cama de puré de berenjena",
                "nameAR": "سمك على هريس الباذنجان",
                "price": "16,50",
                "image": "assets/img/products/fisch_auf_auberginenpuereebett.jpg",
                "allergens": "4,7",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 43,
                "nameTR": "Balık Kokoreç",
                "nameDE": "Geschnetzelte Fischpfanne",
                "nameEN": "Fish Kokoretsi (Sautéed Spiced Fish)",
                "nameRU": "Рыбный кокореч",
                "nameES": "Kokoretsi de pescado",
                "nameAR": "كوكوريتش سمك",
                "price": "15,50",
                "image": "assets/img/products/geschnetzelte_fischpfanne.jpg",
                "allergens": "4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 44,
                "nameTR": "Deniz Mahsülleri Taka Spesiyal",
                "nameDE": "Meeresfrüchte Taka Spezial",
                "nameEN": "Seafood Taka Special",
                "nameRU": "Морепродукты Taka Special",
                "nameES": "Mariscos especial Taka",
                "nameAR": "مأكولات بحرية تاكا سبيشال",
                "price": "18,50",
                "image": "assets/img/products/deniz_mahsulleri_taka_spesiyal_ai.jpg",
                "allergens": "2,4,14",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 45,
                "nameTR": "Kaşarlı Mantar",
                "nameDE": "Gegrillte Champions mit Käse überbacken",
                "nameEN": "Grilled Mushrooms baked with Cheese",
                "nameRU": "Грибы, запеченные с сыром",
                "nameES": "Champiñones horneados con queso",
                "nameAR": "فطر مخبوز بالجبن",
                "price": "10,50",
                "image": "assets/img/products/kasarli_mantar.jpg",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 46,
                "nameTR": "Kaşarlı Brokoli",
                "nameDE": "Überbackene Brokkoli",
                "nameEN": "Broccoli baked with Cheese",
                "nameRU": "Брокколи, запеченные с сыром",
                "nameES": "Brócoli horneado con queso",
                "nameAR": "بروكلي مخبوز بالجبن",
                "price": "10,50",
                "image": "assets/img/products/ueberbackene_brokkoli.jpg",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 47,
                "nameTR": "Pastırmalı Humus",
                "nameDE": "Humus mit Pastırma",
                "nameEN": "Hummus with Pastrami",
                "nameRU": "Хумус с бастурмой",
                "nameES": "Hummus con pastrami",
                "nameAR": "حمص بالبسطرمة",
                "price": "9,50",
                "image": "assets/img/products/humus_mit_pastirma_ai.jpg",
                "allergens": "7,11",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 49,
                "nameTR": "Tavada Kızarmış Patates, Taka Spesiyal",
                "nameDE": "Bratkartoffel Taka Spezial",
                "nameEN": "Pan-fried Potatoes, Taka Special",
                "nameRU": "Жареный картофель Taka Special",
                "nameES": "Patatas fritas especiales Taka",
                "nameAR": "بطاطس مقلية تاكا سبيشال",
                "price": "7,50",
                "image": "assets/img/products/bratkartoffel_taka_spezial.jpg",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            },
            {
                "id": 50,
                "nameTR": "Patates Kızartması",
                "nameDE": "Pommes frites",
                "image": "assets/img/products/pommes_frites.jpg",
                "nameEN": "French Fries",
                "nameRU": "Картофель фри",
                "nameES": "Patatas fritas",
                "nameAR": "بطاطس مقلية",
                "price": "4,50",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            },
            {
                "id": 9701,
                "nameTR": "Peynir Dolgulu Çıtır Enginar",
                "nameDE": "Knusprige Artischocken mit Käsefüllung",
                "nameEN": "Crispy Artichoke with Cheese Filling",
                "nameRU": "Хрустящие артишоки с сырной начинкой",
                "nameES": "Alcachofas crujientes rellenas de queso",
                "nameAR": "خرشوف مقرمش محشو بالجبن",
                "price": "17,50",
                "image": "assets/img/products/spesiyal_enginar_ai.jpg",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            }
        ]
    },
    {
        "categoryId": "deniz-mahsulleri",
        "categoryTR": "Deniz Mahsülleri",
        "categoryDE": "Meeresfrüchte",
        "categoryNameEN": "Seafood",
        "categoryNameRU": "Морепродукты",
        "categoryNameES": "Mariscos",
        "categoryNameAR": "المأكولات البحرية",
        "icon": "fa-shrimp",
        "items": [
            {
                "id": 73,
                "nameTR": "Kendi yapımımız Kalamar Halka",
                "nameDE": "Hausgemachte panierte Kalamaresringe",
                "nameEN": "Homemade Calamari Rings",
                "nameRU": "Домашние кольца кальмара",
                "nameES": "Anillos de calamar caseros",
                "nameAR": "حلقات حبار منزلية",
                "price": "22,00",
                "image": "assets/img/products/kalamaresringe.jpg",
                "allergens": "1,14",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 75,
                "nameTR": "Tereyağlı Büyük Karides Tavası",
                "nameDE": "Garnelenpfanne in Butter",
                "nameEN": "Jumbo Shrimp Pan in Butter",
                "nameRU": "Тигровые креветки на сливочном масле",
                "nameES": "Sartén de camarones jumbo a la mantequilla",
                "nameAR": "مقلاة جمبري جامبو بالزبدة",
                "price": "25,00",
                "image": "assets/img/products/garnelenpfanne_butter.jpg",
                "allergens": "2,7",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 76,
                "nameTR": "Domates Soslu Karides Tavası, acı",
                "nameDE": "Garnelenpfanne in Tomatensoße, scharf",
                "nameEN": "Shrimp Pan in Spicy Tomato Sauce",
                "nameRU": "Креветки в остром томатном соусе",
                "nameES": "Sartén de camarones en salsa de tomate picante",
                "nameAR": "مقلاة جمبري بصلصة طماطم حارة",
                "price": "25,00",
                "image": "assets/img/products/garnelenpfanne_tomatensosse.jpg",
                "allergens": "2",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 77,
                "nameTR": "Taka Spesiyal Karides Tavası",
                "nameDE": "Garnelenpfanne TAKA Spezial",
                "image": "assets/img/products/garnelenpfanne_taka_spezial.jpg",
                "nameEN": "TAKA Special Shrimp Pan",
                "nameRU": "Креветки на сковороде TAKA Special",
                "nameES": "Sartén de camarones TAKA Especial",
                "nameAR": "مقلاة جمبري تاكا سبيشال",
                "price": "28,00",
                "allergens": "2,4,7,14",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 78,
                "nameTR": "Izgara Ahtapot",
                "nameDE": "Gegrillter Octopus",
                "nameEN": "Grilled Octopus",
                "nameRU": "Осьминог на гриле",
                "nameES": "Pulpo a la parrilla",
                "nameAR": "أخطبوط مشوي",
                "price": "32,00",
                "image": "assets/img/products/izgara_ahtapot.jpg",
                "allergens": "14",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 38,
                "nameTR": "Kaşarlı Karides Güveç",
                "nameDE": "Überbackener Garnelenauflauf",
                "nameEN": "Shrimp Casserole baked with Cheese",
                "nameRU": "Запеканка с креветками и сыром",
                "nameES": "Cazuela de camarones horneada con queso",
                "nameAR": "طاجن جمبري مخبوز بالجبن",
                "price": "19,50",
                "image": "assets/img/products/ueberbackener_garnelenauflauf.jpg",
                "allergens": "2,7",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 39,
                "nameTR": "Izgara Karides (3 Adet Jumbo)",
                "nameDE": "Gegrillte Jumbo Garnelen (3 Stück)",
                "nameEN": "Grilled Jumbo Shrimp (3 Pieces)",
                "nameRU": "Тигровые креветки на гриле (3 шт.)",
                "nameES": "Camarones jumbo a la parrilla (3 Piezas)",
                "nameAR": "جمبري جامبو مشوي (3 قطع)",
                "price": "21,50",
                "image": "assets/img/products/jumbo_garnelen_ai.jpg",
                "allergens": "2",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 41,
                "nameTR": "Pastırmalı Ahtapot",
                "nameDE": "Oktopus mit Pastırma",
                "nameEN": "Octopus with Pastrami",
                "nameRU": "Осьминог с бастурмой",
                "nameES": "Pulpo con pastrami",
                "nameAR": "أخطبوط بالبسطرمة",
                "price": "18,50",
                "image": "assets/img/products/oktopus_mit_pastirma.jpg",
                "allergens": "14",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 9992,
                "nameTR": "Taka Deniz Mahsülleri Spesiyal",
                "nameDE": "Taka Meeresfrüchte Spezial",
                "nameEN": "Taka Seafood Special",
                "nameRU": "Така Спешл Морепродукты",
                "nameES": "Especial Mariscos Taka",
                "nameAR": "طبق تاكا البحري الخاص",
                "price": "35,00",
                "image": "assets/img/products/taka_meeresfruechte_spezial.jpg",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 9991,
                "nameTR": "Çıtır Karides",
                "nameDE": "Crispy Garnellen",
                "nameEN": "Crispy Shrimp",
                "nameRU": "Хрустящие Креветки",
                "nameES": "Camarones Crujientes",
                "nameAR": "جمبري مقرمش",
                "price": "22,50",
                "image": "assets/img/products/crispy_garnelen.jpg",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 9993,
                "nameTR": "Zinnur (stok bitene kadar, sadece Cuma-Pazar)",
                "nameDE": "Zinnur (solange Vorrat reicht, nur freitags bis sonntags)",
                "nameEN": "Zinnur (while stocks last, Fri–Sun only)",
                "nameRU": "Зиннур (пока есть в наличии, только пт-вс)",
                "nameES": "Zinnur (hasta agotar existencias, solo vie-dom)",
                "nameAR": "زينور (حتى نفاد الكمية، جمعة-أحد فقط)",
                "price": "28,50",
                "allergens": "4",
                "storyTR": "Çıtır kızartılmış deniz mahsülleri sarması, özel bir sos eşliğinde sunulur.",
                "storyDE": "Knusprig gebackene Rolle mit Meeresfrüchten, serviert mit einer speziellen Sauce.",
                "storyEN": "Crispy baked roll with seafood, served with a special sauce.",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            }
        ]
    },
    {
        "categoryId": "balik-ekmek",
        "categoryTR": "Balık Sandviç / Dürüm",
        "categoryDE": "Fisch Sandwich / Dürüm",
        "categoryNameEN": "Fish Sandwich / Wrap",
        "categoryNameRU": "Рыбный сэндвич / дюрюм",
        "categoryNameES": "Sándwich de pescado / dürüm",
        "categoryNameAR": "ساندويتش السمك / دوروم",
        "icon": "fa-hotdog",
        "items": [
            {
                "id": 90,
                "nameTR": "Somon Sandviç",
                "nameDE": "Lachs Sandwich",
                "nameEN": "Salmon Sandwich",
                "nameRU": "Сэндвич с лососем",
                "nameES": "Sándwich de salmón",
                "nameAR": "ساندويتش سلمون",
                "price": "9,00",
                "image": "assets/img/products/lachs_sandwich.jpg",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 91,
                "nameTR": "Çipura Sandviç",
                "nameDE": "Dorade Sandwich",
                "nameEN": "Sea Bream Sandwich",
                "nameRU": "Сэндвич с дорадо",
                "nameES": "Sándwich de dorada",
                "nameAR": "ساندويتش دنيس",
                "price": "9,00",
                "image": "assets/img/products/dorade_sandwich.jpg",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 92,
                "nameTR": "Uskumru Sandviç",
                "nameDE": "Makrele Sandwich",
                "nameEN": "Mackerel Sandwich",
                "nameRU": "Сэндвич со скумбрией",
                "nameES": "Sándwich de caballa",
                "nameAR": "ساندويتش إسقمري",
                "price": "8,00",
                "image": "assets/img/products/makrele_sandwich.jpg",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 93,
                "nameTR": "Sardalya/Hamsi Sandviç",
                "nameDE": "Sardine Sandwich",
                "nameEN": "Sardine Sandwich",
                "nameRU": "Сэндвич с мерлангом",
                "nameES": "Sándwich de merlán",
                "nameAR": "ساندويتش بياض",
                "price": "8,00",
                "image": "assets/img/products/sardine_sandwich.jpg",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 94,
                "nameTR": "Karides Sandviç",
                "nameDE": "Garnele Sandwich",
                "nameEN": "Shrimp Sandwich",
                "nameRU": "Сэндвич с хамсой",
                "nameES": "Sándwich de anchoa",
                "nameAR": "ساندويتش أنشوجة",
                "price": "9,00",
                "image": "assets/img/products/garnele_sandwich.jpg",
                "allergens": "1,2",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 98,
                "nameTR": "Somon Dürüm",
                "nameDE": "Lachs Dürüm",
                "nameEN": "Salmon Wrap",
                "nameRU": "Ролл с лососем",
                "nameES": "Wrap de salmón",
                "nameAR": "راب سلمون",
                "price": "10,00",
                "image": "assets/img/products/lachs_dorade_durum.png",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 99,
                "nameTR": "Çipura Dürüm",
                "nameDE": "Dorade Dürüm",
                "nameEN": "Sea Bream Wrap",
                "nameRU": "Ролл с дорадо",
                "nameES": "Wrap de dorada",
                "nameAR": "راب دنيس",
                "price": "10,00",
                "image": "assets/img/products/lachs_dorade_durum.png",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 100,
                "nameTR": "Uskumru Dürüm",
                "nameDE": "Makrele Dürüm",
                "nameEN": "Mackerel Wrap",
                "nameRU": "Ролл со скумбрией",
                "nameES": "Wrap de caballa",
                "nameAR": "راب إسقمري",
                "price": "9,00",
                "image": "assets/img/products/makrele_duerum.jpg",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 101,
                "nameTR": "Sardalya/Hamsi Dürüm",
                "nameDE": "Sardine Dürüm",
                "nameEN": "Sardine Wrap",
                "nameRU": "Дюрюм с сардинами",
                "nameES": "Dürüm de Sardina",
                "nameAR": "دوروم السردين",
                "price": "9,00",
                "allergens": "1,4",
                "image": "assets/img/products/sardine_duerum.jpg",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 102,
                "nameTR": "Karides Dürüm",
                "nameDE": "Garnele Dürüm",
                "nameEN": "Shrimp Wrap",
                "nameRU": "Ролл с хамсой",
                "nameES": "Wrap de anchoa",
                "nameAR": "راب أنشوجة",
                "price": "10,00",
                "image": "assets/img/products/garnele_duerum.jpg",
                "allergens": "1,2",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            }
        ]
    },
    {
        "categoryId": "cocuk-menusu",
        "categoryTR": "Çocuk Menüsü",
        "categoryDE": "Kindermenü",
        "categoryNameEN": "Kids' Menu",
        "categoryNameRU": "Детское меню",
        "categoryNameES": "Menú infantil",
        "categoryNameAR": "قائمة الأطفال",
        "icon": "fa-child",
        "items": [
            {
                "id": 108,
                "nameTR": "Balık Burger Menü",
                "nameDE": "Fisch-Burger, Pommes, Getränk",
                "nameEN": "Fish Burger Menu (w/ Fries & Drink)",
                "nameRU": "Рыбный бургер меню (с фри и напитком)",
                "nameES": "Menú de hamburguesa de pescado (con patatas y bebida)",
                "nameAR": "قائمة برجر سمك (مع بطاطس ومشروب)",
                "price": "16,00",
                "allergens": "1,4",
                "image": "assets/img/products/fisch_burger.jpg",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 109,
                "nameTR": "Balık Köfte Menü",
                "nameDE": "Fisch-Bouletten, Pommes oder Reis, Getränk",
                "image": "assets/img/products/balik_kofte_pilav_01.jpg",
                "nameEN": "Fish Meatball Menu (w/ Fries/Rice & Drink)",
                "nameRU": "Меню рыбных котлет (с фри/рисом и напитком)",
                "nameES": "Menú de albóndigas de pescado (con patatas/arroz y bebida)",
                "nameAR": "قائمة كفتة سمك (مع بطاطس/أرز ومشروب)",
                "price": "16,00",
                "allergens": "1,4",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 112,
                "nameTR": "Somonlu Makarna (Özel Sos)",
                "nameDE": "Nudeln mit Lachsfilet in hausgemachter Soße",
                "nameEN": "Salmon Pasta (Special Sauce)",
                "nameRU": "Паста с лососем (Особый соус)",
                "nameES": "Pasta con salmón (Salsa especial)",
                "nameAR": "مكرونة بالسلمون (صلصة خاصة)",
                "price": "20,00",
                "image": "assets/img/products/somonlu_makarna.jpg",
                "allergens": "1,4,7",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            },
            {
                "id": 113,
                "nameTR": "Karidesli Makarna (Özel Sos)",
                "nameDE": "Nudeln mit Garnelen in hausgemachter Soße",
                "nameEN": "Shrimp Pasta (Special Sauce)",
                "nameRU": "Паста с креветками (Особый соус)",
                "nameES": "Pasta con camarones (Salsa especial)",
                "nameAR": "مكرونة بالجمبري (صلصة خاصة)",
                "price": "20,00",
                "image": "assets/img/products/penne_mit_garnelen.jpg",
                "allergens": "1,2,7",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": false
                }
            }
        ]
    },
    {
        "categoryId": "tatlilar",
        "categoryTR": "Tatlılar",
        "categoryDE": "Desserts",
        "categoryNameEN": "Desserts",
        "categoryNameRU": "Десерты",
        "categoryNameES": "Postres",
        "categoryNameAR": "الحلويات",
        "icon": "fa-ice-cream",
        "items": [
            {
                "id": 116,
                "nameTR": "Dondurmalı İrmik Helvası",
                "nameDE": "Warmer Grieß-Halva mit Eis",
                "nameEN": "Warm Semolina Halva with Ice Cream",
                "nameRU": "Теплая манная халва с мороженым",
                "nameES": "Halva de sémola tibia con helado",
                "nameAR": "حلاوة سميد دافئة مع آيس كريم",
                "price": "9,00",
                "image": "assets/img/products/warmer_griess_halva.jpg",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            },
            {
                "id": 118,
                "nameTR": "Fırında Meyhane Helvası",
                "nameDE": "Gebackener 'Kneipen' Halva",
                "nameEN": "Baked Tavern Halva",
                "nameRU": "Запеченная халва",
                "nameES": "Halva horneada",
                "nameAR": "حلاوة مخبوزة",
                "price": "7,90",
                "image": "assets/ubereats_imgs/gebackener_kneipen_halva.jpg",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            },
            {
                "id": 120,
                "nameTR": "Hamsiköy Sütlacı (Fırında)",
                "nameDE": "Türkischer Milchreis aus dem Ofen",
                "nameEN": "Hamsiköy Baked Rice Pudding",
                "nameRU": "Рисовый пудинг в духовке (Хамсикёй)",
                "nameES": "Arroz con leche al horno (Hamsiköy)",
                "nameAR": "أرز بالحليب مخبوز في الفرن (هامسيكوي)",
                "price": "5,90",
                "image": "assets/img/products/hamsikoy_sutlac_ai.jpg",
                "allergens": "7",
                "diet": {
                    "vegetarian": false,
                    "glutenFree": true
                }
            },
            {
                "id": 122,
                "nameTR": "Çilekli Magnolia",
                "nameDE": "Erdbeer Magnolia",
                "nameEN": "Strawberry Magnolia",
                "nameRU": "Клубничная магнолия",
                "nameES": "Magnolia de Fresa",
                "nameAR": "ماغنوليا فراولة",
                "price": "5,90",
                "image": "assets/img/products/erdbeer_magnolia.jpg",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 121,
                "nameTR": "Kızarmış Dondurma",
                "nameDE": "Fritierte Eiscreme",
                "nameEN": "Fried Ice Cream",
                "nameRU": "Жареное мороженое",
                "nameES": "Helado frito",
                "nameAR": "آيس كريم مقلي",
                "price": "9,00",
                "image": "assets/img/products/kizarmis_dondurma_ai.jpg",
                "allergens": "7",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": false
                }
            }
        ]
    },
    {
        "categoryId": "soguk-icecekler",
        "categoryTR": "Soğuk İçecekler",
        "categoryDE": "Kalte Getränke",
        "categoryNameEN": "Cold Drinks",
        "categoryNameRU": "Холодные напитки",
        "categoryNameES": "Bebidas frías",
        "categoryNameAR": "المشروبات الباردة",
        "icon": "fa-glass-water",
        "items": [
            {
                "id": 130,
                "nameTR": "Su (0,25l)",
                "nameDE": "Stilles Wasser 0,25l",
                "nameEN": "Still Water (0.25l)",
                "nameRU": "Вода (0.25л)",
                "nameES": "Agua sin gas (0.25l)",
                "nameAR": "ماء (0.25 لتر)",
                "image": "assets/drinks/vio_still_pro.png",
                "price": "2,50 / 6,50",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 131,
                "nameTR": "Maden Suyu (0,25l)",
                "nameDE": "Mineralwasser mit Kohlensäure 0,25l",
                "nameEN": "Sparkling Water (0.25l)",
                "nameRU": "Минеральная вода (0.25л)",
                "nameES": "Agua con gas (0.25l)",
                "nameAR": "مياه غازية (0.25 لتر)",
                "image": "assets/drinks/appolinaris_pro.png",
                "price": "2,90 / 6,90",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 132,
                "nameTR": "Coca Cola (0,2l)",
                "nameDE": "Coca Cola 0,2l",
                "image": "https://wolt-menu-images-cdn.wolt.com/menu-images/5f96f0713ecde1f8e087069e/0211094c-17a7-11eb-8056-b6507305cae7_cocacola_0_2.jpeg",
                "nameEN": "Coca Cola (0.2l)",
                "nameRU": "Кока-Кола (0.2л)",
                "nameES": "Coca Cola (0.2l)",
                "nameAR": "كوكا كولا (0.2 لتر)",
                "price": "2,90",
                "allergens": "A,E,F,H,I,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 133,
                "nameTR": "Coca Cola Zero (0,2l)",
                "nameDE": "Cola Zero 0,2l",
                "image": "https://wolt-menu-images-cdn.wolt.com/menu-images/5f96f0713ecde1f8e087069e/2faec65a-17a7-11eb-9f4b-b26fbf627d3c_cocacola_zero_0_2.jpeg",
                "nameEN": "Cola Zero (0.2l)",
                "nameRU": "Кока-Кола Зеро (0.2л)",
                "nameES": "Cola Zero (0.2l)",
                "nameAR": "كوكا كولا زيرو (0.2 لتر)",
                "price": "2,90",
                "allergens": "A,E,F,H,I,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 134,
                "nameTR": "Fanta (0,2l)",
                "nameDE": "Fanta 0,2l",
                "image": "https://wolt-menu-images-cdn.wolt.com/menu-images/5fbe3fd5b9861614046e6930/3f846a1a-2f23-11eb-bd32-c2695b788ece_fanta_0_2.jpeg",
                "nameEN": "Fanta (0.2l)",
                "nameRU": "Фанта (0.2л)",
                "nameES": "Fanta (0.2l)",
                "nameAR": "فانتا (0.2 لتر)",
                "price": "2,90",
                "allergens": "A,E,F,H,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 135,
                "nameTR": "Sprite (0,2l)",
                "nameDE": "Sprite 0,2l",
                "image": "https://wolt-menu-images-cdn.wolt.com/menu-images/5f96f0713ecde1f8e087069e/2a2f2782-17a8-11eb-9abd-fe05229f24a2_sprite_0_2l_.jpeg",
                "nameEN": "Sprite (0.2l)",
                "nameRU": "Спрайт (0.2л)",
                "nameES": "Sprite (0.2l)",
                "nameAR": "سبرايت (0.2 لتر)",
                "price": "2,90",
                "allergens": "E,F,H,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 144,
                "nameTR": "Mezzo Mix (0,2l)",
                "nameDE": "Mezzo Mix 0,2l",
                "image": "https://wolt-menu-images-cdn.wolt.com/menu-images/5fe1c838e1d7dcb5af1c43d8/fc113ac8-4a80-11eb-8d33-866b5695d3f0_mezzo_mix_0_2l.jpeg",
                "nameEN": "Mezzo Mix (0.2l)",
                "nameRU": "Mezzo Mix (0.2л)",
                "nameES": "Mezzo Mix (0.2l)",
                "nameAR": "ميزو ميكس (0.2 لتر)",
                "price": "2,90",
                "allergens": "A,E,F,H,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 9584,
                "nameTR": "Uludag Gazoz 0,25l",
                "nameDE": "Uludag Gazoz 0,25l",
                "nameEN": "Uludag Gazoz 0,25l",
                "nameRU": "Uludag Gazoz 0,25l",
                "nameES": "Uludag Gazoz 0,25l",
                "nameAR": "Uludag Gazoz 0,25l",
                "price": "3,00",
                "image": "assets/img/products/uludag_gazoz.png",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 142,
                "nameTR": "Çamlıca Gazoz (0,2l)",
                "nameDE": "Çamlıca Gazoz 0,2l",
                "nameEN": "Çamlıca Gazoz (0.2l)",
                "nameRU": "Çamlıca Gazoz (0.2л)",
                "nameES": "Çamlıca Gazoz (0.2l)",
                "nameAR": "شامليجا غازوز (0.2 لتر)",
                "image": "assets/drinks/camlica.jpg",
                "price": "2,90",
                "allergens": "A,E,H",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 140,
                "nameTR": "7gün Ayran (0,25l)",
                "nameDE": "7gün Ayran 0,25l",
                "nameEN": "7gün Ayran (0.25l)",
                "nameRU": "Айран (0.25л)",
                "nameES": "Ayran (0.25l)",
                "nameAR": "عيران (0.25 لتر)",
                "image": "assets/img/products/ayran_7gun.png",
                "price": "2,90",
                "allergens": "7,A,H,F",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 143,
                "nameTR": "Şalgam Suyu (0,25l)",
                "nameDE": "Salgam (Rübensaft) 0,25l",
                "nameEN": "Turnip Juice (0.25l)",
                "nameRU": "Сок из репы (0.25л)",
                "nameES": "Jugo de nabo (0.25l)",
                "nameAR": "عصير شلغم (0.25 لتر)",
                "image": "assets/img/products/salgam_v2.png",
                "price": "2,90",
                "allergens": "B",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 136,
                "nameTR": "Fritz Cola (0,2l)",
                "nameDE": "Fritz Cola 0,2l",
                "nameEN": "Fritz Cola (0.2l)",
                "nameRU": "Fritz Cola (0.2л)",
                "nameES": "Fritz Cola (0.2l)",
                "nameAR": "فريتز كولا (0.2 لتر)",
                "image": "assets/img/products/fritz_cola_classic.jpg",
                "price": "2,90",
                "allergens": "A,E,I,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 137,
                "nameTR": "Fritz Cola Zero (0,2l)",
                "nameDE": "Fritz Cola Zero 0,2l",
                "nameEN": "Fritz Cola Zero (0.2l)",
                "nameRU": "Fritz Cola Zero (0.2л)",
                "nameES": "Fritz Cola Zero (0.2l)",
                "nameAR": "فريتز كولا زيرو (0.2 لتر)",
                "image": "assets/img/products/fritz_cola_zero.png",
                "price": "2,90",
                "allergens": "A,E,I,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 138,
                "nameTR": "Fritz Orange (0,2l)",
                "nameDE": "Fritz Orange 0,2l",
                "nameEN": "Fritz Orange (0.2l)",
                "nameRU": "Fritz Orange (0.2л)",
                "nameES": "Fritz Orange (0.2l)",
                "nameAR": "فريتز برتقال (0.2 لتر)",
                "image": "https://wolt-menu-images-cdn.wolt.com/menu-images/5fe058d382df4b51bda8658e/26a7725a-44fc-11eb-8728-1233a3d50ac2_fritz_limo_orange__21.jpeg",
                "price": "2,90",
                "allergens": "A,E,F,H,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 7892,
                "nameTR": "FuzeTea (çeşitli tatlar) 0,4l",
                "nameDE": "FuzeTea (verschiedene Sorten) 0,4l",
                "nameEN": "FuzeTea (various flavors) 0,4l",
                "nameRU": "FuzeTea (разные вкусы) 0,4l",
                "nameES": "FuzeTea (varios sabores) 0,4l",
                "nameAR": "FuzeTea (نكهات متنوعة) 0,4l",
                "image": "https://images.unsplash.com/photo-1556679343-c7306c1976bc?w=400&q=80",
                "price": "2,90",
                "allergens": "A,E,H",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 147,
                "nameTR": "Schweppes (0,2l)",
                "nameDE": "Schweppes 0,2l",
                "nameEN": "Schweppes (0.2l)",
                "nameRU": "Schweppes (0.2л)",
                "nameES": "Schweppes (0.2l)",
                "nameAR": "شويبس (0.2 لتر)",
                "image": "assets/drinks/schweppes.webp",
                "price": "2,90",
                "allergens": "A,E,F,H,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 139,
                "nameTR": "Christinen Elma Suyu (0,33l)",
                "nameDE": "Christinen Apfelschorle 0,33l",
                "nameEN": "Christinen Apple Spritzer (0.33l)",
                "nameRU": "Яблочный шорле (0.33л)",
                "nameES": "Zumo de manzana con gas (0.33l)",
                "nameAR": "عصير تفاح مكربن (0.33 لتر)",
                "image": "https://wolt-menu-images-cdn.wolt.com/menu-images/5f96f0713ecde1f8e087069e/76f4b770-4927-11eb-9330-4e241e2ced00_christinen_apfelschorle_0_33l.jpeg",
                "price": "2,90",
                "allergens": "H,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 148,
                "nameTR": "Christinen Multivitamin (0,33l)",
                "nameDE": "Christinen Multivitamin 0,33l",
                "nameEN": "Multivitamin Juice (0.33l)",
                "nameRU": "Мультивитаминный сок (0.33л)",
                "nameES": "Jugo Multivitamínico (0.33l)",
                "nameAR": "عصير فواكه مشكلة (0.33 لتر)",
                "image": "https://wolt-menu-images-cdn.wolt.com/menu-images/5f96f0713ecde1f8e087069e/645e9f72-4927-11eb-9c98-16866cd60e34_christinen_multivitamin_0_33l.jpeg",
                "price": "2,90",
                "allergens": "A,E,F,H,J",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 141,
                "nameTR": "Capri Sonne (0,2l)",
                "nameDE": "Capri Sonne 0,2l",
                "nameEN": "Capri Sonne (0.2l)",
                "nameRU": "Capri Sonne (0.2л)",
                "nameES": "Capri Sonne (0.2l)",
                "nameAR": "كابري سون (0.2 لتر)",
                "image": "assets/img/products/capri_sonne.png",
                "price": "2,50",
                "allergens": "E,H,C,F",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 145,
                "nameTR": "Tymbark (0,25l)",
                "nameDE": "Tymbark 0,25l",
                "nameEN": "Tymbark (0.25l)",
                "nameRU": "Tymbark (0.25л)",
                "nameES": "Tymbark (0.25l)",
                "nameAR": "تيمبارك (0.25 لتر)",
                "image": "assets/drinks/tymbark-mix-die-beliebtesten-sorten-in-einem-set.png",
                "price": "2,90",
                "allergens": "A,E,F,H",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            }
        ]
    },
    {
        "categoryId": "sicak-icecekler",
        "categoryTR": "Sıcak İçecekler",
        "categoryDE": "Warme Getränke",
        "categoryNameEN": "Hot Drinks",
        "categoryNameRU": "Горячие напитки",
        "categoryNameES": "Bebidas calientes",
        "categoryNameAR": "المشروبات الساخنة",
        "icon": "fa-mug-hot",
        "items": [
            {
                "id": 91,
                "nameTR": "Türk Çayı (Küçük)",
                "nameDE": "Türkischer Tee klein",
                "nameEN": "Turkish Tea (Small)",
                "nameRU": "Турецкий чай (маленький)",
                "nameES": "Té turco (pequeño)",
                "nameAR": "شاي تركي (صغير)",
                "image": "assets/img/products/kucuk_cay_v2.png",
                "price": "1,50",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 911,
                "nameTR": "Türk Çayı (Büyük)",
                "nameDE": "Türkischer Tee groß",
                "nameEN": "Turkish Tea (Large)",
                "nameRU": "Турецкий чай (большой)",
                "nameES": "Té turco (grande)",
                "nameAR": "شاي تركي (كبير)",
                "image": "assets/img/products/buyuk_cay_v2.png",
                "price": "2,50",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 92,
                "nameTR": "Çay Çeşitleri",
                "nameDE": "Verschiedene Teesorten",
                "nameEN": "Assorted Teas",
                "nameRU": "Разные сорта чая",
                "nameES": "Variedades de té",
                "nameAR": "أنواع شاي متنوعة",
                "image": "assets/img/products/cay_cesitleri.png",
                "price": "2,50",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 167,
                "nameTR": "Türk Kahvesi",
                "nameDE": "Türkischer Mokka",
                "nameEN": "Turkish Coffee",
                "nameRU": "Турецкий кофе",
                "nameES": "Café turco",
                "nameAR": "قهوة تركية",
                "image": "assets/img/products/turk_kahvesi_v2.png",
                "price": "3,00",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 97,
                "nameTR": "Espresso",
                "nameDE": "Espresso",
                "nameEN": "Espresso",
                "nameRU": "Espresso",
                "nameES": "Espresso",
                "nameAR": "Espresso",
                "image": "https://images.unsplash.com/photo-1510591509098-f4fdc6d0ff04?w=400&q=80",
                "price": "3,00",
                "allergens": "I",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 163,
                "nameTR": "Café Cream",
                "nameDE": "Café Cream",
                "nameEN": "Café Cream",
                "nameRU": "Кафе Крем",
                "nameES": "Café Crema",
                "nameAR": "كافيه كريم",
                "image": "assets/img/products/kaffee_crema_v2.png",
                "price": "3,50",
                "allergens": "I",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 164,
                "nameTR": "Cappuccino",
                "nameDE": "Cappuccino",
                "nameEN": "Cappuccino",
                "nameRU": "Капучино",
                "nameES": "Capuchino",
                "nameAR": "كابتشينو",
                "image": "assets/img/products/cappuccino.png",
                "price": "3,50",
                "allergens": "7,I",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            },
            {
                "id": 165,
                "nameTR": "Café Latte",
                "nameDE": "Café Latte",
                "nameEN": "Café Latte",
                "nameRU": "Латте",
                "nameES": "Café Latte",
                "nameAR": "كافيه لاتيه",
                "image": "assets/img/products/kaffee-latte.jpeg",
                "price": "3,50",
                "allergens": "7,I",
                "diet": {
                    "vegetarian": true,
                    "glutenFree": true
                }
            }
        ]
    }
];

window.menuData = menuData;
