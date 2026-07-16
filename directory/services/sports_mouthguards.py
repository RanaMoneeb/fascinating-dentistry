"""Content for /australia/sports-mouthguards/ — Top 10 Sports Mouthguard Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Sports Mouthguard Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 sports mouthguard clinics in Australia. Custom-fitted mouthguards for rugby, football, MMA, and contact sports. Verified clinics near you."
H1 = "Top 10 Sports Mouthguard Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "A custom sports mouthguard is a professionally fitted dental appliance made from impressions of your teeth to protect against dental injuries during contact sports. Unlike boil-and-bite mouthguards from pharmacies, custom mouthguards provide precise fit, superior shock absorption, and optimal protection. The Australian Dental Association recommends custom-fitted mouthguards for all contact sports including rugby, AFL, football, hockey, boxing, martial arts, and basketball. Sports Medicine Australia reports that dental injuries from sport account for over 30% of all facial injuries.",
    "We ranked Australia's top sports mouthguard clinics based on six criteria: custom-fitted mouthguard fabrication, range of materials and thickness options, colour and design customisation, AHPRA registration, published pricing, and Google review scores. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need a sports mouthguard?"
WHEN = [
    "A custom sports mouthguard is made from dental impressions of your teeth, then vacuum-formed or pressure-formed over a stone model to create a precise fit. The Australian Dental Association and Sports Medicine Australia both recommend custom-fitted mouthguards as the gold standard for dental protection during contact sport.",
    "There are 3 types of mouthguards. Stock mouthguards come pre-formed off the shelf and cannot be adjusted. Boil-and-bite mouthguards from pharmacies are softened in hot water then bitten into, but fit poorly and may dislodge during impact. Custom-fitted mouthguards from a dentist provide the highest level of protection, comfort, and fit.",
    "You need a sports mouthguard for any contact sport including rugby, AFL, football, hockey, boxing, martial arts, basketball, cricket batting, lacrosse, and water polo. The mouthguard absorbs and distributes impact force, preventing tooth fracture, tooth avulsion (knocked out tooth), soft tissue laceration, and jaw fracture.",
    'A custom mouthguard is essential for children playing school and club sport. A [children\'s dentist](https://fascinatingdentistry.com/australia/childrens-dentist/) can fabricate a properly fitted mouthguard that stays in place during impact. Children need replacement every 6 to 12 months as their teeth and jaws grow. Schedule a [dental check-up](https://fascinatingdentistry.com/australia/dental-check-up/) to have a mouthguard made.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide custom sports mouthguards across Sydney, Melbourne, Brisbane, Perth, Adelaide, Newcastle, and Darwin. Each entry includes verified contact details, mouthguard pricing, and services sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Sydney Dental Surgeons", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (210 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Suite 1003, Level 10, 135 Macquarie Street, Sydney NSW 2000", "phone": "(02) 9221 1530",
     "website": "https://www.sydneydentalsurgeons.com.au",
     "body": [
        "Sydney Dental Surgeons has provided custom-fitted mouthguards for nearly 40 years. The practice offers custom mouthguards designed for specific needs including sports protection. Made from dental impressions for precise fit, comfort, and effective protection.",
        "The practice serves patients from its Macquarie Street location in the Sydney CBD. Custom mouthguards from Sydney Dental Surgeons stay securely in place during impact and provide superior shock absorption compared to over-the-counter options.",
     ]},
    {"rank": 2, "name": "Pure Dentistry", "location": "Brisbane, QLD", "featured": True, "ahpra": True,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 11, The Village Shopping Centre, 1932-1974 Logan Road, Upper Mount Gravatt QLD 4122", "phone": "(07) 3343 4880",
     "website": "https://www.puredentistry.com.au",
     "body": [
        "Pure Dentistry provides custom-made mouthguards professionally fitted for maximum protection against traumatic sports injuries. The practice uses shock-absorbing material for superior impact resistance. Open 7 days a week at The Village Shopping Centre in Upper Mount Gravatt with free parking.",
     ]},
    {"rank": 3, "name": "ADDC Dental", "location": "Perth, WA", "featured": True, "ahpra": True,
     "rating": "4.7/5 (150 reviews)", "pricing": "Budget (from $200)", "hours": "Mon-Fri, Sat by appointment",
     "address": "426 Alexander Drive, Dianella WA 6059", "phone": "(08) 9276 1540",
     "website": "https://addcdental.com.au",
     "body": [
        "ADDC Dental provides custom sports mouthguards from $200 for athletes playing fast, active sports. The practice offers properly fitted mouthguards for rugby, football, hockey, and all contact sports. Located on Alexander Drive in Dianella, serving the northern Perth suburbs.",
     ]},
    {"rank": 4, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental provides custom sports mouthguards across six Melbourne locations. Preferred provider for Bupa, Medibank, and HCF. Open 7 days a week with online booking available.",
     ]},
    {"rank": 5, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry provides custom sports mouthguards across four Adelaide locations. All major health funds accepted with HICAPS on-the-spot claiming. The practice offers mouthguards in various colours and thickness options.",
     ]},
    {"rank": 6, "name": "Malouf Dental", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Thu, Fri mornings",
     "address": "1476 Wynnum Road, Tingalpa QLD 4173", "phone": "(07) 3390 6100",
     "website": "https://cosmeticdentistinbrisbane.com.au",
     "body": [
        "Malouf Dental provides custom-fitted sports mouthguards from its Tingalpa practice in Brisbane. Complimentary initial appointments and interest-free payment plans available.",
     ]},
    {"rank": 7, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": [
        "Bayview Dental provides custom sports mouthguards with digital scanning technology for precise fit. Interest-free payment plans available.",
     ]},
    {"rank": 8, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental provides custom-fitted sports mouthguards from two Newcastle locations. Online booking available 7 days a week.",
     ]},
    {"rank": 9, "name": "Clear Dental", "location": "Sydney, NSW", "featured": False,
     "rating": "4.8/5 (320 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "131 Clarence St, Sydney NSW 2000", "phone": "(02) 9456 6557",
     "website": "https://www.cleardental.com.au",
     "body": [
        "Clear Dental provides custom sports mouthguards including children's mouthguards from its Sydney CBD location. Open 7 days a week. CDBS available for eligible children.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides custom sports mouthguards from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan. Sedation options available for anxious patients.",
     ]},
]

COST_HEADING = "How much does a custom sports mouthguard cost in Australia?"
COST = [
    "A custom-fitted sports mouthguard costs between $100 and $300 in Australia depending on the material, thickness, and design. While more expensive than boil-and-bite options, custom mouthguards provide superior protection and comfort.",
]
COST_PRICES = [
    ("Custom-fitted mouthguard (single colour)", "$100 - $250"),
    ("Custom-fitted mouthguard (multi-colour/design)", "$150 - $300"),
    ("Junior custom mouthguard (under 12)", "$90 - $180"),
    ("Boil-and-bite (pharmacy, not recommended)", "$20 - $50"),
]
COST_AFTER = [
    'Some private health funds cover custom mouthguards under dental extras. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. Schedule a <a href="/australia/dental-check-up/">dental check-up</a> to have impressions taken.',
]

CHOOSE_HEADING = "How do you choose a sports mouthguard clinic in Australia?"
CHOOSE_INTRO = "Selecting the right sports mouthguard clinic ensures your mouthguard fits properly and provides maximum protection. Ask these 5 questions."
CHOOSE_CRITERIA = [
    ("Does the clinic make custom-fitted mouthguards from dental impressions?",
     "Custom mouthguards require dental impressions and laboratory fabrication. Avoid clinics that only offer boil-and-bite options, as these provide inferior protection."),
    ("What thickness options do they offer?",
     "Different sports require different thicknesses: light (2mm) for low-contact, medium (3mm) for moderate contact, and heavy (4mm+) for full contact sports like rugby and boxing."),
    ("Do they offer colour and design customisation?",
     "Many clinics offer team colours, patterns, and name insertion in the mouthguard. This is particularly popular for junior sports."),
    ("Do they have experience fitting children's mouthguards?",
     'Children need properly fitted mouthguards that account for growing jaws. A [children\'s dentist](https://fascinatingdentistry.com/australia/childrens-dentist/) experienced in sports mouthguards is ideal.'),
    ("Does the clinic offer quick turnaround?",
     "Custom mouthguards typically take 1 to 2 weeks to fabricate. If you need one urgently for a sports season start, confirm the turnaround time."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these sports mouthguard clinics?"
METHODOLOGY = [
    "We evaluated dental practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "Custom-fitted mouthguard fabrication from dental impressions",
    "Range of material thickness options (light, medium, heavy)",
    "Colour and design customisation availability",
    "AHPRA registration verified for all treating practitioners",
    "Experience fitting children's and junior mouthguards",
    "Pricing transparency with published fees",
    "Patient outcomes: Google review scores above 4.5",
    "Accessibility including weekend and evening appointments",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("How much does a custom sports mouthguard cost?",
     'Custom mouthguards cost $100 to $300 depending on design and material. Boil-and-bite from pharmacies cost $20 to $50 but offer poor protection. Read our <a href="/blog/costs/">dental costs guide</a>.'),
    ("Are custom mouthguards better than boil-and-bite?",
     "Yes. Custom-fitted mouthguards provide superior fit, comfort, and protection. Studies show they reduce dental injury risk by up to 82% compared to over-the-counter options."),
    ("What sports require a mouthguard?",
     "Rugby, AFL, football, hockey, boxing, martial arts, basketball, cricket batting, lacrosse, and water polo. The ADA recommends mouthguards for any sport with risk of facial impact."),
    ("How long does a custom mouthguard last?",
     "12 to 18 months for adults. Children need replacement every 6 to 12 months as their teeth and jaws grow. Replace immediately if damaged or loose."),
    ("Can children wear boil-and-bite mouthguards?",
     'The ADA recommends custom-fitted mouthguards for children. Boil-and-bite options often fit poorly and may dislodge during impact. A [children\'s dentist](https://fascinatingdentistry.com/australia/childrens-dentist/) can make a properly fitted mouthguard.'),
    ("What thickness mouthguard do I need?",
     "Light (2mm) for low-contact sports. Medium (3mm) for moderate contact. Heavy (4mm+) for full contact sports like rugby, boxing, and MMA. Your dentist recommends the right thickness."),
    ("Does health insurance cover mouthguards?",
     "Some private health funds cover custom mouthguards under dental extras. Check your policy. HICAPS claiming available at most dental clinics."),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/sports-mouthguards/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Sports mouthguards in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Sports Mouthguards", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
