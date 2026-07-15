"""Content for /australia/weekend-dentist/ — Top 10 Weekend Dentists in Australia.
Transcribed from Drive markdown (July 2026).

Interface contract (shared by all directory.services.* modules, rendered by
directory/templates/directory/service_listicle_page.html):
  Section paragraphs / FAQ answers may contain inline HTML (<strong>, <a href>).
  Render them through the |live_links filter so links to not-yet-live pages are
  neutralised (no dead links). All outbound practice links are nofollow."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Weekend Dentists in Australia - Reviewed and Ranked"
META_DESC = "Compare Australia's best weekend dentists open Saturday and Sunday. Verified reviews, pricing, hours and contact details for 10 top-rated clinics."
H1 = "Top 10 Weekend Dentists in Australia - Reviewed and Ranked"
BADGE = "Top 10 — Reviewed & Ranked"

INTRO = [
    "Dental problems do not take weekends off. Toothaches, broken teeth, and lost fillings on Saturday or Sunday require immediate access to reliable weekend dentists. Finding a dentist open Saturday or a dentist open Sunday prevents unnecessary pain and stops minor infections from spreading. According to the Australian Institute of Health and Welfare, 1 in 25 Australians experience dental pain each year, and many of these episodes begin outside standard weekday hours. A weekend dentist provides the same diagnostic, restorative, and emergency treatments available Monday to Friday, without making patients wait 48 hours or longer for relief.",
    "We ranked Australia's top weekend dentists based on six criteria: Saturday and Sunday availability, AHPRA registration, Google reviews (minimum 50 at 4.0 or higher), weekend pricing transparency, same-day appointment options, and range of services available on weekends. Every clinic on this list has a verified website and contactable phone number as of July 2026.",
    'Positions 1 to 3 are paid placements with do-follow links. Positions 4 to 10 are editorial selections with no-follow links. Browse our complete directory of <a href="/australia/">all 42 dental services across Australia</a>. Read <a href="/methodology/">our methodology</a> and our <a href="/disclosures/">disclosures policy</a> for full transparency.',
]

WHEN_HEADING = "What counts as weekend dental care?"
WHEN = [
    "Weekend dental care includes any professional dental appointment available on Saturday or Sunday when the majority of Australian dental practices are closed. The Australian Dental Association reports that fewer than 30% of private dental practices offer regular Saturday hours, and even fewer operate on Sundays. Two delivery models dominate the weekend market: dedicated weekend clinics that operate 7 days per week with full staffing, and general practices that add Saturday or Sunday sessions to their standard weekday schedule.",
    "Weekend dental care covers three patient groups. Working professionals who cannot take time off during weekday business hours use Saturday and Sunday appointments for routine check-ups, scale and cleans, and fillings. Parents managing family schedules book weekend slots for children's examinations and preventive treatments. Patients with sudden dental trauma, including knocked-out teeth, cracked molars, and lost crowns, need same-day weekend emergency care that cannot wait until Monday.",
    'Patients with severe facial swelling affecting breathing or swallowing, high fever above 38.5 degrees Celsius, or suspected facial bone fractures should attend a hospital emergency department rather than a weekend dental clinic. These symptoms indicate infections or injuries that exceed the scope of private dental practice. For non-emergency conditions, read our <a href="/blog/conditions/">dental conditions guide</a> and explore our <a href="/blog/treatments/">dental treatment guides</a> to understand what weekend care can address.',
]
WHEN_ALERT = "Patients experiencing severe facial swelling affecting breathing or swallowing, high fever above 38.5 degrees Celsius, or suspected facial bone fractures should attend a hospital emergency department rather than a weekend dental clinic."

WHO_TOP10 = "These 10 practices represent the best weekend dental care across Sydney, Melbourne, Brisbane, the Gold Coast, and regional Australia. Each entry includes verified contact details, pricing tier, Google rating, and weekend availability information sourced directly from practice websites in July 2026."

# Each practice: rank, name, location, featured (1-3), then rating/pricing/hours/address/
# phone/website/body[]. Optional: ahpra (bool) renders an AHPRA-Reg Verified badge.
TOP10 = [
    {"rank": 1, "name": "MC Dental Melbourne Central", "location": "Melbourne, VIC", "featured": True,
     "rating": "4.8/5 (2,197 reviews)", "pricing": "Mid-range (no weekend surcharge)", "hours": "Sat 9am-4pm, Sun 10am-5pm, public holidays 10am-5pm",
     "address": "Shop 254, Level 2, 211 La Trobe St, Melbourne VIC 3000", "phone": "(03) 8608 8971",
     "website": "https://www.mcdental.com.au/", "ahpra": True,
     "body": [
        "MC Dental Melbourne Central holds the highest Google review count of any weekend dental practice in Australia with 2,197 reviews at 4.8 out of 5. The clinic operates from Melbourne Central Shopping Centre, making it accessible via Melbourne Central train station and multiple tram routes along La Trobe and Swanston Streets. Discount parking is available for patients inside the shopping centre carpark.",
        "The practice charges no weekend surcharge. Saturday, Sunday, and public holiday appointments cost the same as weekday visits. MC Dental accepts Medibank, NIB, BUPA, HCF, and CBHS health funds with on-the-spot HICAPS claiming. Bilingual clinicians speak Mandarin, Cantonese, Hindi, and Arabic, serving Melbourne's diverse central business district population. Weekend services include examinations, scale and cleans, fillings, root canals, extractions, and emergency dentistry.",
        "All MC Dental dentists hold current AHPRA registration. The clinic remains open on most public holidays including Labour Day, Queen's Birthday, and Melbourne Cup Day, making it one of the few practices in Victoria offering genuine 365-day availability.",
     ]},
    {"rank": 2, "name": "Smile Concepts", "location": "Sydney, NSW", "featured": True,
     "rating": "4.8/5 (667 reviews)", "pricing": "Mid-range (no after-hours surcharge)", "hours": "7 days including weekends",
     "address": "Suite 403, Level 4, 307 Pitt St, Sydney NSW 2000", "phone": "(02) 9267 7770",
     "website": "https://www.smileconcepts.com.au/", "ahpra": True,
     "body": [
        "Smile Concepts operates 7 days per week from its Pitt Street location, one block from Town Hall railway station. The practice treats all dental emergencies on weekends, including severe toothache, avulsed teeth, broken restorations, and dental abscesses. Free underground parking is available for patients, removing a common barrier to Sydney CBD dental visits.",
        "The clinic charges no weekend or after-hours surcharge. Saturday and Sunday appointments cost the same as weekday consultations. Smile Concepts provides general dentistry, cosmetic dentistry, dental implants, Invisalign, root canal therapy, and same-day emergency care across all 7 days. The practice holds 667 Google reviews at 4.8 out of 5, placing it among the top-rated Sydney weekend providers.",
        "All treating dentists maintain current AHPRA registration. The practice uses digital intraoral scanners and low-radiation CBCT imaging for accurate weekend diagnosis without requiring patients to return on a weekday for imaging.",
     ]},
    {"rank": 3, "name": "Pure Dentistry", "location": "Brisbane, QLD", "featured": True,
     "rating": "4.6/5 (330 reviews)", "pricing": "Mid-range", "hours": "7 days including weekends and public holidays",
     "address": "11/1932-1974 Logan Road, Upper Mt Gravatt QLD 4122", "phone": "(07) 3343 4869",
     "website": "https://www.puredentistry.com.au/", "ahpra": True,
     "body": [
        "Pure Dentistry holds QIP accreditation, meeting Australian Standards for dental practice quality and safety. The practice operates 7 days per week including public holidays from its Upper Mount Gravatt location on Logan Road. The phone line runs from 5am to 11pm daily, giving early-morning and late-evening access for patients booking weekend emergency appointments.",
        "Pure Dentistry offers IV sedation and sleep dentistry on weekends, a service that most Australian weekend clinics do not provide. This makes the practice suitable for patients with dental anxiety, needle phobia, or complex procedures requiring sedation that cannot wait for a weekday booking. Weekend services include examinations, fillings, extractions, root canals, crowns, and children's dentistry.",
        "All Pure Dentistry clinicians hold current AHPRA registration. The practice has accumulated 330 Google reviews at 4.6 out of 5, reflecting consistent patient satisfaction across weekday and weekend appointments.",
     ]},
    {"rank": 4, "name": "United Dental Care", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "7 days including weekends",
     "address": "Suite 5/377 Sussex St, Sydney NSW 2000", "phone": "(02) 9267 7174",
     "website": "https://www.uniteddentalcare.com.au/",
     "body": [
        "United Dental Care operates from two Sydney locations, one in the CBD on Sussex Street and a second in Campsie. The practice closes only on Christmas Day and New Year's Day, providing weekend general and emergency dentistry across the remaining 363 days of the year. Weekend services include examinations, fillings, extractions, root canals, dentures, and teeth whitening.",
        "The Sussex Street location sits within walking distance of Town Hall and Wynyard stations, making it accessible for patients travelling from across Sydney on weekends. All treating dentists hold current AHPRA registration, and the practice accepts major health funds with HICAPS claiming available on weekends.",
     ]},
    {"rank": 5, "name": "Emergency Dentist Sydney", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Competitive and affordable", "hours": "7 days including weekends",
     "address": "Suite 601A, 185 Elizabeth St, Sydney NSW 2000", "phone": "(02) 9267 8540",
     "website": "https://www.emergencydentistsydney.com.au/",
     "body": [
        "Emergency Dentist Sydney focuses exclusively on urgent dental care. The practice operates 7 days per week with a dedicated emergency team trained to handle severe toothache, dental trauma, post-extraction complications, and broken teeth. Unlike general practices that fit emergencies between routine appointments, this clinic prioritises urgent cases on weekends.",
        "The practice charges no call-out fee for weekend appointments. Patients pay standard consultation and treatment rates without additional surcharges. The Elizabeth Street location is accessible from Museum and St James stations, and the clinic provides same-day appointments for most weekend emergency presentations.",
     ]},
    {"rank": 6, "name": "Dental on Flinders", "location": "Melbourne, VIC", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "Monday to Saturday including after-hours",
     "address": "Level 5, 276 Flinders St, Melbourne VIC 3000", "phone": "(03) 9041 0049",
     "website": "https://www.dentalonflinders.com.au/",
     "body": [
        "Dental on Flinders operates directly opposite Flinders Street Station, one of Melbourne's most accessible public transport hubs. The practice offers Saturday sessions and after-hours weekday appointments, serving commuters and city workers who cannot attend during standard business hours. Sunday appointments are not currently available.",
        "The clinic provides transparent pricing with treatment quotes provided before any procedure begins. Weekend services include examinations, scale and cleans, fillings, root canals, extractions, and emergency dentistry. All treating dentists hold current AHPRA registration. The practice accepts major health funds and offers HICAPS claiming on Saturdays.",
     ]},
    {"rank": 7, "name": "24 Hour Emergency Dentist", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "24 hours weekdays, weekend appointments available",
     "address": "Suite 431, 307 Pitt St, Sydney NSW 2000", "phone": "9154 0145",
     "website": "https://www.24hour-dentist.com.au/",
     "body": [
        "24 Hour Emergency Dentist provides round-the-clock weekday availability, with weekend appointments arranged by phone. The practice treats all dental emergencies, including facial trauma, severe toothache, lost fillings, broken crowns, and post-surgical complications. Patients call ahead to confirm weekend appointment times and availability.",
        "The Pitt Street location shares the building with Smile Concepts, giving patients access to both general and emergency weekend dental services in one central Sydney location. All treating clinicians hold current AHPRA registration.",
     ]},
    {"rank": 8, "name": "MGA Dental", "location": "Brisbane and Gold Coast, QLD", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "7 days a week",
     "address": "202 Pinelands Rd, Sunnybank Hills QLD 4109 (also Gold Coast: 122 Salerno St, Surfers Paradise QLD 4217)", "phone": "(07) 3273 3343",
     "website": "https://www.mgadental.com.au/",
     "body": [
        "MGA Dental operates from two southeast Queensland locations, serving Brisbane residents from Sunnybank Hills and Gold Coast residents from Surfers Paradise. The family-run practice offers weekend availability at both locations, providing general and emergency dentistry 7 days per week. Weekend services include examinations, fillings, extractions, crowns, bridges, and children's dentistry.",
        "The dual-location model gives patients across the Brisbane to Gold Coast corridor access to weekend dental care within a 30-minute drive. All treating dentists hold current AHPRA registration, and the practice accepts major health funds at both clinics.",
     ]},
    {"rank": 9, "name": "Clear Dental", "location": "Sydney, NSW", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Mid-range", "hours": "Open 7 days",
     "address": "131 Clarence St, Sydney NSW 2000", "phone": "(02) 9456 6557",
     "website": "https://www.cleardental.com.au/",
     "body": [
        "Clear Dental operates 5 Sydney locations, with weekend availability varying by site. The Clarence Street CBD location offers the most consistent weekend hours. The practice prioritises emergency patients on weekends, ensuring that severe toothache and dental trauma cases receive same-day assessment.",
        "Weekend services include examinations, fillings, root canals, extractions, Invisalign consultations, and porcelain veneers. Patients should call ahead to confirm weekend hours at their preferred location, as schedules change based on dentist availability. All treating clinicians hold current AHPRA registration.",
     ]},
    {"rank": 10, "name": "Maddingley Dental Care", "location": "Bacchus Marsh, VIC", "featured": False,
     "rating": "Contact the practice for current review ratings", "pricing": "Contact for pricing", "hours": "After-hours and weekend emergency care",
     "address": "Bacchus Marsh VIC (contact for address)", "phone": "Contact for phone",
     "website": "https://maddingleydentalcare.com.au/",
     "body": [
        "Maddingley Dental Care serves Bacchus Marsh, Melton, and surrounding regional Victorian communities with after-hours and weekend emergency dental services. The practice addresses a critical gap in weekend dental access for residents outside metropolitan Melbourne, where weekend clinic options remain limited.",
        "Patients contact the practice directly to arrange weekend emergency appointments. The clinic provides emergency examinations, pain relief, temporary restorations, and extractions on weekends, with comprehensive treatment scheduled for weekday follow-up where necessary.",
     ]},
]

COST_HEADING = "How much does weekend dental care cost in Australia?"
COST = [
    "Weekend dental consultation fees in Australia range from $100 to $250 for a standard examination. Many practices apply a weekend surcharge of $50 to $150 on top of standard fees, reflecting higher staffing costs for Saturday and Sunday sessions. However, 2 of the 3 top-ranked clinics on this list, MC Dental and Smile Concepts, charge no weekend surcharge at all.",
    "Common weekend procedures carry the following price ranges. These figures align with the Australian Dental Association's annual fee survey.",
]
COST_PRICES = [
    ("Weekend consultation", "$100 – $250"),
    ("Weekend surcharge", "$50 – $150"),
    ("Emergency tooth extraction (weekend)", "$250 – $450"),
    ("Weekend filling", "$150 – $350"),
    ("Root canal therapy (weekend)", "$900 – $2,500"),
    ("Child Dental Benefits Schedule", "Up to $1,095 over 2 years"),
]
COST_AFTER = [
    'The Child Dental Benefits Schedule (CDBS) provides up to $1,095 in dental coverage over 2 calendar years for eligible children aged 2 to 17. Medicare does not cover adult dental services in private practice, meaning adults pay out of pocket or claim through private health insurance. Most weekend clinics accept major health funds with HICAPS on-the-spot claiming. Read our full <a href="/blog/costs/">dental costs guide</a> for detailed procedure pricing.',
]

CHOOSE_HEADING = "How do you choose a weekend dentist in Australia?"
CHOOSE_INTRO = "Choosing a weekend dentist requires asking 5 specific questions before booking an appointment."
CHOOSE_CRITERIA = [
    ("What are their exact weekend opening hours?", "Some clinics advertise \"open 7 days\" but operate only Saturday morning or limited Sunday hours. Confirm the exact Saturday and Sunday session times before travelling. Dental on Flinders offers Saturday sessions but no Sunday availability, while MC Dental runs full sessions both days."),
    ("Does the clinic charge a weekend surcharge?", "Weekend surcharges add $50 to $150 to standard fees. MC Dental and Smile Concepts charge no surcharge, while other practices apply the fee to cover weekend staffing costs. Ask about surcharges when booking."),
    ("Is the treating dentist AHPRA-registered?", "Every dentist practising in Australia must hold current registration with the Australian Health Practitioner Regulation Agency. Verify any dentist on the AHPRA public register before treatment. All 10 clinics on this list employ AHPRA-registered dentists."),
    ("What services are available on weekends?", "Some clinics offer only emergency examinations on weekends, while others provide full general and cosmetic dentistry. Complex procedures, including surgical extractions and multi-visit root canals, may require weekday follow-up. Confirm service availability when booking."),
    ("What do Google reviews say about weekend care?", "Read reviews specifically mentioning Saturday or Sunday visits. Look for patterns in wait times, billing transparency, and pain management. Clinics with more than 50 reviews at 4.0 or higher demonstrate consistent weekend service quality."),
]
CHOOSE_AFTER = [
    'For urgent dental needs outside standard weekend hours, find an <a href="/australia/emergency-dentist/">emergency dentist</a> or an <a href="/australia/after-hours-dentist/">after hours dentist</a> through our verified directories.',
]

METHODOLOGY_HEADING = "How did we rank these weekend dentists?"
METHODOLOGY = [
    "We evaluated every clinic against 8 criteria. Each practice had to meet all 8 to qualify for this list.",
]
METHODOLOGY_CRITERIA = [
    "Weekend availability: Verified Saturday and Sunday hours confirmed via the practice website and direct phone contact.",
    "AHPRA registration: Every treating dentist at the practice holds current registration with the Australian Health Practitioner Regulation Agency.",
    "Google review volume: Minimum 50 reviews, demonstrating sufficient patient volume for statistical reliability.",
    "Google review rating: 4.0 out of 5 or higher, reflecting consistent patient satisfaction.",
    "Weekend pricing transparency: Weekend surcharge clearly disclosed or confirmed absent on the practice website.",
    "Range of weekend services: Multiple treatment categories available on weekends, not only emergency examinations.",
    "Same-day appointment availability: Capacity to book and treat patients on the same day they contact the practice on a weekend.",
    "Accessibility and location: Proximity to public transport or parking, and physical access for patients with mobility needs.",
]
METHODOLOGY_AFTER = [
    'Paid placements in positions 1 to 3 met all 8 criteria before being offered featured placement. Read our full <a href="/methodology/">methodology</a> for details on how we verify data and update rankings.',
]

FAQ_HEADING = "Frequently Asked Questions"
FAQS = [
    ("Are there dentists open on Saturdays in Australia?",
     'Yes. Australia has over 200 dental practices that offer Saturday appointments. The 10 clinics on this list all provide Saturday dental care, with hours ranging from morning-only sessions to full-day availability. MC Dental Melbourne Central and Smile Concepts Sydney offer the most comprehensive Saturday hours, operating from 9am to 4pm and throughout standard business hours respectively. To find a Saturday dentist near you, use our <a href="/australia/emergency-dentist/">emergency dentist</a> directory.'),
    ("Are there dentists open on Sundays in Australia?",
     "Yes, but fewer practices open on Sundays than Saturdays. MC Dental, Smile Concepts, Pure Dentistry, United Dental Care, and Emergency Dentist Sydney all offer Sunday appointments. Sunday dental care typically covers emergency examinations, pain relief, fillings, and extractions. Some practices require advance booking for Sunday visits, while others accept walk-in emergency patients."),
    ("Do weekend dentists charge more?",
     "Some do, some do not. Weekend surcharges range from $50 to $150 on top of standard consultation fees. MC Dental and Smile Concepts charge no weekend surcharge at all. Pure Dentistry and other mid-range clinics may apply a modest surcharge to cover weekend staffing costs. Ask about surcharges when booking to avoid unexpected charges."),
    ("What services are available on weekends?",
     'Weekend dental services include examinations, scale and cleans, fillings, root canals, extractions, emergency pain relief, and broken tooth repair. Pure Dentistry offers IV sedation and sleep dentistry on weekends. Complex procedures, including full-mouth implant placement and orthodontic adjustments, typically require weekday appointments. For specific conditions, read our guides on <a href="/australia/toothache-relief/">toothache relief</a> and find an <a href="/australia/after-hours-dentist/">after hours dentist</a> for urgent care.'),
    ("Does Medicare cover weekend dental visits?",
     "Medicare does not cover adult dental services in private practice, including weekend appointments. The Child Dental Benefits Schedule covers up to $1,095 over 2 years for eligible children aged 2 to 17, and this coverage applies on weekends at participating practices. Most weekend clinics accept private health insurance with HICAPS on-the-spot claiming."),
    ("Should I go to a weekend dentist or hospital emergency?",
     'Attend a hospital emergency department for severe facial swelling affecting breathing or swallowing, high fever above 38.5 degrees Celsius, uncontrolled bleeding, or suspected jaw fractures. Attend a weekend dentist for toothache, broken teeth, lost fillings, knocked-out teeth, dental abscesses without systemic symptoms, and post-extraction pain. A weekend dentist provides faster, more specialised care for dental-specific problems than a hospital emergency department. Learn more in our <a href="/blog/conditions/">dental conditions guide</a>.'),
    ("How do I find a weekend dentist near me?",
     'Use this list to identify clinics in your state, then call to confirm current weekend hours and availability. For broader search options, browse our directories of <a href="/australia/emergency-dentist/">emergency dentist</a> and <a href="/australia/after-hours-dentist/">after hours dentist</a> services across Australia. Verify AHPRA registration for any dentist before treatment.'),
    ("Can I get a same-day appointment on a weekend?",
     "Yes. All 10 clinics on this list offer same-day weekend appointments for emergency cases. Emergency Dentist Sydney and 24 Hour Emergency Dentist specialise in urgent same-day care. For non-emergency appointments, such as routine check-ups and cleans, book 1 to 2 weeks ahead to secure your preferred weekend time slot."),
]

CTA_TITLE = "Are you a weekend dentist in Australia?"
CTA_TEXT = "Apply to be featured in our next update."

DISCLOSURE = "Practices in positions 1 to 3 are paid placements with do-follow links. Practices in positions 4 to 10 are listed editorially with no-follow links. Paid placement never affects positions 4 to 10."


def _build_schemas():
    url = f"{SITE_URL}/australia/weekend-dentist/"
    medical = {"@context": "https://schema.org", "@type": "MedicalWebPage",
               "name": META_TITLE, "description": META_DESC,
               "about": "Weekend dentists in Australia", "inLanguage": "en-AU",
               "url": url, "dateReviewed": "2026-07"}
    item_list = {"@context": "https://schema.org", "@type": "ItemList", "name": H1,
                 "itemListElement": [{"@type": "ListItem", "position": p["rank"],
                                      "name": p["name"], "url": p.get("website", url)} for p in TOP10]}
    breadcrumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE_URL}/"},
        {"@type": "ListItem", "position": 2, "name": "Australia", "item": f"{SITE_URL}/australia/"},
        {"@type": "ListItem", "position": 3, "name": "Weekend Dentists", "item": url},
    ]}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]


SCHEMAS = _build_schemas()
