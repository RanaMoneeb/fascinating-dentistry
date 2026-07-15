"""Content for /australia/after-hours-dentist/ — Top 10 After-Hours Dentists in Australia.
Transcribed from Google Doc (July 2026).

Interface contract (shared by all directory.services.* modules, rendered by
directory/templates/directory/service_listicle_page.html):
  Section paragraphs / FAQ answers may contain inline HTML (<strong>, <a href>).
  Render them through the |live_links filter so links to not-yet-live pages are
  neutralised (no dead links). All outbound practice links are nofollow."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 After-Hours Dentists in Australia: Ranked and Reviewed"
META_DESC = "Compare Australia's best after-hours dentists for 24-hour, weekend, and public holiday dental care. See pricing, ratings, hours, and locations reviewed."
H1 = "Top 10 After-Hours Dentists in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Dental pain does not respect business hours. Toothaches, broken teeth, abscesses, and lost fillings can strike at night, on weekends, or during public holidays. Australian patients need access to qualified dentists who offer after-hours appointments when standard clinics are closed.",
    "We ranked Australia's top after-hours dentists based on six criteria: extended opening hours, weekend and public holiday availability, AHPRA registration, Google reviews (minimum 50 at 4.0 or higher), same-day appointment options, and transparent after-hours pricing. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "What counts as after-hours dental care?"
WHEN = [
    "After-hours dental care covers any dental treatment provided outside standard weekday business hours of 8am to 5pm. This includes evening appointments after 5pm or 6pm on weekdays, Saturday sessions, Sunday sessions, and public holiday availability.",
    "Two main service models operate across Australia. Dedicated after-hours clinics run extended or 24-hour rosters with dentists specifically rostered for emergency and urgent call. General practices with extended hours add evening or weekend sessions to their standard schedule without a dedicated emergency team. Phone triage services connect patients with on-call dentists who assess urgency over the phone before scheduling an in-person appointment.",
    'Some health funds and state dental associations operate after-hours hotlines that direct patients to the nearest available dentist. For deeper information on specific dental problems, read our <a href="/blog/conditions/">dental conditions guide</a> and our <a href="/blog/basics/">oral hygiene guide</a>.',
]
WHEN_ALERT = "Patients experiencing severe facial swelling that affects breathing, high fever combined with dental pain, uncontrolled bleeding, or facial trauma involving bone fractures should attend a hospital emergency department immediately rather than waiting for an after-hours dentist."

WHO_TOP10 = "These 10 practices represent the best after-hours dental care across Sydney, Melbourne, Brisbane, the Gold Coast, and regional Victoria. Each entry includes verified contact details, pricing tier, Google rating, and availability information sourced directly from practice websites in July 2026."

# Each practice: rank, name, location, featured (1-3), then rating/pricing/hours/address/
# phone/website/body[]. Optional: ahpra (bool) renders an AHPRA-Reg Verified badge.
TOP10 = [
    {"rank": 1, "name": "Smile Concepts", "location": "Sydney, NSW", "featured": True,
     "rating": "4.8/5 (667 reviews)", "pricing": "Mid-range (no after-hours surcharge)", "hours": "7 days including after-hours",
     "address": "Suite 403, Level 4, 307 Pitt St, Sydney NSW 2000", "phone": "(02) 9267 7777",
     "website": "https://www.smileconcepts.com.au/",
     "body": [
        "Smile Concepts operates as one of Sydney's most established after-hours dental practices, offering 24-hour emergency dental care 7 days a week. The practice holds AHPRA registration for all treating dentists and maintains a 4.8 out of 5 Google rating across 667 verified patient reviews. Patients can access same-day appointments for toothache relief, broken tooth repair, and dental trauma management.",
        "A distinguishing feature of Smile Concepts is the absence of an after-hours surcharge. The practice charges standard rates regardless of when a patient is seen, whether that is a weekday morning or a Sunday evening. This pricing model is rare among after-hours clinics in the Sydney CBD and makes Smile Concepts a cost-effective option for patients without health fund cover.",
        "The practice is located on Level 4 at 307 Pitt Street, a short walk from Town Hall station. Free underground parking is available for patients, which reduces the stress of an already uncomfortable emergency visit. The clinic treats dental trauma from sports injuries, knocked-out teeth, severe toothaches, and lost fillings.",
     ]},
    {"rank": 2, "name": "Emergency Dentist Sydney", "location": "Sydney, NSW", "featured": True,
     "rating": "Contact the practice for current review ratings", "pricing": "Competitive and affordable", "hours": "7 days including after-hours",
     "address": "Suite 601A, 185 Elizabeth St, Sydney NSW 2000", "phone": "(02) 9267 8540",
     "website": "https://www.emergencydentistsydney.com.au/",
     "body": [
        "Emergency Dentist Sydney operates a dedicated emergency dental team available 7 days a week with after-hours and weekend care. All treating dentists hold current AHPRA registration. The practice focuses exclusively on urgent dental problems rather than general dentistry, which means the team has extensive experience handling dental trauma, knocked-out teeth, and severe toothache scenarios.",
        "The clinic does not charge a call-out fee for after-hours appointments, keeping costs manageable for patients who need urgent care outside business hours. Services include toothache relief, broken tooth repair, management of knocked-out teeth, and treatment of sports-related dental injuries. The Elizabeth Street location in the Sydney CBD is accessible by public transport at all hours.",
     ]},
    {"rank": 3, "name": "MC Dental Melbourne Central", "location": "Melbourne, VIC", "featured": True,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range (no weekend surcharge)", "hours": "Open 7 days including public holidays",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8971",
     "website": "https://www.mcdental.com.au/",
     "body": [
        "MC Dental at Melbourne Central is the highest-rated clinic on this list, with 2,197 Google reviews at an average of 4.8 out of 5. All dentists hold AHPRA registration and the practice maintains membership with the Australian Dental Association. The team includes bilingual clinicians who speak Mandarin, Cantonese, Vietnamese, and other languages to serve Melbourne's diverse population.",
        "The practice charges the same fees every day of the week with no weekend or public holiday surcharge. Opening hours extend to 7pm on Tuesdays and Fridays, with Saturday sessions from 9am to 4pm and Sunday sessions from 10am to 5pm. The clinic operates on public holidays from 10am to 5pm, making it one of the few Melbourne practices reliably open on long weekends.",
        "Located above Melbourne Central station on La Trobe Street, the practice offers discount parking for patients. MC Dental operates 6 locations across Melbourne, but the Melbourne Central clinic offers the most comprehensive after-hours availability. Accepted health funds include Medibank, NIB, BUPA, HCF, and CBHS.",
     ]},
    {"rank": 4, "name": "Pure Dentistry", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.6/5 (330 reviews)", "pricing": "Mid-range", "hours": "7 days including public holidays",
     "address": "11/1932-1974 Logan Road, Upper Mt Gravatt QLD 4122", "phone": "(07) 3343 4869",
     "website": "https://www.puredentistry.com.au/",
     "body": [
        "Pure Dentistry holds full QIP accreditation and operates 7 days a week including public holidays. All treating dentists hold AHPRA registration and ADA membership. The practice phone line operates from 5am to 11pm, giving patients extended access to schedule same-day emergency appointments.",
        "The clinic offers IV sedation and sleep dentistry for anxious patients, a service rarely available outside standard hours. Services span emergency dentistry, general dentistry, and complex procedures including surgical extractions and root canal therapy.",
     ]},
    {"rank": 5, "name": "United Dental Care", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "7 days including public holidays",
     "address": "Suite 5/377 Sussex St, Sydney NSW 2000 (also at 1st Floor/260-262 Beamish St, Campsie NSW 2194)", "phone": "(02) 9267 7174",
     "website": "https://www.uniteddentalcare.com.au/",
     "body": [
        "United Dental Care operates two Sydney locations, both open 7 days including public holidays. The practice closes only on Christmas Day and New Year's Day. All dentists hold AHPRA registration and the practice accepts major health funds.",
        "After-hours emergency care is available at both the Sussex Street CBD location and the Campsie location. Services include family dentistry, root canal therapy, general dentistry, and emergency after-hours treatment.",
     ]},
    {"rank": 6, "name": "Dental on Flinders", "location": "Melbourne, VIC", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "Monday to Saturday including after-hours",
     "address": "Level 5, 276 Flinders St, Melbourne VIC 3000", "phone": "(03) 9041 0049",
     "website": "https://www.dentalonflinders.com.au/",
     "body": [
        "Dental on Flinders offers after-hours dental appointments and Saturday sessions from its Melbourne CBD location opposite Flinders Street Station. All treating dentists hold AHPRA registration. The practice provides general and preventative dentistry alongside emergency after-hours care.",
        "The clinic publishes transparent pricing on its website, which helps patients understand costs before booking an after-hours appointment. Services include emergency dental care, general check-ups, and preventative treatments.",
     ]},
    {"rank": 7, "name": "24 Hour Emergency Dentist", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "24 hours a day on weekdays",
     "address": "Suite 431, 307 Pitt St, Sydney NSW 2000", "phone": "9154 0145",
     "website": "https://www.24hour-dentist.com.au/",
     "body": [
        "24 Hour Emergency Dentist operates as a dedicated emergency clinic with 24-hour weekday availability. All treating dentists hold AHPRA registration. The practice treats toothaches, broken teeth, tooth infections, knocked-out teeth, chipped teeth, and bleeding teeth at any hour of the day or night on weekdays.",
        "The clinic is located on Pitt Street near Town Hall station, making it accessible for Sydney CBD residents and workers who need dental care outside standard hours. Contact the practice for weekend availability details.",
     ]},
    {"rank": 8, "name": "MGA Dental", "location": "Brisbane and Gold Coast, QLD", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "7 days a week",
     "address": "202 Pinelands Rd, Sunnybank Hills QLD 4109", "phone": "(07) 3273 3343",
     "website": "https://www.mgadental.com.au/",
     "body": [
        "MGA Dental is a family-run practice operating across Brisbane and the Gold Coast with extended hours 7 days a week. The practice offers emergency dentistry, general dentistry, and family dentistry with weekend availability at both locations.",
        "The Sunnybank Hills clinic serves southern Brisbane suburbs, while the Gold Coast location provides after-hours access for coastal residents. Contact the practice for specific after-hours session times at each location.",
     ]},
    {"rank": 9, "name": "Clear Dental", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "Open 7 days (hours vary by location)",
     "address": "131 Clarence St, Sydney NSW 2000 (also at Parramatta, Castle Hill, Chatswood, and Berowra Heights)", "phone": "(02) 9456 6557",
     "website": "https://www.cleardental.com.au/",
     "body": [
        "Clear Dental operates 5 Sydney locations with emergency patients prioritised across all sites. All treating dentists hold AHPRA registration. The practice offers emergency dentistry, general dentistry, cosmetic dentistry, Invisalign, and dental implants.",
        "Opening hours vary by location, so patients should call ahead to confirm after-hours availability at their nearest clinic. The Clarence Street CBD location offers the most extended hours of the 5 sites.",
     ]},
    {"rank": 10, "name": "Maddingley Dental Care", "location": "Bacchus Marsh, VIC", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Contact the practice for current pricing", "hours": "After-hours emergency care 7 days",
     "address": "Bacchus Marsh VIC (contact the practice for exact address)", "phone": "Contact the practice for current phone details",
     "website": "https://maddingleydentalcare.com.au/",
     "body": [
        "Maddingley Dental Care provides after-hours emergency dental services 7 days a week for patients in Bacchus Marsh, Melton, and surrounding regional areas. All treating dentists hold AHPRA registration.",
        "The practice offers general dentistry and emergency dentistry with after-hours availability, filling a service gap in Melbourne's outer western suburbs. Contact the practice directly to confirm address, phone number, and current after-hours session times.",
     ]},
]

COST_HEADING = "How much does after-hours dental care cost in Australia?"
COST = [
    "After-hours dental care costs more than standard weekday treatment because clinics roster additional staff and pay penalty rates. Understanding the fee structure helps patients budget for unexpected dental emergencies.",
    "Typical after-hours costs in Australia include:",
]
COST_PRICES = [
    ("After-hours consultation", "$120 – $280"),
    ("Standard weekday consultation", "$80 – $150"),
    ("Weekend surcharge", "$50 – $150"),
    ("Public holiday surcharge", "$75 – $200"),
    ("After-hours tooth extraction", "$250 – $450"),
    ("Phone triage", "Free or $20 – $50"),
]
COST_AFTER = [
    'Some clinics on this list, including Smile Concepts and MC Dental, do not charge an after-hours surcharge. This can save patients between $50 and $200 per visit compared to clinics that apply weekend or public holiday loading.',
    'The Child Dental Benefits Schedule (CDBS) provides up to $1,095 over two years for eligible children aged 2 to 17. CDBS covers basic treatments such as examinations, fillings, and extractions but typically does not cover after-hours surcharges. For a detailed breakdown of dental costs across Australia, read our <a href="/blog/costs/">dental costs guide</a>.',
]

CHOOSE_HEADING = "How do you choose an after-hours dentist in Australia?"
CHOOSE_INTRO = "Choosing the right after-hours dentist requires checking 5 specific factors before booking an appointment. Use this checklist to compare clinics quickly:"
CHOOSE_CRITERIA = [
    ("What are their actual after-hours opening hours?", "Check the practice website for current session times. Some clinics advertise \"7 days\" but close at 2pm on Sundays. Confirm the exact hours for the day you need care."),
    ("Do they charge an after-hours surcharge, and is it disclosed upfront?", "Ask for the total cost including any surcharge before confirming the appointment. Reputable clinics quote the full fee over the phone."),
    ("Is the dentist AHPRA-registered?", "Every dentist in Australia must hold current registration with the Australian Health Practitioner Regulation Agency. You can verify registration on the AHPRA website."),
    ("What do Google reviews say about after-hours care?", "Read reviews specifically mentioning evening, weekend, or emergency visits. Look for patterns in wait times, pain management, and billing transparency."),
    ("Can they handle your specific dental issue after-hours?", "Complex procedures such as root canals or implant surgery may not be available outside standard hours. Ask whether the clinic offers temporary management with a follow-up booking during regular hours."),
]
CHOOSE_AFTER = [
    'For related services, you can also browse our <a href="/australia/emergency-dentist/">emergency dentist</a> directory and our <a href="/australia/weekend-dentist/">weekend dentist</a> listings.',
]

METHODOLOGY_HEADING = "How did we rank these after-hours dentists?"
METHODOLOGY = [
    "We evaluated every clinic on this list against 8 weighted criteria to produce a fair, transparent ranking. Our assessment methodology applies consistently to both paid and editorial entries.",
    "The 8 ranking criteria are:",
]
METHODOLOGY_CRITERIA = [
    "After-hours availability: Number of days per week with extended hours, including evenings, weekends, and public holidays.",
    "AHPRA registration: Verified current registration for all treating dentists at each practice.",
    "Google review volume and rating: Minimum 50 reviews at 4.0 or higher for editorial inclusion. Practices with higher volumes and ratings ranked higher.",
    "Pricing transparency: Whether the practice publishes after-hours fees or provides quotes over the phone without obligation.",
    "Range of after-hours services: Whether the clinic offers emergency care only or also provides general, cosmetic, and specialist dentistry outside standard hours.",
    "Accessibility: Proximity to public transport, parking availability, and physical access for patients in pain.",
    "Health fund partnerships: Number of major health funds accepted, including HICAPS claiming for on-the-spot rebates.",
    "Accreditation: QIP or other independent practice accreditation demonstrating adherence to Australian dental standards.",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Editorial selections in positions 4 to 10 met a minimum of 6 of 8 criteria. Read the full <a href="/methodology/">our methodology</a> page for detailed scoring weights and evaluation dates.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What counts as after-hours dental care?", 'After-hours dental care covers appointments and treatments outside standard business hours of 8am to 5pm weekdays. This includes evening appointments after 5pm, Saturday and Sunday sessions, and public holiday availability. Read our <a href="/blog/conditions/">dental conditions guide</a> for specific problems that require after-hours attention.'),
    ("Is after-hours dental care more expensive than standard hours?", 'Yes. After-hours consultations range from $120 to $280 compared to $80 to $150 during standard weekday hours. Weekend surcharges add $50 to $150 and public holiday surcharges add $75 to $200. Some clinics like Smile Concepts and MC Dental charge standard rates regardless of the day. See our <a href="/blog/costs/">dental costs guide</a> for a full breakdown.'),
    ("Does Medicare cover after-hours dental visits?", "Medicare does not cover most after-hours dental services for adults. The Child Dental Benefits Schedule provides up to $1,095 over two years for eligible children aged 2 to 17. CDBS covers basic treatments but typically does not cover after-hours surcharges applied by the clinic."),
    ("What treatment can I get during an after-hours appointment?", 'After-hours dentists handle tooth extractions, fillings, temporary crowns, abscess treatment, toothache management, and broken tooth repair. Complex procedures such as full root canal therapy or implant placement may receive temporary management with a follow-up scheduled during regular hours. Browse <a href="/australia/">all 42 dental services across Australia</a> for specific treatment types.'),
    ("Should I go to an after-hours dentist or a hospital emergency department?", 'Visit an after-hours dentist for tooth-specific problems including toothache, broken teeth, lost fillings, and dental trauma. Go to a hospital emergency department for facial swelling that affects breathing, high fever combined with dental pain, uncontrolled bleeding, or facial trauma involving bone fractures. Learn more in our <a href="/blog/basics/">oral hygiene guide</a>.'),
    ("How do I find an after-hours dentist near me?", 'Search online for "after hours dentist near me" or use Google Maps to find practices with extended hours. Many clinics display after-hours availability on their website homepage. Call ahead to confirm the dentist is available and ask about the total cost including any surcharge. Our <a href="/australia/emergency-dentist/">emergency dentist</a> and <a href="/australia/weekend-dentist/">weekend dentist</a> directories list additional options.'),
    ("Do after-hours dentists accept private health insurance?", "Most after-hours dental clinics accept major private health funds and offer HICAPS claiming for on-the-spot rebates. The rebate amount depends on your level of cover and policy terms. Health fund rebates typically apply to the standard treatment component but may not cover the after-hours surcharge portion. Check with your fund before booking."),
    ("Are after-hours dentists qualified the same as regular dentists?", 'Yes. All after-hours dentists in Australia must hold current AHPRA registration, the same regulatory requirement as any practising dentist. Some after-hours clinics employ dentists with additional emergency or trauma management experience. You can verify any dentist\'s registration on the AHPRA public register. Read more <a href="/about/">about Fascinating Dentistry</a> and our review standards.'),
]

CTA_TITLE = "Are you an after-hours dentist in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/after-hours-dentist/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "After-hours dentists in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "After-Hours Dentists", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
