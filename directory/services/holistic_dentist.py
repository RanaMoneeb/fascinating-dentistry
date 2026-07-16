"""Content for /australia/holistic-dentist/ — Top 10 Holistic Dentists in Australia."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Holistic Dentists in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 holistic dentists in Australia. Mercury-free dentistry, SMART amalgam removal, biological dentistry, and whole-body health approach. Verified clinics near you."
H1 = "Top 10 Holistic Dentists in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "A holistic dentist (also called a biological or biocompatible dentist) approaches oral health as an integral part of overall physical health. Holistic dentists avoid mercury amalgam fillings, use biocompatible materials, follow Safe Mercury Amalgam Removal Technique (SMART) protocols, and consider the impact of dental treatments on the entire body. The International Academy of Oral Medicine and Toxicology (IAOMT) provides certification for SMART amalgam removal. Holistic dentistry emphasises prevention, minimally invasive treatment, and the connection between oral health and systemic conditions.",
    "We ranked Australia's top holistic dentists based on six criteria: IAOMT membership or SMART certification, mercury-free practice policy, range of biocompatible materials, holistic treatment philosophy, AHPRA registration, and Google review scores. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need a holistic dentist?"
WHEN = [
    "Holistic dentistry treats the mouth as an integral part of the whole body. Key principles include mercury-free fillings, SMART amalgam removal, biocompatible materials, minimally invasive techniques, and a nutrition and prevention focus. Holistic dentists consider how dental materials and treatments affect your entire system.",
    "You may want a holistic dentist if you want mercury amalgam fillings safely removed using SMART protocol, have metal allergies or sensitivities, prefer natural and biocompatible materials, are concerned about the connection between oral health and systemic conditions, or want fluoride-free treatment options.",
    'The SMART protocol (Safe Mercury Amalgam Removal Technique) developed by the IAOMT uses protective barriers, high-volume filtration, separate air supplies, and specific removal techniques to minimise mercury vapour exposure during amalgam removal. Only IAOMT-certified dentists should perform SMART removal.',
    'Holistic dentists use composite resin, ceramic, zirconia, and glass ionomer instead of mercury amalgam or metal alloys. Some offer biocompatibility testing to select materials compatible with your immune system. Schedule a [dental check-up](https://fascinatingdentistry.com/australia/dental-check-up/) with a holistic dentist to discuss mercury-free [fillings](https://fascinatingdentistry.com/australia/fillings/) and biocompatible treatment options.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide holistic and biological dentistry across Sydney, Melbourne, Brisbane, Perth, Adelaide, Newcastle, and Darwin. Each entry includes verified contact details, holistic certifications, and services sourced from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Smile In Style", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.9/5 (160 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "77 Wimborne Street, Sunbury VIC 3429", "phone": "(03) 9740 5522",
     "website": "https://www.smileinstyle.com.au",
     "body": [
        "Smile In Style is a holistic dental practice offering mercury-free dentistry at two Melbourne locations in Sunbury and Moonee Ponds. The practice is certified in Safe Mercury Amalgam Removal Technique (SMART) by the IAOMT. Dr Rose is pursuing accreditation as a Biological Dentist.",
        "The practice serves Melbourne families with biocompatible dental care including mercury-free fillings, SMART amalgam removal, and holistic treatment planning.",
     ]},
    {"rank": 2, "name": "Holistic Dental Donvale", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.8/5 (90 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "1080 Doncaster Road, Donvale VIC 3111", "phone": "(03) 9842 6675",
     "website": "https://www.holisticdentists.au/holistic-dentists/holistic-dental-donvale",
     "body": [
        "Led by Darren Ma, Holistic Dental Donvale prioritises a holistic approach to oral health. The practice combines evidence-based treatment with holistic principles including mercury-free dentistry and biocompatible materials in Donvale, Melbourne.",
     ]},
    {"rank": 3, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": True, "ahpra": True,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry takes a holistic approach to dental care across four Adelaide locations. Offers mercury-free options, TMJ therapies, periodontal treatment, and non-surgical treatment options. All major health funds accepted with HICAPS.",
     ]},
    {"rank": 4, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": ["MC Dental offers mercury-free composite filling options across six Melbourne locations. Open 7 days a week."]},
    {"rank": 5, "name": "My Dentist Brisbane", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.7/5 (110 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "2/405 Coronation Drive, Auchenflower QLD 4066", "phone": "(07) 3870 3344",
     "website": "https://www.mydentistbrisbane.com.au",
     "body": ["My Dentist Brisbane features Dr Kat Marhfour, an IAOMT member providing SMART amalgam removal and biological dentistry from Auchenflower in Brisbane."]},
    {"rank": 6, "name": "Clear Dental", "location": "Sydney, NSW", "featured": False,
     "rating": "4.8/5 (320 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "131 Clarence St, Sydney NSW 2000", "phone": "(02) 9456 6557",
     "website": "https://www.cleardental.com.au",
     "body": ["Clear Dental provides mercury-free composite fillings and tooth-coloured restorations. Open 7 days a week."]},
    {"rank": 7, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": ["Bayview Dental offers mercury-free options and biocompatible materials with iTero digital scanning. Interest-free plans available."]},
    {"rank": 8, "name": "Malouf Dental", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Thu, Fri mornings",
     "address": "1476 Wynnum Road, Tingalpa QLD 4173", "phone": "(07) 3390 6100",
     "website": "https://cosmeticdentistinbrisbane.com.au",
     "body": ["Malouf Dental provides composite fillings and mercury-free options. Complimentary initial appointments available."]},
    {"rank": 9, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": ["7 Pearls Dental offers mercury-free filling options. Two Newcastle locations. Open 7 days a week."]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": ["Extreme Dentistry takes a comprehensive holistic approach to dental care. Led by Dr Anand Murugappan. Sedation options available."]},
]

COST_HEADING = "How much does holistic dental treatment cost in Australia?"
COST = ["Holistic dental treatment costs are comparable to standard private dental fees. SMART amalgam removal involves additional protocols and protective equipment, making it more expensive than standard filling removal."]
COST_PRICES = [
    ("SMART amalgam removal (per filling)", "$250 - $500"),
    ("Composite (mercury-free) filling", "$180 - $350"),
    ("Biocompatibility testing", "$200 - $500"),
    ("Holistic consultation", "$100 - $250"),
    ("Ceramic implant (metal-free)", "$4,500 - $7,000"),
]
COST_AFTER = ['Most private health funds cover <a href="/australia/fillings/">fillings</a>, check-ups, and cleaning regardless of whether the practice is holistic. Read our <a href="/blog/costs/">dental costs guide</a> for details.']

CHOOSE_HEADING = "How do you choose a holistic dentist in Australia?"
CHOOSE_INTRO = "Selecting the right holistic dentist involves verifying their credentials and approach to whole-body dental care. Ask these 5 questions."
CHOOSE_CRITERIA = [
    ("Is the dentist IAOMT certified for SMART amalgam removal?", "IAOMT certification ensures the dentist follows strict protocols for safe mercury removal including protective barriers, filtration, and proper disposal."),
    ("Is the practice mercury-free?", "Confirm the practice does not place new mercury amalgam fillings and only uses composite, ceramic, or glass ionomer materials."),
    ("Do they offer biocompatibility testing?", "Some holistic dentists offer blood tests or electrodermal screening to identify materials compatible with your immune system before placing restorations."),
    ("What is their approach to fluoride?", "Holistic dentists may offer fluoride-free alternatives. Discuss their position on fluoride and whether they respect your preferences."),
    ("Do they consider systemic health connections?", "A true holistic dentist considers how periodontal disease, oral infections, and dental materials may affect conditions like cardiovascular disease, diabetes, and chronic inflammation."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these holistic dentists?"
METHODOLOGY = ["We evaluated dental practices across Australia. Each was assessed against 8 criteria."]
METHODOLOGY_CRITERIA = [
    "IAOMT membership or SMART certification",
    "Mercury-free practice policy",
    "Range of biocompatible materials offered",
    "Holistic treatment philosophy and whole-body approach",
    "AHPRA registration verified",
    "Pricing transparency",
    "Google reviews above 4.5",
    "Patient education on holistic dental health",
]
METHODOLOGY_AFTER = ['Paid placements in positions 1 to 3 met all 8 criteria. Read our full <a href="/methodology/">methodology</a>.']

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is a holistic dentist?", "A dentist who treats oral health as part of overall physical health. Avoids mercury amalgam, uses biocompatible materials, and follows SMART protocols for safe amalgam removal."),
    ("Is holistic dentistry safe?", "Yes. Holistic dentistry uses evidence-based techniques with additional focus on material biocompatibility and safety. SMART amalgam removal follows IAOMT protocols."),
    ("How much does SMART amalgam removal cost?", '$250 to $500 per filling. Includes protective barriers, filtration, and disposal protocols. Read our <a href="/blog/costs/">dental costs guide</a>.'),
    ("Are mercury amalgam fillings dangerous?", "The Australian Dental Association states amalgam is safe for most patients. Holistic dentists prefer mercury-free alternatives. If you want amalgams removed, SMART protocol minimises mercury exposure."),
    ("What materials do holistic dentists use?", 'Composite resin, ceramic, zirconia, and glass ionomer instead of mercury amalgam or metal alloys. Some offer biocompatibility testing. Used in <a href="/australia/fillings/">fillings</a> and restorations.'),
    ("Does health insurance cover holistic dentistry?", "Most private health funds cover fillings, check-ups, and cleaning regardless of whether the practice is holistic. SMART removal may have limited cover depending on the fund."),
    ("What is IAOMT certification?", "The International Academy of Oral Medicine and Toxicology provides SMART (Safe Mercury Amalgam Removal Technique) certification. Certified dentists follow strict protocols to protect patients and staff from mercury vapour."),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."
DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."

def _build_schemas():
    url = f"{SITE_URL}/australia/holistic-dentist/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage", "name": META_TITLE, "description": META_DESC, "about": "Holistic dentistry in Australia", "inLanguage": "en-AU", "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1, "itemListElement": [{"@type": "ListItem", "position": p["rank"], "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"}, {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"}, {"@type": "ListItem", "position": 3, "name": "Holistic Dentist", "item": url}]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]

SCHEMAS = _build_schemas()
