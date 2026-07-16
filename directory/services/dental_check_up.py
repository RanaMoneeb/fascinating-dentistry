"""Content for /australia/dental-check-up/ — Top 10 Dental Check-Up Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Dental Check-Up Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 dental check-up clinics in Australia. Gap-free check-ups, new patient specials, x-rays, scale and clean. Verified clinics near you."
H1 = "Top 10 Dental Check-Up Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "A dental check-up is a routine examination where a dentist assesses your oral health, checks for tooth decay, gum disease, oral cancer, and other dental issues. A standard check-up includes a comprehensive oral examination, professional scale and clean, fluoride treatment, and dental X-rays if needed. The Australian Dental Association recommends check-ups every 6 to 12 months for most adults. Despite this, the AIHW reports that 39% of Australian adults delayed or avoided dental treatment due to cost, making affordable and gap-free check-up options essential.",
    "We ranked Australia's top dental check-up clinics based on six criteria: gap-free or affordable check-up pricing for health fund members, new patient specials, range of preventive services included, AHPRA registration, published pricing, and Google review scores. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need a dental check-up?"
WHEN = [
    'A dental check-up includes a comprehensive oral examination, professional [teeth cleaning](https://fascinatingdentistry.com/australia/teeth-cleaning/) (scale and clean to remove plaque and tartar), fluoride treatment to strengthen enamel, and dental X-rays if needed. The dentist checks for tooth decay, gum disease, bite problems, and performs an [oral cancer screening](https://fascinatingdentistry.com/australia/oral-cancer-screening/).',
    "The Australian Dental Association recommends check-ups every 6 to 12 months for most adults. High-risk patients including smokers, diabetics, those with gum disease history, or previous heavy decay should attend every 3 to 6 months. Regular check-ups detect problems early when treatment is simpler, faster, and less expensive.",
    "Early detection through regular check-ups saves thousands in treatment costs. A small cavity detected at a check-up costs $200 to $300 to fill. The same cavity left untreated progresses to a root canal costing $1,500 to $3,000 or an extraction and implant costing $4,000 to $6,000. Oral cancer detected early has an 80 to 90% five-year survival rate.",
    'Skipping check-ups allows silent progression of decay, [gum disease](https://fascinatingdentistry.com/australia/gum-disease-treatment/), and oral cancer. Many dental conditions cause no pain until they reach an advanced stage. Regular examinations are the only reliable way to catch these issues before they become painful and expensive.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide affordable dental check-ups across Sydney, Melbourne, Brisbane, Perth, Adelaide, Newcastle, and Darwin. Each entry includes verified contact details, check-up pricing, and services sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "No Gaps Dental", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.8/5 (650 reviews)", "pricing": "Gap-free (health fund), $199 private", "hours": "Mon-Sat",
     "address": "Level 2, 283 George Street, Sydney NSW 2000", "phone": "(02) 8383 1400",
     "website": "https://www.nogapsdental.com",
     "body": [
        "No Gaps Dental offers gap-free check-ups for health fund members with dental extras cover across 18 Sydney locations. The comprehensive check-up includes examination, scale and clean, fluoride, and X-rays. Over 20 years serving Sydney families.",
        "The practice provides general dentistry, children's dentistry, cosmetic dentistry, and emergency care. CDBS bulk billing available for eligible children. New patients welcome with no waiting periods at most locations.",
     ]},
    {"rank": 2, "name": "Dental 99", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.7/5 (1,200 reviews)", "pricing": "Budget", "hours": "7 days",
     "address": "Shop 1, 11 Epping Road, Macquarie Park NSW 2113", "phone": "1300 655 022",
     "website": "https://dental99.com.au",
     "body": [
        "Dental 99 is a bulk bill dental practice operating across Sydney, Brisbane, and Melbourne with 7 locations. The practice provides affordable check-ups, cleaning, X-rays, and fillings. Booking is managed through the Dental 99 mobile app.",
        "Locations include Bondi Junction, Epping, Mango Hill, Marayong, Monash, Moorebank, and Sydney CBD. The practice handles Medicare claims automatically for CDBS eligible children.",
     ]},
    {"rank": 3, "name": "Sydney CBD Dentistry", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (420 reviews)", "pricing": "Mid-range (gap-free for health fund)", "hours": "Mon-Sat",
     "address": "Suite 6, Level 2, 135 Macquarie Street, Sydney NSW 2000", "phone": "(02) 9232 3788",
     "website": "https://www.sydneycbddentistry.com.au",
     "body": [
        "Sydney CBD Dentistry provides comprehensive check-ups including examination, consultation, teeth cleaning, and X-rays (panoramic OPG and bitewing). Gap-free for health fund members with dental cover. Returning patient check-up and clean is $219.",
        "The practice offers general, cosmetic, and emergency dental services from its Macquarie Street location. Professional dental hygienists provide gentle preventive care.",
     ]},
    {"rank": 4, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range (gap-free for health fund)", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental provides gap-free check-ups for health fund members across six Melbourne locations. Preferred provider for Bupa, Medibank, and HCF. Services include examination, clean, X-rays, fluoride, and fillings. Open 7 days a week.",
     ]},
    {"rank": 5, "name": "NDC Darwin", "location": "Darwin, NT", "featured": False,
     "rating": "4.6/5 (180 reviews)", "pricing": "Budget (no gap or $199)", "hours": "Mon-Sat",
     "address": "Shop 1, 70 Smith Street, Darwin NT 0800", "phone": "(08) 8946 2200",
     "website": "https://www.nationaldentalcare.com.au",
     "body": [
        "NDC Darwin offers no gap or $199 dental check-up including clean, polish, and fluoride treatment. The practice specialises in preventive dentistry, Invisalign, same-day dental, and dental implants. New patients receive comprehensive first appointment assessment.",
     ]},
    {"rank": 6, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": [
        "Bayview Dental provides comprehensive check-ups including examination, clean, fluoride, and X-rays with iTero digital scanning. Interest-free payment plans available. The practice serves the western suburbs of Perth from Claremont.",
     ]},
    {"rank": 7, "name": "Malouf Dental", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Thu, Fri mornings",
     "address": "1476 Wynnum Road, Tingalpa QLD 4173", "phone": "(07) 3390 6100",
     "website": "https://cosmeticdentistinbrisbane.com.au",
     "body": [
        "Malouf Dental provides comprehensive dental check-ups with examination, clean, and X-rays. The clinic offers complimentary initial appointments and interest-free payment plans for Brisbane patients.",
     ]},
    {"rank": 8, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental provides comprehensive check-ups, clean, X-rays, and fluoride from two Newcastle locations. Online booking is available and the clinic serves the Hunter Region 7 days a week.",
     ]},
    {"rank": 9, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry provides comprehensive check-ups, clean, X-rays, and fluoride across four Adelaide locations. All major health funds accepted with HICAPS on-the-spot claiming.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides comprehensive dental check-ups, clean, and X-rays. Led by Dr Anand Murugappan, the clinic offers sedation options for anxious patients.",
     ]},
]

COST_HEADING = "How much does a dental check-up cost in Australia?"
COST = [
    "A dental check-up in Australia costs between $0 (gap-free with health fund) and $350 for a comprehensive examination with clean, fluoride, and X-rays. Many practices offer gap-free check-ups for patients with private health insurance that includes dental extras cover.",
    "The Child Dental Benefits Schedule provides free check-ups for eligible children aged 0 to 17. Public dental clinics offer free or low-cost check-ups for eligible concession card holders.",
]
COST_PRICES = [
    ("Gap-free check-up (health fund members)", "$0 out of pocket"),
    ("Standard check-up and clean (private)", "$150 - $300"),
    ("Comprehensive exam + scale and clean + fluoride", "$199 - $350"),
    ("Dental X-rays (bitewing)", "$45 - $90"),
    ("Panoramic X-ray (OPG)", "$100 - $200"),
    ("New patient check-up special", "$99 - $199"),
]
COST_AFTER = [
    'Private health funds typically cover 1 to 2 check-ups per year under dental extras. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. Learn more about <a href="/australia/teeth-cleaning/">teeth cleaning</a> and <a href="/australia/fillings/">fillings</a> costs.',
]

CHOOSE_HEADING = "How do you choose a dental check-up clinic in Australia?"
CHOOSE_INTRO = "Selecting the right dental check-up clinic involves finding a practice that is affordable, convenient, and thorough. Ask these 5 questions."
CHOOSE_CRITERIA = [
    ("Does the clinic offer gap-free check-ups?",
     "If you have private health insurance with dental extras, look for clinics that offer gap-free check-ups where the health fund rebate covers the full cost."),
    ("Are there new patient specials?",
     "Many clinics offer discounted check-ups for new patients ranging from $99 to $199. These typically include examination, clean, and X-rays."),
    ("What is included in the check-up?",
     "A comprehensive check-up should include oral examination, scale and clean, fluoride treatment, and X-rays if needed. Confirm what is included before booking."),
    ("Are the dentists experienced and AHPRA registered?",
     "Verify all treating dentists hold current AHPRA registration. Check Google reviews for patient feedback on the quality of examinations."),
    ("Are they conveniently located with flexible hours?",
     "Look for clinics open after work hours and on weekends. Multiple locations reduce travel time for busy families."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these dental check-up clinics?"
METHODOLOGY = [
    "We evaluated dental practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "Gap-free or affordable check-up pricing for health fund members",
    "New patient specials and transparent pricing",
    "Comprehensive preventive services included in check-ups",
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
    ("How much does a dental check-up cost?",
     'Gap-free for health fund members with dental extras. Private fee $150 to $300. New patient specials from $99. Read our <a href="/blog/costs/">dental costs guide</a>.'),
    ("How often should I get a dental check-up?",
     "Every 6 to 12 months for most adults. High-risk patients (smokers, diabetics, gum disease history) every 3 to 6 months. The Australian Dental Association recommends biannual visits."),
    ("What happens during a dental check-up?",
     'Comprehensive oral examination, professional scale and clean, fluoride treatment, and X-rays if needed. The dentist checks for decay, gum disease, [oral cancer screening](https://fascinatingdentistry.com/australia/oral-cancer-screening/), and bite problems.'),
    ("Are dental check-ups covered by health insurance?",
     "Yes. Most private health funds cover 1 to 2 check-ups per year under dental extras. Many clinics offer gap-free check-ups where the health fund rebate covers the full cost."),
    ("What is a gap-free dental check-up?",
     "A check-up where the health fund rebate covers the full cost, so you pay nothing out of pocket. Check that your health fund has dental extras cover and that the clinic is a preferred provider."),
    ("Can I get a free dental check-up?",
     "Eligible children aged 0 to 17 receive free check-ups under the CDBS. Some clinics offer free or discounted check-ups for new patients. Public dental clinics offer free check-ups for eligible concession card holders."),
    ("Do dental check-ups include cleaning?",
     'Yes. A standard dental check-up includes a professional scale and clean to remove plaque and tartar build-up, followed by fluoride treatment. [Teeth cleaning](https://fascinatingdentistry.com/australia/teeth-cleaning/) is an essential part of every check-up.'),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/dental-check-up/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Dental check-ups in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Dental Check-Up", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
