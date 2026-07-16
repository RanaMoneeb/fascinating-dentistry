"""Content for /australia/clear-aligners/ — Top 10 Clear Aligner Providers in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Clear Aligner Providers in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 clear aligner providers in Australia. ClearCorrect, Spark, and Invisalign options. Costs, treatment timelines, and free consultations near you."
H1 = "Top 10 Clear Aligner Providers in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Clear aligners are removable orthodontic devices made from transparent medical-grade plastic that gradually move teeth into correct alignment. Unlike traditional metal braces, clear aligners are virtually invisible, comfortable to wear, and can be removed for eating, drinking, brushing, and flossing. The Australian Society of Orthodontists reports that clear aligner treatment has grown by 41% since 2020, with over 100,000 Australians currently using aligner therapy. Multiple brands are available in Australia including Invisalign, ClearCorrect, Spark, and ClearPath, each offering different material properties and treatment protocols.",
    "We ranked Australia's top clear aligner providers based on six criteria: range of aligner systems offered (Invisalign, ClearCorrect, Spark, or multiple brands), AHPRA registration, digital scanning technology, published pricing, Google review scores, and free consultation availability. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need clear aligners?"
WHEN = [
    'Clear aligners treat mild to moderate orthodontic issues including dental crowding, spacing, overbite, underbite, crossbite, open bite, and relapse after previous <a href="/australia/braces/">braces</a>. The system uses a digital scan to design a custom series of plastic trays. Each aligner is worn for 1 to 2 weeks for 22 hours per day to move teeth incrementally into correct alignment. Patients remove the devices to eat, brush, and floss.',
    'Different brands offer unique material properties and software capabilities. <a href="/australia/invisalign/">Invisalign</a> uses SmartTrack material and ClinCheck software to predict tooth movement with high precision. ClearCorrect provides flexible treatment options with highly adaptable plastic. Spark aligners use a highly transparent material that resists staining. An <a href="/australia/orthodontist/">orthodontist</a> or qualified general dentist assesses patient suitability during an initial consultation.',
    'Clear aligners are not suitable for every orthodontic presentation. Patients with severe skeletal discrepancies, severely rotated teeth, or cases requiring surgical extractions often require traditional orthodontic hardware. Complex malocclusion demands fixed appliances to achieve proper structural alignment. Patients with minor cosmetic concerns might also explore <a href="/australia/cosmetic-dentistry/">cosmetic dentistry</a> as an alternative to orthodontic treatment.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide clear aligner treatment across Sydney, Melbourne, Brisbane, Perth, Adelaide, the Gold Coast, Newcastle, and Darwin. Each entry includes verified contact details, aligner systems offered, digital scanning capability, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Smile By Design", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (250 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "76 Old South Head Rd, Bondi Junction NSW 2022", "phone": "(02) 9389 3333",
     "website": "https://smilebydesign.com.au",
     "body": [
        "Smile By Design provides clear aligner treatment using Invisalign and ClearCorrect systems from its Bondi Junction and North Sydney clinics. Led by Dr Michael Tam, the practice holds Diamond-tier status with Align Technology. The practice uses iTero 3D digital scanning to create precise treatment plans and preview projected outcomes before any aligner fabrication begins.",
        "Every treatment plan includes remote dental monitoring, allowing the dental team to track aligner progress through smartphone check-ins. This reduces in-person appointment frequency. Smile By Design offers complimentary initial consultations and interest-free payment plans for clear aligner candidates.",
     ]},
    {"rank": 2, "name": "Clear Dental", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.8/5 (320 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "131 Clarence St, Sydney NSW 2000", "phone": "(02) 9456 6557",
     "website": "https://cleardental.com.au",
     "body": [
        "Clear Dental is a Diamond-tier clear aligner provider operating from Clarence Street in the Sydney CBD. The practice offers Invisalign, ClearCorrect, and Spark aligner systems. Diamond status reflects the highest case volume tier from Align Technology. Clear Dental uses iTero digital scanning and ClinCheck software to design customised aligner treatment plans.",
        "The clinic operates seven days a week and offers complimentary clear aligner consultations. Patients receive a 3D digital preview of projected tooth movement before committing to treatment. Clear Dental provides interest-free payment plans for qualifying patients.",
     ]},
    {"rank": 3, "name": "Malouf Dental", "location": "Brisbane, QLD", "featured": True, "ahpra": True,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Thu, Fri mornings",
     "address": "1476 Wynnum Road, Tingalpa QLD 4173", "phone": "(07) 3390 6100",
     "website": "https://cosmeticdentistinbrisbane.com.au",
     "body": [
        "Malouf Dental provides clear aligner treatment from its Tingalpa practice in Brisbane, led by Dr James Malouf. The practice offers multiple aligner systems including Invisalign and ClearCorrect, with treatment plans customised based on each patient's tooth movement requirements. Dr Malouf has provided clear aligner therapy since 2011.",
        "The clinic offers a complimentary initial appointment for aligner candidates, including a 3D smile preview and treatment timeline estimate. Malouf Dental provides interest-free payment plans and serves patients from Tingalpa, Carina, Cannon Hill, Wynnum, and surrounding eastern Brisbane suburbs.",
     ]},
    {"rank": 4, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental provides ClearCorrect and Invisalign aligner treatment across six Melbourne locations. The practice offers complimentary aligner consultations with iTero digital scanning and 3D treatment previews. MC Dental offers flexible payment options including Zip and Afterpay and is a preferred provider for Bupa, Medibank, and HCF. All locations operate seven days a week.",
     ]},
    {"rank": 5, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": [
        "Bayview Dental is a Diamond clear aligner provider in Claremont, Perth, led by Dr Akhil Chandra. The practice offers Invisalign and ClearCorrect systems with iTero digital scanning technology. Their QuickAlign Protocol optimises treatment timelines for faster results. Clear aligner treatment starts from $2,750 with interest-free payment plans available.",
     ]},
    {"rank": 6, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry is a Diamond clear aligner provider operating across four Adelaide locations. The practice offers Invisalign and ClearCorrect with iTero digital scanning and 3D treatment previews. Diamond status reflects high case volume and advanced training. Payment plans are available and the practice accepts all major health funds.",
     ]},
    {"rank": 7, "name": "Proud Smile", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (190 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "1 Markwell Ave, Bundall QLD 4217", "phone": "(07) 5570 3311",
     "website": "https://proudsmile.com.au",
     "body": [
        "Proud Smile is a Platinum clear aligner provider on the Gold Coast with locations in Hope Island, Bundall, and Pacific Fair. The practice offers Invisalign clear aligner systems with free assessments including a virtual smile preview. Treatment options range from Express at $2,950 to Comprehensive with unlimited refinements for 5 years.",
     ]},
    {"rank": 8, "name": "Hyde Park Dental Care", "location": "Sydney, NSW", "featured": False,
     "rating": "4.7/5 (150 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "Level 2, 325 Liverpool St, Darlinghurst NSW 2010", "phone": "(02) 9358 2155",
     "website": "https://www.hydeparkdentalcare.com.au",
     "body": [
        "Hyde Park Dental Care provides clear aligner treatment from its Darlinghurst practice in Sydney. The practice offers custom clear aligner systems using digital scanning technology to create precise treatment plans. The clinic serves patients from Darlinghurst, Surry Hills, Paddington, Kings Cross, and surrounding inner-Sydney suburbs.",
     ]},
    {"rank": 9, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental operates two Newcastle locations in Wickham and Belmont, offering clear aligner treatment 7 days a week. The practice provides orthodontic services including multiple aligner systems with digital treatment planning. Online booking is available for aligner consultations and the clinic serves the Hunter Region.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides clear aligner treatment from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan, the clinic offers orthodontic services including clear aligner therapy alongside comprehensive cosmetic and restorative dentistry. The practice serves patients across the Darwin metropolitan area.",
     ]},
]

COST_HEADING = "How much does clear aligner treatment cost in Australia?"
COST = [
    "Clear aligner treatment in Australia costs between $2,500 and $9,500 depending on the selected brand and treatment complexity. The largest cost factors include aligner brand, treatment complexity, clinic location, and provider experience.",
    "Additional costs to consider are post-treatment retainers, which cost $400 to $800. Digital scans and initial consultations are free at most clinics. Most dental practices offer interest-free payment plans to spread the cost over 12 to 24 months. Always request an itemised quote before committing.",
]
COST_PRICES = [
    ("ClearCorrect (full treatment)", "$2,500 - $6,000"),
    ("Spark aligners (full treatment)", "$3,000 - $7,000"),
    ("Invisalign Express (minor)", "$2,750 - $3,500"),
    ("Invisalign Comprehensive (full)", "$6,500 - $9,500"),
    ("Post-treatment retainers", "$400 - $800"),
]
COST_AFTER = [
    'Private health insurance with orthodontic cover may provide a rebate of $1,000 to $3,000. Review our complete <a href="/blog/costs/">dental costs guide</a> to understand all associated fees. Compare specific treatment systems by visiting our pages for <a href="/australia/invisalign/">Invisalign</a> and traditional <a href="/australia/braces/">braces</a>.',
]

CHOOSE_HEADING = "How do you choose a clear aligner provider in Australia?"
CHOOSE_INTRO = "To choose a clear aligner provider in Australia, evaluate 5 key criteria to ensure you receive safe and effective treatment."
CHOOSE_CRITERIA = [
    ("Which aligner brands does the clinic offer?",
     'A practice offering multiple systems like <a href="/australia/invisalign/">Invisalign</a>, ClearCorrect, and Spark provides greater flexibility to match the material to your specific clinical needs.'),
    ("Does the clinic use digital scanning?",
     "Clinics using iTero or equivalent intraoral scanners provide precise treatment planning without messy putty moulds."),
    ("What is the total cost including retainers?",
     "Always request an itemised quote that details the full expenditure, ensuring no hidden fees arise at the end of your treatment."),
    ("How many aligner cases has the dentist completed?",
     'Experienced providers manage tooth movement more predictably. Case volume directly correlates with clinical expertise in <a href="/australia/braces/">braces</a> and aligner therapy.'),
    ("Does the clinic offer free consultations?",
     "Utilising free initial appointments allows you to compare recommendations and pricing from different practices before making a financial commitment."),
]
CHOOSE_AFTER = [
    'For complex structural issues, always verify if the provider is a specialist <a href="/australia/orthodontist/">orthodontist</a>. General dentists can provide aligner therapy, but severe malocclusion requires specialist intervention. Patients seeking aesthetic improvements alongside alignment should verify the provider\'s experience in <a href="/australia/cosmetic-dentistry/">cosmetic dentistry</a>.',
]

METHODOLOGY_HEADING = "How did we rank these clear aligner providers?"
METHODOLOGY = [
    "We ranked these clear aligner providers using 8 objective criteria to ensure clinical quality and patient safety. Every practice on this list meets a minimum standard of care and technological capability.",
]
METHODOLOGY_CRITERIA = [
    "Aligner systems offered: Invisalign, ClearCorrect, Spark, or multiple brands",
    "Provider tier status with aligner manufacturers indicating high case volume",
    "AHPRA registration verified for every practising dentist",
    "Digital scanning technology using iTero or equivalent intraoral scanners",
    "Treatment volume with a minimum of 50 cases completed annually",
    "Pricing transparency with published fees or free consultations",
    "Patient outcomes demonstrated by Google review scores above 4.5",
    "Health fund partnerships with HICAPS claiming for instant rebates",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read <a href="/methodology/">our methodology</a> to understand our full evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is the difference between clear aligners and Invisalign?",
     'Invisalign is a specific brand of clear aligner made by Align Technology using SmartTrack material and ClinCheck software. Clear aligners is the general category that includes <a href="/australia/invisalign/">Invisalign</a>, ClearCorrect, Spark, and other brands. Invisalign is the most clinically researched system.'),
    ("Are clear aligners as effective as braces?",
     'Clear aligners are equally effective as <a href="/australia/braces/">braces</a> for mild to moderate crowding, spacing, overbite, and crossbite. Severe skeletal malocclusion or severely rotated teeth may require traditional braces. Consult an <a href="/australia/orthodontist/">orthodontist</a> for complex cases.'),
    ("How much do clear aligners cost in Australia?",
     'Clear aligners cost $2,500 to $9,500 depending on the brand and treatment complexity. ClearCorrect costs $2,500 to $6,000. Invisalign costs $2,750 to $9,500. Read our <a href="/blog/costs/">dental costs guide</a> for details.'),
    ("How long do clear aligners take to work?",
     "Clear aligner treatment takes 6 to 18 months depending on case complexity. Minor crowding resolves in 7 to 14 weeks. Moderate cases take 26 weeks. Complex full-arch treatment takes 12 to 18 months with 22 hours daily wear."),
    ("Can I eat with clear aligners in?",
     "No. You must remove clear aligners before eating or drinking anything other than water. Eating with aligners in damages the plastic and introduces food particles. You should brush your teeth before reinserting aligners after meals."),
    ("Do clear aligners hurt?",
     "Clear aligners cause mild pressure discomfort for 1 to 2 days after inserting each new aligner. The transparent plastic applies gentle force without metal brackets or wires. No mouth sores occur. Most patients adapt within the first week of treatment."),
    ("What happens after clear aligner treatment?",
     "After clear aligner treatment, you must wear retainers to prevent teeth from shifting back. Retainers are worn full-time for 3 to 6 months, then nightly. Vivera retainers cost $400 to $800. Without retainers, teeth will relapse within months."),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/clear-aligners/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Clear aligners in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Clear Aligners", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
