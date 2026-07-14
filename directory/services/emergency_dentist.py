"""Content for /australia/emergency-dentist/ — Top 10 Emergency Dentists in Australia.
Transcribed verbatim from content/02-australia-emergency-dentist.md. ALL website links
are nofollow (matches the /australia/ hub convention)."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Emergency Dentists in Australia - Reviewed & Ranked"
META_DESC = "Find the top 10 emergency dentists in Australia. Compare after-hours, 24/7, and weekend dental clinics for toothaches, broken teeth, and extractions."
H1 = "Top 10 Emergency Dentists in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Dental emergencies cause severe pain and require immediate clinical intervention. Sudden toothaches, broken teeth, dental abscesses, and knocked-out teeth cannot wait for regular business hours. Australian patients need rapid access to qualified emergency dentists who can provide same-day or after-hours treatment.",
    "We ranked Australia's top emergency dentists based on AHPRA registration, after-hours availability, Google reviews (minimum 50 at 4.0+), same-day appointment options, weekend/public holiday access, and transparent emergency pricing. Read our methodology for a detailed breakdown.",
    "Browse the ranked list below. Positions 1-3 are paid placements with do-follow links. Positions 4-10 are editorial selections with no-follow links. Paid placement never affects positions 4-10. Read our disclosures policy.",
]

WHEN_HEADING = "When should you seek emergency dental care?"
WHEN = [
    "You should seek emergency dental care for severe toothache, knocked-out teeth, dental abscesses, uncontrolled bleeding, and post-surgical infections. A dental emergency involves any oral issue requiring immediate intervention to save a tooth, stop bleeding, or relieve severe pain. Severe toothache or dental pain lasting more than 48 hours requires urgent assessment. A knocked-out (avulsed) tooth is time-critical, with the best prognosis if treated within 1 hour. Cracked, chipped, or fractured teeth causing pain also need immediate repair.",
    "A dental abscess presenting with swelling, pus, or fever can become systemic, so patients must seek immediate care. Uncontrolled bleeding from the mouth, lost fillings or crowns causing pain, and infection post-extraction or post-surgery are definite emergencies. Trauma from sports injuries, falls, or accidents requires immediate evaluation.",
]

WHO_TOP10 = "The top 10 emergency dentists in Australia include dedicated emergency clinics and mixed-practice clinics offering extensive after-hours and same-day appointments. These clinics were selected based on verified AHPRA registration, Google reviews, and emergency service availability."

TOP10 = [
    {"rank": 1, "name": "Emergency Dental Centre", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "intro": "Emergency Dental Centre provides dedicated urgent dental services 7 days a week. AHPRA-registered dentists staff the clinic and maintain strict compliance with Australian dental regulations. Practitioners hold extensive experience in emergency triage and acute pain management. Patients receive care from qualified professionals specifically trained to handle urgent dental trauma.",
     "body": [
        "The practice specialises in abscessed teeth, broken dentures, chipped and broken teeth, infections, and lost crowns or veneers. Their expertise covers trauma and sports injuries. They prioritise same-day treatment for emergencies to ensure rapid pain relief and prevent further complications.",
        "Facilities are equipped for immediate emergency interventions 7 days a week, including public holidays. The clinic operates dedicated after-hours services. This ensures patients access necessary diagnostic and treatment technologies outside standard operating times.",
        "Patients consistently report high satisfaction with the clinic's rapid response times. The practice accepts various health funds, though patients should contact the practice for accepted health funds. Mid-range pricing provides accessible emergency care.",
     ],
     "pricing_tier": "Mid-range",
     "address": "Contact the practice for current address",
     "phone": "(03) 9347 1610",
     "website": "https://www.emergencydentalcentre.com.au/",
     "rating": "Contact the practice for current Google rating information",
     "health_funds": "Contact the practice for accepted health funds"},
    {"rank": 2, "name": "Emergency Dentist Sydney", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "intro": "Emergency Dentist Sydney provides 24-hour after-hours emergency dental care. AHPRA-registered dentists staff the clinic and maintain full regulatory compliance. Dentists at the practice focus on delivering urgent care with no call-out fee for after-hours services. The team provides evidence-based treatment for acute dental issues.",
     "body": [
        "The clinic offers 24-hour after-hours emergency dental care, 7 days a week. Special interests include toothache relief, broken tooth repair, knocked-out tooth management, and dental trauma from sports injuries. Their central location allows easy access for patients across Sydney requiring immediate attention.",
        "The practice utilises modern dental technology suitable for emergency diagnostics and surgical interventions. Their facilities support same-day treatments. They maintain affordable rates while operating from a single, consistent CBD location for reliable patient access.",
        "Reviews highlight the clinic's affordable pricing and reliable after-hours availability. Patients appreciate the absence of after-hours call-out fees. The practice accepts major health funds, but patients should contact the practice for accepted health funds.",
     ],
     "pricing_tier": "Competitive/affordable",
     "address": "Suite 601A, 185 Elizabeth St, Sydney NSW 2000",
     "phone": "(02) 9267 8540",
     "website": "https://www.emergencydentistsydney.com.au/",
     "rating": "Contact the practice for current Google rating information",
     "health_funds": "Contact the practice for accepted health funds"},
    {"rank": 3, "name": "Pure Dentistry", "location": "Brisbane, QLD", "featured": True, "ahpra": True,
     "intro": "Pure Dentistry operates with full Quality Innovation Performance (QIP) accreditation. AHPRA-registered dentists and Australian Dental Association (ADA) members staff the clinic. The practice operates 7 days a week, including public holidays, with phone availability from 5am to 11pm to handle urgent enquiries.",
     "body": [
        "The clinic provides emergency dentistry alongside general, cosmetic, implant, and paediatric dentistry. Their emergency focus includes same-day appointments for acute pain and trauma. They offer specialised sleep dentistry, including IV sedation and general anaesthesia for anxious patients or complex surgical needs.",
        "The Upper Mt Gravatt facility supports comprehensive emergency and surgical protocols. Same-day emergency appointments utilise modern diagnostic equipment. The integration of sedation dentistry allows the team to perform complex emergency extractions and procedures safely on-site.",
        "The practice holds a 4.6 out of 5 Google rating from 330 reviews. Patients commend the extended operating hours and availability of sedation options. Mid-range pricing applies, and patients should contact the practice for accepted health funds.",
     ],
     "pricing_tier": "Mid-range",
     "address": "11/1932-1974 Logan Road, Upper Mt Gravatt QLD 4122",
     "phone": "(07) 3343 4869",
     "website": "https://www.puredentistry.com.au/",
     "rating": "4.6/5 (330 reviews)",
     "health_funds": "Contact the practice for accepted health funds"},
    {"rank": 4, "name": "MGA Dental", "location": "Brisbane & Gold Coast, QLD", "featured": False,
     "body": [
        "MGA Dental is a family-run practice offering emergency and general dentistry. The clinic operates 7 days a week with extended hours to accommodate urgent dental needs. Emergency appointments are available for patients experiencing acute pain or dental trauma.",
        "The Sunnybank Hills facility provides accessible care for Brisbane and Gold Coast residents. Patients should contact the practice for current Google rating information and accepted health funds.",
     ],
     "address": "202 Pinelands Rd, Sunnybank Hills QLD 4109",
     "phone": "(07) 3273 3343",
     "website": "https://www.mgadental.com.au/",
     "rating": "Contact the practice for current Google rating information"},
    {"rank": 5, "name": "Smile Concepts", "location": "Sydney, NSW", "featured": False,
     "body": [
        "Smile Concepts offers emergency dentistry alongside cosmetic and orthodontic services from their Sydney CBD location. The clinic operates for emergencies including after-hours and holidays. They utilise advanced dental technology for rapid diagnosis and treatment of acute dental issues.",
        "The practice holds a 4.8 out of 5 Google rating from 667 reviews. Operating hours are Monday to Friday 8am to 6pm and Saturday 8:30am to 1:30pm. Patients should contact the practice for accepted health funds.",
     ],
     "address": "Suite 403, Level 4/307 Pitt St, Sydney NSW 2000",
     "phone": "(02) 9267 7777",
     "website": "https://www.smileconcepts.com.au/",
     "rating": "4.8/5 (667 reviews)"},
    {"rank": 6, "name": "Dental SOS", "location": "Melbourne, VIC", "featured": False,
     "body": [
        "Dental SOS provides out-of-hours emergency dental care 7 days a week. AHPRA-registered dentists staff the clinic. The practice focuses on fixed, transparent pricing and same-day emergency appointments for Melbourne patients.",
        "Patients requiring urgent care can access consistent after-hours services. Patients should contact the practice for current address, phone number, Google rating information, and accepted health funds.",
     ],
     "address": "Contact the practice for current address",
     "phone": "Contact the practice for current phone number",
     "website": "https://dentalsos.com.au/",
     "rating": "Contact the practice for current Google rating information"},
    {"rank": 7, "name": "Dentistry on George", "location": "Brisbane, QLD", "featured": False,
     "body": [
        "Dentistry on George provides emergency dentistry from their Brisbane CBD location. Both principal dentists are AHPRA-registered and ADA members. The practice offers same-day emergency appointments and IV or twilight sedation for complex procedures.",
        "The clinic has served Brisbane for over 40 years. It holds a 5.0 out of 5 Google rating from 191 reviews. Operating hours are Monday to Tuesday 8am to 4pm, Wednesday to Thursday 9am to 5pm, and Friday 9am to 2:30pm. Patients should contact the practice for accepted health funds.",
     ],
     "address": "Level 12, 239 George Street, Brisbane QLD 4000",
     "phone": "(07) 3211 1155",
     "website": "https://www.dentistryongeorge.com.au/",
     "rating": "5.0/5 (191 reviews)"},
    {"rank": 8, "name": "Gorgeous Smiles", "location": "Melbourne, VIC", "featured": False,
     "body": [
        "Gorgeous Smiles provides emergency dental care from their Melbourne CBD location. The clinic has treated over 30,000 patients. Emergency appointments are available for acute pain, trauma, and dental infections.",
        "The practice holds a 4.9 out of 5 Google rating from 1,496 reviews. Patients should contact the practice for accepted health funds and current operating hours.",
     ],
     "address": "121 Exhibition St, Melbourne VIC 3000",
     "phone": "(03) 9042 0483",
     "website": "https://www.gorgeoussmiles.com.au/",
     "rating": "4.9/5 (1,496 reviews)"},
    {"rank": 9, "name": "Balmoral Dental Centre", "location": "Brisbane, QLD", "featured": False,
     "body": [
        "Balmoral Dental Centre offers weekend dentist services and emergency dentistry. The clinic operates 7 days a week, including weekends, to provide emergency care for Brisbane patients.",
        "The practice focuses on general and emergency dental treatments. Patients should contact the practice for current address, phone number, Google rating information, and accepted health funds.",
     ],
     "address": "Contact the practice for current address",
     "phone": "Contact the practice for current phone number",
     "website": "https://www.balmoraldental.com.au/",
     "rating": "Contact the practice for current Google rating information"},
    {"rank": 10, "name": "Hyde Park Dental Care", "location": "Sydney, NSW", "featured": False,
     "body": [
        "Hyde Park Dental Care offers emergency dentistry and same-day dental care in Sydney. The clinic features experienced emergency dentists capable of handling acute pain and dental trauma.",
        "The practice provides same-day emergency appointments for urgent cases. Patients should contact the practice for current address, phone number, Google rating information, and accepted health funds.",
     ],
     "address": "Contact the practice for current address",
     "phone": "Contact the practice for current phone number",
     "website": "https://www.hydeparkdentalcare.com.au/",
     "rating": "Contact the practice for current Google rating information"},
]

COST_HEADING = "How much does emergency dental care cost in Australia?"
COST = [
    "Emergency dental care in Australia costs between $100 and $250 for a standard consultation, with after-hours and weekend surcharges adding $50 to $150 to the total bill. Treatment costs vary by procedure. An emergency tooth extraction for a simple case costs $200 to $400. An emergency filling costs $150 to $350. An emergency root canal for a front tooth costs $800 to $1,500. Reimplantation of a knocked-out tooth costs $200 to $500.",
    "Many clinics offer payment plans and accept major health funds. The Child Dental Benefits Schedule (CDBS) provides up to $1,095 over two years for eligible children, but it does not typically cover after-hours surcharges. Medicare does not cover most emergency dental services for adults.",
]

CHOOSE_HEADING = "How do you choose an emergency dentist in Australia?"
CHOOSE_INTRO = "You choose an emergency dentist in Australia by verifying their AHPRA registration, checking same-day availability, reviewing Google ratings, confirming transparent pricing, and ensuring they can handle specific emergency procedures on-site."
CHOOSE_CRITERIA = [
    ("Do they offer same-day or after-hours appointments?", "Clinics providing 7-day or 24-hour service ensure you receive care when pain strikes outside standard business hours."),
    ("Is the dentist AHPRA-registered?", "Verification with the Australian Health Practitioner Regulation Agency guarantees the practitioner meets national legal and professional standards."),
    ("What are their Google reviews and rating?", "A minimum of 50 reviews at 4.0 stars or higher indicates reliable patient experiences and consistent clinical outcomes."),
    ("Is pricing transparent with an upfront quote?", "Reputable emergency dentists provide clear cost estimates before treatment begins to prevent unexpected financial burdens."),
    ("What emergency procedures can they handle on-site?", "Ensure the clinic has the facilities for extractions, root canals, and trauma management without referring you elsewhere."),
]

METHODOLOGY_HEADING = "What methodology did we use to rank these emergency dentists?"
METHODOLOGY = [
    "We ranked these emergency dentists using 8 criteria: AHPRA registration, after-hours availability, Google reviews, years of experience, emergency treatment options, and transparent pricing. The 8 evaluation criteria are:",
]
METHODOLOGY_CRITERIA = [
    "Current AHPRA registration verification.",
    "Availability of after-hours and weekend appointments.",
    "Google review volume, requiring a minimum of 50 reviews.",
    "Google review rating, requiring a minimum of 4.0 stars.",
    "Years of clinical experience in emergency dentistry.",
    "Range of emergency treatment options provided on-site.",
    "Transparent and accessible pricing structures.",
    "Same-day appointment availability for acute cases.",
]

FAQ_HEADING = "What are the most common questions about emergency dentists?"
FAQS = [
    ("When should I see an emergency dentist instead of going to a hospital?", "You should see an emergency dentist for tooth-related problems such as severe toothache, broken or knocked-out teeth, lost fillings or crowns, and dental abscesses that are localised to the mouth. Visit a hospital emergency department for facial swelling affecting your breathing, high fever accompanying dental pain, uncontrolled bleeding, or trauma involving facial bones."),
    ("What counts as a dental emergency?", "A dental emergency includes severe toothache lasting more than 48 hours, knocked-out teeth, cracked or broken teeth causing pain, dental abscesses with swelling, uncontrolled oral bleeding, lost fillings or crowns causing pain, and post-surgical infections. If you are unsure, call the clinic, as most emergency dentists can advise over the phone."),
    ("How much does an emergency dentist cost in Australia?", "Emergency dental consultation fees range from $100 to $250 for standard hours. After-hours, weekend, and public holiday appointments typically include a surcharge of $50 to $150. Treatment costs vary by procedure: simple extractions $200-$400, fillings $150-$350, and root canal treatment $800-$1,500 per tooth. Many clinics offer payment plans and accept major health funds."),
    ("Does Medicare cover emergency dental visits?", "Medicare does not cover most emergency dental services for adults. The Child Dental Benefits Schedule (CDBS) provides up to $1,095 over two years for eligible children aged 0-17, which can cover some emergency treatments. Public hospital emergency departments can provide dental care in severe cases, but waiting times are often long."),
    ("Can I go to a hospital emergency department for dental pain?", "Yes, hospital emergency departments can treat dental pain with pain relief and antibiotics, but they typically cannot perform definitive dental treatments such as root canals or permanent fillings. They will refer you to an emergency dentist for ongoing care. For tooth-specific emergencies, seeing an emergency dentist directly is usually faster and more appropriate."),
    ("Are emergency dentists open on weekends and public holidays?", "Many emergency dentists operate 7 days a week, including weekends and public holidays. Some clinics offer dedicated after-hours services, while others provide same-day emergency appointments during extended business hours. It is advisable to call ahead to confirm availability and any after-hours surcharges."),
    ("What should I do if my tooth gets knocked out?", "Pick up the tooth by the crown (the white part), not the root. Rinse it gently with milk or saline if dirty, do not scrub or use soap. Try to reinsert the tooth into its socket if possible, or store it in milk or saliva. See an emergency dentist within 1 hour for the best chance of saving the tooth."),
    ("How do I know if my dental pain is serious enough for emergency care?", "Severe pain that interrupts sleep, pain accompanied by facial swelling, fever, or difficulty swallowing are signs that require immediate emergency care. Persistent throbbing pain, sensitivity to hot and cold that lingers, and visible swelling around a tooth also warrant urgent dental attention. When in doubt, call an emergency dentist for advice."),
]

CTA_TITLE = "Are you an emergency dentist in Australia?"
CTA_TEXT = "Apply to be featured in our directory. Contact us to learn more about our listing options and evaluation criteria."

DISCLOSURE = "Practices in positions 1-3 are paid placements with do-follow links. Practices in positions 4-10 are listed editorially with no-follow links. Paid placement never affects positions 4-10."


def _build_schemas():
    url = f"{SITE_URL}/australia/emergency-dentist/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Emergency dentists in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Emergency Dentists", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
