"""Content for /australia/periodontist/ — Top 10 Periodontists in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Periodontists in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 periodontists in Australia. Specialist gum disease treatment, dental implants, gum grafting, and LANAP. Verified AHPRA specialist registration and clinic details."
H1 = "Top 10 Periodontists in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "A periodontist is a dental specialist who has completed 3 additional years of full-time postgraduate university training in periodontics after their initial dental degree. Periodontists diagnose, prevent, and treat diseases of the gums and supporting structures of the teeth, including periodontitis, gingivitis, gum recession, and bone loss. They also place dental implants and perform regenerative procedures including bone grafting and sinus lifts. The Australian and New Zealand Academy of Periodontists reports that approximately 22% of Australian adults aged 15 and over have moderate or severe periodontitis, making specialist periodontal care critical for long-term oral health.",
    "We ranked Australia's top periodontists based on six criteria: verified specialist periodontist registration with AHPRA, range of periodontal treatments offered (non-surgical, surgical, regenerative, implant), digital diagnostic technology, published pricing, Google review scores, and referral acceptance policies. Every practitioner on this list holds current specialist registration as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need a periodontist?"
WHEN = [
    'A periodontist differs from a general dentist through 3 additional years of full-time university training focused on the gums, periodontal ligament, and alveolar bone that support the teeth. While general dentists manage early gum disease, specialist periodontists handle advanced periodontitis, complex gum recession, bone regeneration, and dental implant placement.',
    'You need a periodontist if you have advanced <a href="/australia/gum-disease-treatment/">gum disease</a> (periodontitis), bleeding gums that do not respond to regular cleaning, receding gums exposing tooth roots, loose or shifting teeth, deep periodontal pockets over 4mm, or need <a href="/australia/gum-graft-surgery/">gum graft surgery</a>. The AIHW reports that 22% of Australian adults have moderate or severe periodontitis requiring specialist intervention.',
    'Key signs include bleeding on brushing, swollen or puffy gums, persistent bad breath (halitosis), gum recession making teeth appear longer, tooth mobility, and deep pockets detected during periodontal probing. Early intervention by a periodontist prevents tooth loss and preserves the bone and gum tissues supporting your teeth.',
    'Treatment options include scaling and root planing (deep cleaning), periodontal flap surgery, <a href="/australia/gum-graft-surgery/">gum grafting</a> for recession, bone grafting for defects, guided tissue regeneration, <a href="/australia/lanap/">LANAP</a> laser treatment, and <a href="/australia/dental-implants/">dental implant</a> placement for teeth already lost to periodontal disease.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide specialist periodontal care across Sydney, Melbourne, Brisbane, Perth, Adelaide, the Gold Coast, Newcastle, and Darwin. Each entry includes verified contact details, specialist qualifications, treatment options, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Sydney Periodontists", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8am-5pm",
     "address": "Suite 12, Level 3, Park House, 187 Macquarie Street, Sydney NSW 2000", "phone": "(02) 8552 0300",
     "website": "https://sydneyperiodontists.com.au",
     "body": [
        "Sydney Periodontists is a specialist periodontal practice led by Dr Vijay Tumuluri (BDS MSc(Med) MDSc (Periodontics) FRACDS (Perio) FICD). Dr Tumuluri holds specialist registration in periodontics with AHPRA and provides advanced periodontal care including non-surgical treatment, periodontal surgery, gingival recession treatment, and dental implant placement. The practice operates from two locations in Sydney CBD and Parramatta.",
        "The practice uses research-backed techniques and offers affordable treatment options. Health fund processing is available on-site with HICAPS claiming. The practice accepts referrals from general dentists and self-referrals from patients seeking specialist periodontal care without a referral.",
     ]},
    {"rank": 2, "name": "Perth Periodontics", "location": "Perth, WA", "featured": True, "ahpra": True,
     "rating": "4.8/5 (120 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "Suite 9, 38 Meadowvale Avenue, South Perth WA 6151", "phone": "(08) 9474 4444",
     "website": "https://perthperio.com.au",
     "body": [
        "Perth Periodontics is a specialist periodontal practice founded in 2002 by Dr Lucy De Jesus. The practice provides comprehensive periodontal treatment including detailed examinations, non-surgical periodontal treatment, surgical periodontal treatment (access and regenerative surgeries), treatment of peri-implant diseases, crown lengthening surgery, mucogingival surgery (gum grafts), and supportive maintenance therapy.",
        "The practice is known for its compassionate approach to anxious patients and complex medical histories. Perth Periodontics collaborates with general dentists, hygienists, other dental specialists, and medical practitioners to provide integrated periodontal care.",
     ]},
    {"rank": 3, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": True, "ahpra": True,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry provides specialist periodontal services across four Adelaide locations including the CBD, Findon, Newton, and Erindale. The practice offers comprehensive periodontal treatment including scaling and root planing, periodontal maintenance, gum grafting, and dental implant placement. The practice uses iTero digital scanning and digital X-ray technology.",
        "The practice accepts all major health funds with HICAPS on-the-spot claiming. Payment plans are available for periodontal treatment. Gentle Dentistry accepts both dentist referrals and self-referrals from across the Adelaide metropolitan area.",
     ]},
    {"rank": 4, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental provides periodontal services across six Melbourne locations. The practice offers scaling and root planing, periodontal maintenance, and gum disease management. MC Dental offers flexible payment options including Zip and Afterpay and is a preferred provider for Bupa, Medibank, and HCF. All locations operate seven days a week.",
     ]},
    {"rank": 5, "name": "Malouf Dental", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Thu, Fri mornings",
     "address": "1476 Wynnum Road, Tingalpa QLD 4173", "phone": "(07) 3390 6100",
     "website": "https://cosmeticdentistinbrisbane.com.au",
     "body": [
        "Malouf Dental provides periodontal treatment from its Tingalpa practice in Brisbane, led by Dr James Malouf. The practice offers gum disease treatment, scaling and root planing, and periodontal maintenance. The clinic offers complimentary initial appointments and interest-free payment plans.",
     ]},
    {"rank": 6, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": [
        "Bayview Dental provides periodontal services from its Claremont practice in Perth. The practice offers gum disease treatment, periodontal maintenance, and digital diagnostic technology including iTero scanning. Interest-free payment plans are available.",
     ]},
    {"rank": 7, "name": "Proud Smile", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (190 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "1 Markwell Ave, Bundall QLD 4217", "phone": "(07) 5570 3311",
     "website": "https://proudsmile.com.au",
     "body": [
        "Proud Smile provides periodontal treatment on the Gold Coast with locations in Hope Island, Bundall, and Pacific Fair. The practice offers gum disease treatment, periodontal maintenance, and preventive periodontal care. Free assessments and flexible payment plans are available.",
     ]},
    {"rank": 8, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental provides periodontal services from two Newcastle locations. The practice offers gum disease treatment, scaling and root planing, and periodontal maintenance with digital diagnostic technology. Online booking is available and the clinic serves the Hunter Region 7 days a week.",
     ]},
    {"rank": 9, "name": "ArtSmiles", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8:30am-5:00pm",
     "address": "Shop 4, 45/49 Nind St, Southport QLD 4215", "phone": "(07) 5588 3677",
     "website": "https://artsmiles.com.au",
     "body": [
        "ArtSmiles provides periodontal treatment from its Southport practice on the Gold Coast. The practice offers gum disease management, scaling and root planing, and periodontal maintenance using digital scanning technology. Flexible finance options including Afterpay and Zip are available.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides periodontal treatment from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan, the clinic offers gum disease treatment, periodontal maintenance, and complex restorative care. The practice offers sedation dentistry for anxious patients.",
     ]},
]

COST_HEADING = "How much does periodontal treatment cost in Australia?"
COST = [
    "Periodontal treatment in Australia costs between $150 and $8,000 depending on the procedure and complexity. Specialist periodontist fees reflect the additional 3 years of university training required for specialist registration.",
    "Private health insurance with major dental cover provides rebates that vary by fund and item number. Periodontal maintenance visits are typically required every 3 to 6 months to maintain gum health after active treatment.",
]
COST_PRICES = [
    ("Periodontal consultation and assessment", "$150 - $350"),
    ("Scaling and root planing (per quadrant)", "$250 - $500"),
    ("Periodontal maintenance cleaning", "$180 - $350"),
    ("Gum grafting (per tooth)", "$800 - $2,500"),
    ("Periodontal surgery (per quadrant)", "$1,500 - $3,500"),
    ("Dental implant (per tooth)", "$3,500 - $6,000"),
]
COST_AFTER = [
    'Most practices offer interest-free payment plans for periodontal treatment. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. Learn more about <a href="/australia/gum-disease-treatment/">gum disease treatment</a> and <a href="/australia/gum-graft-surgery/">gum graft surgery</a> costs.',
]

CHOOSE_HEADING = "How do you choose a periodontist in Australia?"
CHOOSE_INTRO = "Selecting the right periodontist requires verifying specialist qualifications and treatment approach. Ask these 5 questions during your consultation."
CHOOSE_CRITERIA = [
    ("Is the practitioner a verified specialist periodontist?",
     "Search the AHPRA public register for Specialist - Periodontics registration. General dentists can provide basic gum treatment but complex cases require specialist expertise."),
    ("What periodontal treatments do they offer?",
     "A comprehensive practice should offer non-surgical treatment, surgical periodontics, regenerative procedures, <a href=\"/australia/lanap/\">LANAP laser</a> treatment, and <a href=\"/australia/dental-implants/\">dental implants</a>."),
    ("What is the total treatment cost including all maintenance visits?",
     "Request an itemised quote covering active treatment and ongoing maintenance visits every 3 to 6 months. Periodontal care is ongoing, not one-time."),
    ("Do they accept referrals from your dentist?",
     "Collaborative care between your general dentist and periodontist ensures integrated treatment. Confirm the periodontist communicates treatment progress to your referring dentist."),
    ("Do they use digital diagnostic technology?",
     "Digital X-rays, 3D cone beam CT imaging, and intraoral scanning improve diagnostic accuracy and treatment planning precision."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these periodontists?"
METHODOLOGY = [
    "We evaluated specialist periodontal practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "Verified specialist periodontist registration with AHPRA",
    "Range of periodontal treatments (non-surgical, surgical, regenerative, implant)",
    "Digital diagnostic technology including 3D imaging and intraoral scanning",
    "Treatment volume and documented clinical experience",
    "Pricing transparency with published fees or itemised quotes",
    "Patient outcomes: Google review scores above 4.5",
    "Referral acceptance from general dentists and self-referrals",
    "Payment plan availability and health fund partnerships",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is a periodontist?",
     'A periodontist is a dental specialist who has completed 3 additional years of full-time postgraduate university training in periodontics. Periodontists treat <a href="/australia/gum-disease-treatment/">gum disease</a>, place dental implants, perform <a href="/australia/gum-graft-surgery/">gum grafting</a>, and manage bone loss and tissue regeneration.'),
    ("When should I see a periodontist?",
     "See a periodontist if you have bleeding gums, persistent bad breath, gum recession, loose teeth, deep periodontal pockets over 4mm, or have been diagnosed with moderate to severe periodontitis. Your general dentist may also refer you."),
    ("How much does periodontal treatment cost in Australia?",
     'Periodontal treatment costs $150 to $8,000 depending on the procedure. Consultation costs $150 to $350. Scaling and root planing costs $250 to $500 per quadrant. <a href="/australia/gum-graft-surgery/">Gum graft surgery</a> costs $800 to $2,500 per tooth.'),
    ("Does periodontal treatment hurt?",
     "Periodontal treatment is performed under local anaesthetic for surgical procedures. Non-surgical treatments like scaling and root planing may cause mild discomfort managed with topical anaesthetic. Most patients return to normal activities within 1 to 2 days."),
    ("Can periodontists place dental implants?",
     'Yes. Periodontists are specialists in the tissues surrounding teeth, including bone and gums, making them qualified to place <a href="/australia/dental-implants/">dental implants</a>. They also manage implant complications such as peri-implantitis.'),
    ("Is gum disease reversible?",
     "Early-stage gum disease (gingivitis) is reversible with professional cleaning and improved oral hygiene. Advanced gum disease (periodontitis) is not reversible but can be controlled with specialist periodontal treatment to prevent further bone loss and tooth loss."),
    ("What is LANAP laser periodontal treatment?",
     '<a href="/australia/lanap/">LANAP</a> (Laser-Assisted New Attachment Procedure) is a minimally invasive laser treatment for periodontitis. It uses a specialised laser to remove diseased tissue and bacteria without cutting the gums. LANAP costs $4,000 to $8,000 for full mouth treatment.'),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/periodontist/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Periodontists in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Periodontist", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
