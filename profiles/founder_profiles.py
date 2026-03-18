# Regulatory profiles drive personalized monitoring per founder.
# product_category maps to FDA device classification and CPT code families.

FOUNDER_PROFILES = [
    {
        "client_id": "client_001",
        "company": "Example Women's Health Co.",
        "founder_name": "Founder Name",
        "email": "founder@example.com",
        "indication": "maternal health",
        "product_category": "digital therapeutic",  # device | digital therapeutic | diagnostic | drug | SaMD
        "fda_pathway": "De Novo",  # 510(k) | De Novo | PMA | EUA | exempt
        "product_codes": ["QMS", "NOB"],  # FDA product codes relevant to their device
        "cpt_codes_of_interest": ["99441", "99442", "0770T"],  # CPT codes they bill or plan to bill
        "key_payers": ["CMS", "UnitedHealthcare", "Aetna", "BCBS"],
        "state_markets": ["MI", "TX", "CA", "NY"],
    },
    # Add additional client profiles here
]
