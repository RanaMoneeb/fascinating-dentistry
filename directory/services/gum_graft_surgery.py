"""Content for /australia/gum-graft-surgery/ — Top 10 Gum Graft Surgery Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Gum Graft Surgery Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 gum graft surgery clinics in Australia. Connective tissue grafts, free gingival grafts, and pinhole technique. Verified periodontists and clinic details."
H1 = "Top 10 Gum Graft Surgery Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Gum graft surgery is a periodontal procedure that restores receding gum tissue by transplanting tissue from the palate or a donor source to the affected area. Gum recession exposes tooth roots, causing sensitivity, increased decay risk, and aesthetic concerns. The Australian Research Centre for Population Oral Health reports that 23% of Australian adults aged 15 and over have at least one site with gum recession of 3mm or more. The three main graft types are connective tissue grafts (most common, for root coverage), free gingival grafts (for thickening thin gum tissue), and pedicle grafts (using adjacent tissue).",
    "We ranked Australia's top gum graft surgery clinics based on six criteria: specialist periodontist availability with AHPRA registration, range of graft techniques offered (connective tissue, free gingival, pinhole), digital diagnostic technology, published pricing, Google review scores, and free consultation availability. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need gum graft surgery?"
WHEN = [
    "Gum graft surgery is needed when gum recession exposes tooth roots, causing sensitivity, aesthetic concerns, or increased risk of decay and further tissue loss. Recession of 2mm or more typically warrants assessment by a specialist periodontist. The procedure restores protective gum tissue over exposed root surfaces.",
    "Causes of gum recession include aggressive tooth brushing with hard bristle brushes, periodontal disease destroying supporting tissue, orthodontic treatment moving teeth beyond the bone envelope, bruxism (teeth grinding), tobacco use, and naturally thin gum tissue (thin gingival biotype). Identifying and addressing the underlying cause is essential before grafting to prevent recurrence.",
    "There are 4 main graft types. Connective tissue grafts take tissue from underneath the palate surface, providing the most predictable root coverage of 80% to 95%. Free gingival grafts take tissue directly from the palate surface to thicken thin gum tissue. Pedicle grafts use adjacent gum tissue repositioned over the recession site. Alloderm uses donor tissue, avoiding palate harvesting entirely.",
    'The Pinhole Surgical Technique is a minimally invasive alternative that requires no incisions or sutures. A small pinhole is made in the gum to reposition tissue over exposed roots. Not all cases are suitable for this technique. A qualified <a href="/australia/periodontist/">periodontist</a> assesses suitability during consultation. The technique may also be combined with <a href="/australia/cosmetic-dentistry/">cosmetic dentistry</a> for comprehensive smile rehabilitation.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide gum graft surgery across Sydney, Melbourne, Perth, Adelaide, and the Gold Coast. Each entry includes verified contact details, graft techniques offered, specialist qualifications, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Sydney Periodontist Centre", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (160 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "Level 2, 183 Macquarie Street, Sydney NSW 2000", "phone": "(02) 9221 2007",
     "website": "https://www.periodontists.com.au",
     "body": [
        "Sydney Periodontist Centre is led by three specialist periodontists: Dr David Grossberg, Dr Kevin Todes, and Dr Alex Kalos. The practice offers the full scope of periodontics including cosmetic periodontal surgery, gum grafting for receding gums, and crown lengthening. All practitioners hold AHPRA specialist registration in periodontics.",
        "The practice uses state-of-the-art diagnostic technology including digital imaging for precise treatment planning. Sydney Periodontist Centre accepts referrals from general dentists and direct patient bookings from its Macquarie Street location.",
     ]},
    {"rank": 2, "name": "Melbourne Periocare", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.7/5 (140 reviews)", "pricing": "Mid-range", "hours": "Mon-Wed, Fri 9am-5pm",
     "address": "7 Whitehorse Road, Balwyn VIC 3103", "phone": "(03) 9817 1860",
     "website": "https://melbourneperiocare.com.au",
     "body": [
        "Melbourne Periocare is a specialist periodontal practice led by Dr Nupur Kataria, a periodontist with over two decades of experience. The practice provides gum grafting procedures to correct gum recession, with modern facilities and state-of-the-art equipment in Balwyn. Dr Kataria specialises in connective tissue grafts and comprehensive periodontal disease treatment.",
        "The practice offers 45-minute initial consultations for comprehensive assessment. No referral is required. Melbourne Periocare provides gum grafting alongside dental implant placement and periodontal maintenance.",
     ]},
    {"rank": 3, "name": "Perth Periodontics", "location": "Perth, WA", "featured": True, "ahpra": True,
     "rating": "4.8/5 (120 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "Suite 9, 38 Meadowvale Avenue, South Perth WA 6151", "phone": "(08) 9474 4444",
     "website": "https://perthperio.com.au",
     "body": [
        "Perth Periodontics is a specialist practice founded in 2002 by Dr Lucy De Jesus. The practice provides mucogingival surgery (gum grafts) alongside comprehensive periodontal treatment. Dr De Jesus offers connective tissue grafts, free gingival grafts, and crown lengthening for both functional and aesthetic indications.",
        "The practice is known for its compassionate approach to anxious patients and complex medical histories. Perth Periodontics collaborates with general dentists and medical practitioners to provide integrated periodontal care.",
     ]},
    {"rank": 4, "name": "Kew Periodontics and Dental Implants", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (90 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "Level 2, 1-9 Derrick Street, Kew VIC 3101", "phone": "(03) 9853 7700",
     "website": "https://www.kewperiodontics.com.au",
     "body": [
        "Kew Periodontics is a specialist periodontal practice in Kew, Melbourne, providing treatment for gum disease, receding gums, and dental implants. The practice offers connective tissue grafts and free gingival grafts for root coverage and tissue thickening in a gentle, professional environment.",
     ]},
    {"rank": 5, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry provides soft tissue grafting across four Adelaide locations. The practice performs grafting for gum recession caused by aggressive brushing, gum disease, previous dental treatments, and naturally thin gum tissue. All major health funds accepted with HICAPS on-the-spot claiming.",
     ]},
    {"rank": 6, "name": "Greenhill Periodontics and Implants", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (100 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "62 Greenhill Road, Wayville SA 5034", "phone": "(08) 8208 5800",
     "website": "https://www.periodontics.com.au",
     "body": [
        "Greenhill Periodontics is a specialist practice offering soft tissue grafting for gum recession. The practice treats localised, generalised, trauma-induced, and pathologic gum recession using connective tissue grafts, free gingival grafts, and donor tissue options.",
     ]},
    {"rank": 7, "name": "Oasis Dental Studio", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (834 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "21/15 Victoria Ave, Broadbeach QLD 4218", "phone": "(07) 5526 8722",
     "website": "https://www.oasisdentalstudio.com.au",
     "body": [
        "Oasis Dental Studio provides gum graft treatment from its Broadbeach practice on the Gold Coast. The practice offers donor graft materials and traditional grafting techniques. Multiple Gold Coast locations include Broadbeach, Palm Beach, Chirn Park, and Ferry Road. HICAPS available.",
     ]},
    {"rank": 8, "name": "Dentistry on Solent", "location": "Sydney, NSW", "featured": False,
     "rating": "4.9/5 (239 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "12-14 Solent Circuit, Bella Vista NSW 2153", "phone": "(02) 9158 6137",
     "website": "https://www.dentistryonsolent.com.au",
     "body": [
        "Dentistry on Solent provides gum grafting from its Bella Vista practice in Sydney. The practice offers soft-tissue grafting to rebuild thin or receding gums and cover exposed roots. The clinic serves patients from Norwest, Kellyville, Baulkham Hills, Castle Hill, and Rouse Hill.",
     ]},
    {"rank": 9, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": [
        "Bayview Dental provides gum grafting procedures from its Claremont practice in Perth. The practice offers soft tissue grafting with iTero digital scanning technology for precise treatment planning. Interest-free payment plans are available.",
     ]},
    {"rank": 10, "name": "Sydney Periodontists", "location": "Sydney, NSW", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8am-5pm",
     "address": "Suite 12, Level 3, Park House, 187 Macquarie Street, Sydney NSW 2000", "phone": "(02) 8552 0300",
     "website": "https://sydneyperiodontists.com.au",
     "body": [
        "Sydney Periodontists is led by Dr Vijay Tumuluri offering gingival recession treatment and gum grafting. The practice operates from two locations in Sydney CBD and Parramatta. HICAPS on-site and accepts referrals and self-referrals.",
     ]},
]

COST_HEADING = "How much does gum graft surgery cost in Australia?"
COST = [
    "Gum graft surgery in Australia costs between $600 and $3,000 per tooth depending on the graft type, number of teeth treated, and provider qualifications. Specialist periodontist fees reflect the additional 3 years of university training required for specialist registration.",
    "Private health insurance with major dental cover provides rebates that vary by fund and item number. Some practices offer Alloderm donor tissue grafts that avoid palate harvesting, though these cost more than traditional autogenous grafts.",
]
COST_PRICES = [
    ("Connective tissue graft (per tooth)", "$800 - $2,500"),
    ("Free gingival graft (per tooth)", "$600 - $1,800"),
    ("Pedicle graft (per tooth)", "$500 - $1,500"),
    ("Alloderm donor tissue graft (per tooth)", "$1,000 - $3,000"),
    ("Pinhole Surgical Technique (per tooth)", "$600 - $1,500"),
    ("Consultation", "Free - $350"),
]
COST_AFTER = [
    'Most practices offer interest-free payment plans for gum graft treatment. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. Learn more about <a href="/australia/periodontist/">periodontist fees</a> and <a href="/australia/gum-disease-treatment/">gum disease treatment</a> costs.',
]

CHOOSE_HEADING = "How do you choose a gum graft surgery clinic in Australia?"
CHOOSE_INTRO = "Selecting the right gum graft surgery clinic requires verifying specialist qualifications and graft technique expertise. Ask these 5 questions during your consultation."
CHOOSE_CRITERIA = [
    ("Is there a specialist periodontist on staff?",
     'Gum grafting is a specialist periodontal procedure. Verify the practitioner holds AHPRA specialist registration in periodontics. A <a href="/australia/periodontist/">periodontist</a> has completed 3 additional years of university training in soft tissue surgery.'),
    ("What graft techniques do they offer?",
     "A comprehensive practice should offer connective tissue grafts, free gingival grafts, pinhole technique, and donor tissue options. Limited options may mean the clinic cannot select the optimal technique for your case."),
    ("What is the total cost including follow-up visits?",
     "Request an itemised quote covering the graft procedure, sutures, follow-up reviews, and any adjunctive procedures. Confirm whether retainers or stents are included."),
    ("Do they use digital scanning technology?",
     "Digital scanning and 3D imaging improve treatment planning precision and allow accurate before-and-after comparison of root coverage outcomes."),
    ("What is the expected healing timeline?",
     "Initial healing takes 1 to 2 weeks with sutures removed at 10 to 14 days. Complete tissue maturation takes 4 to 6 weeks. Ask for a realistic recovery estimate based on your specific case."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these gum graft surgery clinics?"
METHODOLOGY = [
    "We evaluated periodontal and dental practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "Specialist periodontist with AHPRA registration on staff",
    "Range of graft techniques offered (connective tissue, free gingival, pinhole, donor)",
    "Digital diagnostic technology including 3D imaging and intraoral scanning",
    "Documented experience in mucogingival surgery",
    "Pricing transparency with itemised quotes",
    "Patient outcomes: Google review scores above 4.5",
    "Referral acceptance and collaborative care approach",
    "Payment plan availability and health fund partnerships",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is gum graft surgery?",
     "Gum graft surgery is a periodontal procedure transplanting tissue to cover exposed roots and restore a receding gum line. Connective tissue grafts from the palate are most common, providing predictable root coverage of 80% to 95%."),
    ("How much does gum graft surgery cost?",
     'Gum graft surgery costs $600 to $3,000 per tooth depending on graft type. Connective tissue grafts cost $800 to $2,500. Free gingival grafts cost $600 to $1,800. Read our <a href="/blog/costs/">dental costs guide</a> for details.'),
    ("Is gum graft surgery painful?",
     "Gum graft surgery is performed under local anaesthetic. Mild discomfort lasts 3 to 5 days post-surgery. The palatal donor site may be tender. Over-the-counter analgesics manage pain effectively. Most patients rate pain 3 out of 10."),
    ("How long does gum graft surgery take to heal?",
     "Initial healing takes 1 to 2 weeks. Complete tissue integration takes 4 to 6 weeks. Avoid hard, hot, or crunchy foods for the first week. Sutures dissolve or are removed at 10 to 14 days."),
    ("What are the different types of gum grafts?",
     'Connective tissue graft (under palate surface, best root coverage), free gingival graft (palate surface, for thickening thin tissue), pedicle graft (adjacent tissue), and Alloderm (donor tissue avoiding palate harvesting). A <a href="/australia/periodontist/">periodontist</a> recommends the best option.'),
    ("Will my gum recession come back after grafting?",
     'Grafting is highly predictable when performed by a specialist. Recurrence is rare with proper oral hygiene, soft brushing technique, and management of contributing factors like bruxism or <a href="/australia/gum-disease-treatment/">gum disease</a>.'),
    ("Can I get gum graft surgery without cutting?",
     'The Pinhole Surgical Technique is a minimally invasive alternative requiring no incisions or sutures. A small pinhole is made to reposition gum tissue over exposed roots. Not all cases are suitable. Consult a <a href="/australia/periodontist/">periodontist</a> for assessment.'),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/gum-graft-surgery/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Gum graft surgery in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Gum Graft Surgery", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
