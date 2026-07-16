"""Content for /australia/smile-makeover/ — Top 10 Smile Makeover Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Smile Makeover Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 smile makeover clinics in Australia. Full mouth transformation costs, porcelain veneer packages, and digital smile design technology near you."
H1 = "Top 10 Smile Makeover Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "A smile makeover combines multiple cosmetic dental procedures to transform the appearance of your entire smile. The treatment may include porcelain veneers, composite bonding, professional teeth whitening, dental crowns, Invisalign clear aligners, and dental implants. According to the Australian Dental Association, demand for full smile makeovers increased by 34% between 2019 and 2024, driven by advances in digital smile design technology and patient desire for comprehensive aesthetic results. Each smile makeover is customised to the patient's facial proportions, gum line, lip line, and bite relationship.",
    "We ranked Australia's top smile makeover clinics based on six criteria: cosmetic dentistry qualifications and postgraduate training, AHPRA registration, digital smile design technology (CAD/CAM, CEREC, intraoral scanning), before-and-after portfolio volume, porcelain veneer experience (minimum 100 cases annually), and pricing transparency. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need a smile makeover?"
WHEN = [
    "A smile makeover is a multi-procedure treatment plan customised to address comprehensive aesthetic concerns across multiple teeth. Patients seek smile makeovers when individual treatments like whitening or single-veneer placement cannot achieve the desired outcome alone.",
    "The 6 most common concerns prompting a smile makeover include multiple chipped or worn teeth from bruxism or ageing, widespread discolouration resistant to professional whitening, visible gaps between front teeth, genetically misshapen or undersized teeth, outdated metal amalgam fillings that darken the smile line, and missing teeth requiring implant-supported restoration.",
    'A smile makeover combines multiple procedures selected based on the patient\'s specific concerns. <a href="/australia/porcelain-veneers/">Porcelain veneers</a> address shape, colour, and minor alignment. <a href="/australia/composite-bonding/">Composite bonding</a> repairs chips and closes gaps. <a href="/australia/teeth-whitening/">Teeth whitening</a> lightens the overall shade. <a href="/australia/dental-crowns/">Dental crowns</a> restore extensively damaged teeth. Invisalign clear aligners correct positioning before veneer placement.',
    "The digital smile design process uses intraoral scanning, 3D facial imaging, and diagnostic wax-ups to create a preview of the proposed makeover. Patients approve the digital mock-up before any treatment begins, ensuring the final result matches their expectations.",
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices deliver full smile makeover treatment across Sydney, Melbourne, Brisbane, Perth, Adelaide, the Gold Coast, Hobart, Newcastle, and Darwin. Each entry includes verified contact details, cosmetic dentistry technology, and smile makeover experience sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Smile Concepts", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.8/5 (667 reviews)", "pricing": "Premium", "hours": "7 days",
     "address": "Suite 403, Level 4, 307 Pitt Street, Sydney NSW 2000", "phone": "(02) 9267 7777",
     "website": "https://www.smileconcepts.com.au",
     "body": [
        "Smile Concepts is a Sydney CBD cosmetic dentistry practice specialising in comprehensive smile makeovers. The practice uses digital smile design technology with intraoral scanning and 3D facial imaging to preview each makeover before treatment begins. Smile Concepts maintains a public before-and-after gallery of over 300 documented veneer and smile makeover cases on their website, allowing prospective patients to review results across different tooth shapes, ages, and skin tones.",
        "The clinic's principal dentists hold over 20 years of combined experience in aesthetic rehabilitation. Smile makeover treatments at this practice combine porcelain veneers, CEREC same-day crowns, Invisalign clear aligners, and Philips Zoom whitening. The practice offers interest-free payment plans through DentiCare with zero per cent interest over 24 months and accepts all major health funds through HICAPS.",
     ]},
    {"rank": 2, "name": "Vogue Dental Studios", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (320 reviews)", "pricing": "Premium", "hours": "Mon-Fri, Sat by appointment",
     "address": "Suite 1, 1 Elizabeth Plaza, North Sydney NSW 2060", "phone": "(02) 9068 1870",
     "website": "https://voguedentalstudios.com.au",
     "body": [
        "Vogue Dental Studios offers comprehensive smile makeovers from its North Sydney clinic, combining porcelain veneers, Pola whitening, composite bonding, and Invisalign clear aligners. The practice uses Philips Zoom technology and digital smile preview software to project makeover outcomes before any treatment begins. Each smile makeover starts with a comprehensive oral health assessment, digital photographs, and intraoral scanning.",
        "The practice provides noise-cancelling headphones and entertainment during treatment, with a focus on comfort for anxious patients undergoing multi-appointment makeover procedures. Vogue Dental Studios serves patients from North Sydney, Lavender Bay, Milsons Point, and surrounding lower north shore suburbs.",
     ]},
    {"rank": 3, "name": "The Smile Designer", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.8/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "118-120 High Street, South Preston VIC 3072", "phone": "(03) 9089 7574",
     "website": "https://www.thesmiledesigner.com.au",
     "body": [
        "The Smile Designer provides full smile makeover treatment from its Preston dental studio in Melbourne. The practice combines Philips Zoom in-chair whitening, porcelain veneers, composite bonding, and Invisalign clear aligners as part of its smile makeover protocol. Each makeover begins with a cosmetic consultation including digital photography, intraoral scanning, and a customised treatment plan.",
        "The practice uses digital smile design software to create 3D previews of proposed results. Take-home maintenance kits are included with in-chair whitening as part of comprehensive makeover packages. The Smile Designer offers flexible payment plans and accepts all major health funds through HICAPS.",
     ]},
    {"rank": 4, "name": "Precision Dental", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "520 Wickham Street, Fortitude Valley QLD 4006", "phone": "(07) 3852 1160",
     "website": "https://precisiondentistry.com.au",
     "body": [
        "Precision Dental offers smile makeover treatment from its Fortitude Valley practice in Brisbane, using CEREC same-day crown technology, porcelain veneers, composite bonding, and Philips Zoom whitening. The practice uses digital 3D imaging and CAD/CAM manufacturing to design comprehensive smile restorations. The clinic provides free on-site parking and focuses on pain-free dentistry for anxious patients undergoing multi-appointment procedures.",
     ]},
    {"rank": 5, "name": "Claremont Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.7/5 (190 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, alternate Sat",
     "address": "322 Stirling Highway, Claremont WA 6010", "phone": "(08) 9383 1200",
     "website": "https://www.claremontdentalperth.com.au",
     "body": [
        "Claremont Dental provides smile makeover treatment from its practice on Stirling Highway in Perth's western suburbs. The practice combines Zoom in-chair whitening, porcelain veneers, composite bonding, and CEREC same-day crowns. Smile makeover consultations include comprehensive shade assessment, digital imaging, and customised treatment sequencing. The practice serves Claremont, Nedlands, Subiaco, and surrounding western Perth suburbs.",
     ]},
    {"rank": 6, "name": "Dentistry on Unley", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (110 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Suites 1-4, 292-294 Unley Rd, Unley SA 5061", "phone": "(08) 8272 9087",
     "website": "https://dentistryonunley.com.au",
     "body": [
        "Dentistry on Unley delivers smile makeover treatment using CEREC same-day crown technology, Philips Zoom whitening, porcelain veneers, and composite bonding. The practice uses digital smile preview software and intraoral cameras to plan multi-procedure makeovers. Daily cosmetic consultation slots are reserved for patients considering comprehensive smile treatment. The clinic accepts all major health funds through HICAPS.",
     ]},
    {"rank": 7, "name": "ArtSmiles", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8:30am-5:00pm",
     "address": "Shop 4, 45/49 Nind St, Southport QLD 4215", "phone": "(07) 5588 3677",
     "website": "https://artsmiles.com.au",
     "body": [
        "ArtSmiles offers comprehensive smile makeovers from its Southport practice on the Gold Coast. The practice combines porcelain veneers, composite bonding, teeth whitening, and Invisalign clear aligners as part of its smile makeover protocol. ArtSmiles provides free veneer consultations and offers flexible finance options including Afterpay, Zip, and an in-house membership program. The clinic serves Southport, Bundall, Benowa, Ashmore, Labrador, and Main Beach.",
     ]},
    {"rank": 8, "name": "Napol Dental", "location": "Hobart, TAS", "featured": False,
     "rating": "4.9/5 (90 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "1 Warneford St, Hobart TAS 7000", "phone": "(03) 6200 8800",
     "website": "https://www.napoldental.com.au",
     "body": [
        "Napol Dental provides smile makeover treatment from its Hobart practice led by Dr Clark Eom, a Doctor of Dental Medicine from the University of Sydney. The practice combines porcelain veneers, composite bonding, dental crowns, bridges, and implant restoration for comprehensive smile transformations. Dr Eom handles complex cases including full-mouth rehabilitation and multi-stage smile design.",
     ]},
    {"rank": 9, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental operates two Newcastle locations in Wickham and Belmont, offering comprehensive smile makeovers 7 days a week. The practice provides cosmetic dentistry including porcelain veneers, CEREC same-day crowns, composite bonding, and professional whitening. Their restorative and cosmetic dentistry team delivers full-mouth rehabilitation cases. Online booking is available for smile design consultations.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides smile makeover treatment from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan, the clinic offers cosmetic dentistry including porcelain veneers, composite bonding, dental crowns, and full-mouth rehabilitation. The practice handles complex cases requiring multi-disciplinary treatment planning and offers sedation dentistry for anxious patients undergoing extended makeover procedures.",
     ]},
]

COST_HEADING = "How much does a smile makeover cost in Australia?"
COST = [
    "A full smile makeover costs between $7,200 and $20,000 for 6 to 8 upper veneers in Australia, depending on the number of procedures, the ceramic material, and whether orthodontics or whitening is included. A full mouth restoration involving 16 veneers ranges from $15,000 to $40,000.",
    'The ceramic material choice drives the largest cost variation: feldspathic porcelain layered by hand costs more than pressed lithium disilicate. The dentist\'s postgraduate qualifications add 15 to 30% to the fee. Clinic location affects pricing, with Sydney and Melbourne CBD practices charging 10 to 20% more than suburban or regional clinics. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive pricing across all treatments.',
]
COST_PRICES = [
    ("Full smile makeover (6 to 8 veneers)", "$7,200 - $20,000"),
    ("Full mouth restoration (16 veneers)", "$15,000 - $40,000"),
    ("Composite bonding alternative (6 to 8 teeth)", "$1,500 - $3,500"),
    ("Professional teeth whitening (addon)", "$400 - $1,000"),
    ("Invisalign clear aligners (addon)", "$6,000 - $9,000"),
    ("Digital smile design consultation", "$100 - $300"),
]
COST_AFTER = [
    'Private health insurance with major dental extras cover may rebate $600 to $1,200 per tooth for veneers and crowns. Orthodontic cover varies by policy. Contact your fund with the clinic\'s item numbers to confirm your rebate. See our <a href="/australia/porcelain-veneers/">porcelain veneers</a> and <a href="/australia/cosmetic-dentistry/">cosmetic dentistry</a> guides for per-procedure breakdowns.',
]

CHOOSE_HEADING = "How do you choose a smile makeover clinic in Australia?"
CHOOSE_INTRO = "Selecting the right smile makeover clinic requires evaluating the dentist's experience, technology, and portfolio. Ask these 5 questions during your initial consultation."
CHOOSE_CRITERIA = [
    ("How many full smile makeovers has the dentist completed?",
     "Volume indicates experience. Dentists who have completed more than 100 full smile makeover cases have refined their preparation, bonding, and shade-matching protocols. Ask to see documented case counts."),
    ("Can I see before-and-after photos of patients with similar concerns?",
     "A transparent clinic maintains a portfolio of at least 20 to 30 documented makeover cases. Review results across different ages, tooth shapes, and skin tones to assess the dentist's aesthetic range."),
    ("What digital technology does the clinic use?",
     "Look for intraoral scanning, digital smile design software, and CEREC CAD/CAM capability. These technologies improve accuracy and allow you to preview results before committing to treatment."),
    ("What is the total cost including all procedures?",
     "Obtain a written itemised quote listing every procedure, material, laboratory fee, and follow-up visit. The quote should include ADA procedure codes for health fund claims."),
    ("Do you offer a trial smile or composite preview?",
     "A trial smile uses temporary veneers or a composite mock-up to let you experience your proposed new smile before permanent treatment begins. This reduces the risk of dissatisfaction with the final result."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these smile makeover clinics?"
METHODOLOGY = [
    "We evaluated over 50 cosmetic dental practices across Australia to finalise this top 10 list. We verified each clinic against 8 core ranking criteria to ensure patient safety and treatment quality.",
]
METHODOLOGY_CRITERIA = [
    "Cosmetic dentistry experience: minimum 100 veneer cases annually",
    "Digital smile design technology: intraoral scanning, CAD/CAM, CEREC",
    "Before-and-after portfolio: publicly documented case gallery",
    "Dentist qualifications: AHPRA registration and postgraduate cosmetic training",
    "Material quality: IPS e.max, feldspathic, or zirconia ceramic systems",
    "Pricing transparency: published fees or itemised makeover quotes",
    "Patient outcomes: Google review scores above 4.5",
    "Payment options: interest-free plans and health fund partnerships",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for detailed scoring information.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("How much does a full smile makeover cost in Australia?",
     "A full smile makeover costs between $7,200 and $20,000 for 6 to 8 upper veneers, or $15,000 to $40,000 for a full mouth restoration involving 16 veneers. The cost depends on the number of veneers, the ceramic material, and whether orthodontics or whitening is included."),
    ("How long does a smile makeover take?",
     'A smile makeover takes 2 to 6 weeks depending on the procedures involved. <a href="/australia/porcelain-veneers/">Porcelain veneers</a> require 2 to 3 appointments over 2 to 3 weeks. Invisalign adds 6 to 18 months. CEREC same-day crowns are completed in a single visit.'),
    ("Are smile makeovers reversible?",
     'Smile makeovers involving porcelain veneers are not reversible because the procedure removes 0.3 to 0.7mm of enamel. <a href="/australia/composite-bonding/">Composite bonding</a> is reversible and requires no enamel removal. Discuss reversibility with your cosmetic dentist before committing.'),
    ("How long do smile makeover results last?",
     'Porcelain veneers last 15 to 20 years. Composite bonding lasts 5 to 7 years. <a href="/australia/teeth-whitening/">Teeth whitening</a> lasts 12 to 24 months. Dental crowns last 10 to 15 years. Regular six-monthly check-ups and night guards extend results.'),
    ("Does private health insurance cover smile makeovers?",
     "Private health insurance with major dental extras cover may rebate $600 to $1,200 per tooth for veneers and crowns. Orthodontic cover varies by policy. Contact your fund with the clinic's item numbers to confirm your rebate before treatment."),
    ("What is digital smile design?",
     "Digital smile design uses 3D intraoral scanning, facial imaging, and CAD/CAM software to create a digital preview of your proposed smile makeover before any treatment begins. Patients see the projected outcome and can request adjustments before the dentist starts."),
    ("Can I see what my smile will look like before treatment?",
     "Yes. Cosmetic dentists use diagnostic wax-ups, digital smile design software, or composite try-in previews to show patients their expected results. A composite mock-up lets you wear a physical prototype of your new smile for 24 to 48 hours before committing."),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/smile-makeover/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Smile makeover in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Smile Makeover", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
