"""Content for /australia/teeth-whitening/ — Top 10 Teeth Whitening Clinics in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Teeth Whitening Clinics in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 teeth whitening clinics in Australia. Philips Zoom in-chair whitening costs, take-home kits, and professional results near you."
H1 = "Top 10 Teeth Whitening Clinics in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Professional teeth whitening is the most popular cosmetic dental procedure in Australia. The Australian Dental Association reports that professional whitening demand increased by 34% between 2019 and 2024, driven by patient awareness of safe, dentist-supervised options. In-chair procedures using Philips Zoom technology lighten tooth shade by up to 8 shades in a single 60-minute session, while custom take-home kits deliver gradual results over 2 to 3 weeks. Unlike over-the-counter products, professional whitening uses higher-concentration gels applied under dental supervision, producing faster results with minimal sensitivity.",
    "We ranked Australia's top teeth whitening clinics based on six criteria: professional whitening systems offered (Philips Zoom, SDI Pola, Opalescence), dentist qualifications and AHPRA registration, published pricing, Google review scores, take-home kit availability, and same-day appointment options. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need professional teeth whitening?"
WHEN = [
    'Tooth discolouration occurs through two distinct mechanisms: extrinsic staining and intrinsic staining. Extrinsic stains bond to the outer enamel surface due to dietary consumption of coffee, tea, red wine, and tobacco products. Intrinsic stains originate within the dentin layer beneath the enamel, resulting from tetracycline antibiotics, dental trauma, natural ageing, or fluorosis. Professional <a href="/australia/cosmetic-dentistry/">cosmetic dentistry</a> interventions successfully address both stain types.',
    "Over-the-counter whitening products fail to match professional results due to strict regulatory limits on peroxide concentration. Pharmacies and supermarkets sell products containing 3% to 6% hydrogen peroxide, which produce minimal shade improvement over 14 to 30 days. Dentists access professional-grade whitening gels containing 25% to 40% hydrogen peroxide for in-chair treatments, or 10% to 16% carbamide peroxide for custom take-home kits. The Australian Dental Association restricts high-concentration peroxide to dental professionals to ensure gum isolation and enamel safety.",
    "Patients choose between two primary professional whitening methods. In-chair whitening utilises Philips Zoom LED-activated technology to complete treatment in 60 minutes, achieving up to 8 shades of improvement in a single visit. Take-home kits utilise custom-fitted whitening trays tailored to the patient's gum line. Patients inject a lower-concentration gel into the trays and wear them daily, delivering gradual results over 2 to 3 weeks.",
    'Dentists identify specific contraindications that make teeth whitening unsuitable for certain individuals. Pregnant women, patients under 16 years old, individuals with active gum disease, untreated cavities, or severely worn enamel cannot undergo peroxide-based whitening. Dentists treat active decay and gum inflammation before administering cosmetic treatments. For patients with intrinsic stains that resist peroxide bleaching, <a href="/australia/porcelain-veneers/">porcelain veneers</a> or <a href="/australia/composite-bonding/">composite bonding</a> provide alternative cosmetic solutions.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide professional teeth whitening across Sydney, Melbourne, Brisbane, Perth, Adelaide, the Gold Coast, Hobart, Newcastle, and Darwin. Each entry includes verified contact details, whitening systems offered, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Vogue Dental Studios", "location": "Sydney, NSW", "featured": True, "ahpra": True,
     "rating": "4.9/5 (320 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Suite 1, 1 Elizabeth Plaza, North Sydney NSW 2060", "phone": "(02) 9068 1870",
     "website": "https://voguedentalstudios.com.au",
     "body": [
        "Vogue Dental Studios offers professional teeth whitening at its North Sydney clinic using Philips Zoom in-chair technology and Pola take-home systems. The practice begins every whitening consultation with a comprehensive oral health assessment to ensure the procedure is safe and appropriate. Their clinicians apply a protective gum barrier before using professional-grade whitening gel activated by specialised LED light, delivering up to 8 shades of improvement in a single session.",
        "The practice provides noise-cancelling headphones and entertainment during treatment, with desensitising gel applied for patients prone to sensitivity. In-chair whitening costs $850 per session, with a take-home kit included for maintenance. Vogue Dental Studios serves patients from North Sydney, Lavender Bay, Milsons Point, and surrounding lower north shore suburbs.",
     ]},
    {"rank": 2, "name": "The Smile Designer", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.8/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "118-120 High Street, South Preston VIC 3072", "phone": "(03) 9089 7574",
     "website": "https://www.thesmiledesigner.com.au",
     "body": [
        "The Smile Designer provides professional teeth whitening from its Preston dental studio in Melbourne, offering both Philips Zoom in-chair whitening and SDI Pola take-home systems. In-chair Zoom whitening combined with a take-home kit costs $750, while standalone take-home kits cost $490. Each treatment begins with a dental assessment to confirm suitability before the whitening gel is applied.",
        "The practice uses Zoom LED-activated technology for in-chair procedures, completing treatment in approximately 60 minutes. Take-home kits include custom-fitted whitening trays designed to align with the patient's gum line, delivering gradual results over 2 to 3 weeks. The Smile Designer offers flexible payment plans and accepts all major health funds through HICAPS.",
     ]},
    {"rank": 3, "name": "Precision Dental", "location": "Brisbane, QLD", "featured": True, "ahpra": True,
     "rating": "4.9/5 (280 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "520 Wickham Street, Fortitude Valley QLD 4006", "phone": "(07) 3852 1160",
     "website": "https://precisiondentistry.com.au",
     "body": [
        "Precision Dental offers professional teeth whitening from its Fortitude Valley practice in Brisbane, using Philips Zoom in-chair technology and custom take-home whitening trays. The practice provides free on-site parking and focuses on pain-free dentistry for anxious patients. Their whitening services include both single-session in-chair treatment and gradual take-home kits tailored to each patient's tooth sensitivity.",
        "The clinic serves Fortitude Valley, New Farm, Newstead, Teneriffe, Spring Hill, and Hamilton. Precision Dental provides transparent pricing with written quotes before treatment and accepts all major health funds.",
     ]},
    {"rank": 4, "name": "Claremont Dental", "location": "Perth, WA", "featured": False,
     "rating": "4.7/5 (190 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, alternate Sat",
     "address": "322 Stirling Highway, Claremont WA 6010", "phone": "(08) 9383 1200",
     "website": "https://www.claremontdentalperth.com.au",
     "body": [
        "Claremont Dental provides Zoom in-chair teeth whitening and take-home whitening kits from its practice on Stirling Highway in Perth's western suburbs. In-chair Zoom whitening lightens teeth up to 8 shades in a single 60-minute session using LED-activated gel. Take-home kits include custom-fitted trays for gradual whitening over 2 weeks. The practice serves Claremont, Nedlands, Subiaco, and surrounding western Perth suburbs.",
     ]},
    {"rank": 5, "name": "Dentistry on Unley", "location": "Adelaide, SA", "featured": False,
     "rating": "4.8/5 (110 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Suites 1-4, 292-294 Unley Rd, Unley SA 5061", "phone": "(08) 8272 9087",
     "website": "https://dentistryonunley.com.au",
     "body": [
        "Dentistry on Unley offers professional teeth whitening using CEREC-compatible cosmetic systems and Philips Zoom technology. The practice provides both in-chair and take-home whitening options, with daily appointment slots reserved for cosmetic consultations. Their services include comprehensive shade assessment, gum protection during treatment, and post-whitening desensitising care. The clinic accepts all major health funds through HICAPS.",
     ]},
    {"rank": 6, "name": "Smile Concepts", "location": "Sydney, NSW", "featured": False,
     "rating": "4.8/5 (667 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 403, Level 4, 307 Pitt Street, Sydney NSW 2000", "phone": "(02) 9267 7777",
     "website": "https://www.smileconcepts.com.au",
     "body": [
        "Smile Concepts delivers professional teeth whitening from its Sydney CBD practice on Pitt Street, using Philips Zoom in-chair technology and custom take-home whitening systems. The practice uses digital smile design technology to preview whitening outcomes before treatment. Seven-day availability suits CBD workers and weekend patients. Smile Concepts publishes before-and-after galleries showing whitening results on its website.",
     ]},
    {"rank": 7, "name": "ArtSmiles", "location": "Gold Coast, QLD", "featured": False,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri 8:30am-5:00pm",
     "address": "Shop 4, 45/49 Nind St, Southport QLD 4215", "phone": "(07) 5588 3677",
     "website": "https://artsmiles.com.au",
     "body": [
        "ArtSmiles offers professional teeth whitening from its Southport practice on the Gold Coast, providing both in-chair Zoom whitening and custom take-home kits. The practice identifies the cause of discolouration before recommending the most appropriate whitening approach. ArtSmiles serves Southport, Bundall, Benowa, Ashmore, Labrador, and Main Beach with flexible finance options including Afterpay and Zip.",
     ]},
    {"rank": 8, "name": "Napol Dental", "location": "Hobart, TAS", "featured": False,
     "rating": "4.9/5 (90 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "1 Warneford St, Hobart TAS 7000", "phone": "(03) 6200 8800",
     "website": "https://www.napoldental.com.au",
     "body": [
        "Napol Dental provides professional teeth whitening from its Hobart practice led by Dr Clark Eom, a Doctor of Dental Medicine from the University of Sydney. The practice offers both in-chair and take-home whitening systems, with treatment plans tailored to each patient's tooth shade and sensitivity level. Saturday appointments are available for patients unable to attend during business hours.",
     ]},
    {"rank": 9, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental operates two Newcastle locations in Wickham and Belmont, offering professional teeth whitening 7 days a week. The practice provides cosmetic dentistry services including in-chair whitening and take-home kits. Their cosmetic dentistry team serves Newcastle, Wickham, Belmont, and surrounding Hunter Region suburbs with online booking available for whitening consultations.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides professional teeth whitening from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan, the clinic offers cosmetic dentistry including in-chair whitening and take-home systems. The practice serves patients across the Darwin metropolitan area and offers sedation options for anxious patients.",
     ]},
]

COST_HEADING = "How much does teeth whitening cost in Australia?"
COST = [
    "Patients access professional whitening through four primary treatment pathways. Costs reflect the concentration of whitening gel, the technology used, and the inclusion of custom maintenance equipment.",
    "Four primary factors dictate the final cost of a whitening procedure. The selected whitening system alters the price, as branded technologies like Philips Zoom require specific LED activation equipment. Clinic location impacts overhead costs, with Sydney and Melbourne practices charging higher fees than regional clinics. The dentist's experience level influences chair time costs. Finally, the inclusion of a take-home maintenance kit adds $150 to $300 to the total invoice.",
]
COST_PRICES = [
    ("In-chair Philips Zoom whitening (single session)", "$600 - $1,000"),
    ("In-chair whitening with take-home kit", "$750 - $1,200"),
    ("Take-home whitening kit (custom trays + gel)", "$300 - $550"),
    ("Porcelain veneer (for intrinsic stains)", "$1,200 - $2,500 per tooth"),
    ("Composite bonding (alternative for stained teeth)", "$200 - $500 per tooth"),
]
COST_AFTER = [
    'Private health insurance policies that include major dental cover provide rebates for teeth whitening. Most clinics across Australia offer HICAPS instant claiming. Review our comprehensive <a href="/blog/costs/">dental costs guide</a> or explore general <a href="/australia/cosmetic-dentistry/">cosmetic dentistry</a> pricing. Patients managing intrinsic discolouration should review the costs of <a href="/australia/porcelain-veneers/">porcelain veneers</a>.',
]

CHOOSE_HEADING = "How do you choose a teeth whitening clinic in Australia?"
CHOOSE_INTRO = "Selecting a safe and effective teeth whitening provider requires evaluating clinical protocols and technology. Patients must assess 5 specific checklist questions before committing to treatment."
CHOOSE_CRITERIA = [
    ("What whitening system does the clinic use?",
     "Philips Zoom represents the gold standard for in-chair whitening due to its proprietary LED light and desensitising gel. For take-home options, SDI Pola and Opalescence provide reliable, pH-balanced carbamide peroxide formulations."),
    ("Does the clinic assess suitability before whitening?",
     "Dentists must examine the oral cavity for cavities, gum disease, and worn enamel. Peroxide gel penetrating an untreated cavity causes severe nerve inflammation. Reputable clinics treat active decay before administering whitening gel."),
    ("Is pricing transparent?",
     "Clinics must publish their fees online or provide itemised quotes. The quote must separate the in-chair session cost from the take-home maintenance kit to prevent hidden fees."),
    ("Does the clinic offer sensitivity management?",
     "High-concentration peroxide causes temporary tooth sensitivity in 30 to 40% of patients. Clinics must provide desensitising gel applications or offer lower concentration take-home alternatives for patients with a history of enamel sensitivity."),
    ("Does the clinic provide a take-home maintenance kit?",
     'Long-lasting whitening requires periodic touch-ups. The clinic must include custom-fitted trays and supplementary gel to maintain the initial shade improvement. For alternative treatments, evaluate <a href="/australia/porcelain-veneers/">porcelain veneers</a>, <a href="/australia/composite-bonding/">composite bonding</a>, or general <a href="/australia/dental-fillings/">dental fillings</a> offered by the practice.'),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these teeth whitening clinics?"
METHODOLOGY = [
    "Our editorial team evaluated over 60 dental practices across Australia to finalise this top 10 list. We verified each clinic against 8 core ranking criteria to ensure patient safety and treatment efficacy.",
]
METHODOLOGY_CRITERIA = [
    "Whitening technology: Philips Zoom, SDI Pola, or equivalent TGA-approved professional peroxide systems",
    "Dentist qualifications: current AHPRA registration with cosmetic dentistry experience",
    "Pricing transparency: published base fees or clear itemised written quotes",
    "Take-home kit availability: custom-fitted trays and professional-grade gel for maintenance",
    "Patient outcomes: minimum Google review score of 4.5 out of 5",
    "Sensitivity management: gum isolation, protective barriers, and post-operative desensitising gel",
    "Accessibility: appointment availability outside standard business hours",
    "Health fund partnerships: HICAPS terminals for instant private health insurance claiming",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read the complete breakdown in <a href="/methodology/">our methodology</a>.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("How long does professional teeth whitening last?",
     "Professional teeth whitening lasts 12 to 24 months depending on diet, oral hygiene, and lifestyle habits. Coffee, tea, red wine, and tobacco accelerate staining. Regular dental check-ups and take-home maintenance kits extend results."),
    ("Is teeth whitening safe?",
     "Yes, when performed by a qualified dentist. Professional whitening uses regulated peroxide concentrations applied under dental supervision. Temporary tooth sensitivity affects 30 to 40% of patients and resolves within 48 hours."),
    ("How many shades whiter will my teeth get?",
     "Philips Zoom in-chair whitening lightens teeth by up to 8 shades in a single 60-minute session. Take-home kits deliver 4 to 6 shades over 2 to 3 weeks. Results vary based on starting shade and enamel condition."),
    ("Does teeth whitening work on all stains?",
     'Professional whitening removes most extrinsic stains from coffee, tea, wine, and tobacco. Intrinsic stains from tetracycline antibiotics, fluorosis, or trauma respond less predictably. <a href="/australia/porcelain-veneers/">Porcelain veneers</a> or <a href="/australia/composite-bonding/">composite bonding</a> cover intrinsic stains that whitening cannot remove.'),
    ("How long does an in-chair whitening session take?",
     "In-chair Philips Zoom whitening takes approximately 60 minutes from start to finish. The procedure includes gum protection, 3 to 4 gel applications of 15 minutes each under LED light, and post-treatment desensitising gel."),
    ("Can I whiten my teeth if I have crowns or fillings?",
     "Dental crowns, veneers, and fillings do not respond to whitening gel. Only natural tooth enamel lightens. Dentists recommend whitening before placing new restorations to match the shade. Existing restorations may need replacement to match whitened teeth."),
    ("What is the difference between in-chair and take-home whitening?",
     "In-chair whitening uses higher-concentration gel (25 to 40% hydrogen peroxide) activated by LED light, delivering results in 60 minutes. Take-home kits use lower-concentration gel (10 to 16% carbamide peroxide) in custom trays, delivering gradual results over 2 to 3 weeks."),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/teeth-whitening/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Teeth whitening in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Teeth Whitening", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
