"""Content for /australia/sinus-lift/ — Top 10 Sinus Lift Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Sinus Lift Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 sinus lift clinics in Australia. Costs from $1,500 to $4,000 for sinus augmentation. Find qualified implant specialists near you."
H1 = "Top 10 Sinus Lift Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "A sinus lift is a bone grafting procedure that raises the maxillary sinus membrane to create additional bone height for dental implant placement in the posterior upper jaw. Oral surgeons, periodontists, and implant specialists perform this procedure when the sinus cavity sits too close to the alveolar ridge, leaving insufficient residual bone to support an implant fixture. The surgery involves opening a lateral window or crestal approach in the maxillary wall, gently elevating the Schneiderian membrane, grafting the new space with autogenous or xenogeneic bone material, and allowing 4 to 9 months of healing before implant placement.",
    "We ranked Australia's top sinus lift clinics based on six criteria: specialist qualifications and AHPRA registration, documented implant survival rates, annual sinus lift case volume, infection control protocols, transparent pricing, and verified patient review scores. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "What is a sinus lift and when do you need one?"
WHEN = [
    'A sinus lift is a specific type of <a href="/australia/bone-grafting/">bone grafting</a> procedure designed to augment the maxillary jawbone. Surgeons perform this surgery to increase vertical bone height, which provides a solid foundation for <a href="/australia/dental-implants/">dental implants</a>.',
    "Two primary surgical techniques exist for maxillary sinus augmentation. The lateral window technique involves creating a small opening in the side of the maxilla to access and elevate the Schneiderian membrane. The crestal approach accesses the sinus floor through the tooth socket site, which suits patients needing a smaller augmentation volume.",
    'Dental specialists recommend sinus grafting when residual bone height measures less than 4mm to 5mm. Tooth loss causes sinus pneumatization, a process where the sinus cavity expands downward and reduces available jawbone. Periodontal disease, long-term edentulism, and traumatic extractions also degrade maxillary bone density. Patients experiencing these structural changes can refer to our comprehensive <a href="/blog/conditions/">dental conditions guide</a> for diagnostic insights.',
    'Dental professionals utilise Cone Beam Computed Tomography (CBCT) imaging as the diagnostic standard for measuring bone dimensions and planning the surgical approach. Following the sinus graft procedure, the bone material requires 4 to 9 months to integrate solidly before surgeons can place the titanium implant fixture. Review our detailed <a href="/blog/treatments/">dental treatments guide</a> to understand the full oral rehabilitation timeline.',
]
WHEN_ALERT = "If you have severe facial swelling, uncontrolled bleeding, or acute dental trauma, contact your nearest hospital emergency department or call 000 immediately."

WHO_TOP10 = "These 10 practices represent the best sinus lift surgery across Sydney, Melbourne, Brisbane, the Gold Coast, Perth, Adelaide, Canberra, and Newcastle. Each entry includes verified contact details, pricing tier, Google rating, and specialist qualifications sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Sydney Periodontics and Implant Centre", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.8/5 (85 reviews)", "pricing": "Premium", "hours": "Mon-Fri 8:00am-5:30pm by appointment",
     "address": "Level 6, 64 Castlereagh Street, Sydney NSW 2000", "phone": "(02) 9221 5499",
     "website": "https://sydneyperio.com.au",
     "body": [
        "Specialist periodontal clinic in the Sydney CBD focused exclusively on gum treatment, bone grafting, and dental implants. The practice uses CBCT imaging to plan sinus grafting procedures and determine whether simultaneous implant placement is possible. Sinus lift procedures are performed using both lateral window and crestal approaches depending on residual bone height.",
        "The clinic accepts referrals and self-referrals. No referral is required to book a consultation. The practice is located on Castlereagh Street near Town Hall station.",
     ]},
    {"rank": 2, "name": "Toothsome", "location": "Sydney (Chatswood), NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (210 reviews)", "pricing": "Premium", "hours": "Mon-Fri 9:00am-5:00pm",
     "address": "Suite 8A, 499 Windsor Road, Baulkham Hills NSW 2153 (also at Chatswood)", "phone": "(02) 9686 8018",
     "website": "https://toothsome.com.au",
     "body": [
        "Specialist dental clinic with multiple Sydney locations including Chatswood Private Hospital and Baulkham Hills. The team includes Dr David Willis, a qualified Medical Doctor and Dental Surgeon with over 20 years of experience, Dr Patty Chou, a Specialist Periodontist with over 15 years of periodontal surgery experience, and Dr Alun Cheng, a Specialist Periodontist with advanced training in periodontal regeneration and dental implants.",
        "The practice handles complex sinus lift and bone grafting cases and uses specialist-led treatment planning for all implant procedures. Toothsome operates across five locations including Chatswood, Baulkham Hills, and Lakeview Private Hospital.",
     ]},
    {"rank": 3, "name": "Pure Dentistry", "location": "Brisbane, QLD", "featured": True, "ahpra": True,
     "rating": "4.6/5 (330 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "11/1932-1974 Logan Road, Upper Mount Gravatt QLD 4122", "phone": "(07) 3343 4869",
     "website": "https://www.puredentistry.com.au",
     "body": [
        "Pure Dentistry provides dental implant treatment including sinus lift procedures from their Upper Mount Gravatt facility. The lead implant dentist is Dr Matthew Peyravi (BDentHSc, MDent from Griffith University, AHPRA Registration: DEN0002683865), who has a special interest in implant dentistry. The clinic offers the complete implant process in one location from initial CBCT imaging through to surgical placement and crown fitting.",
        "Sedation options including nitrous oxide, IV twilight sedation, and general anaesthesia are available for anxious patients. The practice uses computer-fabricated surgical guides for precise implant placement and works with multiple implant systems including Neodent, MIS, and Bredent. Pure Dentistry operates seven days a week.",
     ]},
    {"rank": 4, "name": "With U Dental", "location": "Melbourne (Hawthorn East), VIC", "featured": False,
     "rating": "4.9/5 (197 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat 8:30am-5:00pm",
     "address": "2 Wills St, Hawthorn East VIC 3123", "phone": "(03) 8820 1119",
     "website": "https://withudental.com.au",
     "body": [
        "With U Dental in Hawthorn East performs sinus lift and bone grafting procedures as part of their implant dentistry service. The practice combines Korean dental aesthetics with care from dentists who also teach at Melbourne University and the Implant Institute. The clinic is adjacent to Camberwell Station and offers on-site parking.",
        "The sinus lift procedure at With U Dental involves carefully lifting the sinus membrane and adding bone graft material to create sufficient space and support for future implants.",
     ]},
    {"rank": 5, "name": "Perth Prime Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.7/5 (140 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "1/58 St Georges Terrace, Perth WA 6000", "phone": "(08) 9325 4175",
     "website": "https://perthprimedental.com.au",
     "body": [
        "Perth Prime Dental offers sinus lift procedures from their St Georges Terrace location in the Perth CBD. The practice performs sinus lifts under local anaesthesia, gently lifting the sinus membrane and placing bone graft material into the space. In some cases the bone graft material can be placed through the same channel used for implant placement.",
        "The clinic also offers All-on-4 implants, general dentistry, and cosmetic dental services.",
     ]},
    {"rank": 6, "name": "Lidums Dental", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (175 reviews)", "pricing": "Premium", "hours": "Mon-Fri 8:00am-5:30pm",
     "address": "75 Hindmarsh Square, Adelaide SA 5000", "phone": "(08) 8232 3531",
     "website": "https://www.lidumsdental.com.au",
     "body": [
        "Lidums Dental is an Adelaide prosthodontic and dental implant practice led by Dr Arnis Lidums. The practice uses Straumann dental implant systems and offers comprehensive implant solutions including sinus lift surgery, bone grafting, and full-arch restoration.",
        "The clinic is fitted with modern dental equipment and CBCT imaging for precise surgical planning. Dr Lidums has established a reputation for complex implant cases requiring significant bone augmentation.",
     ]},
    {"rank": 7, "name": "Gold Coast Oral Surgery Implant Group (OSIG)", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.8/5 (95 reviews)", "pricing": "Premium", "hours": "By appointment",
     "address": "Multiple locations including Robina Private Hospital and Gold Coast Private Hospital, Southport", "phone": "(07) 5562 5591",
     "website": "https://www.osig.com.au",
     "body": [
        "OSIG is a specialist oral and maxillofacial surgery group operating across four Gold Coast locations. The practice performs sinus lift surgery as a core procedure alongside dental implants, wisdom teeth removal, and corrective jaw surgery.",
        "Surgeons hold membership with the Royal Australasian College of Dental Surgeons, the Australian and New Zealand Association of Oral and Maxillofacial Surgeons, and the Australian Dental Association. Day surgery and in-patient treatments are undertaken at Robina Private Hospital and Gold Coast Private Hospital.",
     ]},
    {"rank": 8, "name": "Canberra Oral and Maxillofacial Centre", "location": "Canberra (Phillip), ACT", "featured": False,
     "rating": "4.7/5 (68 reviews)", "pricing": "Mid-range", "hours": "By appointment",
     "address": "Suite 14, Level 3, Francis Chambers, 40-42 Corinna Street, Phillip ACT 2606", "phone": "(02) 5110 3032",
     "website": "https://www.canberraomfc.com.au",
     "body": [
        "Canberra Oral and Maxillofacial Centre is led by Dr Ragu Krishnamoorthy, an oral and maxillofacial surgeon who performs sinus lift and bone graft surgery for dental implant placement. The practice treats patients requiring sinus augmentation when insufficient bone exists in the upper jaw to accommodate conventional dental implants.",
        "The clinic is located in Phillip, serving Canberra and surrounding ACT regions. Dr Krishnamoorthy performs these procedures under IV sedation or general anaesthesia.",
     ]},
    {"rank": 9, "name": "Wood Street Specialists", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.6/5 (52 reviews)", "pricing": "Premium", "hours": "By appointment",
     "address": "18 Wood Street, Newcastle West NSW 2302", "phone": "(02) 4023 5504",
     "website": "https://www.woodstreetspecialists.com.au",
     "body": [
        "Wood Street Specialists is an oral and maxillofacial surgery practice in Newcastle West led by Dr Patrick Mehanna (BDS, MBBS, FRACDS, FDS RCS, FRACDS OMS). Dr Mehanna holds the FRACDS OMS Fellowship, the only recognised Oral and Maxillofacial Surgery qualification in Australia, and was awarded the 2007 Examination Medal.",
        "He is a part-time Staff Specialist at John Hunter Hospital and consults privately in Newcastle West. His surgical interests include dental implants, complex facial trauma, and reconstructive surgery, with sinus lift procedures forming part of his implant rehabilitation work.",
     ]},
    {"rank": 10, "name": "Gold Coast Implants and Periodontal Specialists (GIPS)", "location": "Southport, QLD", "featured": False,
     "rating": "4.8/5 (78 reviews)", "pricing": "Premium", "hours": "By appointment",
     "address": "Suite 202, Level 2, Pivotal Point, 50 Marine Parade, Southport QLD 4215", "phone": "(07) 5619 6688",
     "website": "https://gips.com.au",
     "body": [
        "GIPS is a specialist periodontal and implant practice located at Pivotal Point in Southport overlooking the Broadwater. The practice is led by Dr Charles Snyman and Dr Soo Jin Lim, who provide dental implant treatment including sinus augmentation and bone grafting.",
        "All referrals are welcome but patients can also self-refer. The practice arranges OPG radiographs prior to the first appointment if needed and offers comprehensive periodontal care alongside implant services.",
     ]},
]

COST_HEADING = "How much does a sinus lift cost in Australia?"
COST = [
    'A sinus lift procedure in Australia costs between $1,500 and $4,000 for a standalone treatment. The total expense fluctuates based on the surgical technique, anatomical complexity, and chosen bone graft material. Review our complete <a href="/blog/costs/">dental costs guide</a> for comprehensive pricing data across various oral surgeries.',
    'Diagnostic imaging and sedation add separate fees to the total surgical cost. Four main variables determine the final out-of-pocket cost: surgeon specialist qualifications, the volume and type of graft material required, the surgical technique complexity, and geographic clinic location. Patients with private health insurance requiring <a href="/australia/bone-grafting/">bone grafting</a> can expect major dental cover rebates ranging from $400 to $1,200, depending on their specific policy limits. Combine the grafting procedure with <a href="/australia/dental-implants/">dental implants</a> to minimise overall surgical and anaesthesia costs.',
]
COST_PRICES = [
    ("Lateral window sinus lift (standalone)", "$2,000 - $4,000"),
    ("Crestal approach sinus lift (standalone)", "$1,500 - $3,200"),
    ("Sinus lift with implant and crown", "$4,500 - $8,500"),
    ("Additional bone graft material", "$400 - $800"),
    ("CBCT imaging", "$200 - $400"),
    ("Sedation or general anaesthesia", "$400 - $900"),
]
COST_AFTER = [
    'A sinus lift is often performed alongside <a href="/australia/bone-grafting/">bone grafting</a> procedures before <a href="/australia/dental-implants/">dental implant</a> placement. For full-arch solutions, <a href="/australia/all-on-4/">All-on-4 implants</a> may reduce or eliminate the need for sinus augmentation by using angled posterior implants.',
]

CHOOSE_HEADING = "How do you choose a sinus lift clinic in Australia?"
CHOOSE_INTRO = "To choose a reliable sinus lift clinic in Australia, evaluate the surgeon's specific experience, technology standards, and pricing structures. Patients must assess multiple variables when selecting an oral surgeon or periodontist for bone grafting procedures to ensure optimal implant longevity."
CHOOSE_CRITERIA = [
    ("Is the surgeon a registered specialist with verified AHPRA credentials?",
     "Confirm the surgeon holds current specialist registration with the Dental Board of Australia as an oral and maxillofacial surgeon or periodontist by searching the AHPRA public register. Specialists complete 4 to 6 additional years of surgical training and manage complications at higher rates of success."),
    ("How many sinus lifts has the surgeon performed in the last 12 months?",
     "Surgeons performing more than 50 sinus lifts annually report Schneiderian membrane perforation rates under 5%, compared to 10 to 20% perforation rates among low-volume operators. Ask for the specific number, not a vague estimate."),
    ("What imaging technology does the clinic use?",
     "CBCT imaging is the minimum standard for sinus lift planning. Clinics using CBCT with computer-fabricated surgical guides achieve more precise graft placement, reduced membrane perforation, and shorter surgical times. Avoid clinics that rely solely on panoramic radiographs."),
    ("What graft material does the surgeon recommend and why?",
     "Each graft material carries specific trade-offs. Autogenous bone offers the fastest integration at 3 to 4 months but requires a second surgical site. Xenografts (Bio-Oss) provide excellent volume stability with slower integration over 6 to 9 months. The surgeon should explain their material choice for your specific anatomy."),
    ("What is the total cost including all components?",
     "Request a written itemised quote covering the surgery fee, graft material, collagen membrane, CBCT imaging, sedation, all follow-up visits, and any potential complication management. Avoid clinics that quote only the base surgical fee without disclosing material costs or review appointment charges."),
]
CHOOSE_AFTER = [
    'Confirming these 5 points ensures the practitioner follows strict clinical guidelines. Surgeons placing <a href="/australia/dental-implants/">dental implants</a> should integrate digital planning software and surgical guides for accurate fixture positioning. Patients requiring full-arch rehabilitation should verify the clinic\'s expertise in <a href="/australia/all-on-4/">All-on-4 implants</a> and <a href="/australia/implant-supported-dentures/">implant-supported dentures</a> to ensure comprehensive prosthetic support.',
]

METHODOLOGY_HEADING = "How did we rank these sinus lift clinics?"
METHODOLOGY = [
    "We evaluated and ranked these 10 sinus lift clinics using 8 objective criteria to ensure clinical excellence and patient safety. Every clinic on this list met our minimum thresholds for surgical expertise and diagnostic technology integration.",
]
METHODOLOGY_CRITERIA = [
    "Surgeon qualifications and specialist registration with AHPRA",
    "Documented implant survival rates (5-year above 95%, 10-year above 90%)",
    "Annual sinus lift case volume (minimum 30 procedures)",
    "Strict infection control protocols adhering to ADA guidelines",
    "Transparent and upfront pricing models",
    "Verified patient review scores (minimum 4.5 stars from 50+ reviews)",
    "Advanced technology and equipment (CBCT imaging, piezoelectric instrumentation)",
    "Accessible location and comprehensive follow-up care",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read <a href="/methodology/">our methodology</a> for a complete breakdown of our evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is a sinus lift and why is it needed?",
     'A sinus lift is a bone grafting procedure that raises the maxillary sinus membrane. It creates 8 to 10mm of additional bone height required to support <a href="/australia/dental-implants/">dental implants</a> in the upper jaw. It is needed when tooth loss, periodontal disease, or natural sinus enlargement has reduced the bone below the 4mm minimum required for implant stability.'),
    ("How painful is a sinus lift procedure?",
     "Patients experience minimal pain during the surgery under local anaesthesia. Postoperative discomfort lasts 48 to 72 hours, resolving fully within 7 to 10 days. Surgeons prescribe paracetamol with codeine and ibuprofen for pain management. Most patients return to work within 2 to 3 days."),
    ("How long does a sinus lift take to heal before implants?",
     "The grafted bone requires 4 to 9 months to heal and integrate completely before surgeons can place the dental implant, depending on the specific graft material used. Xenografts integrate over 6 to 9 months, allografts over 4 to 6 months, and autogenous bone over 3 to 4 months."),
    ("What are the risks and complications?",
     "Schneiderian membrane perforation occurs in 5% to 20% of cases. Postoperative infection occurs in 2% to 4% of cases, while graft failure affects 3% to 5% of procedures. Experienced surgeons using piezoelectric instrumentation reduce perforation rates to under 5%. Smoking increases complication rates by 2 to 3 times."),
    ("Can I use my private health insurance?",
     "Yes. Patients with major dental cover receive rebates between $400 and $1,200 for sinus augmentation surgery, depending on their specific policy limits. Contact your health fund with the itemised treatment plan and item numbers before surgery to confirm your rebate and annual limit. Most funds impose a 12-month waiting period for major dental procedures."),
    ("Can a sinus lift and implant be placed at the same time?",
     "Surgeons place the implant simultaneously when the patient possesses residual bone exceeding 4mm, which provides sufficient primary stability for the titanium fixture. This approach reduces total treatment time by 4 to 6 months but carries a slightly higher implant failure rate of 3 to 5% compared to staged procedures."),
    ("What is the difference between a lateral window and crestal sinus lift?",
     "Surgeons utilise a lateral window approach for large augmentations requiring 8mm or more of new bone. The crestal approach addresses smaller vertical deficiencies of 2mm to 4mm. The choice depends on the CBCT scan findings and the amount of residual bone available."),
]

CTA_TITLE = "Are you a sinus lift clinic in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/sinus-lift/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Sinus lift surgery in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Sinus Lift", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
