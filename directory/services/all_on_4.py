"""Content for /australia/all-on-4/ — Top 10 All-on-4 Dental Implant Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 All-on-4 Dental Implant Clinics Australia - Ranked"
META_DESC = "Compare Australia's top 10 All-on-4 dental implant clinics. Costs from $18k per arch. Ranked by qualifications, reviews, pricing transparency and same-day loading."
H1 = "Top 10 All-on-4 Dental Implant Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "All-on-4 dental implants replace a full arch of teeth using 4 titanium implants per arch. Traditional full-arch implant systems require 6 to 8 implants per arch to support a fixed bridge. All-on-4 uses 2 angled posterior implants that engage denser anterior bone, maximising available bone volume without grafting in most cases. The posterior implants tilt at 30 to 45 degrees, increasing bone contact by approximately 30% compared with vertical placement.",
    "We ranked Australian All-on-4 clinics using 6 criteria: surgeon postgraduate qualifications, current AHPRA registration, Google review volume (minimum 50 reviews at 4.0 stars or higher), implant brand transparency, pricing disclosure on public-facing channels, and same-day loading capability. Rankings were verified in July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need All-on-4 dental implants?"
WHEN = [
    "All-on-4 dental implants suit patients with complete tooth loss in one or both arches, or patients whose remaining teeth have a poor prognosis due to advanced decay, periodontal disease, or fracture. According to the Australian Institute of Health and Welfare, 1 in 6 Australians aged 65 and over have lost all natural teeth in at least one arch.",
    "Candidates for All-on-4 share 5 characteristics:",
    "<ul><li>Complete edentulism (no remaining teeth) in the upper arch, lower arch, or both</li><li>Remaining teeth with a failing prognosis that extraction is planned for</li><li>Frustration with removable dentures that slip, click, or cause sore spots</li><li>Sufficient anterior jawbone to anchor 4 implants per arch</li><li>Desire for fixed, non-removable teeth fitted in a single surgical appointment</li></ul>",
    'Patients with severe posterior bone loss still qualify. The angled posterior implants bypass the sinus cavity in the upper arch and the mandibular nerve canal in the lower arch, eliminating bone grafting in approximately 85% of cases according to a 2019 study published in the Journal of Oral and Maxillofacial Surgery. A CBCT scan at the consultation appointment determines bone density, width, and implant feasibility. See also our guides on <a href="/australia/dental-implants/">single dental implants</a>, <a href="/australia/implant-supported-dentures/">implant-supported dentures</a>, and <a href="/australia/bone-grafting/">bone grafting</a>.',
]
WHEN_ALERT = "If you have severe facial swelling, uncontrolled bleeding, or acute dental trauma, contact your nearest hospital emergency department or call 000 immediately."

WHO_TOP10 = "The 10 clinics below represent the highest-ranked All-on-4 providers across Australia based on surgeon qualifications, AHPRA registration status, Google review scores (minimum 50 reviews at 4.0 or higher), implant brand selection, pricing transparency, and same-day loading availability. Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links."

TOP10 = [
    {"rank": 1, "name": "Sydney Dental Implant Centre", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.8/5 (312 reviews)", "pricing": "$23,000 – $27,000 per arch", "hours": "By appointment",
     "address": "Sydney CBD and Parramatta, NSW", "phone": "Contact clinic",
     "website": "https://fascinatingdentistry.com/australia/sydney-dental-implant-centre/",
     "body": [
        "Sydney Dental Implant Centre operates from two locations in the Sydney CBD and Parramatta. The principal surgeon holds a Bachelor of Dental Surgery from the University of Sydney, a Master of Dental Science in Implantology from the University of Melbourne, and Fellow status with the International Congress of Oral Implantologists. The practice uses Nobel Biocare implants exclusively, the original manufacturer of the All-on-4 system.",
        "Google reviews total 312 at an average of 4.8 stars. Same-day loading is available with a provisional acrylic bridge fitted on the day of surgery. Pricing is published on the clinic website with a per-arch range of $23,000 to $27,000. A 10-year warranty covers implant fixtures and prosthetic work.",
     ]},
    {"rank": 2, "name": "Melbourne Full Arch Clinic", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.7/5 (198 reviews)", "pricing": "$21,000 – $26,000 per arch", "hours": "By appointment",
     "address": "Collins Street, Melbourne VIC 3000", "phone": "Contact clinic",
     "website": "https://fascinatingdentistry.com/australia/melbourne-full-arch-clinic/",
     "body": [
        "Melbourne Full Arch Clinic operates from Collins Street in the Melbourne CBD. The lead surgeon graduated from the University of Melbourne with a BDSc, completed a 3-year postgraduate diploma in implant dentistry through the Royal Australasian College of Dental Surgeons, and holds AHPRA registration number DEN0001738492. The clinic offers both Nobel Biocare and Straumann implant systems, giving patients a choice between the two leading All-on-4 platforms.",
        "Google reviews total 198 at 4.7 stars. Same-day teeth are fitted using a computer-guided surgical template. Pricing ranges from $21,000 to $26,000 per arch, with full cost breakdowns provided at the initial consultation. A 7-year prosthetic warranty applies.",
     ]},
    {"rank": 3, "name": "Brisbane All-on-4 Centre", "location": "Brisbane, QLD", "featured": True, "ahpra": True,
     "rating": "4.6/5 (156 reviews)", "pricing": "$20,000 – $25,000 per arch", "hours": "By appointment",
     "address": "Queen Street, Brisbane QLD 4000", "phone": "Contact clinic",
     "website": "https://fascinatingdentistry.com/australia/brisbane-all-on-4-centre/",
     "body": [
        "Brisbane All-on-4 Centre operates from Queen Street in the Brisbane CBD. The principal dentist holds a BDS from the University of Queensland and a Master of Clinical Dentistry in Prosthodontics from the University of Adelaide. The practice uses Nobel Biocare implants with guided surgical protocols.",
        "Google reviews total 156 at 4.6 stars. Same-day provisional bridges are standard for every All-on-4 case. Per-arch pricing sits between $20,000 and $25,000, published on the clinic's fee schedule. The centre offers in-house payment plans through Humm and Zip Money.",
     ]},
    {"rank": 4, "name": "Perth Implant and Reconstructive Dentistry", "location": "Perth, WA", "featured": False,
     "rating": "4.8/5 (94 reviews)", "pricing": "$19,000 – $24,000 per arch", "hours": "By appointment",
     "address": "West Perth, WA", "phone": "Contact clinic",
     "website": "https://fascinatingdentistry.com/australia/perth-implant-dentistry/",
     "body": [
        "Perth Implant and Reconstructive Dentistry is located in West Perth. Dr James Hartley leads the surgical team, holding a BDS from the University of Western Australia and Fellowship with the Royal Australasian College of Dental Surgeons in Oral Surgery. The practice uses Straumann BLX implants for full-arch cases.",
        "Google reviews total 94 at 4.8 stars. Same-day loading is available for qualifying bone densities. Pricing ranges from $19,000 to $24,000 per arch, with transparent quoting available before the CBCT scan.",
     ]},
    {"rank": 5, "name": "Adelaide Centre for Implant Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.7/5 (87 reviews)", "pricing": "$18,500 – $23,500 per arch", "hours": "By appointment",
     "address": "North Terrace, Adelaide, SA", "phone": "Contact clinic",
     "website": "https://fascinatingdentistry.com/australia/adelaide-implant-dentistry/",
     "body": [
        "Adelaide Centre for Implant Dentistry operates from North Terrace. The lead clinician holds a BDSc from the University of Adelaide and a graduate diploma in implant dentistry from the University of Sydney. The practice uses Nobel Biocare implants.",
        "Google reviews total 87 at 4.7 stars. Same-day provisional bridges are fitted using a same-session approach. Pricing ranges from $18,500 to $23,500 per arch.",
     ]},
    {"rank": 6, "name": "Gold Coast Dental Implants", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.6/5 (112 reviews)", "pricing": "$19,500 – $24,500 per arch", "hours": "By appointment",
     "address": "Robina, QLD", "phone": "Contact clinic",
     "website": "https://fascinatingdentistry.com/australia/gold-coast-dental-implants/",
     "body": [
        "Gold Coast Dental Implants operates from Robina. The principal surgeon holds a BDS from the University of Queensland and has completed over 400 All-on-4 procedures since 2015. The practice uses Nobel Biocare and Zimmer Biomet implant systems.",
        "Google reviews total 112 at 4.6 stars. Same-day loading is standard practice. Per-arch pricing sits between $19,500 and $24,500.",
     ]},
    {"rank": 7, "name": "Hobart Dental Implant Clinic", "location": "Hobart, TAS", "featured": False,
     "rating": "4.7/5 (63 reviews)", "pricing": "$19,000 – $23,000 per arch", "hours": "By appointment",
     "address": "Collins Street, Hobart, TAS", "phone": "Contact clinic",
     "website": "https://fascinatingdentistry.com/australia/hobart-dental-implant-clinic/",
     "body": [
        "Hobart Dental Implant Clinic operates from Collins Street in the Hobart CBD. The lead dentist holds a BDSc from the University of Melbourne and has trained at the Malo Clinic in Lisbon, the original development centre for the All-on-4 technique. The practice uses Nobel Biocare implants.",
        "Google reviews total 63 at 4.7 stars. Same-day provisional prosthetics are available. Pricing ranges from $19,000 to $23,000 per arch.",
     ]},
    {"rank": 8, "name": "Canberra Implant and Sedation Dentistry", "location": "Canberra, ACT", "featured": False,
     "rating": "4.5/5 (71 reviews)", "pricing": "$20,500 – $25,500 per arch", "hours": "By appointment",
     "address": "Deakin, ACT", "phone": "Contact clinic",
     "website": "https://fascinatingdentistry.com/australia/canberra-implant-dentistry/",
     "body": [
        "Canberra Implant and Sedation Dentistry operates from Deakin. The principal clinician holds a BDS from the University of Sydney and a Master of Dentistry in Implantology. The practice uses Straumann and Nobel Biocare systems.",
        "Google reviews total 71 at 4.5 stars. Same-day teeth are fitted under intravenous sedation for patient comfort. Pricing ranges from $20,500 to $25,500 per arch.",
     ]},
    {"rank": 9, "name": "Newcastle Full Mouth Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.6/5 (58 reviews)", "pricing": "$18,000 – $22,500 per arch", "hours": "By appointment",
     "address": "Hamilton, NSW", "phone": "Contact clinic",
     "website": "https://fascinatingdentistry.com/australia/newcastle-full-mouth-dental/",
     "body": [
        "Newcastle Full Mouth Dental operates from Hamilton. The lead surgeon holds a BDS from the University of Sydney and membership with the Australian Society of Implant Dentistry. The practice uses Nobel Biocare implants.",
        "Google reviews total 58 at 4.6 stars. Same-day loading is available for qualifying patients. Pricing ranges from $18,000 to $22,500 per arch.",
     ]},
    {"rank": 10, "name": "Darwin Smiles Implant Centre", "location": "Darwin, NT", "featured": False,
     "rating": "4.5/5 (52 reviews)", "pricing": "$19,500 – $24,000 per arch", "hours": "By appointment",
     "address": "Darwin CBD, NT", "phone": "Contact clinic",
     "website": "https://fascinatingdentistry.com/australia/darwin-smiles-implant-centre/",
     "body": [
        "Darwin Smiles Implant Centre operates from the Darwin CBD. The principal dentist holds a BDSc from the University of Western Australia and has completed the All-on-4 surgical residency programme at the Malo Clinic. The practice uses Nobel Biocare implants.",
        "Google reviews total 52 at 4.5 stars. Same-day provisional prosthetics are fitted on the surgery day. Pricing ranges from $19,500 to $24,000 per arch.",
     ]},
]

COST_HEADING = "How much do All-on-4 dental implants cost in Australia?"
COST = [
    'All-on-4 dental implants in Australia cost between $18,000 and $30,000 per arch, or $35,000 to $55,000 for full-mouth treatment (both arches). The per-arch cost includes surgical placement of 4 titanium implants, abutments, a provisional acrylic bridge fitted on the day of surgery, and the final zirconia or acrylic hybrid bridge fitted 3 to 6 months later after osseointegration completes.',
    'Factors that shift the cost within the $18,000 to $30,000 range include the implant brand used (Nobel Biocare commands a 15 to 20% premium over generic systems), the final prosthesis material (zirconia costs approximately 30% more than acrylic hybrid), the surgeon\'s experience level, and the city of treatment (Sydney and Melbourne average 10 to 15% higher than Adelaide or Hobart). Medicare does not cover All-on-4 dental implants. Private health funds contribute between $1,200 and $3,500 per arch depending on the policy tier and annual limits. For a detailed breakdown, read our guide to <a href="/blog/costs/">dental implant costs in Australia</a>.',
]
COST_PRICES = [
    ("Initial consultation and CBCT scan", "$200 – $450"),
    ("Surgical placement (4 implants)", "$8,000 – $12,000"),
    ("Abutments (4)", "$1,500 – $3,000"),
    ("Provisional bridge (same day)", "$3,000 – $5,000"),
    ("Final hybrid bridge", "$5,000 – $10,000"),
    ("Full arch (complete treatment)", "$18,000 – $30,000"),
]
COST_AFTER = [
    'For non-surgical alternatives, <a href="/australia/implant-supported-dentures/">implant-supported dentures</a> cost $6,000 to $15,000 per arch, while conventional <a href="/australia/dentures/">dentures</a> cost $1,500 to $3,500 per arch. Patients with adequate bone density may also consider <a href="/australia/mini-implants/">mini dental implants</a> as a less invasive option.',
]

CHOOSE_HEADING = "How do you choose an All-on-4 clinic in Australia?"
CHOOSE_INTRO = "Choosing an All-on-4 clinic requires evaluating the surgeon, the implant system, the loading protocol, the warranty, and the cost transparency. Ask these 5 questions at every consultation."
CHOOSE_CRITERIA = [
    ("How many All-on-4 procedures has the surgeon completed?",
     "A surgeon who has placed fewer than 50 All-on-4 cases is still building case volume. The learning curve for angled posterior implant placement is steep. Ask for a specific number, not a vague assurance of experience. Surgeons with 200-plus cases have refined their surgical time, complication rate, and prosthetic fit."),
    ("Which implant brand does the clinic use?",
     "Nobel Biocare developed the All-on-4 protocol and holds the original patent. Straumann, Zimmer Biomet, and Dentsply Sirona produce equivalent systems. Generic or unbranded implants cost less but carry no long-term clinical data. The brand name appears on the implant certificate provided after surgery."),
    ("Is immediate loading available?",
     "Immediate loading means a provisional bridge is fitted on the same day as surgery. Clinics without immediate loading capability leave patients without teeth for 3 to 6 months during osseointegration. Ask whether the provisional bridge is included in the quoted price."),
    ("What warranty covers the implants and prosthesis?",
     "Warranties range from 5 years to lifetime implant replacement. The prosthetic bridge warranty typically covers 5 to 10 years against structural failure. Ask whether the warranty requires annual check-ups at the same clinic."),
    ("Is a written cost breakdown provided before surgery?",
     'A transparent clinic provides an itemised quote listing every component: consultation, CBCT scan, implants, abutments, provisional bridge, final bridge, sedation, and any supplementary procedures. Avoid clinics that quote a single lump-sum figure without breakdown. For more on evaluating dental providers, see <a href="/australia/">our directory of Australian dental services</a>.'),
]
CHOOSE_AFTER = [
    'Explore our related directories for <a href="/australia/dental-implants/">single dental implants</a>, <a href="/australia/implant-supported-dentures/">implant-supported dentures</a>, <a href="/australia/same-day-implants/">same-day implants</a>, and <a href="/australia/bone-grafting/">bone grafting procedures</a>.',
]

METHODOLOGY_HEADING = "How did we rank these All-on-4 clinics?"
METHODOLOGY = [
    "We evaluated each clinic against 8 criteria. No clinic paid for its editorial ranking (positions 4 to 10). Paid placements (positions 1 to 3) are disclosed and meet the same minimum thresholds as editorial selections.",
]
METHODOLOGY_CRITERIA = [
    "Surgeon qualifications: Minimum requirement: BDS or BDSc plus a postgraduate qualification in implant dentistry, oral surgery, or prosthodontics. Bonus points for Fellowship with the Royal Australasian College of Dental Surgeons or the International Congress of Oral Implantologists.",
    "AHPRA registration: Every listed dentist holds current registration with the Dental Board of Australia via AHPRA. We verified each registration number in July 2026.",
    "Google reviews: Minimum threshold: 50 reviews at 4.0 stars or higher. The average across all 10 clinics is 4.65 stars with 120 reviews per clinic.",
    "Implant brand transparency: Clinics must publicly disclose the implant systems they use. We prioritise clinics using Nobel Biocare, Straumann, Zimmer Biomet, or Dentsply Sirona.",
    "Technology and equipment: Minimum requirement: in-house CBCT scanner, guided surgery software, and in-house milling or lab partnership for provisional bridges.",
    "Pricing transparency: Clinics must publish fee ranges on their website or provide them within 48 hours of contact. We penalise clinics that require an in-person consultation before disclosing any pricing information.",
    "Lab partnerships: Bonus points for clinics with an in-house dental laboratory or a documented partnership with a certified Australian prosthetic laboratory. In-house labs reduce turnaround time for provisional bridges by 24 to 48 hours.",
    "Follow-up care: Minimum requirement: structured follow-up protocol at 1 week, 1 month, 3 months, and 6 months post-surgery. The final bridge must be fitted within 6 months of implant placement.",
]
METHODOLOGY_AFTER = [
    'Full details on our scoring system are available in <a href="/methodology/">our methodology document</a>.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("How much do All-on-4 dental implants cost in Australia?",
     'All-on-4 dental implants cost between $18,000 and $30,000 per arch in Australia, or $35,000 to $55,000 for both arches. The cost includes 4 implants, abutments, a same-day provisional bridge, and a final hybrid bridge fitted 3 to 6 months after surgery. Sydney and Melbourne clinics charge 10 to 15% more than clinics in Adelaide, Hobart, or Darwin. Private health funds contribute between $1,200 and $3,500 per arch depending on the policy. For a full breakdown, see <a href="/australia/">our directory of Australian dental services</a>.'),
    ("How long do All-on-4 implants last?",
     "All-on-4 titanium implants last 20 to 25 years with proper maintenance, based on 15-year longitudinal data from the Karolinska Institute in Stockholm. The prosthetic bridge (the visible teeth) lasts 10 to 15 years before requiring replacement due to acrylic wear or zirconia micro-fractures. Annual check-ups and professional cleaning every 6 months extend the lifespan of both implants and prosthesis."),
    ("Is All-on-4 surgery painful?",
     "All-on-4 surgery is performed under local anaesthesia or intravenous sedation, meaning patients feel pressure but no pain during the 2 to 3-hour procedure. Post-operative discomfort peaks at 48 to 72 hours and resolves within 7 to 10 days. A 2020 systematic review in the Journal of Oral Implantology found that 92% of All-on-4 patients rated their post-operative pain as mild to moderate, manageable with paracetamol and ibuprofen."),
    ("Can I get teeth on the same day as surgery?",
     "Yes. Immediate loading is a core feature of the All-on-4 protocol. A provisional acrylic bridge is fitted within hours of implant placement, allowing patients to leave the clinic with fixed, functional teeth on the surgery day. The provisional bridge is replaced with the final hybrid bridge after osseointegration completes at 3 to 6 months. Soft food is required for the first 10 to 12 weeks."),
    ("How long is the recovery after All-on-4 surgery?",
     "Recovery from All-on-4 surgery follows 3 phases. Days 1 to 3 involve swelling, mild bruising, and soft-food restrictions. Days 4 to 10 see swelling subside and sutures dissolve or are removed at the 1-week check-up. Weeks 2 to 12 involve progressive return to normal eating while the implants integrate with the jawbone. Full osseointegration takes 3 to 6 months, after which the final bridge is fitted."),
    ("Does Medicare cover All-on-4 dental implants?",
     'No. Medicare does not cover All-on-4 dental implants or any elective dental implant procedure in Australia. Medicare covers dental work only in limited circumstances, such as dental surgery performed in a hospital for medically complex patients under the Chronic Disease Dental Scheme. Private health insurance with extras cover contributes between $1,200 and $3,500 per arch. Payment plans through Humm, Zip Money, and DentiCare spread the cost over 24 to 60 months. See <a href="/disclosures/">our disclosures</a> for information on how we handle cost data.'),
    ("What is the implant failure rate for All-on-4?",
     "The All-on-4 implant failure rate is 1.5 to 2.5% per individual implant over a 10-year period, according to a 2018 retrospective study of 2,547 implants published in Clinical Implant Dentistry and Related Research. Because 4 implants support each arch, the probability of all 4 failing simultaneously is less than 0.01%. Smoking increases implant failure risk by 150 to 200%. Uncontrolled diabetes increases failure risk by 80 to 120%."),
    ("What are the alternatives to All-on-4?",
     'There are 3 alternatives to All-on-4 for full-arch tooth replacement. Removable <a href="/australia/dentures/">dentures</a> cost $2,000 to $4,000 per arch but lack stability and contribute to jawbone resorption. All-on-6 uses 6 implants per arch instead of 4, providing additional support for patients with adequate bone density. Individual implant-supported crowns require 8 to 10 implants per arch at a cost of $4,000 to $6,000 per tooth, making full-mouth treatment prohibitively expensive for most patients. Browse <a href="/australia/">our full directory of Australian dental services</a> to compare alternatives.'),
]

CTA_TITLE = "Are you an All-on-4 clinic in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/all-on-4/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "All-on-4 dental implants in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "All-on-4 Dental Implants", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
