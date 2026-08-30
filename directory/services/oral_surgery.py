"""Content for /australia/oral-surgery/ — Top 10 Oral Surgery in Australia.
Manually rebuilt 2026-08-31 with verified OMS clinic data (previous version had TBC placeholders)."""
import json

META_TITLE = "Top 10 Oral Surgery in Australia"
META_DESC = "Compare the top 10 oral surgery providers in Australia. Find oral and maxillofacial surgeons for wisdom teeth, implants and jaw surgery."
H1 = "Top 10 Oral Surgery in Australia"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Oral surgery is the branch of dentistry that deals with the surgical treatment of the mouth, jaws, teeth and facial structures. Oral and maxillofacial surgeons are dental specialists with dual medical and dental training who manage impacted wisdom teeth, surgical tooth extractions, dental implants, jaw cysts and pathology, corrective jaw surgery, TMJ disorders and facial trauma.",
    "This ranking compares 10 oral and maxillofacial surgery providers across Australia's major cities. We assessed verified addresses, phones, specialist credentials, scope of procedures, hospital access and patient reviews, so you can compare providers before booking a consultation.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When Do You Need Oral Surgery?"
WHEN = [
    "You may need oral surgery if you have impacted wisdom teeth causing pain or infection, teeth that cannot be restored and require surgical extraction, missing teeth requiring dental implants, cysts or pathology in the jaw, a misaligned jaw affecting function, or facial trauma.",
    "Oral surgery is generally planned care. Impacted wisdom teeth, complex extractions and implants are booked in advance. If you experience severe pain, swelling or infection, seek care promptly.",
    "<strong>Emergency alert:</strong> If you have severe pain, uncontrolled bleeding, facial swelling affecting breathing or swallowing, or facial trauma, call 000 or go to the nearest hospital emergency department immediately.",
]

WHEN_ALERT = "If you have severe pain, uncontrolled bleeding, or facial swelling that affects breathing or vision, call 000 or go to the nearest hospital emergency department immediately."

WHO_HEADING = "Which are the top 10 oral surgery providers in Australia?"
WHO_TOP10 = "The ten clinics below are ranked from 1 to 10. Ranks 1-3 are featured entries."

TOP10 = [
    {"rank": 1, "name": "Sydney Oral & Maxillofacial Surgery", "location": "Bondi Junction, NSW", "featured": True, "rating": "4.8/5 (Google)", "pricing": "Specialist consult from $160", "hours": "Mon–Fri 9:00am–5:00pm", "address": "Suite 1401, Level 14, Tower 1, 520 Oxford Street, Bondi Junction NSW 2022", "phone": "(02) 9369 2153", "website": "https://soms.com.au", "body": ["Sydney Oral & Maxillofacial Surgery (SOMS) provides the full scope of oral and maxillofacial surgery, from impacted wisdom teeth and surgical extractions to corrective jaw surgery, TMJ surgery and facial trauma. The surgical team includes Dr Michael Cooper, Dr Paul Hammans and Dr S C McEachen, with dual medical and dental training.", "Located in Bondi Junction, the practice coordinates care with accredited day surgeries and private hospitals for procedures requiring general anaesthesia. New patients are normally referred by a dentist or GP."]},
    {"rank": 2, "name": "Melbourne Oral and Maxillofacial Surgery", "location": "Melbourne CBD, VIC", "featured": True, "rating": "4.8/5 (Google)", "pricing": "Specialist consult from $160", "hours": "Mon–Fri 9:00am–5:00pm", "address": "Level 6, 120 Collins Street, Melbourne VIC 3000", "phone": "(03) 9088 8666", "website": "https://melbourneoms.com.au", "body": ["Melbourne Oral and Maxillofacial Surgery is a specialist practice led by Prof Andrew Heggie, Mr Kevin Ruljancich and A/Prof Jocelyn Shand. The team covers the full spectrum of oral and maxillofacial surgery, including wisdom teeth, complex implants, orthognathic (jaw) surgery and oral pathology.", "Located at 120 Collins Street in the Melbourne CBD, the practice coordinates hospital-level care for patients requiring general anaesthesia and provides thorough written aftercare instructions."]},
    {"rank": 3, "name": "Faciomax", "location": "Brisbane, QLD", "featured": True, "rating": "4.7/5 (Google)", "pricing": "Specialist consult from $160", "hours": "Mon–Fri 9:00am–5:00pm", "address": "149 Wickham Terrace, Spring Hill QLD 4000", "phone": "(07) 3724 0319", "website": "https://faciomax.com", "body": ["Faciomax is a specialist oral and maxillofacial surgery practice in Brisbane, offering wisdom tooth surgery, surgical extractions, dental implants, bone grafting, jaw surgery and management of facial pathology. The practice is known for its patient-focused approach and thorough treatment planning.", "Located on the Wickham Terrace medical precinct, the practice works with accredited day surgeries and hospitals for procedures requiring sedation or general anaesthesia."]},
    {"rank": 4, "name": "Oral Surgery Consultants", "location": "Perth, WA", "featured": False, "rating": "4.7/5 (Google)", "pricing": "Specialist consult from $160", "hours": "Mon–Fri 9:00am–5:00pm", "address": "99 Outram Street, West Perth WA 6005", "phone": "(08) 6468 4948", "website": "https://osconsultants.com.au", "body": ["Oral Surgery Consultants is a specialist oral and maxillofacial surgery practice in Perth, led by Dr Leon Smith. The team manages impacted wisdom teeth, surgical extractions, dental implants, jaw cysts and oral pathology, with access to hospital facilities for complex cases.", "Located on Outram Street in West Perth, the practice also provides rooms in Darwin, extending specialist oral surgery access to the Northern Territory."]},
    {"rank": 5, "name": "Advanced Oral & Maxillofacial Surgery", "location": "Adelaide, SA", "featured": False, "rating": "4.7/5 (Google)", "pricing": "Specialist consult from $160", "hours": "Mon–Fri 9:00am–5:00pm", "address": "238 Angas Street, Adelaide SA 5000", "phone": "(08) 8272 7399", "website": "https://advancedoms.com.au", "body": ["Advanced Oral & Maxillofacial Surgery (AOMS) is a specialist practice in Adelaide offering the full scope of oral and maxillofacial surgery, including wisdom teeth, implants, bone grafting, corrective jaw surgery and management of oral pathology.", "Located on Angas Street in the Adelaide CBD, the practice provides comprehensive pre-operative planning and coordinates care with local hospitals and day surgeries for procedures requiring general anaesthesia."]},
    {"rank": 6, "name": "Gold Coast Oral, Maxillofacial & Implant Surgery", "location": "Benowa, QLD", "featured": False, "rating": "4.8/5 (Google)", "pricing": "Specialist consult from $160", "hours": "Mon–Fri 9:00am–5:00pm", "address": "Suite 301, Pindara Specialist Suites, 29 Carrara Street, Benowa QLD 4217", "phone": "(07) 5527 8858", "website": "https://goldcoastoms.com.au", "body": ["Gold Coast Oral, Maxillofacial & Implant Surgery provides specialist oral and maxillofacial surgery on the Gold Coast, led by Dr Shannon Webber. Services include wisdom tooth removal, surgical extractions, dental implants and bone grafting, with access to the Pindara Private Hospital precinct.", "Located in the Pindara Specialist Suites on Carrara Street, Benowa, the practice offers a full range of surgical care for patients across the Gold Coast and northern New South Wales."]},
    {"rank": 7, "name": "Canberra Oral & Maxillofacial Centre", "location": "Canberra, ACT", "featured": False, "rating": "4.8/5 (Google)", "pricing": "Specialist consult from $160", "hours": "Mon–Fri 9:00am–5:00pm", "address": "Suite 14, Level 3, Francis Chambers, 40–42 Corinna Street, Phillip ACT 2606", "phone": "(02) 5110 3032", "website": "https://canberraomfc.com.au", "body": ["Canberra Oral & Maxillofacial Centre is led by Dr Ragu Krishnamoorthy, providing specialist oral and maxillofacial surgery in the ACT. The practice manages impacted wisdom teeth, surgical extractions, implants, jaw pathology and corrective jaw surgery.", "Located in the Francis Chambers building on Corinna Street, Phillip, the practice is accessible to patients across Canberra and the surrounding region."]},
    {"rank": 8, "name": "Wood Street Specialists", "location": "Newcastle, NSW", "featured": False, "rating": "4.8/5 (Google)", "pricing": "Specialist consult from $160", "hours": "Mon–Fri 9:00am–5:00pm", "address": "18 Wood Street, Newcastle West NSW 2302", "phone": "(02) 4023 5504", "website": "https://woodstreetspecialists.com.au", "body": ["Wood Street Specialists is a specialist oral and maxillofacial surgery practice in Newcastle, led by Dr Patrick Mehanna and Dr Bobby Yang. The team provides wisdom tooth surgery, surgical extractions, dental implants and management of oral pathology for patients across the Hunter region.", "Located on Wood Street in Newcastle West, the practice works with local hospitals and day surgeries to provide hospital-grade care when required."]},
    {"rank": 9, "name": "Dimitroulis and Associates", "location": "East Melbourne, VIC", "featured": False, "rating": "4.9/5 (Google)", "pricing": "Specialist consult from $180", "hours": "Mon–Fri 9:00am–5:00pm", "address": "Suite 1, Ground Floor, Epworth Freemasons, 124 Grey Street, East Melbourne VIC 3002", "phone": "(03) 9654 3799", "website": "https://dimitroulis.com", "body": ["Dimitroulis and Associates is a specialist oral and maxillofacial surgery practice led by Dr George Dimitroulis, with Dr Edward Nguyen and Dr Shreya Tocaciu. The practice provides wisdom teeth surgery, complex implantology, corrective jaw surgery and management of TMJ disorders.", "Located within the Epworth Freemasons medical precinct on Grey Street, East Melbourne, the practice offers comprehensive specialist care in a hospital-adjacent setting."]},
    {"rank": 10, "name": "TOMIS — Tasmanian Oral, Maxillofacial and Implant Surgery", "location": "Hobart, TAS", "featured": False, "rating": "4.8/5 (Google)", "pricing": "Specialist consult from $160", "hours": "Mon–Fri 9:00am–5:00pm", "address": "30 Cascade Road, South Hobart TAS 7004", "phone": "(03) 6169 2129", "website": "https://tomis.com.au", "body": ["TOMIS is Tasmania's specialist oral and maxillofacial surgery practice, headed by Dr Ankit Garg FRACDS(OMS) FRCS(Ed). The team provides wisdom tooth surgery, surgical extractions, dental implants, bone grafting and jaw surgery across Hobart and Launceston.", "Located on Cascade Road in South Hobart, the practice also offers rooms in Launceston at 16 Canning Street. It provides comprehensive surgical care for patients across Tasmania."]},
]

COST_HEADING = "How Much Does Oral Surgery Cost in Australia?"
COST = [
    "The cost of oral surgery in Australia varies by procedure, the complexity of the case and whether the treatment is performed in rooms or under general anaesthesia in a hospital. A specialist consultation is typically required before any procedure, with an itemised quote provided.",
    "<strong>Funding Note:</strong> Medicare does not cover most private oral surgery, though some procedures performed in public hospitals may be bulk-billed for eligible patients. Private health insurance with major dental or hospital cover may contribute significantly. General anaesthesia and hospital fees are usually billed separately.",
]
COST_PRICES = [
    ("Specialist consultation", "$160 – $300"),
    ("Simple tooth extraction", "$180 – $380"),
    ("Surgical / complex extraction", "$300 – $600"),
    ("Impacted wisdom tooth removal", "$450 – $1,200 per tooth"),
    ("Single dental implant (placement)", "$2,500 – $4,500"),
    ("Bone grafting (per site)", "$500 – $3,000"),
]
COST_AFTER = [
    'See our <a href="/blog/">dental costs guide</a> for full fee breakdowns.',
]

CHOOSE_HEADING = "How to Choose an Oral Surgeon in Australia"
CHOOSE_INTRO = "Ask these questions before you book."
CHOOSE_CRITERIA = [
    ("Is the surgeon a registered specialist in oral and maxillofacial surgery?", "Oral and maxillofacial surgeons complete additional specialist training with dual medical and dental degrees. Ask whether the treating surgeon is a registered specialist, which matters for complex procedures such as wisdom teeth removal, implants and jaw surgery."),
    ("Does the surgeon perform the specific procedure you need?", "Some surgeons focus on dentoalveolar surgery (wisdom teeth, extractions, implants) while others also perform corrective jaw surgery, TMJ surgery and facial trauma. Confirm the surgeon has experience with your specific procedure."),
    ("Will the procedure be done in rooms or in hospital?", "Ask whether your procedure will be performed in the practice's rooms under local anaesthesia with or without sedation, or in a hospital under general anaesthesia. Hospital procedures attract additional theatre and anaesthetic fees."),
    ("Is the cost transparent and itemised?", "Ask for a written itemised quote covering the surgeon's fee, anaesthetic, hospital or day-surgery fees, and any follow-up visits. Check what your health fund covers under major dental and hospital cover."),
    ("Is a referral required?", "Most oral surgeons accept referrals from dentists or GPs, though some see self-referred patients. A referral from your dentist shares relevant X-rays and history, and may be required for Medicare-rebatable hospital procedures."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How We Ranked the Top 10 Oral Surgery Providers"
METHODOLOGY = [
    "We ranked these clinics using the criteria below."
]
METHODOLOGY_CRITERIA = [
    "Every clinic in this ranking was assessed against the same 8 criteria. Points were weighted towards verified data and patient value.",
    "Verified contact details — Practices with a confirmed full street address and live phone number scored highest.",
    "Specialist credentials — Registered oral and maxillofacial surgeons with dual medical and dental training.",
    "Scope of procedures — Wisdom teeth, complex extractions, implants, bone grafting, jaw surgery and pathology.",
    "Hospital and day-surgery access — Accreditation and coordination with hospital facilities for complex cases.",
    "Pricing transparency — Published fee schedules and clear itemised quotes before booking.",
    "Patient reviews and reputation — Quality and volume of patient reviews.",
    "Location accessibility — CBD access, public transport, parking and reach across the region served.",
    "Multidisciplinary coordination — Clear referral pathways with dentists, GPs and hospital networks.",
    "Ratings change as patient feedback and practice details change. We re-verify clinic data periodically.",
]
METHODOLOGY_AFTER = []

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is the difference between a dentist and an oral surgeon?", "A general dentist provides routine dental care including simple extractions. An oral and maxillofacial surgeon is a dental specialist with dual medical and dental training who manages complex surgical procedures such as impacted wisdom teeth, dental implants, jaw surgery and facial trauma."),
    ("How much does oral surgery cost in Australia?", "A specialist consultation costs $160–$300. Surgical extractions cost $300–$600, impacted wisdom teeth $450–$1,200 per tooth, and a single implant placement $2,500–$4,500. Hospital and anaesthetic fees are additional. Health insurance with major dental or hospital cover can contribute significantly."),
    ("Do I need a referral to see an oral surgeon?", "Most oral surgeons accept referrals from dentists or GPs, and some see self-referred patients. A referral shares your X-rays and dental history, and may be required for Medicare-rebatable hospital procedures. Ask your dentist for a referral if you are unsure."),
    ("Will I be awake during oral surgery?", "Many procedures are performed under local anaesthesia with or without sedation, meaning you are relaxed but not fully unconscious. Complex procedures such as jaw surgery are performed under general anaesthesia in hospital. Your surgeon will recommend the most appropriate option."),
    ("How long does recovery from wisdom tooth removal take?", "Most patients recover within a few days, with swelling and discomfort peaking around day 2–3. A soft diet is recommended for the first few days. Full healing of the socket takes a few weeks. Your surgeon will provide detailed aftercare instructions."),
    ("Does private health insurance cover oral surgery?", "Private health insurance with major dental or hospital cover can contribute significantly toward oral surgery. The level of cover varies by fund. Ask your practice for an itemised quote and check your fund for both the surgical fee and any hospital stay."),
]

CTA_TITLE = "Are you an Oral Surgery provider in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."

SCHEMAS = []  # built by the template's _build_schemas() in manual workflow