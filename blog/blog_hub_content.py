"""Blog hub content — transcribed verbatim from blog-hub.markdown."""
import json

META_TITLE = "Dental Blog Australia: Evidence-Based Dental Health Guides"
META_DESC = "Australia's evidence-based dental blog. 1,000+ medically reviewed articles across 28 clusters covering conditions, treatments, costs, and clinical knowledge."
H1 = "Dental Health Blog: Evidence-Based Guides for Australian Patients"

INTRO = [
    "Fascinating Dentistry publishes evidence-based, medically reviewed dental articles written for Australian patients. Trained health writers draft every clinical article, and AHPRA-registered dentists review each piece before publication to verify clinical accuracy against current Australian guidelines. Our medical review process governs how articles move from research to draft to clinical review to publication.",
    "This dental education resource covers 28 topic clusters with over 1,000 articles planned across dental specialties, oral health conditions, treatment procedures, cost breakdowns, clinical materials, imaging technology, and special interest topics. Every article is written for an Australian audience and references Australian clinical guidelines, health fund structures, and government dental programs.",
]

WHAT_HEADING = "What You'll Find in Our Dental Blog"
WHAT_PARAS = [
    "This blog organises 28 topic clusters covering dental specialties, oral health conditions, treatment procedures, patient costs, insurance, government programs, clinical materials, dental instruments, imaging, technology, and special interest topics. Over 1,000 articles are planned across all clusters.",
    "Content types include condition explainers that break down symptoms, causes, and risk factors; procedure guides that walk through each step of dental treatment from consultation to recovery; cost breakdowns that reference the Australian Dental Association fee survey and present price ranges in AUD; and clinical deep dives into dental materials, instruments, and imaging technology.",
    "New articles are published regularly, and existing articles are reviewed on a 12-month clinical cycle. Our editorial standards document how articles are researched, written, and reviewed before publication. Readers can browse clusters by clinical area, by treatment type, or by patient need. Each cluster hub lists its articles with summaries so readers can locate specific information quickly.",
]

CLUSTER_SECTIONS = [
    {
        "heading": "Dental Specialties",
        "intro": "Our Dental Specialties section covers 10 clinical disciplines recognised in Australian dentistry. Each cluster hub links to in-depth articles on conditions, procedures, and evidence-based treatment approaches within that specialty.",
        "clusters": [
            ("Endodontics guides", "/blog/endodontics/", "40 articles covering root canal therapy, pulpitis, apicoectomy, and the management of dental pulp disease."),
            ("Orthodontics guides", "/blog/orthodontics/", "80 articles on braces, Invisalign, clear aligners, retainers, and the correction of misaligned teeth and jaws."),
            ("Periodontics guides", "/blog/periodontics/", "50 articles on gingivitis, periodontitis, gum grafting, LANAP, and the surgical and non-surgical management of periodontal disease."),
            ("Prosthodontics guides", "/blog/prosthodontics/", "45 articles covering crowns, bridges, dentures, veneers, and full mouth rehabilitation for damaged or missing teeth."),
            ("Oral and Maxillofacial Surgery guides", "/blog/oral-surgery/", "45 articles on tooth extractions, wisdom teeth removal, orthognathic surgery, and facial trauma management."),
            ("Paediatric Dentistry guides", "/blog/pediatric-dentistry/", "40 articles on baby teeth, the Child Dental Benefits Schedule, fissure sealants, thumb sucking, and dental trauma in children."),
            ("Dental Implantology guides", "/blog/implantology/", "60 articles on implant systems, All-on-4, bone grafting, sinus lifts, and peri-implantitis management."),
            ("Cosmetic Dentistry guides", "/blog/cosmetic-dentistry/", "70 articles on teeth whitening, porcelain veneers, composite bonding, smile makeovers, and gum contouring."),
            ("Restorative Dentistry guides", "/blog/restorative-dentistry/", "50 articles on fillings, inlays, onlays, cavity classification, adhesive dentistry, and the repair of decayed or damaged teeth."),
            ("Dental Traumatology guides", "/blog/dental-traumatology/", "25 articles on avulsed teeth, luxation injuries, root fractures, splinting protocols, and sports-related dental trauma."),
        ],
    },
    {
        "heading": "Oral Health and Conditions",
        "intro": "Our Oral Health and Conditions section covers common dental problems, daily oral hygiene, oral pathology, public health initiatives, age-specific dental care, and evidence-based holistic approaches.",
        "clusters": [
            ("Oral health conditions guides", "/blog/conditions/", "110 articles on tooth decay, pulpitis, dental abscess, gingivitis, halitosis, bruxism, dry mouth, and tooth sensitivity."),
            ("Oral hygiene basics", "/blog/basics/", "80 articles on brushing technique, flossing methods, toothpaste selection, mouthwash use, dietary impacts on teeth, and electric versus manual toothbrush comparison."),
            ("Oral Pathology guides", "/blog/oral-pathology/", "35 articles on oral cancer, leukoplakia, oral lichen planus, biopsy procedures, and squamous cell carcinoma staging."),
            ("Public Health Dentistry guides", "/blog/public-health-dentistry/", "15 articles on water fluoridation in Australia, community dental programs, and Indigenous oral health initiatives."),
            ("Geriatric Dentistry guides", "/blog/geriatric-dentistry/", "20 articles on dry mouth in older adults, root decay, denture care, dementia-related dental challenges, and polypharmacy effects on oral health."),
            ("Holistic Dentistry guides", "/blog/holistic-dentistry/", "15 articles examining mercury-free dentistry, biocompatible materials, and the scientific evidence for practices such as oil pulling."),
        ],
    },
    {
        "heading": "Treatments and Procedures",
        "intro": "Our Treatments and Procedures cluster provides step-by-step guides for every major dental treatment performed in Australian practices. Each article breaks down the procedure into four phases: pre-operative preparation, intra-operative steps, post-operative care, and recovery timeline. Articles also cover cost estimates in AUD, alternative treatment options, risks and complications, and what patients should expect at each appointment. With 50 articles planned, this cluster covers procedures from routine fillings and scale-and-clean appointments to complex full-arch implant reconstruction and orthognathic surgery.",
        "clusters": [
            ("Treatments and Procedures guides", "/blog/treatments/", "50 articles with step-by-step clinical walkthroughs for every major dental procedure."),
        ],
    },
    {
        "heading": "Costs, Insurance and Government Support",
        "intro": "Understanding dental costs in Australia requires context. Our Costs, Insurance and Government Support section breaks down pricing, health fund cover, and public dental access across three clusters.",
        "clusters": [
            ("Dental cost guides", "/blog/costs/", "50 articles providing per-procedure cost estimates, state-by-state price comparisons, and references to the ADA annual fee survey."),
            ("Dental insurance guides", "/blog/insurance/", "20 articles on Extras cover, waiting periods, gap payments, HICAPS claiming, major versus general dental classification, and strategies for switching health funds."),
            ("Government dental programs", "/blog/government/", "20 articles on the Child Dental Benefits Schedule (CDBS), Medicare dental access, public dental waiting lists, and state-specific schemes."),
        ],
    },
    {
        "heading": "Clinical Knowledge and Technology",
        "intro": "Our Clinical Knowledge and Technology section provides detailed reference material on the materials, instruments, imaging, and technology used in modern Australian dentistry.",
        "clusters": [
            ("Dental Materials guides", "/blog/materials/", "50 articles on amalgam, composite resin, zirconia, dental ceramics, gutta-percha, glass ionomer cement, and the clinical properties that determine material selection."),
            ("Dental Instruments guides", "/blog/instruments/", "65 articles on the dental mirror, explorer probe, extraction forceps, elevators, endodontic files, dental burs, rubber dam, and surgical instruments."),
            ("Dental Radiology guides", "/blog/dental-radiology/", "25 articles on cone beam computed tomography (CBCT), panoramic imaging, bitewing radiographs, radiation dose comparison, and imaging safety during pregnancy."),
            ("Dental technology guides", "/blog/technology/", "35 articles on CAD/CAM dentistry, CEREC same-day crowns, 3D printing in dentistry, intraoral scanning, dental lasers, AI in diagnostics, and teledentistry."),
        ],
    },
    {
        "heading": "Special Topics",
        "intro": "Our Special Topics section covers niche areas where dental knowledge intersects with patient demographics, congenital conditions, forensic science, and history.",
        "clusters": [
            ("Patient Demographics guides", "/blog/demographics/", "30 articles on dental care during pregnancy, senior dental health, children's oral development, diabetic patients, immunocompromised individuals, and athletes."),
            ("Cleft Lip and Palate guides", "/blog/cleft/", "24 articles on causes, surgical timing, repair techniques, speech development, orthodontic management, and multidisciplinary team care."),
            ("Forensic Odontology guides", "/blog/forensic-odontology/", "10 articles on dental identification, bite mark analysis, mass disaster victim identification, and age estimation from dental evidence."),
            ("History of Dentistry", "/blog/history/", "30 articles tracing dental practice from ancient civilisations through Pierre Fauchard's foundational work to the development of the Australian dental profession."),
        ],
    },
]

REVIEW_HEADING = "How Our Blog Content Is Reviewed"
REVIEW_PARAS = [
    "Fascinating Dentistry follows a structured content pipeline to ensure clinical accuracy. Trained health writers with Australian healthcare communications experience draft every article. Each clinical article is then reviewed by an AHPRA-registered dentist who verifies factual accuracy, checks claims against current evidence, and confirms alignment with Australian clinical guidelines.",
    "Sources are cited from four Australian authoritative bodies: the Australian Dental Association (ADA), the Australian Health Practitioner Regulation Agency (AHPRA), the Australian Institute of Health and Welfare (AIHW), and the National Health and Medical Research Council (NHMRC). These organisations represent the authoritative sources for Australian dental standards, clinical guidelines, health practitioner regulation, and public health data.",
    "Articles are reviewed on a 12-month clinical review cycle. Cost-related articles undergo review every 6 months to reflect current pricing data from the ADA fee survey. Our editorial team includes named dental reviewers whose credentials appear on each article.",
]

FAQS = [
    ("Is the dental advice on this blog written by real dentists?", "Every clinical article is written by a trained health writer and reviewed by an AHPRA-registered dentist before publication. Sources are cited from the ADA, AHPRA, AIHW, and NHMRC."),
    ("How often is the blog updated?", "New articles are published regularly. Existing articles are reviewed on a 12-month clinical review cycle, with cost-related articles reviewed every 6 months to reflect current pricing."),
    ("Are the dental cost estimates accurate for Australia?", "All cost figures are based on the Australian Dental Association fee survey and public health data from AIHW. Price ranges are presented rather than fixed quotes, because actual costs vary by practice, location, and clinical complexity."),
    ("Can I find a dentist through this blog?", "Many blog articles link to Top 10 dental practice listings for specific services and locations. Visit our Australia directory to browse dental practices by city and service type."),
    ("Do dentists pay to be featured in blog articles?", "No. Editorial content is independent of advertising revenue. Practices can purchase placements in Top 10 commercial listings (positions 1 to 3 with do-follow links), but this never influences blog articles."),
]

FAQ_SCHEMA = json.dumps({
    "@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS],
})
