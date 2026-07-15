"""Content for /australia/dental-fillings/ — Top 10 Dental Filling Clinics in Australia.
Transcribed from Drive markdown (July 2026).

Interface contract (shared by all directory.services.* modules, rendered by
directory/templates/directory/service_listicle_page.html):
  Section paragraphs / FAQ answers may contain inline HTML (<strong>, <a href>).
  Render them through the |live_links filter so links to not-yet-live pages are
  neutralised (no dead links). All outbound practice links are nofollow.

CONTENT RULE: Never include "(future page)" or similar bracketed markers in text.
Only use <a href> for links. Dead links auto-unwrap to plain text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "10 Best Dental Filling Clinics in Australia - Ranked"
META_DESC = "Compare Australia's top 10 dental filling clinics by ratings, costs, filling materials, and locations. Find the right tooth filling clinic near you."
H1 = "Top 10 Dental Filling Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Dental fillings restore teeth damaged by decay or minor fractures. The dentist removes the decayed portion, cleans the cavity, and fills the space with a restorative material such as composite resin, amalgam, or glass ionomer cement. Without intervention, decay penetrates deeper tooth layers and progresses toward the nerve chamber, causing pain, infection, and eventual tooth loss.",
    "We ranked these 10 dental filling clinics across Australia based on 6 criteria: dentist qualifications, AHPRA registration, Google review volume (minimum 50 reviews at 4.0 stars or higher), material options (composite, amalgam, and GIC), pricing transparency, and same-day availability. Every clinic on this list was verified in July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need a dental filling?"
WHEN = [
    "You need a dental filling when tooth decay creates a cavity, when an existing filling wears down, or when a tooth chips or cracks from biting pressure or grinding. Tooth decay is the most common reason. Bacteria in dental plaque produce acids that dissolve tooth enamel. The enamel breaks down over months and forms a cavity that reaches the softer dentine layer beneath.",
    "Dentists recommend fillings for 4 main reasons. Cavities from tooth decay account for the majority of filling procedures. The Australian Institute of Health and Welfare reports that Australian adults aged 15 and over have an average of 12.8 decayed, missing, or filled teeth. Worn fillings lose their marginal seal over time, with amalgam fillings lasting 10 to 15 years and composite fillings lasting 5 to 10 years. Chipped or cracked teeth expose the inner dentine to bacteria. Tooth surface wear from grinding (bruxism) thins the enamel and creates concave areas that trap plaque, with chronic night grinders losing up to 1mm of enamel per decade.",
    'Untreated cavities grow progressively larger. Decay that reaches the pulp chamber requires root canal treatment costing $1,000 to $3,000, or extraction costing $200 to $500. A filling completed at the cavity stage costs $100 to $500 and preserves the natural tooth structure. Learn more about <a href="/blog/conditions/">dental conditions caused by untreated decay</a> and <a href="/blog/treatments/">treatment options for damaged teeth</a>.',
]
WHEN_ALERT = "Patients experiencing severe facial swelling affecting breathing or swallowing, high fever combined with dental pain, or spreading infection should attend a hospital emergency department immediately."

WHO_TOP10 = "These 10 clinics represent the best dental filling services across Australia based on dentist qualifications, patient reviews, material options, pricing, and appointment availability. Each clinic offers composite and amalgam fillings with same-day or next-day appointments."

TOP10 = [
    {"rank": 1, "name": "MC Dental Melbourne Central", "location": "Melbourne, VIC", "featured": True,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8971",
     "website": "https://www.mcdental.com.au/", "ahpra": True,
     "body": [
        "MC Dental Melbourne Central holds a 4.8-star rating from 2,197 Google reviews, the highest review volume on this list. The clinic operates 7 days a week and offers composite and amalgam fillings with same-day appointments.",
        "The clinical team includes bilingual dentists who speak Mandarin, Vietnamese, and Cantonese. MC Dental accepts all major health funds including Bupa, HCF, and Medibank with on-the-spot HICAPS claiming. The practice publishes transparent pricing for filling procedures using standard ADA item numbers.",
     ]},
    {"rank": 2, "name": "Smile Concepts", "location": "Sydney, NSW", "featured": True,
     "rating": "4.8/5 (667 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 403, Level 4, 307 Pitt St, Sydney NSW 2000", "phone": "(02) 9267 7777",
     "website": "https://www.smileconcepts.com.au/", "ahpra": True,
     "body": [
        "Smile Concepts maintains a 4.8-star rating from 667 Google reviews. The practice operates 7 days a week from its Sydney CBD location near Town Hall station. Smile Concepts places tooth-coloured composite fillings with same-day service.",
        "The clinic charges no after-hours surcharge for weekend or evening appointments. All dentists hold current AHPRA registration and provide itemised quotes before treatment begins. Free underground parking is available for patients.",
     ]},
    {"rank": 3, "name": "Pure Dentistry", "location": "Brisbane, QLD", "featured": True,
     "rating": "4.6/5 (330 reviews)", "pricing": "Mid-range", "hours": "7 days including public holidays",
     "address": "11/1932-1974 Logan Road, Upper Mt Gravatt QLD 4122", "phone": "(07) 3343 4869",
     "website": "https://www.puredentistry.com.au/", "ahpra": True,
     "body": [
        "Pure Dentistry carries a 4.6-star rating from 330 Google reviews and holds QIP accreditation. The clinic operates 7 days a week including public holidays and offers composite fillings with IV sedation for patients with dental anxiety.",
        "The practice provides same-day appointments and accepts health fund benefits through HICAPS. The phone line operates from 5am to 11pm daily for urgent booking enquiries. All dentists hold current AHPRA registration.",
     ]},
    {"rank": 4, "name": "United Dental Care", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact for current ratings", "pricing": "Mid-range", "hours": "7 days including public holidays",
     "address": "Suite 5/377 Sussex St, Sydney NSW 2000", "phone": "(02) 9267 7174",
     "website": "https://www.uniteddentalcare.com.au/",
     "body": [
        "United Dental Care operates across 2 Sydney locations with 7-day availability. The practice is open 363 days a year, closing only on Christmas Day and New Year's Day. The team places composite fillings and provides general restorative dentistry.",
        "All dentists hold current AHPRA registration. The clinic offers transparent pricing with itemised quotes and accepts major health funds through HICAPS claiming on-site.",
     ]},
    {"rank": 5, "name": "Clear Dental", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact for current ratings", "pricing": "Mid-range", "hours": "Open 7 days",
     "address": "131 Clarence St, Sydney NSW 2000", "phone": "(02) 9456 6557",
     "website": "https://www.cleardental.com.au/",
     "body": [
        "Clear Dental runs 5 locations across Sydney, with the flagship practice on Clarence Street placing tooth-coloured fillings 7 days a week. The clinical team uses digital scanning for precise filling margins.",
        "All dentists hold current AHPRA registration. Weekend availability suits patients who cannot attend weekday appointments. The practice provides itemised quotes before treatment and accepts all major health funds.",
     ]},
    {"rank": 6, "name": "Dental on Flinders", "location": "Melbourne, VIC", "featured": False,
     "rating": "Contact for current ratings", "pricing": "Mid-range", "hours": "Monday to Saturday",
     "address": "Level 5, 276 Flinders St, Melbourne VIC 3000", "phone": "(03) 9041 0049",
     "website": "https://www.dentalonflinders.com.au/",
     "body": [
        "Dental on Flinders operates Monday to Saturday opposite Flinders Street Station. The clinic publishes its filling price list online and places composite restorations using layering techniques.",
        "Transparent pricing applies to all restorative procedures including multi-surface fillings. All dentists hold current AHPRA registration. The practice offers HICAPS on-the-spot claiming for eligible patients.",
     ]},
    {"rank": 7, "name": "MGA Dental", "location": "Brisbane and Gold Coast, QLD", "featured": False,
     "rating": "Contact for current ratings", "pricing": "Mid-range", "hours": "7 days a week",
     "address": "202 Pinelands Rd, Sunnybank Hills QLD 4109", "phone": "(07) 3273 3343",
     "website": "https://www.mgadental.com.au/",
     "body": [
        "MGA Dental operates 7 days a week across two locations in Sunnybank Hills and the Gold Coast. This family practice offers all filling types including composite, amalgam, and glass ionomer cement.",
        "The clinic treats both adults and children under the CDBS. All dentists hold current AHPRA registration. The practice provides written quotes before treatment and accepts health fund benefits through HICAPS.",
     ]},
    {"rank": 8, "name": "Midway Dental Clinic", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact for current ratings", "pricing": "Affordable", "hours": "Weekend appointments available",
     "address": "Ryde and Ashfield NSW", "phone": "Contact the practice",
     "website": "https://www.midwaydentalclinic.com.au/",
     "body": [
        "Midway Dental Clinic serves patients in Ryde and Ashfield with weekend availability. The practice uses gentle techniques for nervous patients and charges no weekend surcharge.",
        "Midway Dental focuses on affordable restorative care for families and pensioners. All dentists hold current AHPRA registration. Payment plan options are available for patients requiring multiple fillings.",
     ]},
    {"rank": 9, "name": "Emergency Dentist Sydney", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact for current ratings", "pricing": "Competitive", "hours": "7 days including after-hours",
     "address": "Suite 601A, 185 Elizabeth St, Sydney NSW 2000", "phone": "(02) 9267 8540",
     "website": "https://www.emergencydentistsydney.com.au/",
     "body": [
        "Emergency Dentist Sydney operates 7 days a week with a focus on urgent cases. The clinic handles emergency filling repairs and places new restorations with no call-out fee.",
        "Same-day appointments are available for urgent cases involving lost fillings or broken teeth. All dentists hold current AHPRA registration. The Elizabeth Street location is accessible from Museum and Central stations.",
     ]},
    {"rank": 10, "name": "Maddingley Dental Care", "location": "Bacchus Marsh, VIC", "featured": False,
     "rating": "Contact for current ratings", "pricing": "Contact for pricing", "hours": "After-hours and weekend",
     "address": "Bacchus Marsh VIC", "phone": "Contact the practice",
     "website": "https://www.maddingleydentalcare.com.au/",
     "body": [
        "Maddingley Dental Care serves regional Victoria with after-hours and weekend appointments. The clinic provides emergency fillings and routine restorative care for patients in the Bacchus Marsh and Melton regions.",
        "All dentists hold current AHPRA registration. The practice offers flexible appointment times for rural patients who travel significant distances for dental care.",
     ]},
]

COST_HEADING = "How much do dental fillings cost in Australia?"
COST = [
    "Dental fillings in Australia cost between $100 and $500 per tooth depending on the material, cavity size, and number of tooth surfaces involved.",
    "Composite fillings cost more than amalgam because the placement technique requires more clinical time. The dentist applies composite resin in increments of 1 to 2mm, curing each layer with a blue light for 20 to 40 seconds. Amalgam fillings involve a simpler packing technique that completes faster.",
]
COST_PRICES = [
    ("Composite (white)", "$150 – $350"),
    ("Amalgam (silver)", "$100 – $250"),
    ("Glass Ionomer Cement (GIC)", "$120 – $200"),
    ("Multi-surface filling", "$200 – $500"),
    ("Child Dental Benefits Schedule", "Up to $1,095 over 2 years"),
    ("Health fund rebate (typical)", "50 – 80% of filling fee"),
]
COST_AFTER = [
    'The Child Dental Benefits Schedule (CDBS) covers up to $1,095 over 2 calendar years for eligible children aged 0 to 17, including examinations, X-rays, cleaning, fissure sealing, and fillings. Medicare does not cover dental fillings for adults aged 18 and over. Private health insurance with extras cover reimburses 50% to 80% of filling costs. Learn more about <a href="/blog/costs/">dental costs in Australia</a>.',
]

CHOOSE_HEADING = "How do you choose a dental filling clinic in Australia?"
CHOOSE_INTRO = "You choose a dental filling clinic by evaluating 5 factors: filling materials offered, tooth-coloured composite availability, single-visit capability, pricing transparency, and diagnostic technology."
CHOOSE_CRITERIA = [
    ("What filling materials do they offer?", "A clinic that offers composite, amalgam, and GIC fillings provides options based on tooth location, budget, and aesthetic preferences. Clinics offering only one material type restrict your choices and may push you toward a suboptimal solution for your specific cavity."),
    ("Do they use tooth-coloured composite?", "Composite fillings match your natural tooth colour. The dentist selects a shade from a 16-shade guide that blends with surrounding teeth. This matters for any tooth visible in your smile line, particularly the front 6 teeth on the upper and lower arches."),
    ("Are fillings done in a single visit?", "A standard filling takes 30 to 60 minutes. Clinics with same-day availability save you a second appointment. Ask whether the dentist completes the permanent filling in one visit or places a temporary filling first, then schedules a second appointment for the final restoration."),
    ("Is pricing transparent?", "Reputable clinics quote filling costs before treatment begins. The quote includes the consultation fee, X-ray fee, and filling fee. Ask for an itemised written quote. Avoid clinics that refuse to provide a price range before your appointment."),
    ("Do they check for decay with digital X-rays?", "Digital X-rays detect interproximal decay between teeth that a visual examination misses. The Australian Dental Association recommends bitewing X-rays every 12 to 24 months for adult patients. Clinics with digital X-ray equipment provide faster, more accurate diagnoses with 80% less radiation than traditional film X-rays."),
]
CHOOSE_AFTER = [
    'For related procedures, explore our <a href="/australia/tooth-extraction/">tooth extraction</a> and <a href="/australia/root-canal-treatment/">root canal treatment</a> directories.',
]

METHODOLOGY_HEADING = "How did we rank these dental filling clinics?"
METHODOLOGY = [
    "We ranked these clinics using 8 weighted criteria. Each criterion carries equal weight in the final composite score. Data was collected from clinic websites, the AHPRA public register, Google Business profiles, and direct phone contact with each practice.",
]
METHODOLOGY_CRITERIA = [
    "Dentist qualifications: Every dentist on staff holds a Bachelor of Dental Surgery (BDS) or Doctor of Dental Medicine (DMD) from an accredited Australian or New Zealand university.",
    "AHPRA registration: All treating dentists hold current registration with the Dental Board of Australia via AHPRA, verified through the public register in July 2026.",
    "Review volume: Each clinic maintains a minimum of 50 Google reviews. The top 3 clinics average 1,064 reviews each.",
    "Rating threshold: Each clinic maintains a Google rating of 4.0 stars or higher. The average rating across the top 3 ranked clinics is 4.73 stars.",
    "Material options: Ranked clinics offer at least 2 filling materials. Most offer composite and amalgam. Several offer GIC for paediatric and geriatric cases.",
    "Pricing transparency: Clinics publish fee schedules on their websites or provide written quotes on request.",
    "Same-day availability: Ranked clinics offer same-day or next-day appointments for filling procedures. 8 of the 10 clinics operate 7 days a week.",
    "Accessibility: Clinics located within 10 minutes of public transport or with on-site parking scored higher, with wheelchair access verified for each location.",
]
METHODOLOGY_AFTER = [
    'Read the full <a href="/methodology/">methodology</a> for detailed scoring information and evaluation processes.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What type of filling is best?",
     'Composite fillings are the best option for most patients because they match natural tooth colour and bond chemically to tooth structure. Amalgam fillings provide superior durability for back teeth that bear heavy chewing forces. Glass ionomer cement works well for children and patients with high decay rates because it releases fluoride. Your dentist recommends the material based on cavity location, size, and your bite pattern. Compare <a href="/blog/treatments/">filling treatment options</a> to understand the differences.'),
    ("How long do dental fillings last?",
     "Amalgam fillings last 10 to 15 years. Composite fillings last 5 to 10 years. GIC fillings last approximately 5 years. Filling lifespan depends on 4 factors: oral hygiene habits, teeth grinding (bruxism), dietary sugar intake, and the size of the original cavity. Patients who grind their teeth at night reduce filling lifespan by 30% to 50%. Regular dental check-ups every 6 months extend filling longevity by detecting marginal wear and recurrent decay early."),
    ("How much do fillings cost in Australia?",
     'Dental fillings cost between $100 and $500 per tooth in Australia. Composite fillings range from $150 to $350. Amalgam fillings range from $100 to $250. GIC fillings range from $120 to $200. Large multi-surface fillings cost $200 to $500. The CDBS covers fillings for eligible children aged 0 to 17 up to $1,095 over 2 years. See our detailed <a href="/blog/costs/">dental costs guide</a> for state-by-state pricing and insurance rebate information.'),
    ("Does Medicare cover fillings?",
     'Medicare does not cover dental fillings for adults aged 18 and over. The Child Dental Benefits Schedule (CDBS) covers up to $1,095 over 2 calendar years for eligible children aged 0 to 17, including examinations, cleaning, and basic fillings. Adults with private health insurance extras cover can claim filling costs. Typical reimbursement ranges from 50% to 80% of the filling fee, subject to annual limits. Read more about <a href="/blog/conditions/">dental conditions that require fillings</a>.'),
    ("Is getting a filling painful?",
     "Getting a filling is not painful under local anaesthetic. The dentist injects a numbing agent into the gum tissue surrounding the affected tooth. You feel pressure and vibration during the drilling phase but no sharp pain. The injection itself causes a brief pinching sensation lasting 2 to 3 seconds. Patients with dental anxiety can request nitrous oxide or intravenous sedation. Numbness wears off within 2 to 3 hours after the procedure."),
    ("How long does a filling take?",
     "A single filling takes 30 to 60 minutes from start to finish. The dentist spends 5 to 10 minutes numbing the area, 10 to 15 minutes removing decayed tooth structure, and 15 to 35 minutes placing, shaping, and polishing the filling material. Composite fillings take longer than amalgam because each resin layer requires separate light curing. Multiple fillings in one visit extend the appointment time proportionally. Same-day appointments are available at 8 of the 10 clinics listed in this ranking."),
    ("Can a filling fall out?",
     "A filling can dislodge due to 3 factors: new decay forming around the filling margins, physical trauma to the tooth from biting hard objects, or material degradation over time. If a filling falls out, rinse the area with warm salt water, avoid chewing on that side, and book a dental appointment within 48 hours. Most clinics on this list offer same-day emergency appointments for lost fillings. Delaying treatment risks further decay and fracture of the unsupported tooth structure."),
    ("What happens if I do not get a filling?",
     'Untreated tooth decay grows progressively deeper through the enamel, dentine, and into the pulp chamber. Pulp infection causes severe throbbing pain, abscess formation, and systemic infection risk. Pulp involvement requires <a href="/australia/root-canal-treatment/">root canal treatment</a> costing $1,000 to $3,000 or <a href="/australia/tooth-extraction/">tooth extraction</a> costing $200 to $500. A filling completed at the early cavity stage costs $100 to $500. Early intervention with a filling is 5 to 10 times cheaper than delaying treatment.'),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/dental-fillings/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Dental filling clinics in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Dental Fillings", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
