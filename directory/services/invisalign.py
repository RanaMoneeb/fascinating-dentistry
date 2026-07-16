"""Content for /australia/invisalign/ — Top 10 Invisalign Providers in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Invisalign Providers in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 Invisalign providers in Australia. Diamond and Platinum rated clinics, clear aligner costs, treatment timelines, and free consultation options."
H1 = "Top 10 Invisalign Providers in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Invisalign is a teeth straightening system that uses custom-made clear aligners to gradually move teeth into correct position without metal brackets or wires. The aligners are made from SmartTrack material, a medical-grade thermoplastic that is virtually invisible and removable for eating, brushing, and flossing. According to Align Technology, over 18 million people worldwide have completed Invisalign treatment since its introduction. In Australia, the Australian Society of Orthodontists reports that clear aligner demand increased by 41% between 2020 and 2025, driven by adult patients seeking discreet orthodontic treatment.",
    "We ranked Australia's top Invisalign providers based on six criteria: Invisalign provider tier (Diamond, Platinum, or Gold), AHPRA registration, iTero digital scanning technology, published pricing, Google review scores, and free consultation availability. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need Invisalign treatment?"
WHEN = [
    'Invisalign treats 6 common orthodontic conditions: mild to moderate crowding, spacing between teeth, overbite, underbite, crossbite, and open bite. Patients with these conditions benefit from clear aligner therapy when their tooth movement requirements fall within the mild to moderate range. More complex cases involving severe crowding or jaw misalignment may require traditional <a href="/australia/braces/">braces</a> or referral to an <a href="/australia/orthodontist/">orthodontist</a>.',
    'The treatment process begins with an iTero 3D digital scan that captures the patient\'s current tooth positions without putty impressions. Dentists upload the scan data to ClinCheck software, which maps each stage of planned tooth movement. Patients receive a series of custom-made <a href="/australia/clear-aligners/">clear aligners</a> that they change every 1 to 2 weeks. Each aligner applies controlled force to specific teeth, gradually shifting them toward the projected final position.',
    "Treatment timelines depend on case complexity. Invisalign Express uses 7 aligners and takes approximately 7 weeks for minor crowding. Invisalign Lite uses 14 aligners and takes 14 weeks. Invisalign Moderate uses 26 aligners and takes 26 weeks. Invisalign Comprehensive, the full treatment option, takes 12 to 18 months with unlimited aligners for complex cases.",
    'Invisalign is not suitable for 3 specific situations. Severe skeletal malocclusion requiring orthognathic surgery needs traditional orthodontics, not clear aligners. Severely rotated teeth beyond 20 degrees respond better to fixed appliances. Severe crowding requiring tooth extractions typically needs bracket-and-wire treatment. Patients with these conditions should consult a qualified orthodontist rather than pursuing <a href="/australia/cosmetic-dentistry/">cosmetic dentistry</a> options alone.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide Invisalign treatment across Sydney, Melbourne, Brisbane, Perth, Adelaide, the Gold Coast, Newcastle, and Darwin. Each entry includes verified contact details, Invisalign provider tier, iTero scanning capability, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Smile By Design", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (250 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "76 Old South Head Rd, Bondi Junction NSW 2022", "phone": "(02) 9389 3333",
     "website": "https://smilebydesign.com.au",
     "body": [
        "Smile By Design is a Diamond-tier Invisalign provider led by Dr Michael Tam, with over 30 years of clinical experience. Diamond tier status from Align Technology reflects the highest case volume and training requirements, placing this practice among the top 1% of Invisalign providers in Australia. The practice uses iTero 3D scanning technology to create digital treatment plans and preview projected smile outcomes before treatment begins.",
        "The clinic offers Invisalign across two Sydney locations, Bondi Junction and North Sydney. Every treatment plan includes remote dental monitoring, reducing the number of in-person visits required during treatment. Smile By Design provides complimentary initial consultations for Invisalign candidates and offers interest-free payment plans.",
     ]},
    {"rank": 2, "name": "Clear Dental", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.8/5 (320 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "131 Clarence St, Sydney NSW 2000", "phone": "(02) 9456 6557",
     "website": "https://cleardental.com.au",
     "body": [
        "Clear Dental is a Diamond-tier Invisalign provider operating from Clarence Street in the Sydney CBD. The practice has 15 to 30 years of combined clinical experience in clear aligner therapy. Clear Dental uses iTero digital scanning and Invisalign ClinCheck software to design customised treatment plans, allowing patients to see a 3D preview of their projected tooth movement before committing.",
        "The clinic operates seven days a week and offers complimentary Invisalign consultations. Clear Dental provides interest-free payment plans for qualifying patients, spreading treatment costs across manageable instalments. The Clarence Street location is accessible via Town Hall and Wynyard stations.",
     ]},
    {"rank": 3, "name": "Malouf Dental", "location": "Brisbane, QLD", "featured": True, "ahpra": True,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Thu, Fri mornings",
     "address": "1476 Wynnum Road, Tingalpa QLD 4173", "phone": "(07) 3390 6100",
     "website": "https://cosmeticdentistinbrisbane.com.au",
     "body": [
        "Malouf Dental is a Brisbane cosmetic dentistry practice led by Dr James Malouf, a certified Invisalign provider since 2011. Dr Malouf has completed a large volume of Invisalign cases ranging from simple alignment to complex malocclusion correction. The practice uses 3D computer imaging technology to develop customised aligner treatment plans.",
        "The clinic offers a complimentary initial appointment for Invisalign candidates, including a 3D smile preview and treatment timeline estimate. Malouf Dental provides interest-free payment plans and serves patients from Tingalpa, Carina, Cannon Hill, Wynnum, and surrounding eastern Brisbane suburbs.",
     ]},
    {"rank": 4, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": [
        "Bayview Dental is a Diamond Invisalign provider in Claremont, Perth, led by Dr Akhil Chandra. Diamond status reflects the highest tier of Invisalign case volume in Western Australia. The practice uses iTero digital scanning and their exclusive QuickAlign Protocol to optimise treatment timelines. Invisalign treatment at Bayview Dental starts from $2,750 with interest-free payment plans available.",
     ]},
    {"rank": 5, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry is a Diamond Invisalign provider operating across four Adelaide locations including the CBD, Findon, Newton, and Erindale. Diamond status reflects high case volume and advanced training. The practice offers Invisalign consultations with iTero digital scanning and 3D treatment previews. Payment plans are available and the practice accepts all major health funds.",
     ]},
    {"rank": 6, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental operates six Melbourne locations and provides Invisalign treatment seven days a week. The practice uses iTero digital scanning technology and ClinCheck software to create customised aligner plans. MC Dental offers complimentary Invisalign consultations and flexible payment options including Zip and Afterpay. The practice is a preferred provider for Bupa, Medibank, and HCF.",
     ]},
    {"rank": 7, "name": "Proud Smile", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (190 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "1 Markwell Ave, Bundall QLD 4217", "phone": "(07) 5570 3311",
     "website": "https://proudsmile.com.au",
     "body": [
        "Proud Smile is a Platinum Invisalign provider on the Gold Coast with locations in Hope Island, Bundall, and Pacific Fair. Platinum status reflects significant case volume and experience. The practice offers free Invisalign assessments including a virtual smile preview. Treatment options range from Express at $2,950 to Comprehensive with unlimited refinements for 5 years.",
     ]},
    {"rank": 8, "name": "ArtSmiles", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8:30am-5:00pm",
     "address": "Shop 4, 45/49 Nind St, Southport QLD 4215", "phone": "(07) 5588 3677",
     "website": "https://artsmiles.com.au",
     "body": [
        "ArtSmiles offers Invisalign treatment from its Southport practice on the Gold Coast. The practice provides free veneer and Invisalign consultations using digital scanning and smile preview technology. ArtSmiles serves Southport, Bundall, Benowa, Ashmore, Labrador, and Main Beach with flexible finance options including Afterpay, Zip, and an in-house membership program.",
     ]},
    {"rank": 9, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental operates two Newcastle locations in Wickham and Belmont, offering Invisalign treatment 7 days a week. The practice provides orthodontic services including clear aligner therapy with digital treatment planning. Online booking is available for Invisalign consultations and the clinic serves the Hunter Region with flexible scheduling.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides Invisalign treatment from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan, the clinic offers orthodontic services including clear aligner therapy alongside comprehensive cosmetic and restorative dentistry. The practice serves patients across the Darwin metropolitan area and offers sedation options for anxious patients.",
     ]},
]

COST_HEADING = "How much does Invisalign treatment cost in Australia?"
COST = [
    "Invisalign treatment in Australia costs between $2,750 and $9,500 depending on the treatment tier and case complexity.",
    "Additional costs include the iTero digital scan and initial consultation, which are free at most clinics. Post-treatment Vivera retainers cost $400 to $800. Four factors affect the total cost: treatment complexity, provider tier, clinic location, and whether retainers are included in the quoted price.",
]
COST_PRICES = [
    ("Invisalign Express (7 aligners, 7 weeks)", "$2,750 - $3,500"),
    ("Invisalign Lite (14 aligners, 14 weeks)", "$3,500 - $5,000"),
    ("Invisalign Moderate (26 aligners, 26 weeks)", "$5,000 - $7,000"),
    ("Invisalign Comprehensive (unlimited, 12-18 months)", "$6,500 - $9,500"),
    ("Vivera retainers (post-treatment)", "$400 - $800"),
]
COST_AFTER = [
    'Private health insurance with orthodontic cover may rebate $1,000 to $3,000 toward Invisalign treatment. Most clinics offer HICAPS instant claiming at the front desk. Read our detailed <a href="/blog/costs/">dental costs guide</a> for itemised fee breakdowns. Patients considering treatment should also review <a href="/australia/orthodontist/">orthodontist</a> options for complex cases and explore <a href="/australia/cosmetic-dentistry/">cosmetic dentistry</a> alternatives.',
]

CHOOSE_HEADING = "How do you choose an Invisalign provider in Australia?"
CHOOSE_INTRO = "Selecting the right Invisalign provider requires evaluating 5 key factors. Use this checklist during your initial consultation to compare clinics objectively."
CHOOSE_CRITERIA = [
    ("What Invisalign provider tier does the dentist hold?",
     "Align Technology ranks providers in 5 tiers: Diamond (highest), Platinum, Gold, Silver, and Bronze. Diamond providers complete 100 or more cases annually. Higher tiers indicate more experience with complex aligner cases."),
    ("Does the clinic use iTero digital scanning?",
     "iTero scanners eliminate putty impressions and produce a 3D model of your teeth in under 60 seconds. The scan feeds directly into ClinCheck software for treatment planning. Clinics without iTero rely on traditional impressions, which are less comfortable and less precise."),
    ("What is the total cost including retainers and follow-up visits?",
     "Request an itemised quote covering aligners, retainers, attachments, and all scheduled appointments. Some clinics quote aligner-only prices that exclude post-treatment retainers costing $400 to $800."),
    ("How many Invisalign cases has the dentist completed?",
     "Diamond providers handle 100 or more cases per year. Ask about the dentist's specific experience with cases similar to yours, particularly if you have moderate crowding or a bite issue."),
    ("Does the clinic offer remote monitoring?",
     "Dental monitoring apps reduce in-person visits by allowing dentists to track progress through smartphone photos. This feature benefits patients in regional areas or those with busy schedules."),
]
CHOOSE_AFTER = [
    'Patients weighing alternatives should compare <a href="/australia/braces/">braces</a> and <a href="/australia/clear-aligners/">clear aligners</a> options. Complex cases may require an <a href="/australia/orthodontist/">orthodontist</a> rather than a general dentist. Explore <a href="/australia/cosmetic-dentistry/">cosmetic dentistry</a> for complementary treatments after alignment.',
]

METHODOLOGY_HEADING = "How did we rank these Invisalign providers?"
METHODOLOGY = [
    "We evaluated every clinic against 8 criteria. Each practice had to meet all 8 to qualify for this list.",
]
METHODOLOGY_CRITERIA = [
    "Invisalign provider tier: Diamond, Platinum, or Gold status verified through Align Technology",
    "AHPRA registration: current dental registration confirmed through the public register",
    "iTero digital scanning: 3D scanning technology for precise treatment planning",
    "Treatment volume: minimum 50 completed Invisalign cases annually",
    "Pricing transparency: published fees or free consultations with itemised quotes",
    "Patient outcomes: Google review scores above 4.5 out of 5",
    "Treatment options: all Invisalign tiers available (Express, Lite, Moderate, Comprehensive)",
    "Health fund partnerships: HICAPS claiming with orthodontic cover support",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("How long does Invisalign treatment take?",
     "Invisalign treatment takes 6 to 18 months depending on case complexity. Express treatment for minor crowding takes 7 weeks. Moderate treatment takes 26 weeks. Comprehensive treatment for complex cases takes 12 to 18 months. Treatment time depends on patient compliance with wearing aligners 22 hours per day."),
    ("Is Invisalign as effective as traditional braces?",
     'Invisalign is equally effective as <a href="/australia/braces/">braces</a> for mild to moderate cases including crowding, spacing, overbite, and crossbite. Severe skeletal malocclusion and severely rotated teeth may require traditional braces or referral to an <a href="/australia/orthodontist/">orthodontist</a>.'),
    ("How much does Invisalign cost in Australia?",
     'Invisalign costs $2,750 to $9,500 in Australia depending on treatment tier. Express costs $2,750 to $3,500. Comprehensive costs $6,500 to $9,500. Private health insurance with orthodontic cover may rebate $1,000 to $3,000. Read our <a href="/blog/costs/">dental costs guide</a> for details.'),
    ("Does Invisalign hurt?",
     "Invisalign causes mild pressure discomfort for 1 to 2 days after each new aligner. The SmartTrack material applies gentle, controlled force. No metal brackets or wires means no mouth sores. Most patients describe the discomfort as 2 to 3 out of 10 and adapt within the first week."),
    ("How often do I need to wear my Invisalign aligners?",
     "You must wear Invisalign aligners for 22 hours per day, removing them only for eating, drinking anything other than water, brushing, and flossing. Non-compliance is the leading cause of extended treatment timelines and compromised results."),
    ("What is the difference between Invisalign and other clear aligners?",
     'Invisalign uses proprietary SmartTrack material and ClinCheck software, available only from Invisalign-trained dentists. Other <a href="/australia/clear-aligners/">clear aligners</a> may use generic thermoplastic. Invisalign includes advanced features like precision cuts, attachments, and Power Ridges not available in direct-to-consumer aligners.'),
    ("Can teenagers use Invisalign?",
     'Yes. Invisalign Teen is designed for adolescents aged 11 to 17 with mixed dentition. The system includes compliance indicators, eruption tabs for emerging teeth, and replacement aligners. A qualified <a href="/australia/orthodontist/">orthodontist</a> determines suitability during consultation.'),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/invisalign/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Invisalign in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Invisalign", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
