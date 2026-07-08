# Fascinating Dentistry -- Phase 1 Strategic Plan

_Source: fascinating-dentistry-phase1-strategic-plan.xlsx (all tabs)_

## Tab: Executive Summary

| Item | Value |
| Client | Fascinating Dentistry |
| Domain | https://fascinatingdentistry.com |
| Platform | Headless CMS (Strapi/Sanity) + Next.js — needed for 70k+ scale |
| Site Model | Dental-only directory + informational authority resource |
| Revenue Model | Top 3 paid do-follow + positions 4-10 no-follow |
| Phase 1 Locations | Australia (national), Sydney, Brisbane |
| Phase 1 Commercial Pages | 127 (42 services × 3 locations + 1 hub) |
| Phase 1 Blog Posts | 1,000+ across 28 clusters |
| Phase 1 Page Total | 1,127+ |
| Clusters | 28 (16 specialty + 12 supplementary) |
| Entities Mapped | 500+ |
| Top Commercial KW (Est.) | "top 10 dentists {city}" |
| Top Informational KW (Est.) | "how much do dental implants cost australia" |
| Biggest Content Gap | No AU dental-only city × service × Top 10 directory exists |
| EEAT Score (current) | 0/10 (greenfield) |
| EEAT Score (target Phase 1) | 8/10 |
| Schema Coverage | 100% pages (MedicalWebPage + ItemList + FAQPage + BreadcrumbList + Article/Organization/Person) |
| Internal Link Density | Every blog post: ≥3 inbound + ≥3 outbound contextual links |
| 3-Year Scale Target | 70,000+ indexed pages (Phase 5 international) |
| Phase Priority Distribution | Phase A: 60% of pages / Phase B: 30% / Phase C: 10% |

## Tab: Site Architecture

| Level | URL Pattern | Page Type | Phase 1 Count | Notes |
| L0 | https://fascinatingdentistry.com/ | Homepage | 1 | Aggregates all hubs; portal to services + clusters |
| L0 Trust | /about/ | About | 1 | Mission, model, how directory works |
| L0 Trust | /editorial-team/ | Team | 1 | Editorial + medical review board bios |
| L0 Trust | /medical-review/ | Process | 1 | How medical review works |
| L0 Trust | /methodology/ | Process | 1 | How Top 10 rankings are determined |
| L0 Trust | /disclosures/ | Disclosure | 1 | Paid placements, link attributes, no-follow policy |
| L0 Trust | /privacy/ /terms/ /contact/ | Legal/Contact | 3 | Standard trust pages |
| L1 National Hub | /australia/ | Country hub | 1 | Lists all 42 services + Top 10 national |
| L2 National Service | /australia/{service}/ | Service directory | 42 | Top 10 AU-wide listicles |
| L1 City Hub | /australia/sydney/ | City hub | 1 | Lists all 42 Sydney services |
| L1 City Hub | /australia/brisbane/ | City hub | 1 | Lists all 42 Brisbane services |
| L2 City Service | /australia/sydney/{service}/ | City × service | 42 | Top 10 Sydney listicle |
| L2 City Service | /australia/brisbane/{service}/ | City × service | 42 | Top 10 Brisbane listicle |
| L1 Cluster Hub | /blog/{cluster}/ | Cluster index | 28 | Pillar for each of 28 clusters |
| L2 Blog | /blog/{cluster}/{slug}/ | Article | 1,000+ | Spoke content per cluster |
| L1 Special Hubs (Phase 2+) | /dentists/ /costs/ /insurance/ /government/ /schools/ /organisations/ | Special hub | 6 (P2+) | Cross-cutting vertical hubs |
| L2 Person Bio | /dentists/{name}/ | Person | 15+ P1 | Editorial team + medical reviewers |
| Phase 1 Total | — | — | 1,127+ | Excludes suburb/international expansion |

## Tab: Cluster Strategy

| Cluster | URL Hub | Target Posts | Primary Commercial KW (Est.) | Primary Informational KW (Est.) | Top Sub-Topics (priority posts first) | Internal Links to Service Pages | Cross-Cluster Links | EEAT Signals | Phase |
| Endodontics | /blog/endodontics/ | 40 | "endodontist sydney" | "what is root canal therapy" | Root canal step-by-step / Pulpitis types / Apicoectomy / Pulp capping / Endodontic files / Apexification / Regenerative endo / Retreatment failure | Emergency dentist, Root canal, Endodontist, Toothache relief | Conditions, Treatments, Materials | Reviewed by registered endodontist; cite AAE, ADA PB | A |
| Oral Pathology | /blog/oral-pathology/ | 35 | "oral cancer screening sydney" | "oral cancer symptoms australia" | Oral cancer signs / Leukoplakia / Lichen planus / Biopsy process / SCC staging / Melanoma / Cyst types | Oral cancer screening, Emergency dentist | Conditions, Oral Surgery, Demographics | Reviewed by oral pathologist; ADA oral cancer refs | A |
| Dental Radiology | /blog/dental-radiology/ | 25 | "dental x-ray sydney" | "is dental x-ray safe" | CBCT explained / Panoramic / Ceph / Bitewing / Radiation dose / Digital vs film / Pregnancy safety | Check-up, Implants, Wisdom teeth removal | Technology, Instruments, Conditions | Cite ALARA, ARPANSA, ADA radiation guidelines | B |
| Oral & Maxillofacial Surgery | /blog/oral-surgery/ | 45 | "oral surgeon sydney" | "wisdom teeth removal recovery" | Extractions / Impaction types / Orthognathic / Le Fort / BSSO / Cleft repair / Facial trauma / Pathology excision | Wisdom teeth removal, Tooth extraction, Bone grafting, Sinus lift | Conditions, Implantology, Traumatology, Cleft | Surgeon review; RACDS, IAOMS references | A |
| Orthodontics | /blog/orthodontics/ | 80 | "orthodontist sydney" | "invisalign vs braces" | Malocclusion classes / Braces types / Aligners comparison / Phase I-II / Retainers / Functional appliances / Adult ortho / Lingual / Self-ligating | Invisalign, Clear aligners, Braces, Orthodontist | Conditions, Treatments, Demographics | Reviewed by orthodontist; AAO, ASO references | A |
| Pediatric Dentistry | /blog/pediatric-dentistry/ | 40 | "childrens dentist sydney" | "when should child first see dentist" | Baby teeth / CDBS use / Sealants / Thumb sucking / Dental trauma in kids / Special needs / Preventive program | Pediatric dentist, Children's dentist, Dental sealants | Basics, Demographics, Conditions, Government | Reviewed by pediatric dentist; ADA pediatric, AAPD refs | A |
| Periodontics | /blog/periodontics/ | 50 | "periodontist sydney" | "gum disease treatment options" | Gingivitis vs periodontitis / SRP / LANAP / Gum graft types / Bone graft / Maintenance schedule / Peri-implantitis | Gum disease treatment, Gum graft surgery, LANAP, Periodontist | Conditions, Treatments, Implantology | Reviewed by periodontist; AAP, ASP references | A |
| Prosthodontics | /blog/prosthodontics/ | 45 | "prosthodontist sydney" | "dentures vs implants" | Crown types / Bridge designs / Denture options / Veneers / Full mouth rehab / Occlusion principles / Tooth wear management | Dental crowns, Dental bridges, Dentures, Porcelain veneers | Materials, Cosmetic, Restorative, Geriatric | Reviewed by prosthodontist; APS references | A |
| Public Health Dentistry | /blog/public-health-dentistry/ | 15 | "bulk billing dentist sydney" | "free dental care australia" | CDBS / Medicare / Public clinics / Community programs / Water fluoridation / Indigenous oral health / Rural access | Check-up, Children's dentist, Dental sealants | Government, Costs, Demographics | Cite AIHW, DoHA, NHMRC fluoridation statement | B |
| Cosmetic Dentistry | /blog/cosmetic-dentistry/ | 70 | "cosmetic dentist sydney" | "how long do veneers last" | Whitening options / Veneer types / Bonding / Smile makeover / Lumineers / Tooth jewelry / Gum contouring / Prepless veneers | Cosmetic dentistry, Porcelain veneers, Teeth whitening, Smile makeover, Composite bonding | Materials, Basics, Costs | AACD, ASDA references; cosmetic dentist review | A |
| Dental Implantology | /blog/implantology/ | 60 | "dental implants sydney" | "how much do dental implants cost" | Implant systems / All-on-4 / Bone graft / Sinus lift / Immediate load / Zygomatic / Pterygoid / Maintenance / Peri-implantitis | Dental implants, All-on-4 implants, Mini implants, Same-day implants, Bone grafting, Sinus lift, Implant-supported dentures | Periodontics, Oral Surgery, Costs, Materials | ITI, AO, AGD references; implantologist review | A |
| Geriatric Dentistry | /blog/geriatric-dentistry/ | 20 | "dentist for seniors sydney" | "dental care for elderly" | Dry mouth / Root decay / Denture care / Dementia / Parkinson / Polypharmacy / Care facilities | Dentures, Check-up, Implant-supported dentures | Demographics, Prosthodontics, Conditions | Cite geriatric dental journals; aged care review | B |
| Restorative Dentistry | /blog/restorative-dentistry/ | 50 | "fillings sydney" | "composite vs amalgam fillings" | Filling materials / Inlays onlays / Crown prep / Post placement / Pulp cap / Adhesion systems / Cavity classification | Dental fillings, Dental crowns, Dental bridges | Materials, Endodontics, Prosthodontics | Cite ADA restorative guidelines; FDI refs | A |
| Forensic Odontology | /blog/forensic-odontology/ | 10 | "forensic dentist" | "what is forensic dentistry" | Identification / Bite marks / Mass disasters / DVI / Age estimation / Australian cases | Educational only — authority building | History, Conditions | Cite IAFO, ASFO; Australian DVI protocols | C |
| Dental Traumatology | /blog/dental-traumatology/ | 25 | "knocked out tooth sydney" | "what to do if tooth knocked out" | Avulsion / Intrusion / Luxation / Root fracture / Splinting / Reimplantation / Sports trauma / First aid | Emergency dentist, Broken tooth repair, Sports mouthguards | Conditions, Pediatric, Basics | IADT guidelines; emergency dentist review | A |
| Holistic Dentistry | /blog/holistic-dentistry/ | 15 | "holistic dentist sydney" | "what is holistic dentistry" | Mercury-free / Biocompatible / Fluoride debate / Oil pulling evidence / Alternative therapies / Biological dentistry | Holistic dentist | Materials, Basics, Conditions | Balanced view; cite only peer-reviewed; disclose controversy | B |
| Basics (Oral Hygiene) | /blog/basics/ | 80 | "teeth cleaning sydney" | "how to brush teeth properly" | Brushing technique / Flossing methods / Toothpaste choice / Mouthwash / Diet / Tongue scraping / Electric vs manual / Sonicare vs Oral-B / Kids routine | Dental check-up, Teeth cleaning | Conditions, Demographics, Costs | Cite ADA oral hygiene recommendations; Cochrane reviews | A |
| Conditions | /blog/conditions/ | 110 | "toothache sydney" | "what causes toothache" | Decay / Pulpitis / Abscess / Gingivitis / Periodontitis / Halitosis / Bruxism / Malocclusion / Dry mouth / Erosion / Fluorosis | Emergency dentist, Gum disease, Root canal, Toothache relief | All specialty clusters | Medically reviewed per article; ADA condition pages | A |
| Treatments & Procedures | /blog/treatments/ | 50 | "dental procedure sydney" | "root canal procedure steps" | Step-by-step guides for every treatment; pre-op, intra-op, post-op, recovery, cost, alternatives | All 42 service pages | Materials, Conditions, Costs | Procedural review; cite ADA, RACDS, TGA | A |
| Dental Materials | /blog/materials/ | 50 | "dental crown material" | "porcelain vs zirconia crown" | Amalgam / Composite types / Glass ionomer / Ceramics / Zirconia / Titanium grades / Gutta-percha / Cements / Impression materials | Dental crowns, Dental fillings, Dental implants | Restorative, Prosthodontics, Implantology | Cite ISO 13485, TGA, ADA standards | B |
| Dental Instruments | /blog/instruments/ | 65 | "dental tools" | "names of dental instruments" | Mirror / Explorer / Probe / Excavator / Forceps / Elevator / Files / Burs / Dam / Laser / Scaler / Impression trays | Educational only — supports EEAT | Technology, History, Conditions | Reviewer-checked for accuracy; cite ADA, instrument texts | B |
| Patient Demographics | /blog/demographics/ | 30 | "dentist for pregnancy sydney" | "dental care during pregnancy" | Pregnancy / Seniors / Children / Diabetics / Special needs / Athletes / Musicians / Indigenous / Refugees / Immunocompromised | Pediatric dentist, Holistic dentist, Check-up | Public Health, Conditions | Cultural safety reviewers; NACCHO, AIDA references | B |
| Costs & Pricing | /blog/costs/ | 50 | "dental cost sydney" | "how much is a filling australia" | Cost per procedure / State-by-state / CDBS value / Private health value / Bulk billing reality / Payment plans / Dental tourism | Every service page | Insurance, Government | Cite ADA annual fee survey; transparent methodology | A |
| Insurance | /blog/insurance/ | 20 | "dental insurance australia" | "best dental insurance australia" | Extras cover / Waiting periods / Gap payments / HICAPS / Major vs general / Switching funds / Lifetime ortho | Every service page | Costs, Government | Disclose no insurance affiliate relationships | A |
| Government Programs | /blog/government/ | 20 | "free dental sydney" | "medicare dental coverage" | CDBS eligibility / Medicare / Public dental queues / State schemes (NSW/QLD) / Veteran / Disability / Indigenous programs | Children's dentist, Check-up, Dental sealants | Demographics, Costs, Public Health | Cite Services Australia, state health dept guidelines | A |
| Technology | /blog/technology/ | 35 | "digital dentist sydney" | "what is cerec dentistry" | CAD/CAM / CEREC / 3D printing / Intraoral scan / CBCT / Lasers / AI / Teledentistry / VR/AR | Dental implants, Dental crowns, Check-up | Radiology, Materials, Instruments | Cite peer-reviewed; reviewer-checked claims | A |
| Cleft Lip & Palate | /blog/cleft/ | 24 | "cleft lip surgery australia" | "what is cleft palate" | Causes / Types / Surgery timing / Repair / Bone graft / Speech / Ortho / Feeding / Team care / Adults / Australian services | Orthodontist, Oral surgery, Pediatric dentist | Conditions, Demographics, Public Health | Cite Smile Train, Operation Smile, ACPA; cleft team review | B |
| History of Dentistry | /blog/history/ | 30 | (informational only) | "history of dentistry timeline" | Ancient / Fauchard / Wells / Black / Hobbs / Tooth worm myth / Museums / Dentistry in films / Australian dental history | Educational only — authority + brand depth | Forensic Odontology, Instruments | Historian review; cite primary sources, museum archives | C |

## Tab: ServiceLocation Page Plan

| URL | Service | Location | Primary KW (Est.) | Word Count | Top 10 Listicle Structure | Internal Links FROM Blog Posts | Schema | Phase |
| /australia/ | All | Australia | "top 10 dentists australia" | 2,500 | H1: Top 10 Dentists in Australia / Intro / Ranking methodology / Top 10 list (3 featured + 7 standard) / How we rank / FAQ / CTA | All cluster hubs | Organization + ItemList + BreadcrumbList + FAQPage | A |
| /australia/emergency-dentist/ | Emergency dentist | Australia | "emergency dentist australia" | 2,000 | H1: Top 10 Emergency Dentists in Australia / When to seek emergency care / Top 10 / What costs to expect / FAQ | Endodontics, Traumatology, Conditions | MedicalWebPage + ItemList + FAQPage + Breadcrumb | A |
| /australia/after-hours-dentist/ | After hours dentist | Australia | "after hours dentist australia" | 1,800 | H1: Top 10 After-Hours Dentists / What counts as after-hours / Top 10 / Costs / FAQ | Endodontics, Conditions, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/weekend-dentist/ | Weekend dentist | Australia | "weekend dentist australia" | 1,800 | H1: Top 10 Weekend Dentists / Saturday/Sunday openings / Top 10 / Costs / FAQ | Conditions, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/wisdom-teeth-removal/ | Wisdom teeth | Australia | "wisdom teeth removal australia" | 2,200 | H1: Top 10 Wisdom Teeth Dentists / When removal needed / Impaction types / Top 10 / Costs ($250-$600) / Recovery / FAQ | Oral Surgery, Conditions, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/tooth-extraction/ | Extractions | Australia | "tooth extraction australia" | 1,800 | H1: Top 10 Tooth Extraction Dentists / Reasons / Types / Top 10 / Costs / Aftercare / FAQ | Oral Surgery, Conditions | MedicalWebPage + ItemList + FAQPage | A |
| /australia/root-canal-treatment/ | Root canal | Australia | "root canal treatment australia" | 2,000 | H1: Top 10 Root Canal Specialists / When needed / Procedure / Top 10 / Costs ($900-$2,000) / FAQ | Endodontics, Treatments | MedicalWebPage + ItemList + FAQPage | A |
| /australia/endodontist/ | Endodontist | Australia | "endodontist australia" | 1,800 | H1: Top 10 Endodontists in Australia / What endodontists do / Top 10 / Costs / FAQ | Endodontics, Treatments | MedicalWebPage + ItemList + FAQPage | A |
| /australia/dental-fillings/ | Fillings | Australia | "dental fillings australia" | 1,800 | H1: Top 10 Dentists for Fillings / Amalgam vs composite / Top 10 / Costs ($150-$300) / FAQ | Restorative, Materials, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/dental-crowns/ | Crowns | Australia | "dental crowns australia" | 2,000 | H1: Top 10 Dentists for Crowns / Crown types / Top 10 / Costs ($1,500-$2,500) / FAQ | Prosthodontics, Materials, Restorative | MedicalWebPage + ItemList + FAQPage | A |
| /australia/dental-bridges/ | Bridges | Australia | "dental bridges australia" | 1,800 | H1: Top 10 Dentists for Bridges / Bridge types / Top 10 / Costs / FAQ | Prosthodontics, Restorative | MedicalWebPage + ItemList + FAQPage | A |
| /australia/dentures/ | Dentures | Australia | "dentures australia" | 2,000 | H1: Top 10 Denture Clinics / Denture types / Top 10 / Costs / Adjustments / FAQ | Prosthodontics, Geriatric, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/implant-supported-dentures/ | Implant dentures | Australia | "implant supported dentures australia" | 2,000 | H1: Top 10 Implant Denture Clinics / Overdenture options / Top 10 / Costs / FAQ | Implantology, Prosthodontics, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/all-on-4-dental-implants/ | All-on-4 | Australia | "all on 4 dental implants australia" | 2,200 | H1: Top 10 All-on-4 Clinics / Procedure / Top 10 / Costs ($20k-$30k) / FAQ | Implantology, Costs, Treatments | MedicalWebPage + ItemList + FAQPage | A |
| /australia/dental-implants/ | Implants | Australia | "dental implants australia" | 2,500 | H1: Top 10 Dental Implant Clinics / Implant types / Top 10 / Costs ($3,000-$6,000) / Process / FAQ | Implantology, Treatments, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/mini-dental-implants/ | Mini implants | Australia | "mini dental implants australia" | 1,800 | H1: Top 10 Mini Implant Clinics / MDI use cases / Top 10 / Costs / FAQ | Implantology, Prosthodontics | MedicalWebPage + ItemList + FAQPage | A |
| /australia/same-day-dental-implants/ | Same-day implants | Australia | "same day dental implants australia" | 1,800 | H1: Top 10 Same-Day Implant Clinics / Teeth-in-a-Day / Top 10 / Costs / FAQ | Implantology, Treatments | MedicalWebPage + ItemList + FAQPage | A |
| /australia/bone-grafting/ | Bone graft | Australia | "dental bone grafting australia" | 1,800 | H1: Top 10 Bone Grafting Clinics / When needed / Top 10 / Costs / FAQ | Implantology, Oral Surgery, Periodontics | MedicalWebPage + ItemList + FAQPage | A |
| /australia/sinus-lift/ | Sinus lift | Australia | "sinus lift australia" | 1,800 | H1: Top 10 Sinus Lift Clinics / Procedure / Top 10 / Costs / FAQ | Implantology, Oral Surgery | MedicalWebPage + ItemList + FAQPage | A |
| /australia/toothache-relief/ | Toothache | Australia | "toothache relief australia" | 1,800 | H1: Top 10 Toothache Relief Dentists / Causes / Top 10 / When emergency / FAQ | Endodontics, Conditions, Emergency | MedicalWebPage + ItemList + FAQPage | A |
| /australia/broken-tooth-repair/ | Broken tooth | Australia | "broken tooth repair australia" | 1,800 | H1: Top 10 Broken Tooth Repair / Causes / Top 10 / Costs / FAQ | Traumatology, Restorative, Conditions | MedicalWebPage + ItemList + FAQPage | A |
| /australia/cosmetic-dentistry/ | Cosmetic | Australia | "cosmetic dentistry australia" | 2,200 | H1: Top 10 Cosmetic Dentists / Treatments list / Top 10 / Costs / FAQ | Cosmetic, Materials, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/teeth-whitening/ | Whitening | Australia | "teeth whitening australia" | 2,000 | H1: Top 10 Teeth Whitening Clinics / Methods / Top 10 / Costs ($400-$1,200) / Safety / FAQ | Cosmetic, Basics, Conditions | MedicalWebPage + ItemList + FAQPage | A |
| /australia/porcelain-veneers/ | Veneers | Australia | "porcelain veneers australia" | 2,200 | H1: Top 10 Porcelain Veneer Clinics / Veneer types / Top 10 / Costs ($1,200-$2,500/tooth) / FAQ | Cosmetic, Prosthodontics, Materials | MedicalWebPage + ItemList + FAQPage | A |
| /australia/composite-bonding/ | Bonding | Australia | "composite bonding australia" | 1,800 | H1: Top 10 Composite Bonding Clinics / Uses / Top 10 / Costs / FAQ | Cosmetic, Restorative, Materials | MedicalWebPage + ItemList + FAQPage | A |
| /australia/smile-makeover/ | Smile makeover | Australia | "smile makeover australia" | 2,000 | H1: Top 10 Smile Makeover Clinics / Treatment planning / Top 10 / Costs / FAQ | Cosmetic, Prosthodontics | MedicalWebPage + ItemList + FAQPage | A |
| /australia/invisalign/ | Invisalign | Australia | "invisalign australia" | 2,200 | H1: Top 10 Invisalign Providers / How it works / Top 10 / Costs ($6,000-$9,000) / FAQ | Orthodontics, Treatments, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/clear-aligners/ | Clear aligners | Australia | "clear aligners australia" | 2,000 | H1: Top 10 Clear Aligner Providers / Brands compared / Top 10 / Costs / FAQ | Orthodontics, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/braces/ | Braces | Australia | "braces australia" | 2,000 | H1: Top 10 Braces Clinics / Types (metal/ceramic/lingual) / Top 10 / Costs / FAQ | Orthodontics, Treatments | MedicalWebPage + ItemList + FAQPage | A |
| /australia/orthodontist/ | Orthodontist | Australia | "orthodontist australia" | 1,800 | H1: Top 10 Orthodontists in Australia / What they treat / Top 10 / FAQ | Orthodontics, Conditions | MedicalWebPage + ItemList + FAQPage | A |
| /australia/periodontist/ | Periodontist | Australia | "periodontist australia" | 1,800 | H1: Top 10 Periodontists / Conditions treated / Top 10 / FAQ | Periodontics, Conditions | MedicalWebPage + ItemList + FAQPage | A |
| /australia/gum-disease-treatment/ | Gum disease | Australia | "gum disease treatment australia" | 2,000 | H1: Top 10 Gum Disease Clinics / Stages / Top 10 / Costs / FAQ | Periodontics, Conditions | MedicalWebPage + ItemList + FAQPage | A |
| /australia/gum-graft-surgery/ | Gum graft | Australia | "gum graft surgery australia" | 1,800 | H1: Top 10 Gum Graft Clinics / Types / Top 10 / Costs / FAQ | Periodontics, Treatments | MedicalWebPage + ItemList + FAQPage | A |
| /australia/lanap/ | LANAP | Australia | "lanap laser gum surgery australia" | 1,800 | H1: Top 10 LANAP Clinics / Procedure / Top 10 / Costs / FAQ | Periodontics, Technology | MedicalWebPage + ItemList + FAQPage | B |
| /australia/pediatric-dentist/ | Pediatric | Australia | "pediatric dentist australia" | 2,000 | H1: Top 10 Pediatric Dentists / When to start / Top 10 / CDBS / FAQ | Pediatric, Demographics, Government | MedicalWebPage + ItemList + FAQPage | A |
| /australia/childrens-dentist/ | Children | Australia | "childrens dentist australia" | 2,000 | H1: Top 10 Children's Dentists / First visit / Top 10 / CDBS / FAQ | Pediatric, Government, Demographics | MedicalWebPage + ItemList + FAQPage | A |
| /australia/dental-check-up/ | Check-up | Australia | "dental check up australia" | 1,800 | H1: Top 10 Dentists for Check-Ups / What's included / Top 10 / Costs / Bulk billing / FAQ | Basics, Public Health, Costs | MedicalWebPage + ItemList + FAQPage | A |
| /australia/teeth-cleaning/ | Cleaning | Australia | "teeth cleaning australia" | 1,800 | H1: Top 10 Teeth Cleaning Clinics / Scale and clean / Top 10 / Costs / FAQ | Basics, Periodontics | MedicalWebPage + ItemList + FAQPage | A |
| /australia/sports-mouthguards/ | Mouthguards | Australia | "sports mouthguards australia" | 1,500 | H1: Top 10 Sports Mouthguard Providers / Why needed / Top 10 / Costs / FAQ | Traumatology, Pediatric | MedicalWebPage + ItemList + FAQPage | B |
| /australia/night-guards/ | Night guards | Australia | "night guards australia" | 1,500 | H1: Top 10 Night Guard Providers / Bruxism / Top 10 / Costs / FAQ | Conditions, Basics | MedicalWebPage + ItemList + FAQPage | B |
| /australia/tmj-treatment/ | TMJ | Australia | "tmj treatment australia" | 1,800 | H1: Top 10 TMJ Treatment Clinics / TMD overview / Top 10 / Costs / FAQ | Oral Surgery, Conditions | MedicalWebPage + ItemList + FAQPage | B |
| /australia/oral-cancer-screening/ | Oral cancer | Australia | "oral cancer screening australia" | 1,800 | H1: Top 10 Oral Cancer Screening Clinics / Risk factors / Top 10 / Costs / FAQ | Oral Pathology, Conditions | MedicalWebPage + ItemList + FAQPage | B |
| /australia/holistic-dentist/ | Holistic | Australia | "holistic dentist australia" | 1,800 | H1: Top 10 Holistic Dentists / What is holistic / Top 10 / FAQ | Holistic, Materials | MedicalWebPage + ItemList + FAQPage | B |

## Tab: Top 10 Listicle Template

| Section | Specification |
| URL | /australia/{city}/{service}/ or /australia/{service}/ |
| H1 | Top 10 {Service Providers} in {Location} (Year) — Reviewed & Ranked |
| Word Count | 1,500-2,500 words |
| Meta Title | Top 10 {Service Providers} in {Location} (Year) — Ranked |
| Meta Description | Looking for {service} in {location}? We ranked the top 10 {city} dentists for {service} based on qualifications, reviews, and patient outcomes. |
| Intro Structure (200 words) | Para 1: Problem statement (what {service} is, why patients need it) / Para 2: How we ranked (link to /methodology/) / Para 3: How to use this guide |
| Listicle Entry Template (positions 1-3, featured/do-follow) | Practice name + AHPRA-reg verified badge / One-sentence hook / 4-paragraph enhanced description (qualifications, special interests, technology, patient experience) / Pricing tier indicator / Address + phone + website / Google rating + review count / Insurance/health funds accepted / "Visit {Practice}" CTA button |
| Listicle Entry Template (positions 4-10, standard/no-follow) | Practice name / 2-paragraph description / Address + phone + website (all no-follow) / Google rating + review count |
| Mid-listicle H2: How much does {service} cost in {location}? | 200-word section citing ADA fee survey range + factors |
| Mid-listicle H2: How to choose a {service} provider | 5-question checklist for patients |
| Closing H2: Methodology | "We ranked these dentists based on: AHPRA registration, qualifications, Google reviews (min 50), years of experience, technology, and patient feedback. Read full methodology." |
| FAQ H2: Frequently Asked Questions | 6-8 FAQs with FAQPage schema |
| Final CTA | "Are you a {service} provider in {location}? Apply to be featured" |
| Sidebar | Related services (3) + top 3 blog posts in related cluster |
| Disclosure | "Practices in positions 1-3 are paid placements (do-follow links). Practices in positions 4-10 are listed editorially with no-follow links. Read our disclosures policy." |

## Tab: Blog Post Brief Template

| Element | Specification |
| URL | /blog/{cluster}/{slug}/ |
| Word Count | 1,500-3,500 words (cornerstone 3,500+) |
| Title (H1) | Question-led or benefit-led, NEVER "Best..." |
| Meta Title | Same as H1, optimised for target keyword |
| Meta Description | 150-160 chars with target keyword + CTA |
| Slug | kebab-case, contains target keyword, ≤6 words |
| Author | Real author with Person schema |
| Medical Reviewer | Named dentist with Person schema + AHPRA listed |
| Last Reviewed Date | Visible on page + schema dateReviewed |
| H2 Structure | 5-9 H2 sections; user-intent-mapped |
| Internal Links | ≥3 to service pages + ≥3 to related blog posts + 1 to cluster hub |
| External Links | 2-4 to ADA, AHPRA, peer-reviewed journals (authority outlinks) |
| Citations | Numbered references list with links |
| FAQ Section | 4-6 questions with FAQPage schema |
| CTA | 1-2 in-content CTAs to relevant /australia/{city}/{service}/ page |
| Schema | Article + MedicalWebPage + BreadcrumbList + FAQPage + Person (author + reviewer) |
| Images | Featured image + 2-4 in-content; alt text with keyword |
| Disclosure | "This article is medically reviewed. We may earn fees from clinics listed in our directory — see disclosures." |

## Tab: Internal Linking Strategy

| Layer | Rule | Implementation |
| L0 Homepage | Must link to ALL L1 hubs | Top nav: Australia hub, Sydney hub, Brisbane hub, Blog hub / Footer: all 28 cluster hubs + 8 trust pages |
| L0 Trust pages | Must link to homepage + 1-2 related trust pages | /methodology/ ↔ /disclosures/ ↔ /editorial-team/ ↔ /medical-review/ |
| L1 Hubs (Australia, Sydney, Brisbane) | Must link to ALL 42 child service pages + 1 cross-city link + 5 blog cluster hubs | Service card grid layout + "Related guides" section |
| L1 Cluster hubs | Must link to ALL blog posts in cluster + UP to homepage + ACROSS to 2 related cluster hubs + OUT to 3-5 most relevant service pages | Pillar page architecture: intro + spoke post grid + service page CTAs |
| L2 Service pages | Must link UP to parent hub + ACROSS to 2-3 related services + DOWN to 1-2 most relevant blog posts + OUT to 1 related service in other city | e.g. /sydney/implants/ links to /sydney/ (UP), /sydney/bone-grafting/ + /sydney/all-on-4/ (ACROSS), /blog/implantology/dental-implants-guide/ (DOWN), /brisbane/dental-implants/ (OUT) |
| L2 Blog posts | Must link UP to cluster hub + ACROSS to 2-3 sibling posts in cluster + OUT to 1-2 commercial service pages (conversion path) | In-content contextual links (not just related posts widget) |

## Tab: EEAT Roadmap

| EEAT Signal | Current State | Target State | Pages to Update | Priority | Phase | Notes |
| Editorial team bios | None | 5-8 named writers with bios, photos, credentials | /editorial-team/ + Person schema on every article | Critical | A | Real names, photos, dental writing experience |
| Medical review board | None | 3-5 licensed AU dentists ( BDS/BDSc, AHPRA-listed) reviewing every medical article | /medical-review/ + reviewer Person schema on every article | Critical | A | Paid reviewers; AHPRA registration verified quarterly |
| AHPRA registration of reviewers | None | Reviewer AHPRA numbers listed + linked to AHPRA public register | /editorial-team/ + each reviewer bio | Critical | A | Quarterly verification check |
| Methodology page | None | Detailed ranking methodology with criteria, weights, audit cadence | /methodology/ | Critical | A | Required by Google for review/directory sites |
| Disclosures page | None | Full disclosure of paid placements, do-follow vs no-follow, advertising relationships | /disclosures/ | Critical | A | Per ACCC + Google disclosure requirements |
| Source citations | None | Every medical claim cites ADA, peer-reviewed journal, or government source (numbered references) | Every medical blog post | Critical | A | Minimum 3 citations per article |
| Review/update dates | None | Last reviewed date visible + dateReviewed in schema; re-reviewed every 12 months | Every medical blog post | Critical | A | Editorial calendar for re-review |
| Author attribution on blog posts | None | Named author with byline + Person schema + link to bio | Every blog post | Critical | A | No anonymous content |
| Privacy policy | None | Comprehensive privacy policy | /privacy/ | High | A | Required by Privacy Act 1988 |
| Terms of service | None | Terms covering directory listings, paid placements, user content | /terms/ | High | A | Legal review required |
| Real photos (not stock) for team | None | Real photos of editorial team + reviewers | /editorial-team/ | High | A | Headshots + brief bio video optional |
| Citations to ADA, ADHF, AHPRA | None | Authority citations throughout medical content | Every medical article | High | A | External outlinks to .gov.au, ADA, peer-reviewed |
| About page explaining model | None | Clear about page explaining directory model, ranking process, why we exist | /about/ | High | A | Builds transparency |
| Contact page | None | Real contact info (email, postal address, ABN) | /contact/ | High | A | ABN registered |
| Advertising policy | None | Detailed policy on paid placements, link attributes, ethical guidelines | /disclosures/ | High | A | ACCC compliance |
| Accessibility statement | None | WCAG 2.1 AA statement | /accessibility/ | Medium | B | Required for AU gov-adjacent content |
| Fact-check process documented | None | Step-by-step fact-check process documented | /methodology/ | Medium | B | Builds editorial credibility |
| Correction policy | None | Documented correction process with visible corrections log | /corrections/ | Medium | B | News-style corrections |
| Conflict of interest disclosure | None | COI disclosed for every reviewer (clinic ownership etc.) | /editorial-team/ + per article | Medium | B | Per medical publishing standards |
| Content style guide | None | Editorial style guide publicly documented | /methodology/ | Medium | B | Australian English, terminology |
| Schema for medical content | None | MedicalWebPage schema with reviewer + dateReviewed on all medical articles | Every medical blog post | High | A | Signals to Google this is medical content |
| Trust badges | None | AHPRA-verified reviewer badges, ADA-cited badges | On reviewer bios | Medium | B | Visual EEAT signals |
| Press / media coverage | None | Track and link to media mentions | /about/ | Low | C | As site grows |
| Awards / recognition | None | Apply for industry awards as directory grows | /about/ | Low | C | Year 2+ |
| Community involvement | None | Document any dental community contributions | /about/ | Low | C | Year 2+ |

## Tab: Schema Markup Plan

| Page Type | Schema Types | Required Properties |
| Homepage | Organization + WebSite + SearchAction + BreadcrumbList | name, url, logo, sameAs (ADA, AHPRA, LinkedIn), description, founder |
| Trust pages (about, methodology, disclosures, privacy, terms, contact) | WebPage + BreadcrumbList + (ContactPage for contact) | name, description, inLanguage: en-AU, lastReviewed |
| Cluster hub (/blog/{cluster}/) | CollectionPage + BreadcrumbList + ItemList (of posts) | name, description, hasPart (list of blog URLs) |
| Blog post | Article + MedicalWebPage + BreadcrumbList + FAQPage + Person (author) + Person (reviewer) | headline, author, datePublished, dateModified, dateReviewed, reviewer, medicalAudience, about, citation |
| Service/Location listicle | MedicalWebPage + ItemList + FAQPage + BreadcrumbList + Review (per practice) | name, description, mainEntity (ItemList of practices) |
| Editorial team / reviewer bio | ProfilePage + Person + BreadcrumbList | name, jobTitle, alumnusOf, knowsAbout, award, worksFor |

## Tab: Build Roadmap

| Phase | Timeframe | Scope | Page Count | Cumulative | Key Deliverables |
| Phase 1A | Weeks 1-4 | Foundation | 30 | 30 | Homepage + 8 trust pages + Australia hub + Sydney hub + Brisbane hub + first 18 service pages (national) + first cluster hubs (5) |
| Phase 1B | Weeks 5-12 | Foundation completion + Phase A services + Phase A blogs | 400 | 430 | Remaining 24 national services + 42 Sydney services + 42 Brisbane services = 127 commercial total + first 200 blog posts (priority clusters: Implantology, Ortho, Cosmetic, Conditions, Costs) |
| Phase 1C | Weeks 13-24 | Blog scaling | 700 | 1,130 | Remaining 800 blog posts across all 28 clusters + cluster hubs all live + internal linking complete + first medical reviewer on staff |
| Phase 2 | Year 1 (months 7-12) | City expansion + post scaling | 1,500 | 2,630 | Add Melbourne, Perth, Adelaide, Gold Coast (4 new cities × 42 services = 168 new commercial pages) + 1,300 new blog posts in unexplored sub-topics |
| Phase 3 | Year 2 | Full AU capital cities | 3,000 | 5,630 | Add Hobart, Canberra, Darwin (+ remaining regional cities, ~10 cities × 42 services = 420 commercial pages) + 2,500 new posts |
| Phase 4 | Year 2-3 | Suburb expansion | 50,000 | 55,630 | All Sydney + Brisbane + Melbourne + Perth + Adelaide suburbs × 42 services. Requires programmatic SEO with templated suburb pages. Heavy schema + automated internal linking. |
| Phase 5 | Year 3 | International | 20,000 | 75,630 | UK, Canada, US, NZ expansion. Country-specific schema, language tags (en-GB, en-US, en-NZ), international hreflang. Local authority signals (GDC for UK, state dental boards for US/CA). |

## Tab: Risk & Dependencies

| Risk ID | Category | Risk | Impact | Mitigation | Dependencies Required from User |
| R1 | EEAT | Cannot recruit licensed AU dentist reviewers | Critical | Budget for paid medical reviewers (est. $100-200/article); contact ADA member network | Recruiting budget + reviewer contacts |
| R2 | EEAT | Paid placements perceived as bias | High | Transparent methodology page + clear do-follow vs no-follow disclosure + ACCC compliance | Legal review of disclosures |
| R3 | Content | 1,000+ blog posts require consistent quality at scale | High | Editorial team + style guide + medical review workflow + AI-assisted first drafts with human edit | Content writer team + AI drafting tools |
| R4 | Content | Writers may not be dental-literate | High | Hire dental writers or train generalists with dental glossary + reviewer fact-checks | Writer recruitment |
| R5 | Technical | 70k+ pages require scalable CMS | Critical | Headless CMS (Strapi/Sanity) + Next.js + programmatic templates for suburb pages | Dev team + infrastructure budget |
| R6 | Technical | Internal linking at scale unmanageable manually | High | Build internal linking automation tool; templated related-posts logic per cluster | Dev resource |
| R7 | Local SEO | No clients on platform in Phase 1 — all directory entries no-follow | High | Curate top 10 lists from public sources (AHPRA register, Google reviews, ADA member directory) | Initial directory data |
| R8 | Local SEO | Practice contact info changes | Medium | Quarterly audit of directory entries; automated change detection | Data source subscription |
| R9 | Legal | ACCC disclosure requirements for paid placements | Critical | Legal review of /disclosures/ + /methodology/ + advertising policy | Legal counsel |
| R10 | Legal | Privacy Act 1988 compliance | High | Privacy policy reviewed by counsel; data handling documented | Legal counsel |
| R11 | SEO | Google may treat directory as low-quality if content thin | Critical | Minimum 1,500 words per blog post + 1,500 per service page + medical review + citations | Editorial discipline |
| R12 | SEO | Cannibalisation between /australia/{service}/ and /australia/{city}/{service}/ | High | Clear keyword differentiation: national = "{service} australia", city = "{service} {city}"; canonicals set correctly | SEO review of every page |
| R13 | SEO | Top 10 listicles flagged as "affiliate content" without proper EEAT | High | Real methodology + reviewer credentials + transparent process + quality of descriptions (not just link farm) | EEAT investment |
| R14 | Schema | MedicalWebPage schema may be flagged if reviewers not legitimate | High | Real AHPRA-registered reviewers; quarterly verification; reviewer schema on every page | Reviewer onboarding |
| R15 | Scale | 50,000 suburb pages (Phase 4) risk of duplicate/thin content penalty | Critical | Unique suburb data (postcodes, demographics, transit, local context) per page; not pure templated content | Suburb data source + dev |
| R16 | Brand | "Fascinating Dentistry" name may not signal authority vs medical terms | Medium | Strong visual brand + about page + reviewer credentials; consider tagline "Australia's dental authority" | Brand guidelines |
| R17 | Revenue | Slow client onboarding in Phase 1 (no do-follow placements sold) | Medium | Phase 1 funded as platform build; client sales start once traffic established | Sales pipeline + funding |
| R18 | Quality | Quality drift over 1,000 posts | High | Quarterly editorial audits; rotation of writers; reader feedback mechanism | QA process |
| R19 | Quality | Reviewer availability bottleneck | High | Recruit 3-5 reviewers to distribute load; queue management | Reviewer pipeline |
| R20 | External | AHPRA register changes may break reviewer verification | Low | Quarterly manual check + automated AHPRA API (if available) | AHPRA API access |
| R21 | External | ADA fee survey updates annually | Low | Update cost references annually when new survey released | ADA subscription |
| R22 | External | Google algorithm updates may affect directory sites | Medium | Diversify traffic sources; build real brand authority; avoid PBN-style patterns | Brand building |
| R23 | Timeline | 1,000 posts in 24 weeks = ~42 posts/week = aggressive | High | Phase 1 may need extension to 36 weeks OR scope reduction to 600 posts in 24 weeks + remainder in Phase 2 | Realistic scoping |
| R24 | Content | Some entities in inventory may not warrant standalone post | Low | Cluster entities grouped by importance; only top 1,000 become posts | Editorial judgment |
| R25 | Conversion | Informational traffic may not convert to directory clicks | Medium | Strategic CTAs in every post; conversion path tested monthly | UX + analytics |
