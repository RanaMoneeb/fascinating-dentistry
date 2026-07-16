"""Content for /australia/orthodontist/ — Top 10 Orthodontists in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Orthodontists in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 orthodontists in Australia. Specialist orthodontists for braces, Invisalign, and complex bite correction. Verified AHPRA specialist registration and clinic details."
H1 = "Top 10 Orthodontists in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "An orthodontist is a dental specialist who has completed a 3-year full-time postgraduate university degree in orthodontics after their initial 5-year dental degree. Orthodontists diagnose, prevent, and treat dental and facial irregularities including crooked teeth, misaligned jaws, overbites, underbites, crossbites, and overcrowding. The Australian Society of Orthodontists reports that only 5% of Australian dentists have completed the additional training required to register as specialist orthodontists with AHPRA. Treatment options provided by orthodontists include metal braces, ceramic braces, lingual braces, clear aligners, and functional appliances for jaw modification.",
    "We ranked Australia's top orthodontists based on six criteria: verified specialist orthodontist registration with AHPRA, membership with the Australian Society of Orthodontists, range of treatment options (braces, aligners, functional appliances, surgical orthodontics), digital treatment planning technology, published pricing, and verified patient review scores. Every practitioner on this list holds current specialist registration as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need an orthodontist?"
WHEN = [
    'An orthodontist differs from a general dentist through 3 additional years of full-time university training focused exclusively on tooth and jaw alignment. While general dentists can provide basic orthodontic treatment, specialist orthodontists handle complex malocclusion, jaw discrepancies, surgical orthodontics, and multi-disciplinary cases requiring comprehensive treatment planning.',
    'Patients need an orthodontist when they have malocclusion, overbite, underbite, crossbite, open bite, severe crowding, spacing, impacted teeth, or jaw discrepancies. The Australian Society of Orthodontists recommends children have their first orthodontic assessment at age 7 to 8, when the mix of baby and adult teeth reveals developing alignment issues. Early intervention can guide jaw growth and prevent more complex treatment later.',
    'Treatment options provided by orthodontists include <a href="/australia/braces/">braces</a> (metal, ceramic, lingual, self-ligating), <a href="/australia/invisalign/">Invisalign</a> and <a href="/australia/clear-aligners/">clear aligners</a>, functional appliances (Twin Block, Herbst, expansion plates) for jaw modification in growing children, and surgical orthodontics for severe skeletal discrepancies. Treatment choice depends on the specific diagnosis, patient age, and treatment goals.',
    'Adults increasingly seek orthodontic treatment for both functional and aesthetic reasons. The Australian Society of Orthodontists reports adult treatment has grown 15% annually since 2020. Adult patients may combine orthodontic treatment with <a href="/australia/cosmetic-dentistry/">cosmetic dentistry</a> procedures for comprehensive smile rehabilitation.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices are led by or staffed with specialist orthodontists who hold verified AHPRA specialist registration across Sydney, Melbourne, Brisbane, Perth, Adelaide, the Gold Coast, Newcastle, and Darwin. Each entry includes verified contact details, specialist qualifications, treatment options, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "OrthoBoutique", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "5.0/5 (312 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 1, 155 Castlereagh Street, Sydney NSW 2000", "phone": "(02) 8076 3788",
     "website": "https://orthoboutique.com.au",
     "body": [
        "OrthoBoutique is a specialist orthodontic practice in the Sydney CBD led by a registered specialist orthodontist who has completed 3 years of full-time postgraduate orthodontic training. The practice offers metal braces, ceramic braces, lingual braces, clear aligners by Invisalign and Spark, early intervention for children, and surgical orthodontics. OrthoBoutique uses SureSmile 3D digital planning technology.",
        "The practice holds a 5.0 Google rating from 312 reviews, making it one of the highest-rated orthodontic practices in Sydney. Treatment services cover all age groups from early childhood intervention through adult orthodontics. OrthoBoutique provides complimentary initial consultations and interest-free payment plans.",
     ]},
    {"rank": 2, "name": "Full Face Orthodontics", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (380 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "100 Bligh Street, Sydney NSW 2000", "phone": "(02) 9221 5333",
     "website": "https://www.fullfaceorthodontics.com.au",
     "body": [
        "Full Face Orthodontics is led by Dr Derek Mahony, a registered specialist orthodontist (AHPRA: DEN0001223757) with a special interest in dentofacial orthopaedics. The practice operates across multiple Australian cities including Sydney, Melbourne, Brisbane, Perth, and Hobart. Dr Mahony has trained thousands of dentists worldwide in orthodontic techniques.",
        "The practice treats children, teenagers, and adults using functional appliances, braces, Invisalign aligners, and surgical orthodontics. Full Face Orthodontics emphasises early intervention for children with jaw development issues and provides treatment for sleep-related breathing disorders related to jaw position.",
     ]},
    {"rank": 3, "name": "Mount Lawley Orthodontics", "location": "Perth, WA", "featured": True, "ahpra": True,
     "rating": "4.9/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "695 Beaufort Street, Mount Lawley WA 6050", "phone": "(08) 9371 6088",
     "website": "https://www.mountlawleyorthodontics.com.au",
     "body": [
        "Mount Lawley Orthodontics is staffed by 5 specialist orthodontists who have each completed 5-year dental degrees plus 3-year postgraduate orthodontic specialisation. Established in 2000, the practice offers braces, Invisalign, removable appliances, and surgical orthodontics for children and adults. All practitioners hold current AHPRA specialist registration.",
        "The clinic treats complex cases including orthognathic surgery preparation, early intervention for children, and adult rehabilitation. Mount Lawley Orthodontics uses digital scanning and 3D treatment planning technology. Payment plans are available with no interest.",
     ]},
    {"rank": 4, "name": "Orthodontics Sydney Wide (OSW Group)", "location": "Sydney, NSW", "featured": False,
     "rating": "4.9/5 (450 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "1/287 Penant Hills Rd, Carlingford NSW 2118", "phone": "(02) 9871 0011",
     "website": "https://oswgroup.com.au",
     "body": [
        "Orthodontics Sydney Wide has 50 years of experience with specialist orthodontists across multiple Sydney locations. The practice provides metal braces, ceramic braces, self-ligating Damon braces, and Invisalign. All orthodontists hold ASO membership and AHPRA specialist registration. Free initial consultations and interest-free payment plans are available at all locations.",
     ]},
    {"rank": 5, "name": "Solas Orthodontics", "location": "Perth, WA", "featured": False,
     "rating": "5.0/5 (150 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "168 Vahland Ave, Salter Point WA 6152", "phone": "(08) 9474 5083",
     "website": "https://solasorthodontics.com.au",
     "body": [
        "Solas Orthodontics is a specialist orthodontic practice in Perth led by Dr Richard Gargett, a registered specialist orthodontist. The practice offers metal braces, ceramic braces, lingual braces, and Invisalign aligners for children, teens, and adults. Solas uses digital scanning technology and 3D treatment planning for precise results.",
     ]},
    {"rank": 6, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry provides orthodontic services across four Adelaide locations including metal braces, ceramic braces, Invisalign, and ClearCorrect aligners. The practice offers iTero digital scanning and customised orthodontic treatment plans for children, teens, and adults. Payment plans are available and the practice accepts all major health funds.",
     ]},
    {"rank": 7, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental provides orthodontic services including braces and clear aligners across six Melbourne locations. The practice offers complimentary orthodontic consultations with digital scanning and treatment planning. MC Dental offers flexible payment options including Zip and Afterpay and is a preferred provider for Bupa, Medibank, and HCF.",
     ]},
    {"rank": 8, "name": "ArtSmiles", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8:30am-5:00pm",
     "address": "Shop 4, 45/49 Nind St, Southport QLD 4215", "phone": "(07) 5588 3677",
     "website": "https://artsmiles.com.au",
     "body": [
        "ArtSmiles provides orthodontic treatment from its Southport practice on the Gold Coast. The practice offers metal braces, ceramic braces, and clear aligner options using digital scanning technology. ArtSmiles serves Southport, Bundall, Benowa, Ashmore, Labrador, and Main Beach with flexible finance options.",
     ]},
    {"rank": 9, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental provides orthodontic services from two Newcastle locations. The practice offers comprehensive orthodontic treatment including braces and clear aligners with digital treatment planning. Online booking is available for orthodontic consultations and the clinic serves the Hunter Region 7 days a week.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides orthodontic services from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan, the clinic offers orthodontic treatment including braces and clear aligner therapy. The practice handles complex orthodontic and restorative cases and offers sedation dentistry for anxious patients.",
     ]},
]

COST_HEADING = "How much does orthodontic treatment cost in Australia?"
COST = [
    "Orthodontic treatment in Australia costs between $6,000 and $15,000 depending on the treatment type, complexity, and provider qualifications. Specialist orthodontist fees are higher than general dentists due to the additional 3 years of university training required for specialist registration.",
    "Private health insurance with orthodontic cover typically rebates $1,000 to $3,000 toward treatment. Most funds impose a 12-month waiting period for orthodontic claims. Confirm your annual limits and item numbers with your fund before starting treatment.",
]
COST_PRICES = [
    ("Orthodontic consultation", "Free - $300"),
    ("Metal braces (18-30 months)", "$6,000 - $9,000"),
    ("Ceramic braces", "$6,500 - $9,500"),
    ("Lingual braces (hidden)", "$9,500 - $15,000"),
    ("Invisalign Comprehensive", "$6,500 - $9,500"),
    ("Functional appliances (Twin Block, Herbst)", "$2,500 - $5,000"),
]
COST_AFTER = [
    'Most practices listed above offer interest-free payment plans. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. Compare with <a href="/australia/braces/">braces costs</a> and <a href="/australia/invisalign/">Invisalign pricing</a> for alternative options.',
]

CHOOSE_HEADING = "How do you choose an orthodontist in Australia?"
CHOOSE_INTRO = "Selecting the right orthodontist requires verifying their specialist qualifications and treatment approach. Ask these 5 questions during your initial consultation."
CHOOSE_CRITERIA = [
    ("Is the practitioner a verified specialist orthodontist?",
     "Search the AHPRA public register for specialist registration in orthodontics. General dentists who offer braces do not have specialist status. The Australian Society of Orthodontists also maintains a directory of verified specialist orthodontists."),
    ("Are they a member of the Australian Society of Orthodontists?",
     "ASO membership requires verified specialist orthodontic qualifications. Members commit to continuing education and ethical practice standards set by the peak professional body."),
    ("What treatment options do they offer?",
     "A qualified orthodontist should offer multiple treatment options including braces, aligners, functional appliances, and surgical orthodontics. Limited options may indicate narrow expertise."),
    ("What is the total treatment cost including all appointments?",
     "Request an itemised quote covering the full treatment including all adjustments, retainers, and emergency visits. Confirm the quote includes post-treatment retention."),
    ("Do they use digital scanning technology?",
     "Digital scanners replace uncomfortable putty impressions and improve treatment planning accuracy. Clinics investing in current technology tend to deliver more precise and efficient treatment."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these orthodontists?"
METHODOLOGY = [
    "We evaluated specialist orthodontic practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "Verified specialist orthodontist registration with AHPRA",
    "Australian Society of Orthodontists membership",
    "Range of treatment options (braces, aligners, functional appliances, surgery)",
    "Digital treatment planning technology including 3D scanning",
    "Treatment volume and documented clinical experience",
    "Pricing transparency with published fees or free consultations",
    "Patient outcomes: Google review scores above 4.5",
    "Payment plan availability and health fund partnerships",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is the difference between a dentist and an orthodontist?",
     'An orthodontist is a dental specialist who has completed 3 additional years of full-time university training in orthodontics after their 5-year dental degree. Only 5% of Australian dentists hold this specialist qualification. Orthodontists focus exclusively on tooth and jaw alignment using <a href="/australia/braces/">braces</a>, aligners, and surgical orthodontics.'),
    ("When should my child first see an orthodontist?",
     "The Australian Society of Orthodontists recommends the first orthodontic assessment at age 7 to 8. Early assessment identifies jaw growth issues, crossbites, and crowding before they become complex. Not all children need early treatment, but monitoring allows timely intervention if needed."),
    ("How much does an orthodontist cost in Australia?",
     'Orthodontic treatment costs $6,000 to $15,000 depending on treatment type and complexity. Initial consultations are free at most specialist practices. Private health insurance with orthodontic cover rebates $1,000 to $3,000. Read our <a href="/blog/costs/">dental costs guide</a> for details.'),
    ("Can adults see an orthodontist?",
     'Yes. Adult orthodontics is the fastest-growing segment in Australian orthodontics. Adults can choose <a href="/australia/invisalign/">Invisalign</a>, ceramic braces, or lingual braces for discreet treatment. Adult treatment takes 18 to 30 months.'),
    ("How do I verify if my orthodontist is a specialist?",
     "Search the AHPRA public register online. A specialist orthodontist will have Dental (Specialist - Orthodontics) listed as their registration type. General dentists who offer braces will only have general dental registration without specialist status."),
    ("How long does orthodontic treatment take?",
     "Comprehensive orthodontic treatment takes 18 to 30 months. Mild cases resolve in 12 to 18 months. Complex cases requiring extractions, jaw modification, or surgical orthodontics take 24 to 36 months. Treatment duration depends on case complexity, patient compliance, and biological response."),
    ("Do orthodontists treat sleep apnoea?",
     "Some orthodontists treat mild to moderate sleep apnoea related to jaw position using functional appliances that reposition the lower jaw forward. Severe sleep apnoea requires medical assessment by a sleep physician. Consultation with a specialist orthodontist determines suitability for appliance-based treatment."),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/orthodontist/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Orthodontists in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Orthodontist", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
