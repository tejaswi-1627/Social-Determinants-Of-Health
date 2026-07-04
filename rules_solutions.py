"""
This file contains the rule-based data for detecting Social Determinants of Health (SDoH).
Each category includes keywords for detection and corresponding solutions.
"""

SDOH_DATA = {
    "financial_insecurity": {
        "keywords": [
            "unemployed", "unemployment", "financial", "income", "debt",
            "can't afford", "cannot afford", "struggles to pay", "medical bills",
            "utilities", "disconnection", "no money", "low income", "financial stress",
            "poverty", "financial hardship"
        ],
        "solutions": [
            "Refer to a financial counselor or social worker.",
            "Provide information on local financial assistance programs (e.g., LIHEAP for utilities).",
            "Connect with hospital's charity care or financial aid department.",
            "💰 Financial Counseling: www.nfcc.org",
            "📊 Benefits Eligibility: www.benefits.gov",
            "🏦 Emergency Financial Assistance: Local community action agency",
            "📱 211 Helpline: Dial 2-1-1 for local resources"
        ]
    },
    "food_insecurity": {
        "keywords": [
            "hungry", "hunger", "food insecurity", "no food", "not enough food",
            "poor diet", "malnutrition", "food stamps", "SNAP", "food bank",
            "nutritious food", "can't afford food", "no money for food",
            "skipping meals", "not eating"
        ],
        "solutions": [
            "Screen for food insecurity using a validated tool.",
            "Refer to local food banks, pantries, or soup kitchens.",
            "Provide information on applying for SNAP/WIC benefits.",
            "🍲 Feeding America Food Bank: 1-800-FOOD",
            "🎫 SNAP Benefits: www.fns.usda.gov/snap",
            "🍎 Local Food Pantry Finder: www.feedingamerica.org",
            "👶 WIC Program (Women/Infants/Children): www.fns.usda.gov/wic"
        ]
    },
    "transportation_insecurity": {
        "keywords": [
            "transportation", "no transport", "no car", "can't travel", "missed appointment",
            "no ride", "travel expenses", "bus pass", "can't get to", "transportation issues"
        ],
        "solutions": [
            "Refer to hospital's transportation assistance program.",
            "Provide information on public transit options and subsidized passes.",
            "Connect with volunteer driver programs or medical transportation services.",
            "🚐 Free Medical Transport: Local hospital patient services",
            "🚌 Public Transit Info: www.transit.app",
            "🚕 Medicaid Transportation: Contact your Medicaid office",
            "🚗 Volunteer Driver Programs: Local senior center"
        ]
    },
    "social_isolation": {
        "keywords": [
            "lonely", "loneliness", "isolated", "alone", "no support",
            "no one to help", "caregiver", "social network", "lives alone", "no family"
        ],
        "solutions": [
            "Refer to a social worker for a comprehensive social support assessment.",
            "Connect with local senior centers, community groups, or friendly visitor programs.",
            "Encourage participation in group activities or support groups.",
            "👥 Support Groups: www.supportgroups.com",
            "🤝 Community Centers: Local recreation department",
            "📞 Friendship Line: 1-800-971-0016",
            "⛪ Faith-Based Organizations: Local churches/temples"
        ]
    },
    "housing": {
        "keywords": [
            "homeless",
            "unstable housing",
            "no place to live",
            "evicted",
            "housing insecurity",
            "couch surfing"
        ],
        "solutions": [
            "📞 National Housing Hotline: 1-800-569-4287",
            "🏠 Emergency Shelter Locator: www.shelterlist.com",
            "💰 Housing Assistance Programs: www.hud.gov",
            "📋 Apply for Section 8: Local Housing Authority"
        ]
    },
    "employment": {
        "keywords": [
            "lost job",
            "unemployed",
            "fired",
            "laid off",
            "can't find work",
            "no employment"
        ],
        "solutions": [
            "💼 State Workforce Agency: www.careeronestop.org",
            "📚 Job Training Programs: Local community college",
            "💵 Unemployment Benefits: www.dol.gov/unemployment",
            "🔍 Job Search Resources: www.indeed.com, www.linkedin.com"
        ]
    },
    "education": {
        "keywords": [
            "low education",
            "didn't finish school",
            "no diploma",
            "education barrier",
            "illiterate"
        ],
        "solutions": [
            "🎓 Adult Education Classes: www.ed.gov/adult-education",
            "📖 GED Program: Local community college",
            "💻 Free Online Courses: www.coursera.org, www.khanacademy.org",
            "📚 Literacy Programs: Local library"
        ]
    },
    "intimate_partner_violence": {
        "keywords": [
            "domestic violence",
            "abusive partner",
            "IPV",
            "partner violence",
            "unsafe at home",
            "afraid of partner"
        ],
        "solutions": [
            "🆘 National DV Hotline: 1-800-799-7233 (24/7)",
            "🏠 Emergency Shelter: www.thehotline.org",
            "👮 Safety Planning: Local police victim services",
            "⚖️ Legal Aid: www.legalaidatlast.org"
        ]
    },
    "substance_use": {
        "keywords": [
            "drug use",
            "substance abuse",
            "addiction",
            "opioid",
            "heroin",
            "cocaine",
            "methamphetamine"
        ],
        "solutions": [
            "📞 SAMHSA Helpline: 1-800-662-4357 (24/7)",
            "🏥 Treatment Locator: www.samhsa.gov/find-help",
            "💊 Medication-Assisted Treatment: Local addiction clinic",
            "🤝 Narcotics Anonymous: www.na.org"
        ]
    },
    "alcohol_use": {
        "keywords": [
            "alcohol",
            "drinking problem",
            "alcoholic",
            "heavy drinking",
            "binge drinking",
            "drinks daily"
        ],
        "solutions": [
            "🍺 NIAAA Helpline: 1-800-662-4357",
            "🤝 Alcoholics Anonymous: www.aa.org",
            "🏥 Alcohol Treatment Programs: www.samhsa.gov",
            "👨‍⚕️ Medical Detox: Contact your doctor"
        ]
    },
    "tobacco_use": {
        "keywords": [
            "smoking",
            "tobacco",
            "smoker",
            "cigarettes",
            "vaping",
            "nicotine"
        ],
        "solutions": [
            "🚭 Quit Smoking Hotline: 1-800-QUIT-NOW",
            "💊 Nicotine Replacement: www.smokefree.gov",
            "📱 QuitGuide App: Free from CDC",
            "👨‍⚕️ Cessation Programs: Ask your doctor"
        ]
    },
    "mental_health": {
        "keywords": [
            "depression",
            "anxiety",
            "mental health",
            "suicidal",
            "psychiatric",
            "emotional distress"
        ],
        "solutions": [
            "🆘 Crisis Hotline: 988 (Suicide & Crisis Lifeline)",
            "🧠 Mental Health Services: www.mentalhealth.gov",
            "💬 Free Counseling: Local community mental health center",
            "📱 Crisis Text Line: Text HOME to 741741"
        ]
    },
    "legal": {
        "keywords": [
            "legal issues",
            "arrested",
            "probation",
            "court",
            "criminal record",
            "parole"
        ],
        "solutions": [
            "⚖️ Legal Aid: www.lawhelp.org",
            "👨‍⚖️ Public Defender: Local courthouse",
            "📋 Expungement Services: Local legal aid society",
            "🤝 Reentry Programs: www.prisonfellowship.org"
        ]
    },
    "child_welfare": {
        "keywords": [
            "CPS",
            "child protective services",
            "foster care",
            "custody issues",
            "child welfare",
            "kids taken away"
        ],
        "solutions": [
            "👶 Child Welfare Services: Local CPS office",
            "👨‍👩‍👧 Parenting Classes: Local family services",
            "⚖️ Family Law Attorney: www.lawhelp.org",
            "🤝 Family Support: www.childwelfare.gov"
        ]
    },
    "disability": {
        "keywords": [
            "disabled",
            "disability",
            "can't work due to",
            "physical limitation",
            "chronic condition",
            "unable to function"
        ],
        "solutions": [
            "♿ Social Security Disability: www.ssa.gov/disability",
            "🏥 Vocational Rehabilitation: State VR agency",
            "🦽 Assistive Technology: www.abledata.acl.gov",
            "💰 Disability Benefits: www.disabilitybenefitscenter.org"
        ]
    },
    "language": {
        "keywords": [
            "language barrier",
            "doesn't speak English",
            "interpreter needed",
            "limited English",
            "non-English speaking"
        ],
        "solutions": [
            "🗣️ Medical Interpreter: Hospital interpreter services",
            "📱 Translation App: Google Translate (free)",
            "📚 ESL Classes: Local library or community college",
            "🌐 Multilingual Resources: 211 offers language assistance"
        ]
    },
    "immigration_status": {
        "keywords": [
            "undocumented",
            "immigration status",
            "visa issues",
            "deportation",
            "illegal immigrant",
            "asylum"
        ],
        "solutions": [
            "🗽 Immigration Legal Services: www.immigrationadvocates.org",
            "📋 USCIS Resources: www.uscis.gov",
            "⚖️ Free Immigration Lawyer: www.legalaidimmigration.org",
            "🤝 Immigrant Support: Local immigrant resource center"
        ]
    },
    "access_to_care": {
        "keywords": [
            "no insurance",
            "can't afford healthcare",
            "missed appointments",
            "no doctor",
            "healthcare access",
            "uninsured"
        ],
        "solutions": [
            "🏥 Community Health Center: www.findahealthcenter.hrsa.gov",
            "💳 Medicaid Enrollment: www.medicaid.gov",
            "🩺 Free Clinics: www.freeclinics.com",
            "💊 Prescription Assistance: www.needymeds.org"
        ]
    },
    "health_literacy": {
        "keywords": [
            "doesn't understand",
            "health literacy",
            "confused about treatment",
            "low health knowledge",
            "medical information"
        ],
        "solutions": [
            "📖 Patient Education: Ask for teach-back method",
            "🗣️ Health Advocate: Request patient navigator",
            "📱 Health Info: www.medlineplus.gov (plain language)",
            "👨‍⚕️ Ask Doctor: Request simple explanations"
        ]
    },
    "neighborhood": {
        "keywords": [
            "unsafe neighborhood",
            "crime",
            "violence in area",
            "dangerous area",
            "neighborhood safety"
        ],
        "solutions": [
            "👮 Community Policing: Local police department",
            "🏘️ Neighborhood Watch: www.nnw.org",
            "🚨 Safety Resources: Local community center",
            "🏠 Relocation Assistance: Local housing authority"
        ]
    },
    "other_socioeconomic": {
        "keywords": [
            "socioeconomic",
            "poverty",
            "low SES",
            "disadvantaged",
            "underserved"
        ],
        "solutions": [
            "📞 211 Helpline: Dial 2-1-1 (connects to local resources)",
            "💰 Benefits Screening: www.benefits.gov",
            "🤝 Community Action Agency: Local CAA office",
            "📋 Social Services: County social services department"
        ]
    }
}
