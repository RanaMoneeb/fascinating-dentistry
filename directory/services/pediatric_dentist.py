"""Content for /australia/pediatric-dentist/ — Top 10 Paediatric Dentists in Australia.
Transcribed from Drive markdown (July 2026).

CONTENT RULE: Never include "(future page)" or similar bracket markers in text.
Only use <a href> for links. Dead links auto-show as light gray anchor text via live_links."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Paediatric Dentists in Australia | Reviewed and Ranked"
META_DESC = "Compare the top 10 paediatric dentists in Australia. Specialist children's dental care, early intervention, sedation options. Verified AHPRA specialist registration and clinic details."
H1 = "Top 10 Paediatric Dentists in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "A paediatric dentist is a dental specialist who has completed 3 additional years of full-time postgraduate university training in paediatric dentistry after their initial dental degree. Paediatric dentists provide comprehensive oral health care for infants, children, adolescents, and patients with special healthcare needs. The Australian Institute of Health and Welfare reports that 34% of Australian children aged 5 to 6 years have experienced decay in their primary teeth, and 23.5% of children aged 6 to 14 have decay in their permanent teeth.",
    "We ranked Australia's top paediatric dentists based on six criteria: verified specialist paediatric dentist registration with AHPRA, child-friendly facilities with sedation and general anaesthetic options, experience treating children with special needs, published pricing including Child Dental Benefits Schedule (CDBS) bulk billing, Google review scores, and referral acceptance. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When do you need a paediatric dentist?"
WHEN = [
    'A paediatric dentist has completed 3 years of postgraduate specialist training focused exclusively on children\'s oral health from infancy through adolescence. While general dentists can treat children, specialist paediatric dentists manage complex cases, dental trauma, children with special needs, and severe dental anxiety requiring sedation or general anaesthetic.',
    'The Australian Dental Association recommends children have their first dental visit by age 1 or when the first tooth erupts. Routine [dental check-ups](https://fascinatingdentistry.com/australia/dental-check-up/) every 6 to 12 months allow early detection of decay, monitoring of dental development, and preventive interventions like fluoride and fissure sealants.',
    'Your child needs a paediatric dentist for: tooth decay requiring specialist management, dental trauma (knocked out or fractured teeth), early orthodontic assessment at age 7 to 8, children with special healthcare needs, dental anxiety preventing treatment in a general practice, and complex medical histories requiring hospital-based dental treatment under general anaesthetic.',
    'Paediatric dental services include preventive care (fluoride treatment, fissure sealants), restorative treatment (fillings, [crowns](https://fascinatingdentistry.com/australia/crowns/)), trauma management, sedation options (nitrous oxide or happy gas), general anaesthesia, and habit counselling for thumb sucking and dummy use. The Child Dental Benefits Schedule provides up to $1,095 over 2 years for eligible children aged 0 to 17.',
]
WHEN_ALERT = None

WHO_TOP10 = "These 10 practices provide specialist paediatric dental care across Sydney, Melbourne, Brisbane, Perth, Adelaide, Newcastle, and Darwin. Each entry includes verified contact details, specialist qualifications, services offered, and pricing sourced directly from practice websites in July 2026."

TOP10 = [
    {"rank": 1, "name": "Prime Children's Dental Care", "location": "Perth, WA", "featured": True, "ahpra": True,
     "rating": "4.9/5 (250 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "2/85 Broadhurst Drive, Joondalup WA 6027", "phone": "(08) 9300 0600",
     "website": "https://www.primecdc.com.au",
     "body": [
        "Prime Children's Dental Care has provided children's dental services in Perth for over 35 years. The all-female team of specialist paediatric dentists, therapists, and assistants ensures positive experiences for every child.",
        "Services include preventive dental, dental procedures, children with additional needs, sedation and anaesthesia, and trauma management. Two locations in Joondalup and Wembley serve the Perth metropolitan area.",
     ]},
    {"rank": 2, "name": "Adelaide Children's Dentistry", "location": "Adelaide, SA", "featured": True, "ahpra": True,
     "rating": "4.9/5 (180 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, emergency available",
     "address": "165 Unley Road, Unley SA 5061", "phone": "(08) 8271 9597",
     "website": "https://www.acdentistry.com.au",
     "body": [
        "Adelaide Children's Dentistry is led by Dr Wendy Cheung, a specialist paediatric dentist. The practice provides comprehensive dental care from infancy to teenage years including specialist dental care, general dental care, emergency dental care, happy gas, general anaesthesia, and treatment for children with special needs.",
     ]},
    {"rank": 3, "name": "Melbourne Paediatric Dentistry", "location": "Melbourne, VIC", "featured": True, "ahpra": True,
     "rating": "4.8/5 (110 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "41 Union Road, Ascot Vale VIC 3032", "phone": "0491 628 643",
     "website": "https://melbournepaediatricdentistry.com.au",
     "body": [
        "Melbourne Paediatric Dentistry provides specialised dentistry for infants, children, and adolescents in a safe and happy environment. Services include preventative care, emergency care, fillings and crowns, infant care, general anaesthetic, dental injury management, special needs dentistry, and nitrous oxide sedation.",
     ]},
    {"rank": 4, "name": "Dr Ellie Nadian", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.9/5 (90 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri, Sat by appointment",
     "address": "Shop 6, 1876 Logan Road, Upper Mount Gravatt QLD 4122", "phone": "(07) 3343 4880",
     "website": "https://dr-ellie-nadian.com.au",
     "body": [
        "Dr Ellie Nadian is a specialist paediatric dentist in Brisbane providing dental treatments optimised for children. The practice accepts dentist referrals and provides gentle paediatric dental care including laughing gas sedation for anxious children.",
     ]},
    {"rank": 5, "name": "The Little Happy Tooth Co", "location": "Adelaide, SA", "featured": False,
     "rating": "4.9/5 (100 reviews)", "pricing": "Mid-range", "hours": "Mon-Fri",
     "address": "70 Kensington Road, Rose Park SA 5067", "phone": "(08) 8363 2000",
     "website": "https://www.littlehappytooth.com.au",
     "body": [
        "The Little Happy Tooth Co is a children's dental practice devoted exclusively to caring for smiles of children, adolescents, and those with special needs. The team of highly experienced oral health therapists and paediatric dental staff provide quality care in a child-friendly environment.",
     ]},
    {"rank": 6, "name": "Clear Dental", "location": "Sydney, NSW", "featured": False,
     "rating": "4.8/5 (320 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "131 Clarence St, Sydney NSW 2000", "phone": "(02) 9456 6557",
     "website": "https://www.cleardental.com.au",
     "body": [
        "Clear Dental provides paediatric dental care including children's dentistry, fissure sealants, fluoride treatment, and early orthodontic assessment. The practice operates seven days a week and offers the Child Dental Benefits Schedule for eligible families.",
     ]},
    {"rank": 7, "name": "MC Dental", "location": "Melbourne, VIC", "featured": False,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8968",
     "website": "https://www.mcdental.com.au",
     "body": [
        "MC Dental provides children's dentistry across six Melbourne locations. The practice bulk bills under the Child Dental Benefits Schedule (CDBS) for eligible children aged 0 to 17. Services include check-ups, cleaning, fluoride, fissure sealants, and fillings.",
     ]},
    {"rank": 8, "name": "My Local Dentists", "location": "Sydney, NSW", "featured": False,
     "rating": "4.8/5 (200 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "79 Sailors Bay Road, Northbridge NSW 2063", "phone": "(02) 8318 5966",
     "website": "https://mylocaldentists.com.au",
     "body": [
        "My Local Dentists provides high-quality dental care for children of all ages. The practice recommends children start dental visits from 12 months or first tooth eruption. Services include check-ups, cleaning, fissure sealants, fluoride, and fillings.",
     ]},
    {"rank": 9, "name": "7 Pearls Dental", "location": "Newcastle, NSW", "featured": False,
     "rating": "4.7/5 (220 reviews)", "pricing": "Mid-range", "hours": "7 days",
     "address": "Suite 2, 7 Wickham St, Wickham NSW 2293", "phone": "(02) 4077 3821",
     "website": "https://7pearlsdental.com.au",
     "body": [
        "7 Pearls Dental provides children's dental services from two Newcastle locations. The practice offers child-friendly dental care including check-ups, cleaning, and preventive treatments. Online booking is available and the clinic serves the Hunter Region 7 days a week.",
     ]},
    {"rank": 10, "name": "Extreme Dentistry", "location": "Darwin, NT", "featured": False,
     "rating": "4.7/5 (65 reviews)", "pricing": "Mid-range", "hours": "Mon-Sat",
     "address": "12 Orchard Rd, Coconut Grove NT 0810", "phone": "(08) 8948 1225",
     "website": "https://extremedentistry.com.au",
     "body": [
        "Extreme Dentistry provides paediatric dental services from its Coconut Grove practice in Darwin. Led by Dr Anand Murugappan, the clinic offers children's dental treatment alongside comprehensive restorative care. Sedation options available for anxious children.",
     ]},
]

COST_HEADING = "How much does paediatric dental treatment cost in Australia?"
COST = [
    "Paediatric dental treatment in Australia is significantly subsidised through the Child Dental Benefits Schedule (CDBS), which provides up to $1,095 over 2 calendar years for eligible children aged 0 to 17. Many practices bulk bill under the CDBS with no out-of-pocket cost to families.",
    "For services not covered by CDBS or for non-eligible families, private fees apply. Specialist paediatric dentist fees are higher than general dentist fees due to the additional 3 years of specialist training.",
]
COST_PRICES = [
    ("Routine check-up and clean (CDBS bulk billed)", "Free - $250"),
    ("Fluoride treatment", "$30 - $60"),
    ("Fissure sealants (per tooth)", "$45 - $90"),
    ("Fillings (per tooth)", "$150 - $300"),
    ("Stainless steel crowns", "$300 - $500"),
    ("Nitrous oxide sedation (happy gas)", "$100 - $200"),
]
COST_AFTER = [
    'The CDBS covers check-ups, [teeth cleaning](https://fascinatingdentistry.com/australia/teeth-cleaning/), fillings, fissure sealants, extractions, and root canals. Read our detailed <a href="/blog/costs/">dental costs guide</a> for comprehensive fee breakdowns.',
]

CHOOSE_HEADING = "How do you choose a paediatric dentist in Australia?"
CHOOSE_INTRO = "Selecting the right paediatric dentist requires verifying specialist qualifications and assessing the clinic's child-friendly environment. Ask these 5 questions."
CHOOSE_CRITERIA = [
    ("Is the practitioner a specialist paediatric dentist?",
     "Specialist paediatric dentists complete 3 years of full-time postgraduate training. Verify specialist registration on the AHPRA public register. General dentists can treat children, but complex cases require specialist expertise."),
    ("Does the clinic bulk bill under the CDBS?",
     "The Child Dental Benefits Schedule provides up to $1,095 over 2 years for eligible children. Confirm the practice bulk bills to avoid out-of-pocket costs."),
    ("What sedation options are available?",
     "Look for practices offering nitrous oxide (happy gas) for mild anxiety and general anaesthetic for complex cases. Hospital-based treatment under GA is essential for young children requiring extensive work."),
    ("Do they have experience with special needs children?",
     "Children with autism, developmental delays, or medical complexities need practitioners experienced in adapting treatment. Ask about their experience and facilities for special needs patients."),
    ("Is the clinic child-friendly?",
     "Look for play areas, child-sized dental chairs, and staff experienced in working with children. A positive early dental experience sets the foundation for lifelong oral health."),
]
CHOOSE_AFTER = []

METHODOLOGY_HEADING = "How did we rank these paediatric dentists?"
METHODOLOGY = [
    "We evaluated dental practices across Australia to finalise this top 10 list. Each practice was assessed against 8 criteria.",
]
METHODOLOGY_CRITERIA = [
    "Specialist paediatric dentist registration with AHPRA verified",
    "Child-friendly facilities and appropriately sized equipment",
    "Sedation and general anaesthetic options available",
    "Documented experience treating children with special needs",
    "Child Dental Benefits Schedule (CDBS) bulk billing availability",
    "Patient outcomes: Google review scores above 4.5",
    "Referral acceptance from general dentists and paediatricians",
    "Emergency dental care availability for children",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for the complete evaluation process.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("What is a paediatric dentist?",
     "A specialist who has completed 3 years of postgraduate training in children's oral health after their dental degree. They treat infants, children, adolescents, and patients with special needs."),
    ("When should my child first see a dentist?",
     'The Australian Dental Association recommends the first dental visit by age 1 or when the first tooth erupts. Early visits establish a dental home and allow preventive advice. Book a <a href="/australia/dental-check-up/">dental check-up</a> with a child-friendly dentist.'),
    ("How much does a paediatric dentist cost?",
     'Routine check-ups cost $80 to $250. Many clinics bulk bill under the CDBS, providing up to $1,095 over 2 years for eligible children. Read our <a href="/blog/costs/">dental costs guide</a> for details.'),
    ("What is the Child Dental Benefits Schedule (CDBS)?",
     "Medicare provides up to $1,095 over 2 calendar years for dental treatment for eligible children aged 0 to 17. Services include check-ups, cleaning, fillings, fissure sealants, and extractions. Many practices bulk bill with no out-of-pocket cost."),
    ("Is nitrous oxide safe for children?",
     "Yes. Nitrous oxide (happy gas) is a safe, mild sedative used to relax anxious children during dental treatment. It wears off within minutes of stopping. The child remains conscious and responsive throughout the procedure."),
    ("When does my child need general anaesthetic for dental treatment?",
     "General anaesthetic is recommended for young children requiring extensive treatment, children with severe anxiety, and children with special needs who cannot tolerate treatment in the chair. The procedure is performed in a hospital or licensed day surgery."),
    ("How often should children have dental check-ups?",
     'The Australian Dental Association recommends check-ups every 6 to 12 months depending on cavity risk. Children with high decay risk may need visits every 3 months. Regular <a href="/australia/teeth-cleaning/">teeth cleaning</a> prevents most childhood dental problems.'),
]

CTA_TITLE = "Are you a dental practice in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/pediatric-dentist/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Paediatric dentists in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Paediatric Dentist", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
