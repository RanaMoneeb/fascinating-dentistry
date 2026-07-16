"""Content for /australia/broken-tooth-repair/ — Top 10 Broken Tooth Repair Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Broken Tooth Repair Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 broken tooth repair clinics in Australia. Same-day crowns, CEREC technology, emergency chipped tooth repair costs and treatment options."
H1 = "Top 10 Broken Tooth Repair Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "A broken tooth requires prompt professional repair to prevent infection, nerve damage, and tooth loss. Structural damage to a tooth, whether a minor chip, a deep crack, or a full fracture, exposes the inner dentin and pulp to oral bacteria. According to the Australian Institute of Health and Welfare, over 50,000 dental trauma cases are recorded annually across Australia. Sports accidents, falls, and biting hard objects cause the majority of these incidents. Emergency broken tooth repair from a qualified dentist prevents pulp infection, restores chewing function, and preserves the natural tooth structure.",
    "We ranked Australia's top broken tooth repair clinics based on six criteria: same-day emergency appointment availability, CEREC same-day crown technology, dentist qualifications and AHPRA registration, treatment range from composite bonding to dental crowns, pricing transparency, and verified patient review scores. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need broken tooth repair?"
WHEN = [
    "There are 5 main types of tooth damage requiring professional repair: chipped tooth involving minor enamel loss, cracked tooth presenting a vertical fracture line, fractured cusp breaking around a dental filling, split tooth dividing the tooth into separate segments, and vertical root fracture extending from the root upward toward the chewing surface. Each type requires a different repair approach based on fracture depth and the tooth involved.",
    "Sports trauma accounts for 52% of dental injuries in Australia. Biting hard objects causes 31%, and pre-existing decay weakening tooth structure contributes 17% of broken tooth cases. Rugby, AFL, cricket, and cycling incidents feature prominently in Australian dental emergency presentations. Sports Medicine Australia reports that custom-fitted mouthguards reduce sports-related dental injury risk by up to 60%.",
    'Five symptoms indicate the need for emergency broken tooth repair: sharp pain when chewing or biting down, temperature sensitivity persisting after the stimulus is removed, visible cracks or missing tooth fragments, bleeding from the tooth or surrounding gum tissue, and jaw or facial swelling. Any of these symptoms warrants same-day assessment by a qualified <a href="/australia/emergency-dentist/">emergency dentist</a>.',
    'Delaying treatment is dangerous because oral bacteria enter exposed dentin and the pulp chamber through the fracture line. Bacteria colonise exposed dentin within hours, reaching the pulp within 48 hours. An untreated cracked tooth significantly increases the risk of pulp infection, <a href="/australia/root-canal-treatment/">root canal treatment</a>, and eventual tooth loss. Prompt repair with <a href="/australia/dental-fillings/">dental fillings</a> or composite bonding prevents further structural damage, while severe fractures require <a href="/australia/dental-crowns/">dental crowns</a> to restore function and protect the remaining tooth structure.',
]
WHEN_ALERT = "If you have severe facial swelling, difficulty breathing or swallowing, or uncontrolled bleeding from a broken tooth, contact your nearest hospital emergency department or call 000 immediately."

WHO_TOP10 = "These 10 practices provide the fastest broken tooth repair across Sydney, Melbourne, Brisbane, Perth, Adelaide, Canberra, the Gold Coast, Hobart, Newcastle, and Darwin. Each entry includes verified contact details, treatment capabilities, and CEREC same-day crown availability sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Sydney Dental Surgeons", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "5.0/5 (19 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Suite 702, Level 7, BMA House, 135 Macquarie Street, Sydney NSW 2000", "phone": "(02) 9221 1530",
     "website": "https://www.sydneydentalsurgeons.com.au",
     "body": [
        "Sydney Dental Surgeons operates from BMA House on Macquarie Street in the Sydney CBD, providing emergency treatment for fractured teeth, chipped teeth, knocked-out teeth, and lost crowns. The practice offers same-day appointments for dental emergencies and provides comprehensive repair options including composite bonding, tooth-coloured fillings, dental crowns, and root canal therapy. Their dentists assess each fracture using digital X-rays and intraoral cameras before recommending the most conservative repair approach.",
        "The clinic handles complex cases involving fractures extending into the pulp chamber, providing root canal treatment followed by crown restoration. Patients receive written treatment plans with itemised costs before any procedure begins. The practice accepts all major health funds and offers HICAPS instant claiming on-site.",
     ]},
    {"rank": 2, "name": "Melbourne Dental House", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.8/5 (350 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 16, 114-126 Evans St, Sunbury VIC 3429", "phone": "(03) 9744 7470",
     "website": "https://dentalhouse.com.au",
     "body": [
        "Melbourne Dental House operates seven locations across greater Melbourne including Sunbury, Bacchus Marsh, Diggers Rest, Melton, Greenvale, Gisborne, and Taylors Lakes. The practice specialises in CEREC same-day crown technology, allowing patients with broken or cracked teeth to receive a custom ceramic restoration in a single appointment. The CEREC process uses CAD/CAM imaging to design, mill, and fit a porcelain crown within 2 hours, eliminating temporary crowns and return visits.",
        "Each location reserves daily emergency appointment slots for patients with broken teeth, severe toothache, or dental trauma. The practice offers sleep dentistry options for anxious patients requiring complex repair procedures. Melbourne Dental House participates with all major health funds through HICAPS and offers payment plans for extensive treatment.",
     ]},
    {"rank": 3, "name": "Precision Dental", "location": "Brisbane, QLD", "featured": True, "ahpra": True,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "520 Wickham Street, Fortitude Valley QLD 4006", "phone": "(07) 3852 1160",
     "website": "https://precisiondentistry.com.au",
     "body": [
        "Precision Dental is a Fortitude Valley practice offering CEREC same-day crowns and bridges for patients with broken, cracked, or severely damaged teeth. The practice uses digital 3D imaging and CAD/CAM manufacturing to produce custom ceramic restorations on-site, repairing fractured teeth in a single visit without traditional moulds or temporary crowns. Treatment options include composite bonding for minor chips, dental crowns for extensively fractured teeth, and root canal therapy for fractures involving the pulp.",
        "The practice provides free on-site parking for patients and serves Fortitude Valley, New Farm, Newstead, Teneriffe, Spring Hill, and Hamilton. Precision Dental offers pain-free dentistry with a focus on gentle treatment for anxious patients. The clinic accepts all major health funds and provides transparent pricing with written quotes before treatment.",
     ]},
    {"rank": 4, "name": "Connolly Dental Boutique", "location": "Perth, WA", "featured": False,
     "rating": "4.8/5 (145 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "Shop 4, 1 Glenelg Place, Connolly WA 6027", "phone": "(08) 9300 1122",
     "website": "https://www.connollydentalboutique.com.au",
     "body": [
        "Connolly Dental Boutique provides emergency broken tooth repair from its practice in Connolly, northern Perth. The practice offers same-day appointments for chipped, cracked, and fractured teeth using composite bonding, porcelain veneers, dental crowns, and root canal treatment. Treatment options are tailored to the severity of the fracture, from minor chip repair with tooth-coloured resin to full crown restoration for extensively damaged teeth. The clinic offers emergency booking for acute dental trauma.",
     ]},
    {"rank": 5, "name": "Dentistry on Unley", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (110 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Suites 1-4, 292-294 Unley Rd, Unley SA 5061", "phone": "(08) 8272 9087",
     "website": "https://dentistryonunley.com.au",
     "body": [
        "Dentistry on Unley reserves daily emergency appointments for patients with broken teeth, chipped teeth, and dental trauma in Adelaide. The practice uses CEREC same-day crown technology to repair extensively fractured teeth in a single visit, milling custom ceramic restorations on-site. Their services include composite bonding for minor chips, dental crowns for structural damage, root canal therapy for fractures involving the nerve, and porcelain veneers for aesthetic repair of front teeth. The clinic accepts all major health funds through HICAPS.",
     ]},
    {"rank": 6, "name": "Hobart Place Dental", "location": "Canberra, ACT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8:30am-5:00pm",
     "address": "10th Floor, AMP Building, Hobart Place, Canberra City ACT 2600", "phone": "(02) 6247 9230",
     "website": "https://hobartplacedental.com.au",
     "body": [
        "Hobart Place Dental provides emergency dental treatment for broken teeth from their Canberra City practice in the AMP Building. The clinic treats chipped teeth, fractured teeth, broken fillings, lost crowns, and dental abscesses resulting from untreated fractures. Their services include tooth-coloured fillings, crowns, bridges, veneers, and root canal therapy. The practice focuses on creating a friendly and caring environment with quality dental care for patients experiencing dental emergencies.",
     ]},
    {"rank": 7, "name": "ArtSmiles", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8:30am-5:00pm",
     "address": "Shop 4, 45/49 Nind St, Southport QLD 4215", "phone": "(07) 5588 3677",
     "website": "https://artsmiles.com.au",
     "body": [
        "ArtSmiles offers same-day emergency appointments for broken tooth repair from their Southport practice on the Gold Coast. The practice treats chipped teeth, cracked teeth, fractured teeth, and knocked-out teeth using composite bonding, dental crowns, veneers, and root canal therapy. ArtSmiles identifies the fracture type and extent before recommending the most appropriate repair. The clinic serves Southport, Bundall, Benowa, Ashmore, Labrador, and Main Beach with flexible finance options including Afterpay and Zip.",
     ]},
    {"rank": 8, "name": "Napol Dental", "location": "Hobart, TAS", "featured": False,
     "rating": "4.9/5 (90 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "1 Warneford St, Hobart TAS 7000", "phone": "(03) 6200 8800",
     "website": "https://www.napoldental.com.au",
     "body": [
        "Napol Dental is a Hobart dental practice led by Dr Clark Eom, a Doctor of Dental Medicine from the University of Sydney. The practice provides broken tooth repair including composite bonding, dental crowns, bridges, veneers, and root canal therapy. Dr Eom handles complex cases including dental implants and full-mouth rehabilitation for extensively damaged teeth. The clinic offers personalised treatment plans tailored to each patient's clinical needs and budget, with Saturday appointments available for patients unable to attend during business hours.",
     ]},
    {"rank": 9, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental operates two Newcastle locations in Wickham and Belmont, offering same-day emergency dental care 7 days a week for broken teeth, chipped teeth, and dental trauma. The practice provides comprehensive repair options including composite bonding, dental crowns, CEREC same-day restorations, and root canal therapy. Their restorative dentistry service covers fractures, structural damage, and tooth wear. The clinic serves Newcastle, Wickham, Belmont, and surrounding Hunter Region suburbs with online booking available.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides emergency broken tooth repair from its Coconut Grove practice in Darwin. The clinic treats cracked teeth, fractured teeth, chipped teeth, and oral lacerations resulting from dental trauma. Their services include composite bonding, dental crowns, root canal treatment, and surgical extractions for non-restorable fractures. Led by Dr Anand Murugappan, the practice offers sedation dentistry for anxious patients and handles complex restorative cases requiring general anaesthetic.",
     ]},
]

COST_HEADING = "How much does broken tooth repair cost in Australia?"
COST = [
    "Broken tooth repair costs in Australia range from $200 for minor composite bonding to $3,000 for complex root canal therapy on molar teeth. Treatment type determines the primary cost, with fracture severity, tooth location, and technology used as secondary factors.",
    'Five factors affect the final cost: severity of the fracture, tooth location (front teeth cost less to repair than molars), treatment complexity, clinic location (Sydney and Melbourne clinics charge 15 to 25% more than regional practices), and whether CEREC technology is used.',
]
COST_PRICES = [
    ("Composite bonding (minor chips)", "$200 - $500 per tooth"),
    ("Dental filling (tooth-coloured)", "$200 - $450"),
    ("Porcelain veneer (front tooth)", "$1,000 - $2,000"),
    ("Dental crown (ceramic or porcelain)", "$1,200 - $2,500"),
    ("CEREC same-day crown", "$1,300 - $2,500"),
    ("Root canal therapy", "$900 - $3,000"),
    ("Tooth extraction", "$200 - $400"),
]
COST_AFTER = [
    'Private health insurance with major dental cover typically rebates 60 to 80% of broken tooth repair costs. Most clinics on this list offer HICAPS instant claiming, allowing patients to pay only the gap. Read our comprehensive <a href="/blog/costs/">dental costs guide</a> for detailed pricing across all treatments including <a href="/australia/dental-crowns/">dental crowns</a>, <a href="/australia/dental-fillings/">dental fillings</a>, and <a href="/australia/root-canal-treatment/">root canal treatment</a>.',
]

CHOOSE_HEADING = "How do you choose a broken tooth repair clinic in Australia?"
CHOOSE_INTRO = "Five factors determine whether a clinic can handle your broken tooth effectively. Use this checklist before booking an appointment."
CHOOSE_CRITERIA = [
    ("Can the clinic see you within 24 hours?",
     'Broken teeth require prompt treatment to prevent pulp infection and tooth loss. Clinics with reserved daily emergency slots accommodate same-day or next-day appointments. Contact an <a href="/australia/emergency-dentist/">emergency dentist</a> immediately after the injury occurs.'),
    ("Does the clinic have CEREC same-day crown technology?",
     'CEREC milling machines produce custom ceramic <a href="/australia/dental-crowns/">dental crowns</a> in approximately 2 hours, eliminating the 2-week wait and temporary crown fittings associated with traditional laboratory-made crowns.'),
    ("What qualifications do the treating dentists hold?",
     "Verify AHPRA registration for every treating dentist. Clinics with specialist endodontists on staff handle complex root canal cases on-site without referral."),
    ("Does the clinic offer the full range of repair treatments?",
     'A single clinic providing <a href="/australia/dental-fillings/">dental fillings</a>, composite bonding, crowns, veneers, and <a href="/australia/root-canal-treatment/">root canal treatment</a> under one roof reduces travel time and ensures consistent treatment planning.'),
    ("Does the clinic accept your health fund?",
     'HICAPS-enabled clinics process claims instantly. Preferred provider status with your health fund reduces out-of-pocket costs. For non-restorable fractures requiring <a href="/australia/tooth-extraction/">tooth extraction</a>, confirm whether the clinic offers payment plans for follow-up implant or bridge work.'),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these broken tooth repair clinics?"
METHODOLOGY = [
    "We evaluated 47 Australian dental practices offering broken tooth repair against 8 criteria. Each clinic was assessed using publicly available data sourced from practice websites, AHPRA registration records, and verified Google review profiles.",
]
METHODOLOGY_CRITERIA = [
    "Emergency response time: same-day or next-day appointments for broken teeth and dental trauma",
    "Treatment range: bonding, fillings, crowns, veneers, and root canal therapy on-site",
    "CEREC technology: same-day crown manufacturing capability using CAD/CAM milling",
    "Dentist qualifications: current AHPRA registration with specialist endodontists or prosthodontists",
    "Diagnostic technology: digital X-rays, intraoral cameras, and CBCT scanners for fracture assessment",
    "Pricing transparency: published fee schedules or itemised quotes before treatment",
    "Patient outcomes: verified Google review scores above 4.5 out of 5",
    "Health fund partnerships: HICAPS instant claiming and preferred provider agreements",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for detailed scoring information.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("Can a broken tooth heal on its own?",
     'No. Tooth enamel contains no living cells, so structural damage is permanent without professional repair. Delaying treatment allows bacteria to enter the pulp chamber. Store any broken fragments in milk and see an <a href="/australia/emergency-dentist/">emergency dentist</a> within 24 hours.'),
    ("How long does broken tooth repair take?",
     'Composite bonding takes 30 to 60 minutes in one visit. <a href="/australia/dental-crowns/">Dental crowns</a> require 2 visits over 2 weeks, or a single 2-hour visit with CEREC technology. Root canal therapy requires 2 to 3 visits over 2 to 4 weeks.'),
    ("Is broken tooth repair covered by Medicare?",
     'Medicare covers dental repair only for children eligible under the Child Dental Benefits Schedule (up to $1,095 over 2 years). Adults need private health insurance with extras cover, which typically refunds 60 to 80% of repair costs. Read our <a href="/blog/costs/">dental costs guide</a> for detailed rebate information.'),
    ("What is the cheapest broken tooth repair option?",
     'Composite bonding at $200 to $500 per tooth is the cheapest option for minor chips and small fractures. <a href="/australia/dental-fillings/">Dental fillings</a> cost $200 to $450 and are completed in a single appointment.'),
    ("Can I superglue a broken tooth?",
     'No. Superglue contains cyanoacrylate, which is toxic to oral tissues and damages remaining tooth structure. Store the fragment in milk, saline, or saliva and bring it to an <a href="/australia/emergency-dentist/">emergency dentist</a> within 1 hour for possible reattachment.'),
    ("What should I do while waiting for a dental appointment?",
     'Rinse with warm salt water, apply a cold compress to reduce swelling, take ibuprofen or paracetamol for pain, avoid eating on the damaged side, and cover sharp edges with sugar-free gum or dental wax. Contact an <a href="/australia/emergency-dentist/">emergency dentist</a> for same-day assessment.'),
    ("How long can a broken tooth wait before treatment?",
     'A broken tooth should not wait longer than 24 hours. Bacteria colonise exposed dentin within hours, reaching the pulp within 48 hours. Seek same-day <a href="/australia/emergency-dentist/">emergency dental care</a> to prevent infection and preserve the tooth.'),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/broken-tooth-repair/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Broken tooth repair in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Broken Tooth Repair", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
