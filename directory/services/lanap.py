"""Content for /australia/lanap/ — Top 10 LANAP Laser Gum Treatment Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 LANAP Laser Gum Treatment Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 LANAP laser gum treatment clinics in Australia. Laser-Assisted New Attachment Procedure for periodontitis. No cut, no sew laser alternative."
H1 = "Top 10 LANAP Laser Gum Treatment Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "LANAP (Laser-Assisted New Attachment Procedure) is an FDA-cleared laser treatment for periodontitis that uses the PerioLase MVP-7 dental laser to vaporise bacteria deep within periodontal pockets while leaving healthy tissue intact. Unlike traditional gum surgery, LANAP requires no cutting, no sutures, and minimal recovery time. A tiny fibre about the width of three human hairs is inserted between the gum tissue and tooth to target and destroy diseased tissue. The procedure has been used successfully in Australia since 2011 and has FDA approval for periodontal regeneration.",
    "We ranked Australia's top LANAP laser clinics based on six criteria: verified LANAP certification through the Institute for Advanced Laser Dentistry, PerioLase MVP-7 laser ownership, AHPRA registration, periodontal specialist qualifications, published pricing, and Google review scores. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need LANAP laser treatment?"
WHEN = [
    'LANAP is needed for moderate to severe [gum disease](https://fascinatingdentistry.com/australia/gum-disease-treatment/) where periodontal pockets are too deep for routine cleaning to resolve. The procedure targets bacteria and diseased tissue within the periodontal pocket while preserving healthy gum tissue. LANAP is particularly suited for patients who fear traditional gum surgery or have health concerns that make conventional surgery risky.',
    'The LANAP protocol uses the PerioLase MVP-7 dental laser, a specific wavelength that targets pigmented bacteria and inflamed tissue. The laser fibre is inserted into the periodontal pocket where it vaporises bacteria and removes diseased tissue. Blood clots then form to seal the pocket, creating an environment for periodontal ligament and bone regeneration.',
    'LANAP is suitable for patients with moderate to severe periodontitis, patients with health concerns including diabetes, HIV, haemophilia, or those taking blood thinners, and patients wanting faster recovery than conventional surgery offers. It is not suitable for patients without periodontal disease or those with early-stage gingivitis that can be resolved with professional <a href="/australia/teeth-cleaning/">teeth cleaning</a> alone.',
    'For patients with advanced periodontitis requiring specialist care, consult a qualified <a href="/australia/periodontist/">periodontist</a> to determine whether LANAP or conventional periodontal surgery is most appropriate. Some cases may also require <a href="/australia/gum-graft-surgery/">gum graft surgery</a> for tissue recession alongside laser treatment.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide LANAP and laser periodontal treatment across Sydney, Melbourne, Brisbane, Perth, and Adelaide. Each entry includes verified contact details, laser certification status, specialist qualifications, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "LANAP Australia", "location": "Newcastle, NSW", "featured": True, "ahpra": True,
     "rating": "4.8/5 (90 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "2 Dangar Street, Newcastle NSW 2300", "phone": "(02) 6583 3533",
     "website": "https://www.lanapaustralia.com.au",
     "body": [
        "Dr Peter Elfar was the first dentist to offer LANAP treatment in Australia, introducing the revolutionary laser protocol in 2011. With years of experience and hundreds of satisfied patients, LANAP Australia is the most experienced LANAP provider in the country.",
        "The practice is dedicated to helping patients keep their natural teeth using the no-cut, no-sew laser alternative to traditional gum surgery. LANAP Australia provides comprehensive assessment and treatment planning for periodontal disease using the PerioLase MVP-7 laser.",
     ]},
    {"rank": 2, "name": "Wyndham Periodontics and Dental Implants", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.9/5 (130 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "61 Princes Hwy Service Rd, Werribee VIC 3030", "phone": "(03) 9749 7955",
     "website": "https://www.wyndhamperio.com.au",
     "body": [
        "Dr Leela R Movva obtained further training and certification in the United States to use the LANAP protocol. Wyndham Periodontics uses the PerioLase MVP-7 dental laser to vaporise bacteria deep within gum pockets while leaving healthy tissue intact.",
        "The practice is the leading laser gum therapy provider in Melbourne. Patients see immediate results with less bleeding and less bad breath, with minimal recovery time. The gentle nature of the procedure allows patients to return to daily activities immediately.",
     ]},
    {"rank": 3, "name": "Dental Excellence", "location": "Adelaide, SA", "featured": True, "ahpra": True,
     "rating": "4.8/5 (140 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "Level 3, Suite 302/147 Pirie Street, Adelaide SA 5000", "phone": "(08) 8423 1091",
     "website": "https://www.dental-excellence.com.au",
     "body": [
        "Dental Excellence is a leading provider of LANAP laser-assisted periodontal procedures in Adelaide. The practice specialises in periodontics, gum disease treatment, and advanced LANAP laser therapy. Payment plans including Zip are available for LANAP treatment.",
        "The practice operates from Pirie Street in the Adelaide CBD and provides comprehensive periodontal assessment using laser technology alongside traditional diagnostic methods.",
     ]},
    {"rank": 4, "name": "National Periodontics", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (100 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "250 Payneham Road, Payneham SA 5070", "phone": "(08) 8363 3700",
     "website": "https://natper.com.au",
     "body": [
        "National Periodontics is a specialist periodontal practice using the PerioLase MVP-7 laser for laser gum surgery. The practice has locations in Payneham and Berri, serving Adelaide and regional South Australia. Benefits include preservation of gum tissue and protection against sensitive teeth and receding gums.",
     ]},
    {"rank": 5, "name": "Perio Care Brisbane", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.9/5 (160 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 7:30am-5pm",
     "address": "Level 6, 200 Creek Street, Spring Hill QLD 4000", "phone": "(07) 2142 1774",
     "website": "https://www.periocare.com.au",
     "body": [
        "Perio Care is one of the largest periodontal practices in Australia with locations in Spring Hill and Chermside. The specialist practice provides comprehensive periodontal therapy and laser periodontal treatment. Multiple periodontists on staff including Dr Richard Grant-Thomson, Dr Amro Farag, and Dr Kaye Kendall.",
     ]},
    {"rank": 6, "name": "Foundation Dental Services", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.8/5 (120 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "2/362 Swann Road, Taringa QLD 4068", "phone": "(07) 3878 2519",
     "website": "https://www.foundationdental.com.au",
     "body": [
        "Foundation Dental Services provides comprehensive periodontal evaluation, treatment, and long-term supportive care including laser periodontal therapy. The practice treats periodontitis, acute gum issues, chronic bad breath, and sensitive teeth from its Taringa location in Brisbane.",
     ]},
    {"rank": 7, "name": "Sydney Periodontist Centre", "location": "Sydney, NSW", "featured": False,
     "rating": "4.9/5 (160 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "Level 2, 183 Macquarie Street, Sydney NSW 2000", "phone": "(02) 9221 2007",
     "website": "https://www.periodontists.com.au",
     "body": [
        "Sydney Periodontist Centre offers laser therapy alongside traditional periodontal treatment. Led by Dr David Grossberg, Dr Kevin Todes, and Dr Alex Kalos, the practice provides comprehensive laser and conventional periodontal care including pocket reduction and guided tissue regeneration.",
     ]},
    {"rank": 8, "name": "Gentle Dentistry", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Level 2, 198 North Terrace, Adelaide SA 5000", "phone": "(08) 8223 5908",
     "website": "https://www.gentledentistry.com.au",
     "body": [
        "Gentle Dentistry provides laser-assisted periodontal treatment across four Adelaide locations. The practice offers comprehensive gum disease treatment using modern laser technology. All major health funds accepted with HICAPS on-the-spot claiming.",
     ]},
    {"rank": 9, "name": "Perth Periodontics", "location": "Perth, WA", "featured": False,
     "rating": "4.8/5 (120 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "Suite 9, 38 Meadowvale Avenue, South Perth WA 6151", "phone": "(08) 9474 4444",
     "website": "https://perthperio.com.au",
     "body": [
        "Perth Periodontics provides laser periodontal treatment alongside conventional periodontal surgery. Founded by Dr Lucy De Jesus in 2002, the practice offers investigative, access, and regenerative surgeries using advanced laser and conventional techniques.",
     ]},
    {"rank": 10, "name": "Sydney Periodontists", "location": "Sydney, NSW", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8am-5pm",
     "address": "Suite 12, Level 3, Park House, 187 Macquarie Street, Sydney NSW 2000", "phone": "(02) 8552 0300",
     "website": "https://sydneyperiodontists.com.au",
     "body": [
        "Sydney Periodontists offers laser periodontal treatment and conventional gum disease therapy. Led by Dr Vijay Tumuluri, the practice operates from two Sydney locations. HICAPS on-site and accepts referrals and self-referrals.",
     ]},
]

COST_HEADING = "How much does LANAP laser treatment cost in Australia?"
COST = [
    "LANAP laser treatment in Australia costs between $4,000 and $8,000 for full mouth treatment. The cost reflects the specialised PerioLase MVP-7 laser equipment and the advanced training required for LANAP certification through the Institute for Advanced Laser Dentistry.",
    "Periodontal maintenance visits every 3 to 6 months are essential after LANAP treatment to prevent disease recurrence. Private health insurance with major dental cover may provide rebates.",
]
COST_PRICES = [
    ("LANAP full mouth treatment", "$4,000 - $8,000"),
    ("LANAP per quadrant", "$1,200 - $2,500"),
    ("Initial consultation and assessment", "$150 - $350"),
    ("Periodontal maintenance (post-LANAP)", "$180 - $350"),
]
COST_AFTER = [
    'Most practices offer interest-free payment plans for LANAP treatment. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns. Compare with <a href="/australia/gum-disease-treatment/">gum disease treatment</a> and <a href="/australia/periodontist/">periodontist</a> costs.',
]

CHOOSE_HEADING = "How do you choose a LANAP laser clinic in Australia?"
CHOOSE_INTRO = "Selecting the right LANAP clinic requires verifying laser certification and experience. Ask these 5 questions during your consultation."
CHOOSE_CRITERIA = [
    ("Is the dentist LANAP-certified through the Institute for Advanced Laser Dentistry?",
     "LANAP certification requires specialised training through the IALD. Verify the dentist has completed the certification programme before proceeding with treatment."),
    ("Does the clinic own a PerioLase MVP-7 laser?",
     "The PerioLase MVP-7 is the only FDA-cleared laser for the LANAP protocol. Clinics using alternative lasers cannot perform the official LANAP procedure."),
    ("How many LANAP procedures has the dentist performed?",
     "Experience with the laser protocol directly affects treatment outcomes. Ask about the dentist's case volume and success rates."),
    ("What is the total cost including all follow-up visits?",
     "Request an itemised quote covering the laser treatment, follow-up reviews, and ongoing maintenance visits. Confirm what is included."),
    ("What post-treatment maintenance is required?",
     "Periodontal maintenance every 3 to 6 months is essential after LANAP. Confirm the clinic provides ongoing maintenance care."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these LANAP laser clinics?"
METHODOLOGY = [
    "We evaluated dental practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "LANAP certification through the Institute for Advanced Laser Dentistry",
    "PerioLase MVP-7 laser ownership verified",
    "AHPRA registration and specialist periodontist qualifications",
    "Number of LANAP procedures performed and documented experience",
    "Pricing transparency with published fees or itemised quotes",
    "Patient outcomes: Google review scores above 4.5",
    "Referral acceptance and collaborative care approach",
    "Payment plan availability and health fund partnerships",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is LANAP laser treatment?",
     "LANAP is an FDA-cleared laser protocol using the PerioLase MVP-7 to treat periodontitis without cutting or sutures. The laser targets diseased tissue and bacteria while preserving healthy gum tissue. It has been used in Australia since 2011."),
    ("How much does LANAP cost in Australia?",
     'LANAP costs $4,000 to $8,000 for full mouth treatment. Per quadrant costs $1,200 to $2,500. Read our <a href="/blog/costs/">dental costs guide</a> for details.'),
    ("Is LANAP painful?",
     "LANAP is performed under local anaesthetic. Patients report significantly less discomfort than traditional gum surgery. Most return to normal activities the same day. No cutting or sutures means less pain, bleeding, and swelling."),
    ("How long does LANAP take?",
     "LANAP treatment is typically completed in two sessions of approximately 2 hours each, treating one half of the mouth per session. Sessions are scheduled 1 to 2 weeks apart."),
    ("Is LANAP better than traditional gum surgery?",
     'LANAP offers faster healing, less discomfort, no cutting or sutures, and minimal gum recession compared to traditional surgery. However, some complex cases may still require conventional periodontal surgery. A <a href="/australia/periodontist/">periodontist</a> determines suitability.'),
    ("Does LANAP regenerate bone?",
     "Yes. LANAP has FDA approval for periodontal regeneration, meaning it can help regrow bone and ligament attachment around teeth. This is a significant advantage over traditional surgery which typically only removes diseased tissue."),
    ("Is LANAP safe for patients with health conditions?",
     'LANAP is safe for patients with health concerns including diabetes, HIV, haemophilia, and patients taking blood thinners. The gentle laser protocol reduces surgical risk compared to conventional <a href="/australia/gum-disease-treatment/">gum disease treatment</a>.'),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/lanap/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "LANAP laser treatment in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "LANAP", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
