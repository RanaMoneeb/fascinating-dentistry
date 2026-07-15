"""Content for /australia/emergency-dentist/ — Top 10 Emergency Dentists in Australia.
Transcribed verbatim from content/02-australia-emergency-dentist.md (updated July 2026).

Interface contract (shared by all directory.services.* modules, rendered by
directory/templates/directory/service_listicle_page.html):
  Section paragraphs / FAQ answers may contain inline HTML (<strong>, <a href>).
  Render them through the |live_links filter so links to not-yet-live pages are
  neutralised (no dead links). All outbound practice links are nofollow."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Emergency Dentists in Australia - Reviewed and Ranked"
META_DESC = "Find the best emergency dentists in Australia. Compare 24/7 and after-hours dental clinics, pricing, and reviews for urgent dental care."
H1 = "Top 10 Emergency Dentists in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Dental emergencies cause severe pain and require immediate treatment. Toothaches, broken teeth, abscesses, and knocked-out teeth cannot wait for standard business hours. Immediate clinical intervention prevents infection and permanent tooth loss.",
    "We ranked Australia's top emergency dentists based on six criteria: 24-hour and after-hours availability, AHPRA registration, Google reviews (minimum 50 at 4.0 or higher), same-day appointment options, weekend and public holiday access, and transparent emergency pricing. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "When should you seek emergency dental care?"
WHEN = [
    "You should seek emergency dental care for <strong>severe pain, uncontrolled bleeding, or facial trauma</strong> requiring immediate clinical attention. Patients should seek urgent dental care for 8 specific situations:",
]
WHEN_LIST = [
    "Severe toothache lasting over 48 hours",
    "Knocked-out tooth requiring treatment within 1 hour",
    "Cracked or broken teeth causing sharp pain",
    "Dental abscess with swelling, pus, or fever",
    "Uncontrolled oral bleeding",
    "Lost fillings or crowns causing pain",
    "Post-surgical infections",
    "Sports trauma affecting the mouth",
]
WHEN_AFTER = [
    'Patients with facial swelling affecting breathing, high fever combined with dental pain, uncontrolled bleeding, or facial bone fractures should go to a hospital emergency department instead. Read our <a href="/blog/conditions/">dental conditions guide</a> and <a href="/blog/treatments/">dental treatment guides</a> to identify specific oral health issues.',
]

WHO_TOP10 = "These 10 practices represent the best emergency dental care across Sydney, Melbourne, Brisbane, the Gold Coast, and regional Australia. Each entry includes verified contact details, pricing tier, Google rating, and availability information sourced directly from practice websites in July 2026."

# Each practice: rank, name, location, featured (1-3), then rating/pricing/hours/address/
# phone/website/body[]. Optional: ahpra (bool) renders an AHPRA-Reg Verified badge.
TOP10 = [
    {"rank": 1, "name": "Smile Concepts", "location": "Sydney, NSW", "featured": True,
     "rating": "4.8/5 (667 reviews)", "pricing": "Mid-range (no after-hours surcharge)", "hours": "24/7 emergency care 7 days",
     "address": "Suite 403, Level 4, 307 Pitt St, Sydney NSW 2000", "phone": "(02) 9267 7777",
     "website": "https://www.smileconcepts.com.au/",
     "body": [
        "Smile Concepts provides 24/7 emergency dental care without after-hours surcharges. The clinic treats dental trauma, sports injuries, knocked-out teeth, and severe toothaches. Their AHPRA-registered dentists prioritise same-day appointments for acute pain. The practice uses modern CBCT imaging to diagnose hidden infections rapidly.",
        "The practice is located near Town Hall station and offers free underground parking for patients. They focus on preserving natural teeth and managing infections rapidly. Smile Concepts provides transparent quotes before commencing urgent treatments.",
     ]},
    {"rank": 2, "name": "Emergency Dentist Sydney", "location": "Sydney, NSW", "featured": True,
     "rating": "Contact the practice for current review ratings", "pricing": "Competitive and affordable", "hours": "7 days including after-hours",
     "address": "Suite 601A, 185 Elizabeth St, Sydney NSW 2000", "phone": "(02) 9267 8540",
     "website": "https://www.emergencydentistsydney.com.au/",
     "body": [
        "Emergency Dentist Sydney features a dedicated emergency team with no call-out fee for after-hours services. The clinic focuses exclusively on urgent dental problems. Their clinicians possess extensive experience handling severe dental trauma and knocked-out teeth.",
        "Patients receive immediate pain relief and definitive treatment plans during their first visit. The clinic operates seven days a week to accommodate unexpected dental injuries. Emergency Dentist Sydney maintains strict sterilisation protocols to prevent post-treatment infections.",
     ]},
    {"rank": 3, "name": "MC Dental Melbourne Central", "location": "Melbourne, VIC", "featured": True,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range (no weekend surcharge)", "hours": "Open 7 days including public holidays",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8971",
     "website": "https://www.mcdental.com.au/",
     "body": [
        "MC Dental Melbourne Central operates as the highest-rated clinic on this list. The practice charges no weekend or public holiday surcharge and opens on public holidays from 10am to 5pm. Bilingual clinicians provide accessible care to diverse communities across Melbourne.",
        "They accept multiple health funds including Medibank, NIB, BUPA, HCF, and CBHS. The clinic provides discount parking for patients requiring urgent same-day treatment. MC Dental employs latest digital radiography for precise emergency diagnostics.",
     ]},
    {"rank": 4, "name": "Pure Dentistry", "location": "Brisbane, QLD", "featured": False,
     "rating": "4.6/5 (330 reviews)", "pricing": "Mid-range", "hours": "7 days including public holidays",
     "address": "11/1932-1974 Logan Road, Upper Mt Gravatt QLD 4122", "phone": "(07) 3343 4869",
     "website": "https://www.puredentistry.com.au/",
     "body": [
        "Pure Dentistry holds QIP accreditation, verifying their commitment to stringent clinical protocols. Their phone line operates from 5am to 11pm to manage patient enquiries. The clinic offers IV sedation and sleep dentistry for anxious patients requiring surgical interventions.",
        "The practice treats acute infections, broken teeth, and severe pain. They maintain transparent pricing structures for all emergency interventions. Pure Dentistry uses modern rotary endodontic tools to perform efficient root canal therapies.",
     ]},
    {"rank": 5, "name": "Emergency Dental Centre", "location": "Melbourne, VIC", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "7 days",
     "address": "Contact the practice for address", "phone": "(03) 9347 1610",
     "website": "https://www.emergencydentalcentre.com.au/",
     "body": [
        "The Emergency Dental Centre functions as a dedicated facility for acute dental problems. The clinic treats abscesses, broken teeth, infections, and oral trauma. They offer same-day emergency appointments to manage pain and prevent tooth loss.",
        "Patients receive rapid assessments and targeted treatments. The practice focuses exclusively on resolving severe dental issues efficiently. The Emergency Dental Centre employs experienced oral health professionals to handle complex trauma cases.",
     ]},
    {"rank": 6, "name": "United Dental Care", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "7 days including public holidays",
     "address": "Suite 5/377 Sussex St, Sydney NSW 2000", "phone": "(02) 9267 7174",
     "website": "https://www.uniteddentalcare.com.au/",
     "body": [
        "United Dental Care operates two Sydney locations in the CBD and Campsie. The practice closes only on Christmas Day and New Year's Day, providing year-round emergency access. Their services include family dentistry and root canal therapy.",
        "They treat facial swelling, severe toothaches, and damaged restorations. Their dentists provide transparent quotes before commencing treatment. United Dental Care uses modern intraoral cameras to document dental fractures accurately.",
     ]},
    {"rank": 7, "name": "Dental on Flinders", "location": "Melbourne, VIC", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "Monday to Saturday including after-hours",
     "address": "Level 5, 276 Flinders St, Melbourne VIC 3000", "phone": "(03) 9041 0049",
     "website": "https://www.dentalonflinders.com.au/",
     "body": [
        "Dental on Flinders sits opposite Flinders Street Station, offering immediate accessibility for commuters. The clinic provides after-hours appointments and Saturday sessions. They maintain transparent pricing published directly on their website.",
        "The practice handles acute dental infections, broken teeth, and post-surgical complications. Patients receive itemised quotes before emergency procedures begin. Dental on Flinders uses digital scanning technology to create precise temporary crowns.",
     ]},
    {"rank": 8, "name": "24 Hour Emergency Dentist", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "24 hours weekdays",
     "address": "Suite 431, 307 Pitt St, Sydney NSW 2000", "phone": "9154 0145",
     "website": "https://www.24hour-dentist.com.au/",
     "body": [
        "24 Hour Emergency Dentist provides round-the-clock weekday availability for acute dental issues. The clinic treats toothaches, broken teeth, infections, knocked-out teeth, chipped teeth, and bleeding teeth.",
        "Patients receive immediate pain management and definitive restorative care. The practice focuses on rapid intervention to save damaged teeth. 24 Hour Emergency Dentist employs modern diagnostic tools to identify the source of obscure toothaches.",
     ]},
    {"rank": 9, "name": "MGA Dental", "location": "Brisbane and Gold Coast, QLD", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "7 days a week",
     "address": "202 Pinelands Rd, Sunnybank Hills QLD 4109 (also Gold Coast: 122 Salerno St, Surfers Paradise QLD 4217)", "phone": "(07) 3273 3343",
     "website": "https://www.mgadental.com.au/",
     "body": [
        "MGA Dental operates as a family-run practice across two locations in Brisbane and the Gold Coast. The clinic offers both emergency and general dentistry. They maintain weekend availability for patients experiencing sudden dental trauma.",
        "The practice treats severe toothaches, sporting injuries, and broken restorations. They prioritise same-day appointments for patients in acute pain. MGA Dental provides itemised treatment plans to ensure financial transparency.",
     ]},
    {"rank": 10, "name": "Clear Dental", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "Open 7 days",
     "address": "131 Clarence St, Sydney NSW 2000", "phone": "(02) 9456 6557",
     "website": "https://www.cleardental.com.au/",
     "body": [
        "Clear Dental operates five Sydney locations to serve patients across the metropolitan area. The practice prioritises emergency patients to ensure rapid pain relief. They offer general, cosmetic, and emergency dentistry.",
        "The clinic treats acute infections, cracked teeth, and dental trauma. Their dentists provide transparent pricing structures for all urgent interventions. Clear Dental uses modern composite materials to repair chipped teeth seamlessly.",
     ]},
]

COST_HEADING = "How much does emergency dental care cost in Australia?"
COST = [
    "Emergency dental care costs in Australia range from <strong>$100 to $250 for an initial consultation</strong>. After-hours and weekend surcharges add $50 to $150 to the total bill.",
    "Specific emergency procedures carry distinct price points:",
]
COST_LIST = [
    "Emergency tooth extraction: $200 to $400",
    "Broken tooth filling: $150 to $350",
    "Root canal on an emergency basis: $800 to $1,500 per tooth",
]
COST_AFTER = [
    "Medicare does not cover adult emergency dental care. The Child Dental Benefits Schedule (CDBS) covers up to $1,095 over two years for eligible children. Patients should verify their private health fund coverage before treatment. Review our <a href=\"/blog/costs/\">dental costs guide</a> for detailed pricing across all emergency procedures.",
]

CHOOSE_HEADING = "How do you choose an emergency dentist in Australia?"
CHOOSE_INTRO = "You choose an emergency dentist in Australia by <strong>evaluating their availability, qualifications, and pricing structures</strong>. Patients should ask 5 specific questions when contacting a clinic:"
CHOOSE_CRITERIA = [
    ("Does the clinic offer same-day or after-hours appointments?", ""),
    ("Is the treating dentist AHPRA-registered?", ""),
    ("What Google review rating does the clinic maintain?", ""),
    ("Does the clinic provide transparent pricing with an upfront quote?", ""),
    ("What emergency procedures can they handle on-site?", ""),
]
CHOOSE_AFTER = [
    "Patients experiencing sudden pain on a Saturday or Sunday should seek a <a href=\"/australia/weekend-dentist/\">weekend dentist</a> to avoid waiting until Monday. Individuals suffering late-night trauma should contact an <a href=\"/australia/after-hours-dentist/\">after hours dentist</a> for immediate guidance.",
]

METHODOLOGY_HEADING = "How did we rank these emergency dentists?"
METHODOLOGY = [
    "We ranked these emergency dentists using <strong>8 objective criteria</strong> to ensure patients receive high-quality urgent care.",
]
METHODOLOGY_CRITERIA = [
    "24-hour and after-hours availability",
    "AHPRA registration for all treating dentists",
    "Google review volume (minimum 50 reviews)",
    "Google review rating (4.0 or higher)",
    "Pricing transparency",
    "Range of emergency services offered",
    "Same-day appointment availability",
    "Accessibility and location",
]
METHODOLOGY_AFTER = [
    "We verified all contact details, addresses, and operational hours directly from practice websites in July 2026. Read <a href=\"/methodology/\">our methodology</a> for a complete breakdown of our evaluation process. Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement.",
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("When should I see an emergency dentist instead of going to a hospital?", "You should see an emergency dentist for <strong>toothaches, broken teeth, lost fillings, and knocked-out teeth</strong>. You should go to a hospital emergency department for facial swelling affecting breathing, high fever, uncontrolled bleeding, or facial bone fractures. Contact an <a href=\"/australia/after-hours-dentist/\">after hours dentist</a> for urgent pain management."),
    ("What counts as a dental emergency?", "A dental emergency involves <strong>severe pain, uncontrolled bleeding, or facial trauma</strong>. Specific emergencies include severe toothaches lasting over 48 hours, knocked-out teeth requiring treatment within 1 hour, dental abscesses with swelling, and cracked teeth. Seek immediate <a href=\"/australia/toothache-relief/\">toothache relief</a> for intense oral pain."),
    ("How much does an emergency dentist cost in Australia?", "An emergency dentist in Australia costs <strong>$100 to $250 for an initial consultation</strong>. Emergency tooth extraction costs $200 to $400. After-hours surcharges add $50 to $150. Medicare does not cover adult emergency dental visits."),
    ("Does Medicare cover emergency dental visits?", "Medicare does <strong>not</strong> cover adult emergency dental visits. The Child Dental Benefits Schedule (CDBS) provides up to $1,095 over two years for basic dental services for eligible children. Adults must use private health insurance or pay out-of-pocket for urgent dental care."),
    ("What should I do if my tooth gets knocked out?", "Pick up your knocked-out tooth by the crown, rinse it gently, and <strong>try to reinsert it into the socket</strong>. Store the tooth in milk or saliva if reinsertion fails. Seek treatment from a dentist within 1 hour to save the tooth."),
    ("Are emergency dentists open on weekends and public holidays?", "Many emergency dentists <strong>open on weekends and public holidays</strong>. Clinics like MC Dental operate on public holidays from 10am to 5pm. Finding a <a href=\"/australia/weekend-dentist/\">weekend dentist</a> ensures immediate care for sudden dental trauma outside standard business hours."),
    ("How do I find a 24 hour dentist?", "You find a 24 hour dentist by <strong>searching dedicated emergency dental directories or calling local after-hours lines</strong>. Some clinics like Smile Concepts and 24 Hour Emergency Dentist offer round-the-clock weekday availability for acute oral pain and trauma."),
    ("What treatments does a same day dentist provide?", "A same day dentist provides <strong>emergency tooth extractions, root canal therapy, and <a href=\"/australia/broken-tooth-repair/\">broken tooth repair</a></strong>. They treat acute infections, place temporary fillings, and re-implant knocked-out teeth to provide immediate pain relief."),
]

CTA_TITLE = "Are you an emergency dentist in Australia?"
CTA_TEXT = "Apply to be featured in our directory."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


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
