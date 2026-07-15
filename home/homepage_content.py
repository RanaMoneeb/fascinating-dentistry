"""COMPLETE homepage content, transcribed verbatim from content/01-homepage.md.
Do NOT trim these paragraphs. Internal links to pages that don't exist yet render as
muted text (not broken links) via the is_live_url template tag."""

import json


# ---- Meta ----
META_TITLE = "Fascinating Dentistry: Australian Dental Guide & Directory"
META_DESC = (
    "Find a dentist in Australia. Fascinating Dentistry offers an independent directory of "
    "dental services, conditions, costs, and oral health data reviewed by professionals."
)

# ---- Hero ----
HERO_TITLE = "Australia's Most Comprehensive Dental Resource"
HERO_INTRO = (
    "Fascinating Dentistry is Australia's independent dental information resource, a public "
    "directory of dental services, conditions, treatments, costs, and oral health data, written "
    "and reviewed by AHPRA-registered Australian dental professionals. We do not operate clinics, "
    "sell treatments, or rank providers for payment. Our platform publishes over 10,000 pages of "
    "verified data across 28 distinct oral health topic areas. We connect patients with verified "
    "practice profiles and provide transparent cost estimates based on Australian Dental "
    "Association (ADA) fee surveys. Patients seeking a local practitioner or researching clinical "
    "procedures find factual, unbiased data on our platform."
)

# ---- Find a dentist ----
FIND_DENTIST = {
    "answer": (
        "You find a dentist in Australia by using our location-based directory to browse verified "
        "practice profiles across all states and territories. We do not endorse clinics for payment "
        "or accept advertising to manipulate rankings. We maintain independent practice profiles to "
        "help patients locate local care based on their specific geographic or clinical requirements. "
        "Patients narrow their search using specific locations, priority treatments, or curated top 10 "
        "lists."
    ),
    "australia_wide": {"name": "Australia-wide dental directory", "href": "/australia/"},
    "location": {
        "intro": "Patients locate dental practices by exploring major capital cities and regional hubs. We maintain dedicated directories for 8 capital cities:",
        "items": [
            {"name": "Dentists in Sydney", "href": "/australia/sydney/"},
            {"name": "Dentists in Melbourne", "href": "/australia/melbourne/"},
            {"name": "Dentists in Brisbane", "href": "/australia/brisbane/"},
            {"name": "Dentists in Perth", "href": "/australia/perth/"},
            {"name": "Dentists in Adelaide", "href": "/australia/adelaide/"},
            {"name": "Dentists in Canberra", "href": "/australia/canberra/"},
            {"name": "Dentists in Hobart", "href": "/australia/hobart/"},
            {"name": "Dentists in Darwin", "href": "/australia/darwin/"},
        ],
    },
    "service": {
        "intro": "Patients locate specialists by searching specific treatment types. We list verified providers for 10 high-priority dental services:",
        "items": [
            {"name": "Emergency Dentist", "href": "/australia/emergency-dentist/"},
            {"name": "Cosmetic Dentist", "href": "/australia/cosmetic-dentist/"},
            {"name": "Family Dentist", "href": "/australia/family-dentist/"},
            {"name": "Affordable Dentist", "href": "/australia/affordable-dentist/"},
            {"name": "Teeth Whitening", "href": "/australia/teeth-whitening/"},
            {"name": "Dental Implants", "href": "/australia/dental-implants/"},
            {"name": "Invisalign", "href": "/australia/invisalign/"},
            {"name": "Wisdom Teeth Removal", "href": "/australia/wisdom-teeth-removal/"},
            {"name": "Porcelain Veneers", "href": "/australia/porcelain-veneers/"},
            {"name": "Dental Crowns", "href": "/australia/dental-crowns/"},
        ],
    },
    "top10": {
        "intro": "Patients review curated lists of prominent practices in major metropolitan areas. We publish 6 major city listicles:",
        "items": [
            {"name": "Top 10 Dentists in Sydney", "href": "/australia/sydney/"},
            {"name": "Top 10 Dentists in Melbourne", "href": "/australia/melbourne/"},
            {"name": "Top 10 Dentists in Brisbane", "href": "/australia/brisbane/"},
            {"name": "Top 10 Dentists in Perth", "href": "/australia/perth/"},
            {"name": "Top 10 Dentists in Adelaide", "href": "/australia/adelaide/"},
            {"name": "Top 10 Dentists in Canberra", "href": "/australia/canberra/"},
        ],
    },
}

# ---- Services covered ----
SERVICES = {
    "answer": (
        "Fascinating Dentistry covers 42 specific dental services grouped into 8 distinct specialty "
        "categories. Patients access detailed clinical descriptions, procedure steps, and recovery "
        "timelines for every treatment. We organise these services into clear categories to help "
        "users navigate related procedures and understand their full treatment options."
    ),
    "hub": {"name": "full services hub", "href": "/services/"},
    "specialties": [
        {"name": "General & Preventive Dentistry", "desc": "General dentistry maintains oral health and prevents disease progression. Patients access 6 core preventive services.", "items": [
            {"name": "General Dentistry", "href": "/australia/general-dentistry/"},
            {"name": "Check-up and Clean", "href": "/australia/check-up-and-clean/"},
            {"name": "Dental X-Rays", "href": "/australia/dental-x-rays/"},
            {"name": "Fluoride Treatment", "href": "/australia/fluoride-treatment/"},
            {"name": "Dental Sealants", "href": "/australia/dental-sealants/"},
            {"name": "Oral Hygiene", "href": "/australia/oral-hygiene/"},
        ]},
        {"name": "Restorative Dentistry", "desc": "Restorative procedures repair damaged teeth and restore oral function. We detail 7 restorative treatments.", "items": [
            {"name": "Dental Fillings", "href": "/australia/dental-fillings/"},
            {"name": "Dental Crowns", "href": "/australia/dental-crowns/"},
            {"name": "Dental Bridges", "href": "/australia/dental-bridges/"},
            {"name": "Inlays and Onlays", "href": "/australia/inlays-and-onlays/"},
            {"name": "Root Canal Treatment", "href": "/australia/root-canal-treatment/"},
            {"name": "Dental Bonding", "href": "/australia/dental-bonding/"},
            {"name": "Tooth Extraction", "href": "/australia/tooth-extraction/"},
        ]},
        {"name": "Cosmetic Dentistry", "desc": "Cosmetic procedures improve the aesthetic appearance of teeth and gums. We explain 6 aesthetic services, anchored by the Cosmetic Dentistry hub.", "items": [
            {"name": "Cosmetic Dentistry", "href": "/australia/cosmetic-dentistry/"},
            {"name": "Teeth Whitening", "href": "/australia/teeth-whitening/"},
            {"name": "Porcelain Veneers", "href": "/australia/porcelain-veneers/"},
            {"name": "Composite Veneers", "href": "/australia/composite-veneers/"},
            {"name": "Smile Makeover", "href": "/australia/smile-makeover/"},
            {"name": "Gum Contouring", "href": "/australia/gum-contouring/"},
        ]},
        {"name": "Orthodontics", "desc": "Orthodontic treatment aligns teeth and corrects jaw discrepancies. We outline 6 orthodontic solutions.", "items": [
            {"name": "Traditional Braces", "href": "/australia/traditional-braces/"},
            {"name": "Invisalign", "href": "/australia/invisalign/"},
            {"name": "Clear Aligners", "href": "/australia/clear-aligners/"},
            {"name": "Ceramic Braces", "href": "/australia/ceramic-braces/"},
            {"name": "Lingual Braces", "href": "/australia/lingual-braces/"},
            {"name": "Early Orthodontic Treatment", "href": "/australia/early-orthodontic-treatment/"},
        ]},
        {"name": "Dental Implants", "desc": "Implantology replaces missing teeth with permanent titanium fixtures. We provide guides on 5 implant procedures.", "items": [
            {"name": "Dental Implants", "href": "/australia/dental-implants/"},
            {"name": "Single Tooth Implant", "href": "/australia/single-tooth-implant/"},
            {"name": "All-on-4 Implants", "href": "/australia/all-on-4/"},
            {"name": "Implant-Supported Dentures", "href": "/australia/implant-supported-dentures/"},
            {"name": "Bone Grafting", "href": "/australia/bone-grafting/"},
        ]},
        {"name": "Oral Surgery", "desc": "Oral surgery addresses complex extractions and structural jaw issues. We detail 5 surgical treatments anchored by the Oral Surgery hub.", "items": [
            {"name": "Oral Surgery", "href": "/australia/oral-surgery/"},
            {"name": "Wisdom Teeth Removal", "href": "/australia/wisdom-teeth-removal/"},
            {"name": "Corrective Jaw Surgery", "href": "/australia/corrective-jaw-surgery/"},
            {"name": "Sleep Apnoea Treatment", "href": "/australia/sleep-apnoea-treatment/"},
        ]},
        {"name": "Paediatric Dentistry", "desc": "Paediatric specialists treat infants, children, and adolescents. We cover 5 child-specific areas via the Paediatric Dentistry hub.", "items": [
            {"name": "Paediatric Dentistry", "href": "/australia/paediatric-dentistry/"},
            {"name": "Childrens Dentist", "href": "/australia/childrens-dentist/"},
            {"name": "Fissure Sealants", "href": "/australia/fissure-sealants/"},
            {"name": "Orthodontics for Children", "href": "/australia/orthodontics-for-children/"},
            {"name": "Dental Care During Pregnancy", "href": "/australia/dental-care-during-pregnancy/"},
        ]},
        {"name": "Specialist Services", "desc": "Specialist services address highly specific complex dental conditions. We provide 4 dedicated hubs.", "items": [
            {"name": "Endodontics", "href": "/australia/endodontist/"},
            {"name": "Periodontics", "href": "/australia/periodontics/"},
            {"name": "Prosthodontics", "href": "/australia/prosthodontics/"},
            {"name": "Oral Medicine", "href": "/australia/oral-medicine/"},
        ]},
    ],
}

# ---- How it works ----
HOW_IT_WORKS = (
    "Australian dental services operate as a dual system comprising private clinics and "
    "government-funded public dental clinics. Approximately 84% of dental services in Australia "
    "are delivered by private practitioners, according to the Australian Institute of Health and "
    "Welfare (AIHW). Patients pay out-of-pocket fees or use private health insurance at private "
    "clinics. Public dental clinics provide free or low-cost treatment to eligible individuals, "
    "including concession card holders and children. Eligibility and waiting times for public "
    "dental services vary by state and territory."
)

# ---- Conditions ----
CONDITIONS = {
    "answer": (
        "We cover over 50 distinct oral health conditions ranging from common tooth decay to rare "
        "mucosal diseases. Patients access detailed clinical guides outlining symptoms, causes, and "
        "evidence-based treatment options. We categorise these conditions to help patients locate "
        "specific information quickly. You can browse the complete Conditions Hub to find 20 of the "
        "most searched dental issues:"
    ),
    "hub": {"name": "Conditions Hub", "href": "/blog/conditions/"},
    "items": [
        {"name": "Tooth Decay", "href": "/blog/conditions/tooth-decay/"},
        {"name": "Gum Disease", "href": "/blog/conditions/gum-disease/"},
        {"name": "Gingivitis", "href": "/blog/conditions/gingivitis/"},
        {"name": "Periodontitis", "href": "/blog/conditions/periodontitis/"},
        {"name": "Tooth Abscess", "href": "/blog/conditions/tooth-abscess/"},
        {"name": "Pulpitis", "href": "/blog/conditions/pulpitis/"},
        {"name": "Sensitive Teeth", "href": "/blog/conditions/sensitive-teeth/"},
        {"name": "Bruxism (Teeth Grinding)", "href": "/blog/conditions/bruxism/"},
        {"name": "TMJ Disorders", "href": "/blog/conditions/tmj-disorders/"},
        {"name": "Dry Mouth", "href": "/blog/conditions/dry-mouth/"},
        {"name": "Halitosis (Bad Breath)", "href": "/blog/conditions/halitosis/"},
        {"name": "Canker Sores", "href": "/blog/conditions/canker-sores/"},
        {"name": "Oral Thrush", "href": "/blog/conditions/oral-thrush/"},
        {"name": "Oral Cancer", "href": "/blog/conditions/oral-cancer/"},
        {"name": "Leukoplakia", "href": "/blog/conditions/leukoplakia/"},
        {"name": "Geographic Tongue", "href": "/blog/conditions/geographic-tongue/"},
        {"name": "Dental Fluorosis", "href": "/blog/conditions/dental-fluorosis/"},
        {"name": "Enamel Erosion", "href": "/blog/conditions/enamel-erosion/"},
        {"name": "Malocclusion", "href": "/blog/conditions/malocclusion/"},
        {"name": "Impacted Teeth", "href": "/blog/conditions/impacted-teeth/"},
    ],
}

# ---- Costs ----
COSTS = {
    "answer": (
        "Dental care costs in Australia range from $50 for a basic examination to $7,000 for a "
        "single dental implant. We provide transparent cost estimates using data from the ADA annual "
        "fee survey and AIHW patient expenditure reports. Patients compare exact prices for "
        "treatments before booking appointments. Our cost resources divide into 4 specific categories."
    ),
    "categories": [
        {
            "name": "Cost Guides by Treatment",
            "intro": "We publish 8 detailed cost guides outlining average market rates.",
            "hub": {"name": "Costs Hub", "href": "/blog/costs/"},
            "items": [
                {"name": "Cost of Dental Implants", "href": "/blog/costs/dental-implants/"},
                {"name": "Cost of Root Canal", "href": "/blog/costs/root-canal/"},
                {"name": "Cost of Dental Crown", "href": "/blog/costs/dental-crown/"},
                {"name": "Cost of Wisdom Teeth Removal", "href": "/blog/costs/wisdom-teeth-removal/"},
                {"name": "Cost of Invisalign", "href": "/blog/costs/invisalign/"},
                {"name": "Cost of Teeth Whitening", "href": "/blog/costs/teeth-whitening/"},
                {"name": "Cost of Veneers", "href": "/blog/costs/veneers/"},
                {"name": "Cost of Dental Check-Up", "href": "/blog/costs/dental-check-up/"},
            ],
        },
        {
            "name": "Health Funds & Insurance",
            "intro": "Private health insurance reduces out-of-pocket expenses for dental care. We detail 5 major Australian health funds.",
            "hub": {"name": "Insurance Hub", "href": "/blog/insurance/"},
            "items": [
                {"name": "Best Dental Insurance", "href": "/blog/insurance/best-dental-insurance/"},
                {"name": "HCF Dental Cover", "href": "/blog/insurance/hcf-dental-cover/"},
                {"name": "Bupa Dental Cover", "href": "/blog/insurance/bupa-dental-cover/"},
                {"name": "Medibank Dental Cover", "href": "/blog/insurance/medibank-dental-cover/"},
                {"name": "NIB Dental Cover", "href": "/blog/insurance/nib-dental-cover/"},
            ],
        },
        {
            "name": "Government Dental Programs",
            "intro": "The government funds specific programs for eligible populations. We explain 4 public programs.",
            "hub": {"name": "Government Programs Hub", "href": "/blog/government-programs/"},
            "items": [
                {"name": "Public Dental Services State-by-State", "href": "/blog/government-programs/public-dental-services/"},
                {"name": "Medicare Dental Cover", "href": "/blog/government-programs/medicare-dental-cover/"},
                {"name": "Child Dental Benefits Schedule", "href": "/blog/government-programs/child-dental-benefits-schedule/"},
                {"name": "Veterans Dental", "href": "/blog/government-programs/veterans-dental/"},
            ],
        },
        {
            "name": "Payment Plans & Finance",
            "intro": "Patients use financing options to manage treatment expenses. We cover 4 payment structures.",
            "note": "Privatehealth.gov.au provides independent data on policy inclusions.",
            "items": [
                {"name": "Dental Payment Plans", "href": "/blog/finance/dental-payment-plans/"},
                {"name": "Dental Afterpay", "href": "/blog/finance/dental-afterpay/"},
                {"name": "Buy Now Pay Later Dental", "href": "/blog/finance/buy-now-pay-later-dental/"},
                {"name": "Low-Income Dental Assistance", "href": "/blog/finance/low-income-dental-assistance/"},
            ],
        },
    ],
}

# ---- Life stages ----
LIFE_STAGES = {
    "answer": (
        "Dental care differs by life stage because oral health risks and clinical requirements "
        "evolve from infancy through old age. We provide tailored oral care guides for different "
        "demographics. Every demographic faces specific risks and requires unique preventive "
        "strategies based on physiological changes. Explore the Patient Demographics Hub for "
        "comprehensive age-related data across 5 life stages:"
    ),
    "hub": {"name": "Patient Demographics Hub", "href": "/blog/patient-demographics/"},
    "items": [
        {"stage": "Infants", "title": "Infant Dental Care", "text": "Focuses on teething and early decay prevention.", "href": "/blog/patient-demographics/infant-dental-care/"},
        {"stage": "Children", "title": "Childrens Dental Care", "text": "Covers orthodontic assessments and fissure sealants.", "href": "/blog/patient-demographics/childrens-dental-care/"},
        {"stage": "Adults", "title": "Adult Dental Care", "text": "Addresses restorative work and periodontal maintenance.", "href": "/blog/patient-demographics/adult-dental-care/"},
        {"stage": "Pregnancy", "title": "Pregnancy Dental Care", "text": "Manages pregnancy gingivitis and dietary enamel erosion.", "href": "/blog/patient-demographics/pregnancy-dental-care/"},
        {"stage": "Seniors", "title": "Geriatric Dental Care", "text": "Handles tooth loss, dry mouth from medications, and implant longevity.", "href": "/blog/patient-demographics/geriatric-dental-care/"},
    ],
}

# ---- Who writes ----
WHO_WRITES = {
    "answer": (
        "A dedicated team of Australian journalists and AHPRA-registered dentists writes and "
        "reviews content on Fascinating Dentistry. We do not operate as a clinic, accept paid "
        "placements, or maintain affiliations with dental chains. Our editorial team researches the "
        "clinical data, and our medical reviewers verify the clinical accuracy of every published "
        "page. We enforce a strict citation policy requiring peer-reviewed journals or government "
        "health databases as primary sources. We update our guides regularly to reflect new ADA "
        "guidelines."
    ),
    "links": [
        {"name": "About", "href": "/about/"},
        {"name": "Editorial Policy", "href": "/editorial-policy/"},
        {"name": "Medical Reviewers", "href": "/medical-reviewers/"},
        {"name": "Methodology", "href": "/methodology/"},
        {"name": "Contact Us", "href": "/contact/"},
    ],
}

# ---- Why trust ----
WHY_TRUST = {
    "answer": (
        "You trust Fascinating Dentistry as a dental information source because we operate with "
        "total editorial independence and enforce rigorous medical review standards. We prioritise "
        "factual accuracy over commercial interests. We build trust using transparent operational "
        "standards across 6 core areas:"
    ),
    "points": [
        {"title": "100% Australian-focused", "text": "We cite Australian health data exclusively.", "link": {"name": "Water Fluoridation in Australia", "href": "/blog/public-health-dentistry/water-fluoridation-australia/"}},
        {"title": "Medically reviewed content", "text": "AHPRA-registered dentists verify every clinical statement before publication."},
        {"title": "Cited research sources", "text": "We cite AIHW, ADA, and AHPRA data directly."},
        {"title": "Independent ownership", "text": "We accept no funding from dental clinics, corporate dental chains, or product manufacturers."},
        {"title": "Regular page updates", "text": "We review clinical pages annually to reflect current evidence-based protocols."},
        {"title": "Transparent corrections policy", "text": "We maintain a public log of factual corrections and updates.", "link": {"name": "Corrections", "href": "/corrections/"}},
    ],
}

# ---- Statistics ----
STATS = {
    "answer": (
        "There are 6 key statistics on Australian dental health that define the current population "
        "oral health landscape. Experts use numbers, statistics, and evidence from government "
        "reports to evaluate access to care and disease prevalence. We cite data directly from the "
        "Australian Institute of Health and Welfare (AIHW) and the Australian Dental Health "
        "Foundation (ADHF) to provide factual context."
    ),
    "items": [
        {"label": "Adults with Gum Disease", "stat": "47.8%", "text": "According to AIHW data, 47.8% of Australian adults aged 15 years and over have some form of periodontal disease.", "href": "/blog/conditions/gum-disease/"},
        {"label": "Untreated Tooth Decay", "stat": "32%+", "text": "Over 32% of Australian adults have untreated tooth decay.", "href": "/blog/conditions/tooth-decay/"},
        {"label": "Dental Visitation Rates", "stat": "69.2%", "text": "69.2% of Australians aged 15 years and over visited a dental professional in the previous 12 months."},
        {"label": "Water Fluoridation Coverage", "stat": "89%", "text": "89% of Australians access fluoridated drinking water, a key factor in reducing cavity rates."},
        {"label": "Tooth Loss Prevalence", "stat": "17%", "text": "17% of Australians aged 65 years and over have no natural teeth, highlighting the need for dental implants.", "href": "/australia/dental-implants/"},
        {"label": "Health Fund Coverage", "stat": "60.2%", "text": "60.2% of Australians hold private health insurance with general treatment (extras) cover that includes dental services."},
    ],
}

# ---- Organisations ----
ORGS = {
    "answer": (
        "8 authoritative Australian organisations set dental standards, regulate practitioners, and "
        "govern public health policy. These bodies ensure patient safety, establish clinical "
        "guidelines, and provide public health interventions. We outline the major organisations "
        "governing the Australian dental sector below:"
    ),
    "items": [
        {"name": "Australian Dental Association (ADA)", "site": "https://ada.org.au", "blurb": "The peak national body for dentists, providing clinical guidelines, fee surveys, and continuing professional development.", "guide": {"name": "Read our ADA breakdown", "href": "/blog/organisations/ada-australian-dental-association/"}},
        {"name": "AHPRA (Australian Health Practitioner Regulation Agency)", "site": "https://ahpra.gov.au", "blurb": "The national regulator that registers dental practitioners and handles public complaints.", "guide": {"name": "Verify a practitioner via AHPRA Registration", "href": "/blog/organisations/ahpra-registration/"}},
        {"name": "Australian Dental Health Foundation (ADHF)", "site": "https://adhf.org.au", "blurb": "A charity coordinating pro-bono dental care for disadvantaged Australians."},
        {"name": "Australian Dental Council (ADC)", "site": "https://adc.org.au", "blurb": "The independent authority responsible for the accreditation of dental programs and assessing overseas-trained practitioners."},
        {"name": "Australian Institute of Health and Welfare (AIHW)", "site": "https://aihw.gov.au", "blurb": "A government agency providing national dental statistics and oral health data."},
        {"name": "Child Dental Benefits Schedule (CDBS)", "site": "https://www.servicesaustralia.gov.au/child-dental-benefits-schedule", "blurb": "The Commonwealth program funding basic dental services for eligible children.", "guide": {"name": "Read our CDBS Guide", "href": "/blog/government-programs/cdbs-child-dental-benefits-schedule/"}},
        {"name": "Healthdirect", "site": "https://healthdirect.gov.au", "blurb": "A government-funded service providing quality-approved health information and advice."},
        {"name": "Better Health Channel", "site": "https://betterhealth.vic.gov.au", "blurb": "A Victorian government initiative providing locally relevant oral health facts."},
    ],
}

# ---- FAQ ----
FAQ = {
    "intro": (
        "The 6 most common questions about Australian dental care address clinic operations, "
        "finding providers, treatment costs, registration, government schemes, and visit frequency. "
        "We provide definitive answers to these common patient inquiries below."
    ),
    "items": [
        {"q": "Is Fascinating Dentistry a dental clinic?", "a": "No. Fascinating Dentistry is an independent dental information resource. We do not provide dental treatment, accept patients, or rank clinics for payment. We publish original, AHPRA-reviewed articles about dental services, conditions, costs, and oral health in Australia."},
        {"q": "How do I find a dentist near me in Australia?", "a": "You find a dentist by using our location directory. Start at our Australia-wide directory to browse by state and city, or jump to a specific service like an Emergency Dentist. Every listicle includes verified practice details and a free quote option where available."},
        {"q": "How much does a dentist cost in Australia?", "a": "Costs vary by treatment and state, with check-ups ranging from $150 to $300. As a guide: filling $150-350, crown $1,500-2,500, root canal $1,200-2,500, implant $3,000-7,000. Public dental is free for eligible adults and children via state programs. Private health insurance extras cover reduces out-of-pocket costs by 50-80%."},
        {"q": "Is my dentist AHPRA registered?", "a": "Yes, all Australian dentists must maintain current AHPRA registration. You can verify any dentist's registration, check for restrictions, and confirm their specialty on the public register at ahpra.gov.au."},
        {"q": "What is the Child Dental Benefits Schedule (CDBS)?", "a": "The CDBS provides up to $1,095 over 2 calendar years for basic dental services for eligible children aged 0-17. Families must receive Family Tax Benefit Part A or other qualifying payments. Services include check-ups, cleaning, fillings, x-rays, and extractions."},
        {"q": "How often should Australians see a dentist?", "a": "Most healthy adults should see a dentist every 6-12 months for a check-up and clean. Children, people with gum disease, diabetics, smokers, and pregnant women require more frequent visits. Your dentist recommends a recall interval based on your individual oral health."},
    ],
}

FAQ_SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
        {"@type": "Question", "name": item["q"], "acceptedAnswer": {"@type": "Answer", "text": item["a"]}}
        for item in FAQ["items"]
    ],
})

# ---- Latest articles ----
LATEST_INTRO = (
    "The latest articles on Fascinating Dentistry cover endodontics, cosmetic dentistry, paediatric "
    "milestones, implant costs, and government schemes. We continually publish new clinical guides "
    "and cost analyses to keep patients informed."
)
