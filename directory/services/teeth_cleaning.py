"""Content for /australia/teeth-cleaning/ — Top 10 Teeth Cleaning Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Teeth Cleaning Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 teeth cleaning clinics in Australia. Professional scale and clean, dental hygienist services, fluoride treatment, and deep cleaning. Verified clinics near you."
H1 = "Top 10 Teeth Cleaning Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Professional teeth cleaning is a preventive dental procedure performed by a dentist or dental hygienist to remove plaque, tartar (calculus), and surface stains from your teeth. A standard clean includes scaling to remove hardened deposits above and below the gum line, polishing to remove surface stains, and fluoride application to strengthen enamel. The Australian Dental Association recommends professional cleaning every 6 to 12 months alongside routine check-ups. The AIHW reports that 48% of Australian adults have not visited a dentist in the past 12 months.",
    "We ranked Australia's top teeth cleaning clinics based on six criteria: gap-free cleaning for health fund members, dental hygienist availability, range of cleaning services (scale and clean, deep cleaning, AIRFLOW polishing), AHPRA registration, published pricing, and Google review scores. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need professional teeth cleaning?"
WHEN = [
    'Professional teeth cleaning includes three main steps. Scaling uses ultrasonic instruments and hand scalers to remove plaque and hardened tartar (calculus) from above and below the gum line. Polishing uses a rotating brush with prophylaxis paste to remove surface stains and smooth tooth surfaces. Fluoride application strengthens enamel and helps prevent future decay.',
    'There are different types of professional cleaning. A routine scale and clean (Medicare item 114) is the standard preventive cleaning recommended every 6 to 12 months. Deep cleaning (scaling and root planing) treats [gum disease](https://fascinatingdentistry.com/australia/gum-disease-treatment/) by removing bacteria from root surfaces below the gum line. AIRFLOW polishing uses a fine powder to remove stubborn stains from coffee, tea, and tobacco.',
    "The Australian Dental Association recommends professional cleaning every 6 to 12 months for most adults. High-risk patients including those with gum disease, orthodontic braces, heavy staining, dental implants, or a history of rapid tartar build-up should have cleaning every 3 to 4 months.",
    'Tartar cannot be removed by brushing alone. Once plaque hardens into tartar, it bonds strongly to tooth enamel and requires professional dental instruments to remove. Regular professional cleaning prevents [gum disease](https://fascinatingdentistry.com/australia/gum-disease-treatment/), detects early decay, and maintains fresh breath. Schedule your cleaning alongside a routine [dental check-up](https://fascinatingdentistry.com/australia/dental-check-up/) for comprehensive preventive care.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide professional teeth cleaning across Sydney, Melbourne, Brisbane, Perth, Adelaide, Newcastle, and Darwin. Each entry includes verified contact details, cleaning pricing, and services sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "No Gaps Dental", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.8/5 (650 reviews)", "pricing": "Gap-free (health fund), $199 private", "hours": "Mon-Sat",
     "address": "Level 2, 283 George Street, Sydney NSW 2000", "phone": "(02) 8383 1400",
     "website": "https://www.nogapsdental.com",
     "body": [
        "No Gaps Dental offers gap-free scale and clean for health fund members across 18 Sydney locations. The service includes comprehensive examination, professional cleaning, fluoride, and X-rays. Experienced dental hygienists available at all locations.",
        "Over 20 years serving Sydney families with preventive dental care. CDBS bulk billing available for eligible children.",
     ]},
    {"rank": 2, "name": "Dental 99", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.7/5 (1,200 reviews)", "pricing": "Budget", "hours": "7 days",
     "address": "Shop 1, 11 Epping Road, Macquarie Park NSW 2113", "phone": "1300 655 022",
     "website": "https://dental99.com.au",
     "body": [
        "Dental 99 provides professional scale and clean, fluoride, and X-rays across 7 locations in Sydney, Brisbane, and Melbourne. Booking is managed through the Dental 99 mobile app. CDBS claims handled automatically for eligible children.",
     ]},
    {"rank": 3, "name": "Sydney CBD Dentistry", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (420 reviews)", "pricing": "Mid-range (gap-free for health fund)", "hours": "Mon-Sat",
     "address": "Suite 6, Level 2, 135 Macquarie Street, Sydney NSW 2000", "phone": "(02) 9232 3788",
     "website": "https://www.sydneycbddentistry.com.au",
     "body": [
        "Sydney CBD Dentistry provides professional scale and clean with gentle dental hygienists. The service includes comprehensive examination, polishing, and fluoride treatment. Gap-free for health fund members. Returning patient clean is $219.",
     ]},
    {"rank": 4, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range (gap-free for health fund)", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental provides gap-free scale and clean for health fund members across six Melbourne locations. Preferred provider for Bupa, Medibank, and HCF. Open 7 days a week.",
     ]},
    {"rank": 5, "name": "NDC Darwin", "location": "Darwin, NT", "featured": False,
     "rating": "4.6/5 (180 reviews)", "pricing": "Budget (no gap or $199)", "hours": "Mon-Sat",
     "address": "Shop 1, 70 Smith Street, Darwin NT 0800", "phone": "(08) 8946 2200",
     "website": "https://www.nationaldentalcare.com.au",
     "body": [
        "NDC Darwin offers no gap or $199 scale and clean including polish and fluoride treatment. Professional hygienist services available. The practice provides comprehensive preventive dentistry.",
     ]},
    {"rank": 6, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": [
        "Bayview Dental provides professional scale and clean, AIRFLOW polishing, and fluoride treatment with iTero digital scanning technology. Interest-free payment plans available.",
     ]},
    {"rank": 7, "name": "Malouf Dental", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Thu, Fri mornings",
     "address": "1476 Wynnum Road, Tingalpa QLD 4173", "phone": "(07) 3390 6100",
     "website": "https://cosmeticdentistinbrisbane.com.au",
     "body": [
        "Malouf Dental provides professional teeth cleaning, scale and polish, and fluoride treatment. Complimentary initial appointments and interest-free payment plans available.",
     ]},
    {"rank": 8, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental provides professional scale and clean, fluoride, and polish from two Newcastle locations. Online booking is available 7 days a week.",
     ]},
    {"rank": 9, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry provides professional scale and clean, fluoride, and polish across four Adelaide locations. All major health funds accepted with HICAPS on-the-spot claiming.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides professional teeth cleaning, scale and polish, and fluoride treatment. Led by Dr Anand Murugappan. Sedation options available for anxious patients.",
     ]},
]

COST_HEADING = "How much does professional teeth cleaning cost in Australia?"
COST = [
    "Professional teeth cleaning in Australia costs between $0 (gap-free with health fund dental extras) and $350 for a comprehensive clean with examination and X-rays. Many practices offer gap-free cleaning where the health fund rebate covers the full cost.",
    "Deep cleaning for gum disease (scaling and root planing) costs more as it requires local anaesthetic and treats below the gum line. This is separate from a routine preventive clean.",
]
COST_PRICES = [
    ("Gap-free scale and clean (health fund members)", "$0 out of pocket"),
    ("Standard scale and clean (private, item 114)", "$120 - $250"),
    ("Comprehensive clean (exam + scale + clean + fluoride)", "$199 - $350"),
    ("Deep cleaning (scaling and root planing, per quadrant)", "$250 - $500"),
    ("AIRFLOW polishing (additional)", "$80 - $150"),
    ("Fluoride treatment", "$30 - $60"),
]
COST_AFTER = [
    'Private health funds typically cover 1 to 2 professional cleans per year under dental extras. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. Learn more about <a href="/australia/dental-check-up/">dental check-ups</a> and <a href="/australia/gum-disease-treatment/">gum disease treatment</a>.',
]

CHOOSE_HEADING = "How do you choose a teeth cleaning clinic in Australia?"
CHOOSE_INTRO = "Selecting the right teeth cleaning clinic involves finding a practice that is affordable, gentle, and thorough. Ask these 5 questions."
CHOOSE_CRITERIA = [
    ("Does the clinic offer gap-free cleaning?",
     "If you have private health insurance with dental extras, look for clinics offering gap-free scale and clean where the health fund rebate covers the full cost."),
    ("Does the clinic have dedicated dental hygienists?",
     "Practices with dental hygienists typically provide more thorough and comfortable cleaning. Hygienists specialise in preventive care and spend more time on each cleaning appointment."),
    ("What cleaning techniques do they use?",
     "Modern practices offer ultrasonic scaling, AIRFLOW powder polishing, and digital scanning. These technologies make cleaning more comfortable and effective."),
    ("What is included in the cleaning appointment?",
     "A comprehensive cleaning should include examination, scaling, polishing, and fluoride. Confirm what is included and whether X-rays are additional."),
    ("Are they conveniently located with flexible hours?",
     "Look for practices open after work hours and on weekends. Regular cleaning every 6 months requires a conveniently located practice."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these teeth cleaning clinics?"
METHODOLOGY = [
    "We evaluated dental practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "Gap-free or affordable cleaning pricing for health fund members",
    "Dental hygienist availability for dedicated preventive care",
    "Range of cleaning services (scale and clean, deep cleaning, AIRFLOW)",
    "AHPRA registration verified for all treating practitioners",
    "Digital diagnostic technology including digital X-rays",
    "Patient outcomes: Google review scores above 4.5",
    "Accessibility including weekend and evening appointments",
    "Health fund partnerships and HICAPS claiming",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("How much does professional teeth cleaning cost?",
     'Gap-free with health fund dental extras. Private fee $120 to $350. Read our <a href="/blog/costs/">dental costs guide</a>.'),
    ("How often should I get my teeth cleaned?",
     'Every 6 to 12 months. High-risk patients every 3 to 4 months. Regular <a href="/australia/dental-check-up/">dental check-ups</a> include professional cleaning.'),
    ("Is teeth cleaning painful?",
     'No. Routine cleaning is painless. Mild sensitivity may occur with heavy tartar build-up. Deep cleaning for <a href="/australia/gum-disease-treatment/">gum disease</a> uses local anaesthetic.'),
    ("What is the difference between a scale and clean and teeth whitening?",
     'Scaling and cleaning removes plaque, tartar, and surface stains. <a href="/australia/teeth-whitening/">Teeth whitening</a> uses bleaching agents to lighten tooth colour. Cleaning restores natural colour, whitening goes beyond.'),
    ("How long does a professional clean take?",
     "A routine scale and clean takes 30 to 45 minutes. Deep cleaning takes 1 to 2 hours per quadrant. Allow 60 minutes for a comprehensive clean with examination and X-rays."),
    ("Can tartar be removed at home?",
     "No. Once plaque hardens into tartar (calculus), it bonds strongly to tooth enamel and can only be removed with professional dental instruments. Brushing and flossing prevent plaque from hardening."),
    ("What is AIRFLOW teeth cleaning?",
     "AIRFLOW is a powder-based cleaning system that removes stubborn stains and biofilm using a fine powder mixed with water and compressed air. It is gentler than traditional scaling and ideal for removing coffee, tea, and tobacco stains."),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/teeth-cleaning/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Teeth cleaning in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Teeth Cleaning", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
