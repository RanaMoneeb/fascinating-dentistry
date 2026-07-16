"""Content for /australia/gum-disease-treatment/ — Top 10 Gum Disease Treatment Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Gum Disease Treatment Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 gum disease treatment clinics in Australia. Scaling, root planing, periodontal surgery, and maintenance care. Verified clinics near you."
H1 = "Top 10 Gum Disease Treatment Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Gum disease, also called periodontal disease, is a bacterial infection of the gums and supporting structures of the teeth. It ranges from gingivitis (early-stage inflammation) to periodontitis (advanced infection causing bone loss and tooth mobility). The Australian Institute of Health and Welfare reports that 28.8% of Australian adults have some form of periodontitis, with prevalence increasing to over 50% among adults aged 65 and over. Without treatment, periodontitis leads to tooth loss and has been linked to cardiovascular disease, diabetes complications, and adverse pregnancy outcomes.",
    "We ranked Australia's top gum disease treatment clinics based on six criteria: periodontal treatment capability (scaling, root planing, surgical treatment), AHPRA registration, digital diagnostic technology, published pricing, Google review scores, and maintenance programme availability. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need gum disease treatment?"
WHEN = [
    "Gum disease treatment is required when a bacterial infection damages the gum tissue and bone supporting your teeth. The disease progresses through two stages: gingivitis (early-stage inflammation that is reversible) and periodontitis (irreversible destruction of bone and connective tissue). The Australian Research Centre for Population Oral Health reports that approximately 22.9% of Australians aged 15 and over have moderate or severe periodontitis.",
    "The signs indicating the need for treatment include bleeding gums during brushing, red and swollen gum tissue, persistent bad breath, receding gum lines exposing tooth roots, loose or shifting teeth, and periodontal pockets deeper than 4 millimetres. Risk factors include smoking, poorly managed diabetes, inadequate oral hygiene, genetic predisposition, and chronic stress. The ADA identifies smoking cessation as the single most effective modifiable risk factor.",
    'Treatment options depend on disease severity. Professional <a href="/australia/teeth-cleaning/">teeth cleaning</a> removes plaque and calculus above the gum line. Scaling and root planing, also called deep cleaning, removes bacteria from root surfaces below the gum line. Advanced cases require referral to a specialist <a href="/australia/periodontist/">periodontist</a> for surgical intervention, <a href="/australia/gum-graft-surgery/">gum graft surgery</a> to restore receded tissue, or <a href="/australia/lanap/">LANAP</a> laser therapy.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide gum disease treatment across Sydney, Melbourne, Brisbane, Perth, Adelaide, the Gold Coast, Newcastle, and Darwin. Each entry includes verified contact details, periodontal treatment capabilities, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Sydney Periodontists", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8am-5pm",
     "address": "Suite 12, Level 3, Park House, 187 Macquarie Street, Sydney NSW 2000", "phone": "(02) 8552 0300",
     "website": "https://sydneyperiodontists.com.au",
     "body": [
        "Sydney Periodontists is a specialist periodontal practice led by Dr Vijay Tumuluri offering scaling and root planing, periodontal surgery, gum grafting, and dental implants. The practice operates from two locations in Sydney CBD and Parramatta. Dr Tumuluri holds specialist registration in periodontics with AHPRA.",
        "The practice accepts referrals from general dentists and self-referrals. Health fund processing is available on-site with HICAPS claiming. Research-backed treatment techniques ensure evidence-based periodontal care for all stages of gum disease.",
     ]},
    {"rank": 2, "name": "Perth Periodontics", "location": "Perth, WA", "featured": True, "ahpra": True,
     "rating": "4.8/5 (120 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "Suite 9, 38 Meadowvale Avenue, South Perth WA 6151", "phone": "(08) 9474 4444",
     "website": "https://perthperio.com.au",
     "body": [
        "Perth Periodontics is a specialist practice founded by Dr Lucy De Jesus in 2002. The practice provides comprehensive periodontal treatment including non-surgical treatment, surgical periodontal treatment, regenerative surgeries, crown lengthening, and mucogingival surgery (gum grafts).",
        "The practice is known for its compassionate approach to anxious patients and complex medical histories. Perth Periodontics collaborates with general dentists and medical practitioners for integrated care.",
     ]},
    {"rank": 3, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": True, "ahpra": True,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry provides periodontal services across four Adelaide locations. The practice offers scaling and root planing, periodontal maintenance, gum grafting, and implant placement with iTero digital scanning. All major health funds accepted with HICAPS on-the-spot claiming.",
        "Payment plans are available for periodontal treatment. The practice accepts both dentist referrals and self-referrals from across the Adelaide metropolitan area.",
     ]},
    {"rank": 4, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental provides gum disease treatment including scaling and root planing, periodontal maintenance, and gum disease management across six Melbourne locations. The practice offers flexible payment options including Zip and Afterpay and is a preferred provider for Bupa, Medibank, and HCF. All locations operate seven days a week.",
     ]},
    {"rank": 5, "name": "Malouf Dental", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Thu, Fri mornings",
     "address": "1476 Wynnum Road, Tingalpa QLD 4173", "phone": "(07) 3390 6100",
     "website": "https://cosmeticdentistinbrisbane.com.au",
     "body": [
        "Malouf Dental provides gum disease treatment from its Tingalpa practice in Brisbane. The practice offers scaling and root planing, periodontal maintenance, and gum disease management. The clinic offers complimentary initial appointments and interest-free payment plans.",
     ]},
    {"rank": 6, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": [
        "Bayview Dental provides gum disease treatment from its Claremont practice in Perth. The practice offers scaling, root planing, and periodontal maintenance with iTero digital scanning technology. Interest-free payment plans are available.",
     ]},
    {"rank": 7, "name": "Proud Smile", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (190 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "1 Markwell Ave, Bundall QLD 4217", "phone": "(07) 5570 3311",
     "website": "https://proudsmile.com.au",
     "body": [
        "Proud Smile provides gum disease treatment on the Gold Coast with locations in Hope Island, Bundall, and Pacific Fair. The practice offers periodontal maintenance, scaling, root planing, and preventive care. Free assessments and flexible payment plans are available.",
     ]},
    {"rank": 8, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental provides gum disease treatment from two Newcastle locations. The practice offers scaling, root planing, and periodontal maintenance with digital diagnostic technology. Online booking is available and the clinic serves the Hunter Region 7 days a week.",
     ]},
    {"rank": 9, "name": "ArtSmiles", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8:30am-5:00pm",
     "address": "Shop 4, 45/49 Nind St, Southport QLD 4215", "phone": "(07) 5588 3677",
     "website": "https://artsmiles.com.au",
     "body": [
        "ArtSmiles provides gum disease management from its Southport practice on the Gold Coast. The practice offers scaling, root planing, and periodontal maintenance using digital scanning technology. Flexible finance options including Afterpay and Zip are available.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides gum disease treatment from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan, the clinic offers scaling, root planing, periodontal maintenance, and complex restorative care. Sedation dentistry is available for anxious patients.",
     ]},
]

COST_HEADING = "How much does gum disease treatment cost in Australia?"
COST = [
    "Gum disease treatment in Australia costs between $150 and $8,000 depending on the severity of disease and the type of treatment required. Early-stage gingivitis treatment is significantly less expensive than advanced periodontitis management.",
    "Private health insurance with major dental cover provides rebates that vary by fund. Periodontal maintenance visits are typically required every 3 to 6 months after active treatment to prevent disease recurrence.",
]
COST_PRICES = [
    ("Professional cleaning (scale and clean)", "$150 - $300"),
    ("Scaling and root planing (per quadrant)", "$250 - $500"),
    ("Periodontal maintenance cleaning", "$180 - $350"),
    ("Antibiotic therapy (per site)", "$50 - $200"),
    ("Periodontal surgery (per quadrant)", "$1,500 - $3,500"),
    ("LANAP laser treatment (full mouth)", "$4,000 - $8,000"),
]
COST_AFTER = [
    'Most practices offer interest-free payment plans for periodontal treatment. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. Learn more about <a href="/australia/periodontist/">periodontist fees</a> and <a href="/australia/lanap/">LANAP costs</a>.',
]

CHOOSE_HEADING = "How do you choose a gum disease treatment clinic in Australia?"
CHOOSE_INTRO = "Selecting the right gum disease treatment clinic requires evaluating their periodontal capabilities and maintenance programme. Ask these 5 questions during your consultation."
CHOOSE_CRITERIA = [
    ("Does the clinic offer comprehensive periodontal treatment?",
     "The practice should provide scaling, root planing, and surgical periodontal treatment. Clinics that only offer basic cleaning may not manage advanced periodontitis effectively."),
    ("Is there a periodontist on staff or available for referral?",
     'A <a href="/australia/periodontist/">periodontist</a> is a specialist in gum disease treatment. Complex cases require specialist intervention. Ask whether the clinic has a periodontist or refers to one.'),
    ("What is the maintenance schedule after active treatment?",
     "Periodontal maintenance visits every 3 to 6 months are essential after active treatment. Confirm the clinic offers ongoing maintenance and not just one-time treatment."),
    ("Does the clinic use digital diagnostic technology?",
     "Digital X-rays, periodontal probing, and intraoral scanning improve diagnostic accuracy and allow precise tracking of disease progression over time."),
    ("Are payment plans available?",
     "Gum disease treatment can involve multiple visits over months. Confirm the clinic offers interest-free payment plans and accepts your health fund with HICAPS claiming."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these gum disease treatment clinics?"
METHODOLOGY = [
    "We evaluated dental practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "Periodontal treatment capability including non-surgical and surgical options",
    "AHPRA registration verified for all treating practitioners",
    "Digital diagnostic technology including digital X-rays and intraoral scanning",
    "Periodontal maintenance programme availability",
    "Treatment volume and documented clinical experience",
    "Pricing transparency with published fees or itemised quotes",
    "Patient outcomes: Google review scores above 4.5",
    "Payment plan availability and health fund partnerships",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is gum disease?",
     "Gum disease is a bacterial infection of the gums progressing from gingivitis (reversible inflammation) to periodontitis (irreversible bone loss). The AIHW reports 28.8% of Australian adults have periodontitis. Risk factors include smoking, diabetes, and poor oral hygiene."),
    ("How do I know if I have gum disease?",
     'Bleeding gums on brushing, red swollen gums, persistent bad breath, receding gums, loose teeth, and deep pockets over 4mm are key signs. Your dentist detects periodontitis during routine <a href="/australia/teeth-cleaning/">teeth cleaning</a> appointments.'),
    ("How much does gum disease treatment cost?",
     'Professional cleaning costs $150 to $300. Scaling and root planing costs $250 to $500 per quadrant. Periodontal surgery costs $1,500 to $3,500 per quadrant. Read our <a href="/blog/costs/">dental costs guide</a> for details.'),
    ("Is gum disease treatment painful?",
     "Scaling and root planing are performed under local anaesthetic. Most patients feel pressure but no pain. Mild sensitivity lasts 2 to 3 days. Surgical treatment requires 1 to 2 days recovery."),
    ("Can gum disease be cured?",
     'Gingivitis is reversible with professional cleaning and improved oral hygiene. Periodontitis is not reversible but can be controlled with specialist <a href="/australia/periodontist/">periodontist</a> treatment to stop disease progression and prevent tooth loss.'),
    ("How often should I have periodontal maintenance?",
     "Periodontal maintenance visits every 3 to 6 months are essential after active treatment. Your dentist or periodontist determines the interval based on your disease severity, risk factors, and home care compliance."),
    ("What happens if gum disease is left untreated?",
     "Untreated periodontitis causes progressive bone loss, gum recession, tooth mobility, and eventual tooth loss. Research links untreated periodontitis to increased risk of cardiovascular disease, diabetes complications, and respiratory infections."),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/gum-disease-treatment/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Gum disease treatment in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Gum Disease Treatment", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
