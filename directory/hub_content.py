"""Content for /australia/ — Top 10 Dentists in Australia (v2).
Transcribed verbatim from 01-australia-hub (1).md. ALL website links are nofollow."""
import json

SITE_URL = "https://fascinatingdentistry.com"
META_TITLE = "Top 10 Dentists in Australia - Reviewed and Ranked"
META_DESC = "Compare the top 10 dentists in Australia based on AHPRA registration, qualifications, patient reviews, technology, and pricing transparency. Find the best dental clinics nationwide."
H1 = "Top 10 Dentists in Australia - Reviewed and Ranked"

INTRO = [
    "Australians have access to over 18,000 registered dental practitioners across approximately 8,000 dental practices nationwide. Yet no independent, verified ranking system helps patients identify the best dentists based on objective criteria. Finding reliable, certified dental care remains a significant challenge for many patients.",
    "We ranked Australia's top dentists based on AHPRA registration, qualifications, Google reviews (minimum 50 at 4.5+), years of experience, technology, and patient feedback. This data-driven approach ensures an objective comparison. Read our full criteria in our methodology.",
    "Positions 1-3 are paid placements with do-follow links. Positions 4-10 are editorial selections with no-follow links. Paid placement never affects positions 4-10. Read our disclosures policy to understand our ranking process.",
]

WHO_TOP10 = "The top 10 dentists in Australia include leading practices across Melbourne, Perth, Brisbane, Sydney, Newcastle, and the Gold Coast. These clinics meet strict criteria for professional registration, patient satisfaction, and clinical technology."

TOP10 = [
    {"rank":1,"name":"Smile Solutions","location":"Melbourne, VIC","featured":True,"ahpra":True,
     "intro":"Smile Solutions operates as a leading multi-disciplinary dental practice in Melbourne. The practice combines extensive clinical expertise with high patient satisfaction metrics.",
     "sections":[
        ("Qualifications and credentials","The practice employs board-registered specialists and dual medical-qualified dental surgeons. Operating since 1993, the team has grown its patient base from an initial 8 patients to over 250,000 individuals. The practitioners maintain active AHPRA registration."),
        ("Special interests and expertise","Smile Solutions focuses on general dentistry, cosmetic dentistry, Invisalign, orthodontics, and dental implants. The team handles complex cases requiring integrated specialist care. They have completed over 9,000 Invisalign cases, establishing themselves as Australia's largest specialist Invisalign provider."),
        ("Technology and facilities","Located in the Manchester Unity Building, the facility accommodates comprehensive specialist treatments under one roof. The practice utilises modern dental technology to support precise diagnostics and treatment planning for All-on-4 procedures."),
        ("Patient experience and reviews","Smile Solutions holds a 4.9 out of 5 rating on Google based on 937 reviews. The clinic operates Monday to Friday from 8am to 6pm and Saturday from 8:30am to 1:30pm. The practice maintains a mid-range pricing tier."),
     ],
     "address":"Level 1, 220 Collins Street, Manchester Unity Building, Melbourne VIC 3000","phone":"13 13 96","website":"https://www.smilesolutions.com.au/","rating":"4.9/5 (937 reviews)"},
    {"rank":2,"name":"Advanced Dental Artistry","location":"Perth, WA","featured":True,"ahpra":True,
     "intro":"Advanced Dental Artistry operates as a premium dental practice in West Perth. Dr Adrian Kat leads the clinical team with a focus on full-mouth rehabilitation.",
     "sections":[
        ("Qualifications and credentials","Dr Adrian Kat brings over 25 years of clinical experience to the practice. The team maintains AHPRA registration and follows strict infection control protocols. The clinic has successfully treated over 5,100 patients requiring complex restorative procedures."),
        ("Special interests and expertise","The practice specialises in All-on-4 dental implants, full-mouth reconstruction, and porcelain veneers. The clinical team focuses on comprehensive smile restorations rather than isolated treatments."),
        ("Technology and facilities","Advanced Dental Artistry features an in-house prosthetics laboratory. This facility allows the team to customise All-on-4 prosthetics and porcelain veneers with precise specifications. The practice offers IV sedation to manage patient anxiety during surgical procedures."),
        ("Patient experience and reviews","The clinic holds a 4.9 out of 5 Google rating from 342 reviews. The practice falls into the premium pricing tier due to the complex nature of its prosthetics and surgical offerings."),
     ],
     "address":"555 Newcastle St, West Perth WA 6005","phone":"(08) 6165 3888","website":"https://advanceddentalartistry.com.au/","rating":"4.9/5 (342 reviews)"},
    {"rank":3,"name":"Dentistry on George","location":"Brisbane, QLD","featured":True,"ahpra":True,
     "intro":"Dentistry on George provides comprehensive dental care in the Brisbane central business district. The practice operates with a focus on patient comfort and advanced restorative treatments.",
     "sections":[
        ("Qualifications and credentials","Husband-and-wife dental team Mishari and Kathryn lead the practice. Both principal dentists maintain active AHPRA registration and hold memberships with the Australian Dental Association. The team has cared for Brisbane CBD patients for over 40 years."),
        ("Special interests and expertise","The clinic delivers general, implant, cosmetic, and IV-sedation dentistry. The practitioners excel in dental implants, prosthodontics, and emergency dentistry. Ranked as the number one overall dentist in Australia for 2026 by comparedentists.com.au, the team handles complex restorative cases."),
        ("Technology and facilities","The practice utilises modern dental chairs and imaging technology to support precise diagnoses. IV and twilight sedation facilities allow the team to perform complex surgical procedures comfortably. The clinic focuses on same-day emergency dentistry to address acute dental trauma."),
        ("Patient experience and reviews","Dentistry on George maintains a perfect 5.0 out of 5 Google rating based on 191 reviews. The clinic operates mid-range pricing structures. Opening hours run Monday to Tuesday from 8am to 4pm, Wednesday to Thursday from 9am to 5pm, and Friday from 9am to 2:30pm."),
     ],
     "address":"Level 12, 239 George Street, Brisbane QLD 4000","phone":"(07) 3211 1155","website":"https://www.dentistryongeorge.com.au/","rating":"5.0/5 (191 reviews)"},
    {"rank":4,"name":"Smile Concepts","location":"Sydney, NSW","featured":False,
     "desc":["Smile Concepts delivers routine visits, cosmetic dentistry, and orthodontic care to Sydney patients. The practice focuses on tailor-made treatment plans designed around individual patient needs. The clinical team utilises advanced technologies to ensure precise diagnostic and restorative outcomes. The practice prioritises patient comfort during all phases of treatment.","The clinic holds a 4.8 out of 5 rating on Google across 667 reviews. Patients praise the welcoming environment and the thoroughness of the dental team."],
     "address":"Suite 403, Level 4/307 Pitt St, Sydney NSW 2000","phone":"(02) 9267 7777","website":"https://www.smileconcepts.com.au/","rating":"4.8/5 (667 reviews)"},
    {"rank":5,"name":"Bite Dental Studios","location":"Brisbane, QLD","featured":False,
     "desc":["Established in 2010, Bite Dental Studios operates with a team holding over 40 years of combined experience. The practice delivers general, cosmetic, clear-aligner, and implant dentistry. The clinical team excels in Invisalign, All-on-4 dental implants, smile makeovers, and porcelain veneers.","The clinic maintains a perfect 5.0 out of 5 rating on Google based on 203 reviews. The practice focuses on comprehensive aesthetic and functional restorations."],
     "address":"Level 6, 141 Queen Street, Brisbane QLD 4000","phone":"(07) 3221 5399","website":"https://bitedental.com.au/","rating":"5.0/5 (203 reviews)"},
    {"rank":6,"name":"Pure Dentistry","location":"Brisbane, QLD","featured":False,
     "desc":["Pure Dentistry holds full QIP accreditation and operates 7 days a week, including public holidays. The practice provides general, emergency, cosmetic, implant, and sedation dentistry. The team accepts call inquiries from 5am to 11pm daily.","The clinic features after-hours emergency care, IV sedation, general anaesthesia, and same-day emergency appointments. The practice holds a 4.6 out of 5 rating on Google across 330 reviews."],
     "address":"11/1932-1974 Logan Road, Upper Mt Gravatt QLD 4122","phone":"(07) 3343 4869","website":"https://www.puredentistry.com.au/","rating":"4.6/5 (330 reviews)"},
    {"rank":7,"name":"Greenslopes Dental Studio","location":"Brisbane, QLD","featured":False,
     "desc":["Greenslopes Dental Studio operates as a Diamond Invisalign provider as of 2022. The practice won the Invisalign Lifetime Achievement Award in 2025. The clinical team provides general, cosmetic, implant, and children's dentistry.","The clinic offers flexible payment plans to make orthodontic treatment accessible. The practice maintains a 4.8 out of 5 rating on Google based on 216 reviews."],
     "address":"359 Cornwall Street, Greenslopes QLD 4120","phone":"(07) 3733 3555","website":"https://www.greenslopesdental.com.au/","rating":"4.8/5 (216 reviews)"},
    {"rank":8,"name":"The Good Dentist","location":"Newcastle, NSW","featured":False,
     "desc":["The Good Dentist designs its practice around patient comfort and satisfaction. The clinic creates a friendly, inviting atmosphere specifically for anxious patients. The team performs routine check-ups alongside advanced restorative and cosmetic treatments.","The practice holds a 4.8 out of 5 rating on Google across 461 reviews. Patients highlight the gentle approach of the clinical staff."],
     "address":"Suite 1/93 Darby St, Cooks Hill NSW 2300","phone":"(02) 4929 6007","website":"https://thegooddentist.com.au/","rating":"4.8/5 (461 reviews)"},
    {"rank":9,"name":"Gorgeous Smiles","location":"Melbourne, VIC","featured":False,
     "desc":["Gorgeous Smiles provides individualised and comprehensive treatment plans for over 30,000 patients. The practice delivers routine check-ups, hygiene appointments, dental implants, and cosmetic dentistry. The clinical team focuses on long-term oral health maintenance.","The clinic holds a 4.9 out of 5 rating on Google across 1,496 reviews. The high review volume demonstrates consistent patient satisfaction over time."],
     "address":"121 Exhibition St, Melbourne VIC 3000","phone":"(03) 9042 0483","website":"https://www.gorgeoussmiles.com.au/","rating":"4.9/5 (1,496 reviews)"},
    {"rank":10,"name":"Australia Fair Dental Care","location":"Gold Coast, QLD","featured":False,
     "desc":["Australia Fair Dental Care delivers comprehensive oral care for patients of all ages. The practice operates inside the Australia Fair West Shopping Centre for convenient access. The team handles general, cosmetic, and emergency dental needs.","The clinic holds a 4.3 out of 5 rating on Google based on 62 reviews. The central location makes it a practical choice for families."],
     "address":"Australia Fair West Shopping Centre, Scarborough Street and Young St, Southport QLD 4215","phone":"(07) 5591 2661","website":"http://www.australiafairdental.com.au/","rating":"4.3/5 (62 reviews)"},
]

COST = [
    "Dental care costs in Australia vary significantly based on the complexity of the procedure and the location of the practice. The Australian Dental Association fee survey provides clear cost benchmarks for common treatments.",
    "Routine dental check-ups cost between $150 and $300. Dental fillings range from $150 to $300 depending on the material used. Ceramic or metal dental crowns cost between $1,500 and $2,500. Dental implants represent a significant investment, ranging from $3,000 to $6,500 per tooth. Root canal treatments cost between $900 and $2,000. Medicare does not cover most adult dental services. The Child Dental Benefits Schedule provides up to $1,095 over two years for eligible children aged 0-17. Private health funds cover portions of these costs depending on the policy extras.",
]

CHOOSE_INTRO = "Choosing a dentist in Australia requires evaluating five specific criteria to ensure safe and effective treatment. Patients must verify credentials, review patient feedback, and assess practice technology."
CHOOSE_CRITERIA = [
    ("Is the dentist AHPRA-registered?", "Verify the practitioner's registration status on the AHPRA public register to ensure legal compliance and professional standing."),
    ("What are their qualifications?", "Check for additional qualifications, specialist board registrations, and ongoing continuing professional development."),
    ("How many Google reviews and what rating?", "Look for practices with a minimum of 50 reviews and a rating of 4.5 or higher."),
    ("What technology do they use?", "Assess whether the practice uses modern digital imaging, intraoral scanners, and sterile filtration systems."),
    ("Is pricing transparent?", "Ensure the practice provides itemised treatment plans with clear pricing aligned with ADA fee survey benchmarks."),
]

METHODOLOGY = [
    "Our methodology relies on eight objective criteria to rank dental practices fairly. We evaluate AHPRA registration, professional qualifications, Google review volume, Google review rating, years of clinical experience, adoption of modern technology, patient feedback trends, and pricing transparency.",
    "We cite AHPRA, ADA, AIHW, and Australian government health data as authoritative sources to validate our data.",
]

SERVICE_CATEGORIES = [
    ("Emergency & Urgent Care", [("Emergency Dentist","/australia/emergency-dentist/"),("After-Hours Dentist","/australia/after-hours-dentist/"),("Weekend Dentist","/australia/weekend-dentist/"),("Toothache Relief","/australia/toothache-relief/"),("Broken Tooth Repair","/australia/broken-tooth-repair/")]),
    ("General & Preventive", [("Dental Check-Up","/australia/dental-check-up/"),("Teeth Cleaning","/australia/teeth-cleaning/"),("Sports Mouthguards","/australia/sports-mouthguards/"),("Night Guards","/australia/night-guards/"),("Pediatric Dentist","/australia/pediatric-dentist/"),("Childrens Dentist","/australia/childrens-dentist/")]),
    ("Restorative", [("Dental Fillings","/australia/dental-fillings/"),("Dental Crowns","/australia/dental-crowns/"),("Dental Bridges","/australia/dental-bridges/"),("Dentures","/australia/dentures/"),("Tooth Extraction","/australia/tooth-extraction/"),("Root Canal Treatment","/australia/root-canal-treatment/"),("Endodontist","/australia/endodontist/")]),
    ("Dental Implants", [("Dental Implants","/australia/dental-implants/"),("All-on-4 Dental Implants","/australia/all-on-4/"),("Mini Dental Implants","/australia/mini-implants/"),("Same-Day Dental Implants","/australia/same-day-implants/"),("Implant-Supported Dentures","/australia/implant-supported-dentures/"),("Bone Grafting","/australia/bone-grafting/"),("Sinus Lift","/australia/sinus-lift/")]),
    ("Cosmetic", [("Cosmetic Dentistry","/australia/cosmetic-dentistry/"),("Teeth Whitening","/australia/teeth-whitening/"),("Porcelain Veneers","/australia/porcelain-veneers/"),("Composite Bonding","/australia/composite-bonding/"),("Smile Makeover","/australia/smile-makeover/")]),
    ("Orthodontics", [("Braces","/australia/braces/"),("Invisalign","/australia/invisalign/"),("Clear Aligners","/australia/clear-aligners/"),("Orthodontist","/australia/orthodontist/")]),
    ("Specialist", [("Periodontist","/australia/periodontist/"),("Gum Disease Treatment","/australia/gum-disease-treatment/"),("Gum Graft Surgery","/australia/gum-graft-surgery/"),("LANAP","/australia/lanap/"),("Wisdom Teeth Removal","/australia/wisdom-teeth-removal/"),("TMJ Treatment","/australia/tmj-treatment/"),("Oral Cancer Screening","/australia/oral-cancer-screening/"),("Holistic Dentist","/australia/holistic-dentist/")]),
]

CITIES_INTRO = "Patients can locate top-tier dental care by exploring our dedicated city hubs. Each city hub lists all 42 available services alongside a city-specific Top 10 dentists listicle."
CITIES = [("Top 10 Dentists in Sydney","/australia/sydney/"),("Top 10 Dentists in Brisbane","/australia/brisbane/")]
CITIES_FUTURE = "We plan to launch additional city hubs for Melbourne, Perth, Adelaide, Canberra, Hobart, and Darwin in the near future."

RELATED_INTRO = "We provide five comprehensive cluster hubs covering major dental specialties. These guides offer in-depth information on procedures, candidacy, and recovery."
RELATED = [
    ("Dental Implantology Guide","/blog/implantology/","Learn about implant procedures, bone grafting, and All-on-4 treatments."),
    ("Orthodontics Guide","/blog/orthodontics/","Explore options for braces, clear aligners, and bite correction."),
    ("Cosmetic Dentistry Guide","/blog/cosmetic-dentistry/","Discover treatments for veneers, whitening, and smile makeovers."),
    ("Dental Conditions Guide","/blog/conditions/","Understand symptoms and treatments for common oral health issues."),
    ("Dental Costs Guide","/blog/costs/","Review pricing structures and insurance coverage details."),
]

FAQS = [
    ("How are dentists regulated in Australia?","All Australian dentists must register with the Dental Board of Australia under AHPRA. Registration requires verified qualifications, English language proficiency, and ongoing continuing professional development. Patients can check any dentist's registration status on the AHPRA public register."),
    ("How often should I visit the dentist?","The ADA recommends a dental check-up every 6 to 12 months depending on individual oral health needs. Patients with gum disease, a history of decay, or complex dental work require more frequent visits. Regular visits prevent severe decay and lower overall treatment costs."),
    ("Is dental care covered by Medicare?","Medicare does not cover most dental services for adults. The Child Dental Benefits Schedule provides up to $1,095 over two years for eligible children aged 0-17. Public dental services are available through state health systems but typically have long waiting lists."),
    ("How do I check if a dentist is registered?","You can verify any dentist's AHPRA registration on the AHPRA public register. Search by name or registration number to confirm their status. Registration status should always remain current with no conditions or undertakings."),
    ("Can I get free dental care in Australia?","Free or low-cost dental care is available through state public dental services for eligible concession card holders. Children access free care under the CDBS. Some universities also offer reduced-cost treatment at their dental teaching clinics, though waiting lists apply."),
    ("What should I look for when choosing a dentist in Australia?","Check AHPRA registration, qualifications, Google reviews, technology, transparent pricing, and health fund acceptance. Evaluating these factors ensures safe, high-quality treatment. Our methodology page explains our full ranking criteria in detail."),
    ("Are the dentists on this list paying to be ranked?","Positions 1-3 on our Top 10 lists represent paid placements with do-follow links. Positions 4-10 feature editorial selections with no-follow links. Paid placement never affects the editorial ranking of positions 4-10."),
]

ABOUT = "Fascinating Dentistry operates as an independent dental directory committed to transparency and objective ranking standards. We design our ranking criteria with reference to ADA practitioner standards and AHPRA registration requirements. Learn more about Fascinating Dentistry and our mission to connect patients with verified dental professionals."

DISCLOSURE = "Practices in positions 1-3 are paid placements with do-follow links. Practices in positions 4-10 are listed editorially with no-follow links. Paid placement never affects positions 4-10."

def _build_schemas():
    item_list = {"@context":"https://schema.org","@type":"ItemList","name":H1,"itemListElement":[{"@type":"ListItem","position":p["rank"],"name":p["name"],"url":p.get("website",f"{SITE_URL}/australia/")} for p in TOP10]}
    breadcrumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":f"{SITE_URL}/"},{"@type":"ListItem","position":2,"name":"Australia","item":f"{SITE_URL}/australia/"}]}
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQS]}
    medical = {"@context":"https://schema.org","@type":"MedicalWebPage","name":META_TITLE,"description":META_DESC,"about":"Top 10 dentists in Australia","inLanguage":"en-AU"}
    return [json.dumps(medical), json.dumps(item_list), json.dumps(breadcrumb), json.dumps(faq)]

SCHEMAS = _build_schemas()
