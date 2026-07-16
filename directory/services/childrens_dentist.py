"""Content for /australia/childrens-dentist/ — Top 10 Children's Dentists in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Children's Dentists in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 children's dentists in Australia. CDBS bulk billing, family-friendly clinics, kids dental check-ups, fluoride, and fissure sealants. Verified clinics near you."
H1 = "Top 10 Children's Dentists in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "A children's dentist provides dental care specifically tailored to infants, children, and adolescents in a family-friendly environment. While any general dentist can treat children, practices that focus on children's dentistry invest in child-friendly facilities, experienced staff, and preventive programmes designed for young patients. The Australian Institute of Health and Welfare reports that 34% of Australian children aged 5 to 6 have experienced decay in their primary teeth. The Child Dental Benefits Schedule (CDBS) provides up to $1,095 over 2 years for eligible children aged 0 to 17, covering check-ups, cleaning, fillings, fissure sealants, and extractions.",
    "We ranked Australia's top children's dentists based on six criteria: CDBS bulk billing availability, child-friendly facilities and approach, range of children's dental services, AHPRA registration, published pricing, and Google review scores. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need a children's dentist?"
WHEN = [
    'A children\'s dentist provides preventive care, restorative treatment, early orthodontic assessment, habit counselling, and trauma management for young patients. The Australian Dental Association recommends the first dental visit by age 1 or when the first tooth erupts, followed by check-ups every 6 to 12 months.',
    'The Child Dental Benefits Schedule (CDBS) provides up to $1,095 over 2 calendar years for eligible children aged 0 to 17. The scheme covers basic dental services including examinations, [teeth cleaning](https://fascinatingdentistry.com/australia/teeth-cleaning/), [fillings](https://fascinatingdentistry.com/australia/fillings/), fissure sealants, extractions, and root canals. Many practices bulk bill under the CDBS, meaning eligible families pay nothing.',
    'There is a difference between a children\'s dentist (a general dentist who treats children) and a [paediatric dentist](https://fascinatingdentistry.com/australia/pediatric-dentist/) (a specialist with 3 years of postgraduate training). Most children can be treated by a general children\'s dentist. Complex cases involving severe anxiety, special needs, or extensive treatment may require referral to a specialist paediatric dentist.',
    'Children\'s dental services include fluoride treatment to strengthen enamel, fissure sealants to prevent decay in molars, restorative fillings for cavities, stainless steel crowns for severely decayed teeth, dietary counselling, and habit counselling for thumb sucking and dummy use. Early [dental check-ups](https://fascinatingdentistry.com/australia/dental-check-up/) establish good oral health habits that last a lifetime.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide children's dental care across Sydney, Melbourne, Brisbane, Perth, Adelaide, Newcastle, and Darwin. Each entry includes verified contact details, CDBS bulk billing status, services offered, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "No Gaps Dental", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.8/5 (650 reviews)", "pricing": "Budget (CDBS bulk billed)", "hours": "Mon-Sat",
     "address": "Level 2, 283 George Street, Sydney NSW 2000", "phone": "(02) 8383 1400",
     "website": "https://www.nogapsdental.com",
     "body": [
        "No Gaps Dental has provided affordable children's dentistry across 18 Sydney locations for over 20 years. The practice bulk bills under the CDBS, meaning eligible families pay nothing for children's dental treatment.",
        "Services include check-ups, cleaning, fluoride treatment, fissure sealants, fillings, and emergency dental care. The team is trained to help all children including neurodivergent and special needs patients feel at ease.",
     ]},
    {"rank": 2, "name": "Dental 99", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.7/5 (1,200 reviews)", "pricing": "Budget (CDBS bulk billed)", "hours": "7 days",
     "address": "Ground Floor, 11 Epping Road, Macquarie Park NSW 2113", "phone": "1300 655 022",
     "website": "https://dental99.com.au",
     "body": [
        "Dental 99 is a bulk bill dental practice operating across Sydney, Brisbane, and Melbourne. The practice handles CDBS claims automatically through their app, meaning eligible families pay nothing and do not need to claim from Medicare separately.",
        "Locations include Bondi Junction, Epping, Mango Hill, Marayong, Monash, Moorebank, and Sydney CBD. The practice provides comprehensive children's dental care including check-ups, cleaning, fillings, and preventive treatments.",
     ]},
    {"rank": 3, "name": "Dental on Flinders", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.8/5 (350 reviews)", "pricing": "Budget (CDBS 100% bulk billed)", "hours": "7 days",
     "address": "Level 2, 270 Flinders Street, Melbourne VIC 3000", "phone": "(03) 9639 9911",
     "website": "https://www.dentalonflinders.com.au",
     "body": [
        "Dental on Flinders bulk bills 100% of eligible CDBS claims for children aged 2 to 17 with no gap fees. The practice provides evidence-based children's dentistry in a contemporary Melbourne CBD setting, open 7 days including after-hours appointments.",
     ]},
    {"rank": 4, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Budget (CDBS bulk billed)", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental provides CDBS bulk billing across six Melbourne locations. Services include check-ups, cleaning, fluoride, fissure sealants, and fillings. Open 7 days a week at all locations.",
     ]},
    {"rank": 5, "name": "JC Dental Como", "location": "Perth, WA", "featured": False,
     "rating": "4.8/5 (180 reviews)", "pricing": "Budget (CDBS bulk billed)", "hours": "Mon-Sat",
     "address": "Suite 3, 2 Downey Drive, Como WA 6152", "phone": "(08) 9106 9195",
     "website": "https://jcdental.com.au",
     "body": [
        "JC Dental Como provides children's dentistry with CDBS bulk billing. The practice offers preventive care, fluoride treatment, fissure sealants, and fillings for children. Mandarin-speaking dental team available.",
     ]},
    {"rank": 6, "name": "Prime Children's Dental Care", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (250 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "2/85 Broadhurst Drive, Joondalup WA 6027", "phone": "(08) 9300 0600",
     "website": "https://www.primecdc.com.au",
     "body": [
        "Prime Children's Dental Care has provided children's dental services in Perth for over 35 years. The all-female team provides preventive dental, restorative procedures, sedation, trauma management, and care for children with additional needs. Two locations in Joondalup and Wembley.",
     ]},
    {"rank": 7, "name": "Adelaide Children's Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, emergency available",
     "address": "165 Unley Road, Unley SA 5061", "phone": "(08) 8271 9597",
     "website": "https://www.acdentistry.com.au",
     "body": [
        "Adelaide Children's Dentistry is led by Dr Wendy Cheung, a specialist paediatric dentist. The practice provides specialist dental care, general dental care, emergency dental care, happy gas, general anaesthesia, and treatment for children with special needs.",
     ]},
    {"rank": 8, "name": "The Little Happy Tooth Co", "location": "Adelaide, SA", "featured": False,
     "rating": "4.9/5 (100 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "70 Kensington Road, Rose Park SA 5067", "phone": "(08) 8363 2000",
     "website": "https://www.littlehappytooth.com.au",
     "body": [
        "The Little Happy Tooth Co is a children's dental practice exclusively for kids, adolescents, and those with special needs. The team of experienced oral health therapists provides quality care in a child-friendly environment.",
     ]},
    {"rank": 9, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range (CDBS available)", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental provides children's dental services from two Newcastle locations. The practice offers check-ups, cleaning, and preventive care with CDBS bulk billing. Online booking is available 7 days a week.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides children's dental treatment from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan, the clinic offers preventive care and restorative treatment. Sedation options available for anxious children.",
     ]},
]

COST_HEADING = "How much does children's dental treatment cost in Australia?"
COST = [
    "Children's dental treatment is free for eligible families under the Child Dental Benefits Schedule (CDBS), which provides up to $1,095 over 2 calendar years. Many practices bulk bill under the CDBS with no gap fee.",
    "For families not eligible for the CDBS, private fees apply. The CDBS covers examinations, cleaning, fillings, fissure sealants, extractions, and root canals. It does not cover orthodontic or cosmetic treatment.",
]
COST_PRICES = [
    ("CDBS eligible (bulk billed)", "$0 out of pocket"),
    ("Routine check-up and clean (private)", "$80 - $250"),
    ("Fluoride treatment", "$30 - $60"),
    ("Fissure sealants (per tooth)", "$45 - $90"),
    ("Fillings (per tooth)", "$150 - $300"),
    ("Emergency consultation", "$100 - $200"),
]
COST_AFTER = [
    'Check your child\'s CDBS eligibility through Medicare online, Express Plus app, or by calling 132 011. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. For specialist cases, see our <a href="/australia/pediatric-dentist/">paediatric dentist</a> directory.',
]

CHOOSE_HEADING = "How do you choose a children's dentist in Australia?"
CHOOSE_INTRO = "Selecting the right children's dentist involves finding a practice that makes dental visits positive and affordable. Ask these 5 questions."
CHOOSE_CRITERIA = [
    ("Does the clinic bulk bill under the CDBS?",
     "Confirm the practice bulk bills eligible CDBS claims with no gap fee. This saves up to $1,095 per child over 2 years."),
    ("Is the practice child-friendly?",
     "Look for play areas, child-sized dental chairs, staff experienced in paediatric communication, and a welcoming environment that puts children at ease."),
    ("What services do they offer for children?",
     "The practice should offer check-ups, cleaning, fluoride, fissure sealants, fillings, and emergency care. Some also provide orthodontic assessment."),
    ("Do they have experience with anxious or special needs children?",
     "Children with autism, anxiety, or developmental delays need practitioners experienced in adapting their approach. Ask about their experience and patience."),
    ("Are they conveniently located with flexible hours?",
     "Look for practices open after school hours and on weekends. Multiple locations reduce travel time for busy families."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these children's dentists?"
METHODOLOGY = [
    "We evaluated dental practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "CDBS bulk billing availability with no gap fee",
    "Child-friendly facilities and appropriately sized equipment",
    "Range of children's dental services offered",
    "AHPRA registration verified for all treating practitioners",
    "Documented experience treating anxious and special needs children",
    "Pricing transparency with published fees or free consultations",
    "Patient outcomes: Google review scores above 4.5",
    "Accessibility including weekend and after-school appointments",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is a children's dentist?",
     'A general dentist who provides dental care for children in a family-friendly environment. For complex cases requiring specialist care, see a <a href="/australia/pediatric-dentist/">paediatric dentist</a> who has completed 3 years of specialist training.'),
    ("When should my child first visit the dentist?",
     'By age 1 or when the first tooth erupts. Early visits are mostly educational and help your child feel comfortable. Book a <a href="/australia/dental-check-up/">dental check-up</a>.'),
    ("Is children's dental treatment free in Australia?",
     "Under the CDBS, eligible children aged 0 to 17 receive up to $1,095 over 2 years. Many clinics bulk bill with no out-of-pocket cost. Check eligibility by calling Medicare on 132 011."),
    ("How often should children see the dentist?",
     'Every 6 to 12 months depending on cavity risk. High-risk children may need visits every 3 months. Regular <a href="/australia/teeth-cleaning/">teeth cleaning</a> prevents most problems.'),
    ("What is the CDBS?",
     "Medicare's Child Dental Benefits Schedule provides up to $1,095 over 2 calendar years for basic dental services for eligible children aged 0 to 17. Covers check-ups, cleaning, fillings, fissure sealants, and extractions."),
    ("How do I know if my child is eligible for CDBS?",
     "Check eligibility through your Medicare online account, Express Plus Medicare app, or call Medicare on 132 011. Eligibility is means-tested based on family payments."),
    ("What if my child is scared of the dentist?",
     'Choose a child-friendly practice experienced with anxious children. Techniques include tell-show-do, happy gas (nitrous oxide), and gradual desensitisation. For severe anxiety, a specialist <a href="/australia/pediatric-dentist/">paediatric dentist</a> can provide sedation.'),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/childrens-dentist/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Children's dentists in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Children's Dentist", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
