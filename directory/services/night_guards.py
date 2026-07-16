"""Content for /australia/night-guards/ — Top 10 Night Guard Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Night Guard Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 night guard clinics in Australia. Custom occlusal splints for bruxism, teeth grinding, and clenching. Verified clinics near you."
H1 = "Top 10 Night Guard Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "A night guard, also called an occlusal splint or bite splint, is a custom-made dental appliance worn during sleep to protect teeth from the damaging effects of bruxism (teeth grinding and clenching). Bruxism affects approximately 8% of Australian adults according to the Australian Sleep Health Foundation, causing tooth wear, fractures, jaw pain, headaches, and temporomandibular joint dysfunction. A custom night guard creates a protective barrier between upper and lower teeth, distributing grinding forces evenly.",
    "We ranked Australia's top night guard clinics based on six criteria: custom occlusal splint fabrication, range of splint types (hard, soft, dual-laminate), TMJ treatment capability, AHPRA registration, published pricing, and Google review scores. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need a night guard?"
WHEN = [
    'Bruxism is the involuntary grinding or clenching of teeth during sleep. Signs you may need a night guard include morning headaches, jaw pain or stiffness, worn or chipped teeth, increased tooth sensitivity, a partner reporting grinding sounds during sleep, earaches, and [TMJ](https://fascinatingdentistry.com/australia/tmj-treatment/) clicking or popping.',
    "Common causes of bruxism include stress and anxiety, sleep apnoea, misaligned bite (malocclusion), excessive caffeine or alcohol consumption, and certain medications. The Australian Sleep Health Foundation reports that stress-related bruxism has increased significantly since 2020.",
    "There are 3 main types of night guards. Hard acrylic splints are the most durable and effective for severe grinding. Soft night guards are comfortable and suitable for mild clenching. Dual-laminate splints have a hard outer surface for durability and a soft inner surface for comfort. Your dentist recommends the best type based on your grinding pattern.",
    'A night guard prevents tooth fracture and excessive wear, protects existing dental work such as [crowns](https://fascinatingdentistry.com/australia/crowns/) and implants, reduces jaw muscle tension, and minimises morning headaches. Schedule a [dental check-up](https://fascinatingdentistry.com/australia/dental-check-up/) if you suspect bruxism. A night guard differs from a [sports mouthguard](https://fascinatingdentistry.com/australia/sports-mouthguards/) which is designed for daytime impact protection.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide custom night guards and occlusal splints across Sydney, Melbourne, Brisbane, Perth, Adelaide, Newcastle, and Darwin. Each entry includes verified contact details, splint pricing, and services sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Pure Dentistry", "location": "Brisbane, QLD", "featured": True, "ahpra": True,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 11, The Village Shopping Centre, 1932-1974 Logan Road, Upper Mount Gravatt QLD 4122", "phone": "(07) 3343 4880",
     "website": "https://www.puredentistry.com.au",
     "body": [
        "Pure Dentistry provides personally fitted night guards and occlusal splints for teeth grinding and bruxism. The practice fabricates custom guards from dental impressions for precise fit and comfort. Open 7 days a week at The Village Shopping Centre in Upper Mount Gravatt with free parking.",
     ]},
    {"rank": 2, "name": "Dr Zenaidy Castro", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 1, 6-10 Albert Road, Melbourne VIC 3004", "phone": "(03) 9690 1888",
     "website": "https://www.drzenaidycastro.com.au",
     "body": [
        "Dr Zenaidy Castro provides dental night guards, oral appliances, and oral splints for teeth grinding, clenching, and bruxism in Melbourne CBD. The practice offers comprehensive night grinding solutions including assessment, custom splint fabrication, and ongoing adjustment.",
     ]},
    {"rank": 3, "name": "Sydney Dental Surgeons", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (210 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Suite 1003, Level 10, 135 Macquarie Street, Sydney NSW 2000", "phone": "(02) 9221 1530",
     "website": "https://www.sydneydentalsurgeons.com.au",
     "body": [
        "Sydney Dental Surgeons provides custom-fitted night guards for bruxism protection and TMJ management. With nearly 40 years of experience, the practice fabricates occlusal splints from precise dental impressions. Macquarie Street location in the Sydney CBD.",
     ]},
    {"rank": 4, "name": "Perth Prime Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.8/5 (130 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "8/6 St Georges Terrace, Perth WA 6000", "phone": "(08) 9225 4488",
     "website": "https://perthprimedental.com.au",
     "body": [
        "Perth Prime Dental provides custom night guards, occlusal splints, and bite splints for bruxism and teeth grinding. The practice offers comprehensive assessment for grinding patterns and TMJ symptoms.",
     ]},
    {"rank": 5, "name": "Medindie Dental Care", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (110 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "138 Main North Road, Medindie SA 5081", "phone": "(08) 8267 1111",
     "website": "https://www.medindiedental.com.au",
     "body": [
        "Medindie Dental Care provides custom night guards and splints for bruxism, jaw pain, and teeth grinding. The practice offers TMJ therapies alongside occlusal splint fabrication.",
     ]},
    {"rank": 6, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental provides custom occlusal splints for teeth grinding across six Melbourne locations. Preferred provider for Bupa, Medibank, and HCF. Open 7 days a week.",
     ]},
    {"rank": 7, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": [
        "Bayview Dental provides custom night guards for bruxism protection with iTero digital scanning technology. Interest-free payment plans available.",
     ]},
    {"rank": 8, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry provides custom night guards and TMJ therapies across four Adelaide locations. All major health funds accepted with HICAPS on-the-spot claiming.",
     ]},
    {"rank": 9, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental provides custom night guards and occlusal splints from two Newcastle locations. Online booking available 7 days a week.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides custom night guards for bruxism from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan. Sedation options available for anxious patients.",
     ]},
]

COST_HEADING = "How much does a custom night guard cost in Australia?"
COST = [
    "A custom night guard costs between $300 and $900 in Australia depending on the type of splint and material. Hard acrylic occlusal splints are the most expensive but most durable for severe grinding. Soft guards are more affordable but need more frequent replacement.",
]
COST_PRICES = [
    ("Soft night guard", "$300 - $500"),
    ("Hard acrylic occlusal splint", "$500 - $900"),
    ("Dual-laminate splint (hard/soft)", "$450 - $750"),
    ("Consultation", "Free - $150"),
]
COST_AFTER = [
    'Some private health funds cover custom night guards under dental extras (item numbers 971 or 973). Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. Learn more about <a href="/australia/tmj-treatment/">TMJ treatment</a> costs.',
]

CHOOSE_HEADING = "How do you choose a night guard clinic in Australia?"
CHOOSE_INTRO = "Selecting the right night guard clinic ensures your splint fits properly and effectively protects your teeth. Ask these 5 questions."
CHOOSE_CRITERIA = [
    ("Does the clinic custom-fabricate occlusal splints from dental impressions?",
     "Custom night guards require dental impressions and laboratory fabrication. Avoid clinics offering over-the-counter boil-and-bite options for bruxism as these provide inadequate protection."),
    ("What types of splints do they offer?",
     "Look for clinics offering hard acrylic, soft, and dual-laminate options. Different grinding patterns require different splint materials for optimal protection."),
    ("Do they assess TMJ function alongside splint fabrication?",
     'Bruxism and TMJ dysfunction often coexist. A comprehensive clinic should assess jaw joint function and offer <a href="/australia/tmj-treatment/">TMJ treatment</a> alongside night guard fabrication.'),
    ("Do they provide ongoing adjustment of the splint?",
     "Night guards may need adjustment as your bite adapts. Confirm the clinic includes follow-up adjustments in the initial price."),
    ("Are they experienced with sleep apnoea screening?",
     "Bruxism is sometimes linked to sleep apnoea. Clinics experienced in sleep-disordered breathing can identify when a night guard alone is insufficient."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these night guard clinics?"
METHODOLOGY = [
    "We evaluated dental practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "Custom occlusal splint fabrication from dental impressions",
    "Range of splint types offered (hard, soft, dual-laminate)",
    "TMJ assessment and treatment capability",
    "AHPRA registration verified for all treating practitioners",
    "Experience managing bruxism and related conditions",
    "Pricing transparency with published fees",
    "Patient outcomes: Google review scores above 4.5",
    "Follow-up adjustment included in treatment fee",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("How much does a night guard cost?",
     'Custom night guards cost $300 to $900 depending on type. Hard acrylic splints cost $500 to $900. Soft guards cost $300 to $500. Read our <a href="/blog/costs/">dental costs guide</a>.'),
    ("How do I know if I grind my teeth?",
     'Morning headaches, jaw pain, worn teeth, and partner reports of grinding sounds are key signs. Your dentist checks for wear patterns during a <a href="/australia/dental-check-up/">dental check-up</a>.'),
    ("What is the difference between a night guard and a sports mouthguard?",
     'Night guards are worn during sleep to prevent bruxism damage. <a href="/australia/sports-mouthguards/">Sports mouthguards</a> protect during physical activity. They are made from different materials for different purposes.'),
    ("Can a night guard cure bruxism?",
     'A night guard does not cure bruxism but prevents tooth damage and reduces symptoms. Stress management, <a href="/australia/tmj-treatment/">TMJ treatment</a>, and treating sleep apnoea may address the underlying cause.'),
    ("How long does a night guard last?",
     "2 to 5 years for hard acrylic splints. 1 to 2 years for soft guards. Replace if cracked, loose, or excessively worn. Severe grinders may need replacement more frequently."),
    ("Is a night guard comfortable to wear?",
     "Yes. Custom-fitted night guards are comfortable and most patients adapt within 1 to 2 weeks. Over-the-counter boil-and-bite options are less comfortable and less effective."),
    ("Does health insurance cover night guards?",
     "Some private health funds cover custom night guards under dental extras. Check your policy for item numbers 971 or 973. HICAPS claiming available at most dental clinics."),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/night-guards/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Night guards in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Night Guards", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
