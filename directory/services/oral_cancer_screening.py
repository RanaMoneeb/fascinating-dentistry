"""Content for /australia/oral-cancer-screening/ — Top 10 Oral Cancer Screening Clinics in Australia."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Oral Cancer Screening Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 oral cancer screening clinics in Australia. VELscope technology, early detection, and soft tissue examination. Verified clinics near you."
H1 = "Top 10 Oral Cancer Screening Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Oral cancer screening is a preventive examination that checks for signs of cancer or precancerous lesions in the mouth, lips, tongue, throat, and surrounding tissues. The Cancer Council Australia reports that approximately 3,000 Australians are diagnosed with oral cancer each year, with a 5-year survival rate of 68% when detected early but dropping to 25% when diagnosed at an advanced stage. Risk factors include tobacco use, excessive alcohol consumption, HPV infection, sun exposure, and increasing age.",
    "We ranked Australia's top oral cancer screening clinics based on six criteria: VELscope or similar fluorescence screening technology, frequency of routine screening included in check-ups, AHPRA registration, specialist referral pathways, published pricing, and Google review scores. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need an oral cancer screening?"
WHEN = [
    'Oral cancer screening involves a visual and tactile examination of the lips, tongue, cheeks, throat, palate, and floor of the mouth. The dentist checks for lesions, persistent ulcers, red or white patches (erythroplakia/leukoplakia), lumps, and tissue changes. VELscope technology uses blue-spectrum fluorescent light to detect abnormal tissue invisible to the naked eye.',
    "The Cancer Council Australia recommends annual oral cancer screening as part of your routine dental check-up. Seek immediate assessment if you notice persistent mouth ulcers (over 2 weeks), red or white patches, difficulty swallowing, persistent sore throat, unexplained bleeding, or lumps in the neck or mouth.",
    "Key risk factors include tobacco smoking, chewing tobacco, excessive alcohol consumption, HPV (human papillomavirus) infection, prolonged sun exposure (lip cancer), age over 40, and previous oral cancer history. However, 25% of oral cancer cases occur in people with no identifiable risk factors, making universal screening important.",
    'Early detection dramatically improves outcomes. The 5-year survival rate for oral cancer detected at stage 1 is 80 to 90%, dropping to 25% when detected at stage 4. Regular [dental check-ups](https://fascinatingdentistry.com/australia/dental-check-up/) that include oral cancer screening are the most effective way to catch this disease early.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide oral cancer screening across Sydney, Melbourne, Brisbane, Perth, Adelaide, Newcastle, and Darwin. Each entry includes verified contact details, screening technology, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "The Paddington Dental Surgery", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (190 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat",
     "address": "2A Oxford Street, Paddington NSW 2021", "phone": "(02) 9331 2611",
     "website": "https://www.thepaddingtondentalsurgery.com.au",
     "body": [
        "The Paddington Dental Surgery uses VELscope Vx oral cancer screening technology to examine the inside of the mouth using special light that detects suspicious tissue at the earliest possible stage. Comprehensive soft tissue examination is included in routine check-ups.",
        "The practice serves patients from Paddington, Double Bay, and the Eastern Suburbs of Sydney with world-class oral care including preventive screening.",
     ]},
    {"rank": 2, "name": "Sydney CBD Dentistry", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (420 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "Suite 6, Level 2, 135 Macquarie Street, Sydney NSW 2000", "phone": "(02) 9232 3788",
     "website": "https://www.sydneycbddentistry.com.au",
     "body": [
        "Sydney CBD Dentistry provides comprehensive oral cancer screening as part of routine dental check-ups. Includes soft tissue examination, lymph node assessment, and referral pathway for suspicious lesions.",
     ]},
    {"rank": 3, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": True, "ahpra": True,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry includes oral cancer screening in routine dental examinations across four Adelaide locations. Comprehensive soft tissue examination and lymph node assessment. All major health funds accepted with HICAPS.",
     ]},
    {"rank": 4, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": ["MC Dental includes oral cancer screening in routine check-ups across six Melbourne locations. Open 7 days a week."]},
    {"rank": 5, "name": "No Gaps Dental", "location": "Sydney, NSW", "featured": False,
     "rating": "4.8/5 (650 reviews)", "pricing": "Gap-free (health fund)", "hours": "Mon-Sat",
     "address": "Level 2, 283 George Street, Sydney NSW 2000", "phone": "(02) 8383 1400",
     "website": "https://www.nogapsdental.com",
     "body": ["No Gaps Dental includes oral cancer screening in gap-free check-ups across 18 Sydney locations."]},
    {"rank": 6, "name": "Bayview Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat mornings",
     "address": "1/324 Stirling Highway, Claremont WA 6010", "phone": "(08) 9284 2995",
     "website": "https://bayviewdental.com.au",
     "body": ["Bayview Dental provides oral cancer screening with digital technology. Interest-free payment plans available."]},
    {"rank": 7, "name": "Malouf Dental", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Thu, Fri mornings",
     "address": "1476 Wynnum Road, Tingalpa QLD 4173", "phone": "(07) 3390 6100",
     "website": "https://cosmeticdentistinbrisbane.com.au",
     "body": ["Malouf Dental includes oral cancer screening as part of comprehensive check-up. Complimentary initial appointments."]},
    {"rank": 8, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": ["7 Pearls Dental includes oral cancer screening in routine check-ups. Two locations, online booking, 7 days."]},
    {"rank": 9, "name": "Clear Dental", "location": "Sydney, NSW", "featured": False,
     "rating": "4.8/5 (320 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "131 Clarence St, Sydney NSW 2000", "phone": "(02) 9456 6557",
     "website": "https://www.cleardental.com.au",
     "body": ["Clear Dental provides oral cancer screening and soft tissue examination. Open 7 days. CDBS available."]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": ["Extreme Dentistry provides oral cancer screening. Led by Dr Anand Murugappan. Complex case management."]},
]

COST_HEADING = "How much does oral cancer screening cost in Australia?"
COST = ["Oral cancer screening is typically included in your routine dental check-up at no additional cost. Some clinics offer VELscope screening as an optional add-on."]
COST_PRICES = [
    ("Included in routine check-up", "$0 additional"),
    ("Standalone VELscope screening", "$50 - $100"),
    ("Biopsy (if required)", "$150 - $350"),
]
COST_AFTER = ['Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. Schedule a <a href="/australia/dental-check-up/">dental check-up</a> that includes screening.']

CHOOSE_HEADING = "How do you choose an oral cancer screening clinic?"
CHOOSE_INTRO = "Selecting a clinic that prioritises oral cancer screening ensures early detection. Ask these 5 questions."
CHOOSE_CRITERIA = [
    ("Does the clinic include oral cancer screening in routine check-ups?", "Screening should be a standard part of every dental examination, not an optional extra."),
    ("Do they use VELscope or similar technology?", "Fluorescence screening devices detect abnormalities invisible to the naked eye."),
    ("Do they check lymph nodes and surrounding tissue?", "Comprehensive screening includes neck and lymph node examination, not just the mouth."),
    ("Do they have a referral pathway for suspicious lesions?", "Confirm the clinic can refer to oral surgeons or oncologists for biopsy if needed."),
    ("How often do they recommend screening?", "Annual screening minimum. High-risk patients every 6 months."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these clinics?"
METHODOLOGY = ["We evaluated dental practices across Australia. Each was assessed against 8 criteria."]
METHODOLOGY_CRITERIA = [
    "VELscope or similar fluorescence screening technology",
    "Oral cancer screening included in routine check-ups",
    "Comprehensive soft tissue and lymph node examination",
    "AHPRA registration verified",
    "Referral pathway for suspicious lesions",
    "Pricing transparency",
    "Google reviews above 4.5",
    "Patient education on oral cancer risk factors",
]
METHODOLOGY_AFTER = ['Paid placements in positions 1 to 3 met all 8 criteria. Read our full <a href="/methodology/">methodology</a>.']

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is oral cancer screening?", 'Examination of mouth, tongue, and throat for signs of cancer or precancerous lesions. Often uses VELscope technology. Included in routine <a href="/australia/dental-check-up/">dental check-ups</a>.'),
    ("How much does oral cancer screening cost?", 'Usually free as part of routine check-up. VELscope screening $50 to $100. Read our <a href="/blog/costs/">dental costs guide</a>.'),
    ("How often should I be screened?", "Annually as part of your routine dental check-up. High-risk patients every 6 months."),
    ("What are the signs of oral cancer?", "Persistent mouth ulcers (over 2 weeks), red or white patches, difficulty swallowing, persistent sore throat, unexplained bleeding, lumps in the neck or mouth."),
    ("Is VELscope accurate?", "VELscope detects abnormal tissue changes not visible to the naked eye using fluorescent light. It has high sensitivity for identifying suspicious areas."),
    ("Who is at risk for oral cancer?", "Smokers, tobacco users, heavy alcohol consumers, people with HPV infection, those over 40. However, 25% of cases have no risk factors."),
    ("Can a dentist detect oral cancer?", "Yes. Dentists are often the first to detect oral cancer during routine examinations. They perform soft tissue screening and refer suspicious lesions for biopsy."),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."
DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."

def _build_schemas():
    url = f"{SITE_URL}/australia/oral-cancer-screening/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage", "name": META_TITLE, "description": META_DESC, "about": "Oral cancer screening in Australia", "inLanguage": "en-AU", "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1, "itemListElement": [{"@type": "ListItem", "position": p["rank"], "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"}, {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"}, {"@type": "ListItem", "position": 3, "name": "Oral Cancer Screening", "item": url}]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]

SCHEMAS = _build_schemas()
