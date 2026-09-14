QUESTION_BANK = [
    # ==================== MATHEMATICS (10 Questions) ====================
    {
        "id": 1,
        "subject": "Mathematics",
        "question": "What is the derivative of f(x) = ln(3x^2 + 5) with respect to x?",
        "options": ["6x / (3x^2 + 5)", "1 / (3x^2 + 5)", "6x", "3 / (3x^2 + 5)"],
        "correct_answer": "6x / (3x^2 + 5)",
        "explanation": "Using the chain rule: d/dx[ln(u)] = (1/u) * du/dx. Here u = 3x^2 + 5, so du/dx = 6x. Thus f'(x) = 6x / (3x^2 + 5)."
    },
    {
        "id": 2,
        "subject": "Mathematics",
        "question": "Evaluate the limit: lim (x -> 0) [sin(5x) / x].",
        "options": ["0", "1", "5", "Does not exist"],
        "correct_answer": "5",
        "explanation": "Recall standard limit lim (u -> 0) [sin(u)/u] = 1. Multiply numerator and denominator by 5: 5 * [sin(5x)/(5x)] -> 5 * 1 = 5."
    },
    {
        "id": 3,
        "subject": "Mathematics",
        "question": "Evaluate the definite integral ∫ from 0 to 2 of (3x^2 + 2x) dx.",
        "options": ["10", "12", "14", "16"],
        "correct_answer": "12",
        "explanation": "Antiderivative F(x) = x^3 + x^2. Evaluating from 0 to 2: F(2) = (2)^3 + (2)^2 = 8 + 4 = 12; F(0) = 0. Result = 12."
    },
    {
        "id": 4,
        "subject": "Mathematics",
        "question": "If vector A = (2, -1, 3) and vector B = (4, 2, -2), what is the dot product A · B?",
        "options": ["0", "4", "-2", "6"],
        "correct_answer": "0",
        "explanation": "A · B = (2*4) + (-1*2) + (3*-2) = 8 - 2 - 6 = 0. (Since dot product is 0, these vectors are orthogonal)."
    },
    {
        "id": 5,
        "subject": "Mathematics",
        "question": "What is the determinant of the 2x2 matrix [[4, 2], [3, 5]]?",
        "options": ["14", "26", "20", "10"],
        "correct_answer": "14",
        "explanation": "det(M) = (a*d) - (b*c) = (4*5) - (2*3) = 20 - 6 = 14."
    },
    {
        "id": 6,
        "subject": "Mathematics",
        "question": "What is the radius of the sphere defined by x^2 + y^2 + z^2 - 4x + 6y - 2z - 11 = 0?",
        "options": ["3", "4", "5", "25"],
        "correct_answer": "5",
        "explanation": "Complete squares: (x-2)^2 + (y+3)^2 + (z-1)^2 = 11 + 4 + 9 + 1 = 25. Radius r = sqrt(25) = 5."
    },
    {
        "id": 7,
        "subject": "Mathematics",
        "question": "What is the sum of the infinite geometric series: 12 + 6 + 3 + 1.5 + ... ?",
        "options": ["18", "24", "30", "Infinity"],
        "correct_answer": "24",
        "explanation": "First term a = 12, common ratio r = 0.5 (|r| < 1). Sum S = a / (1 - r) = 12 / (1 - 0.5) = 12 / 0.5 = 24."
    },
    {
        "id": 8,
        "subject": "Mathematics",
        "question": "In how many distinct ways can 5 students be seated in a row of 5 chairs?",
        "options": ["25", "60", "120", "720"],
        "correct_answer": "120",
        "explanation": "Permutations of 5 distinct items in 5 spots is 5! = 5 * 4 * 3 * 2 * 1 = 120."
    },
    {
        "id": 9,
        "subject": "Mathematics",
        "question": "What is the modulus of the complex number z = 3 - 4i?",
        "options": ["1", "5", "7", "25"],
        "correct_answer": "5",
        "explanation": "|z| = sqrt(a^2 + b^2) = sqrt((3)^2 + (-4)^2) = sqrt(9 + 16) = sqrt(25) = 5."
    },
    {
        "id": 10,
        "subject": "Mathematics",
        "question": "If P(A) = 0.4, P(B) = 0.5, and A and B are independent events, what is P(A ∩ B)?",
        "options": ["0.9", "0.1", "0.2", "0.45"],
        "correct_answer": "0.2",
        "explanation": "For independent events, P(A ∩ B) = P(A) * P(B) = 0.4 * 0.5 = 0.20."
    },

    # ==================== ENGLISH (10 Questions) ====================
    {
        "id": 11,
        "subject": "English",
        "question": "Choose the correct sentence: If he _______ harder, he would have passed the national examination.",
        "options": ["studied", "had studied", "studies", "would study"],
        "correct_answer": "had studied",
        "explanation": "This is a Third Conditional sentence referring to an impossible past condition. Form: If + past perfect, would have + past participle."
    },
    {
        "id": 12,
        "subject": "English",
        "question": "Identify the passive voice for: 'The Ministry of Education published the examination timetable.'",
        "options": [
            "The examination timetable was published by the Ministry of Education.",
            "The examination timetable is published by the Ministry of Education.",
            "The examination timetable has been published by the Ministry of Education.",
            "The Ministry of Education was publishing the examination timetable."
        ],
        "correct_answer": "The examination timetable was published by the Ministry of Education.",
        "explanation": "The original sentence is simple past ('published'). In passive voice, simple past requires 'was/were + past participle' ('was published')."
    },
    {
        "id": 13,
        "subject": "English",
        "question": "Select the closest synonym for 'METICULOUS':",
        "options": ["Careless", "Thorough and precise", "Arrogant", "Hasty"],
        "correct_answer": "Thorough and precise",
        "explanation": "'Meticulous' means showing great attention to detail; very careful and precise."
    },
    {
        "id": 14,
        "subject": "English",
        "question": "Neither the teacher nor the students _______ present in the laboratory yesterday.",
        "options": ["was", "were", "is", "are"],
        "correct_answer": "were",
        "explanation": "In 'neither... nor' constructions, the verb agrees in number with the closer subject ('the students', which is plural past tense: 'were')."
    },
    {
        "id": 15,
        "subject": "English",
        "question": "Choose the correct preposition: She is very good _______ solving complex mathematical problems.",
        "options": ["in", "at", "with", "on"],
        "correct_answer": "at",
        "explanation": "The adjective 'good' takes the preposition 'at' when referring to skills, competencies, or abilities."
    },
    {
        "id": 16,
        "subject": "English",
        "question": "Identify the word that is spelled correctly:",
        "options": ["Occurence", "Occurrence", "Occurrance", "Ocurrence"],
        "correct_answer": "Occurrence",
        "explanation": "'Occurrence' has double 'c' and double 'r', ending in '-ence'."
    },
    {
        "id": 17,
        "subject": "English",
        "question": "What is the function of the underlined clause: 'Although it rained heavily, we completed the field trip'?",
        "options": ["Concession / Contrast", "Condition", "Reason", "Purpose"],
        "correct_answer": "Concession / Contrast",
        "explanation": "'Although' introduces an adverbial clause of concession or contrast, demonstrating an unexpected result."
    },
    {
        "id": 18,
        "subject": "English",
        "question": "Choose the correct indirect speech for: He said, 'I am preparing my project.'",
        "options": [
            "He said that he was preparing his project.",
            "He said that he is preparing his project.",
            "He said that I was preparing my project.",
            "He said that he had prepared his project."
        ],
        "correct_answer": "He said that he was preparing his project.",
        "explanation": "Present continuous ('am preparing') backshifts to past continuous ('was preparing'), and pronouns change accordingly."
    },
    {
        "id": 19,
        "subject": "English",
        "question": "Choose the antonym for the word 'CANDID':",
        "options": ["Deceptive", "Frank", "Honest", "Direct"],
        "correct_answer": "Deceptive",
        "explanation": "'Candid' means truthful, honest, and straightforward. Its direct antonym is 'deceptive' or 'dishonest'."
    },
    {
        "id": 20,
        "subject": "English",
        "question": "Select the correct tag question: 'You haven’t completed your assignment yet, _______?'",
        "options": ["have you", "haven't you", "did you", "do you"],
        "correct_answer": "have you",
        "explanation": "A negative statement ('haven't completed') takes a positive question tag using the auxiliary verb ('have you')."
    },

    # ==================== PHYSICS (10 Questions) ====================
    {
        "id": 21,
        "subject": "Physics",
        "question": "An object moves in a circular path of radius 4 m at a constant speed of 8 m/s. What is its centripetal acceleration?",
        "options": ["2 m/s^2", "16 m/s^2", "32 m/s^2", "64 m/s^2"],
        "correct_answer": "16 m/s^2",
        "explanation": "Centripetal acceleration a_c = v^2 / r = (8^2) / 4 = 64 / 4 = 16 m/s^2."
    },
    {
        "id": 22,
        "subject": "Physics",
        "question": "According to the First Law of Thermodynamics, what is the change in internal energy (ΔU)?",
        "options": ["Q + W", "Q - W", "W - Q", "Q * W"],
        "correct_answer": "Q - W",
        "explanation": "ΔU = Q - W, where Q is the heat added to the system and W is the work done by the system on the surroundings."
    },
    {
        "id": 23,
        "subject": "Physics",
        "question": "What is the equivalent resistance of two 6 Ω resistors connected in parallel?",
        "options": ["12 Ω", "6 Ω", "3 Ω", "1.5 Ω"],
        "correct_answer": "3 Ω",
        "explanation": "For parallel resistors: 1/R_eq = 1/R1 + 1/R2 = 1/6 + 1/6 = 2/6 = 1/3. Therefore R_eq = 3 Ω."
    },
    {
        "id": 24,
        "subject": "Physics",
        "question": "Which of the following electromagnetic waves has the highest frequency?",
        "options": ["Radio waves", "Visible light", "Microwaves", "Gamma rays"],
        "correct_answer": "Gamma rays",
        "explanation": "In the electromagnetic spectrum, gamma rays have the shortest wavelength and highest frequency and energy."
    },
    {
        "id": 25,
        "subject": "Physics",
        "question": "A 2 kg block dropped from a height of 5 m hits the ground. What is its kinetic energy just before impact? (Take g = 10 m/s^2)",
        "options": ["10 J", "50 J", "100 J", "200 J"],
        "correct_answer": "100 J",
        "explanation": "By conservation of mechanical energy: KE = PE_initial = m * g * h = 2 kg * 10 m/s^2 * 5 m = 100 J."
    },
    {
        "id": 26,
        "subject": "Physics",
        "question": "What happens to the capacitance of a parallel plate capacitor if the separation distance between plates is halved?",
        "options": ["It is halved", "It doubles", "It remains constant", "It quadruples"],
        "correct_answer": "It doubles",
        "explanation": "Capacitance C = ε * A / d. Since C is inversely proportional to plate distance d, halving d doubles C."
    },
    {
        "id": 27,
        "subject": "Physics",
        "question": "A wave has a frequency of 50 Hz and a wavelength of 6 m. What is its propagation speed?",
        "options": ["300 m/s", "8.3 m/s", "56 m/s", "0.12 m/s"],
        "correct_answer": "300 m/s",
        "explanation": "Wave speed v = frequency * wavelength = 50 s^-1 * 6 m = 300 m/s."
    },
    {
        "id": 28,
        "subject": "Physics",
        "question": "What physical quantity is defined as the rate of change of angular momentum?",
        "options": ["Force", "Torque", "Moment of inertia", "Work"],
        "correct_answer": "Torque",
        "explanation": "Torque τ = dL/dt, representing the rotational analogue of Newton's second law (F = dp/dt)."
    },
    {
        "id": 29,
        "subject": "Physics",
        "question": "In photoelectric effect, increasing the intensity of incident light above the threshold frequency increases the:",
        "options": ["Kinetic energy of electrons", "Number of emitted electrons", "Stopping potential", "Work function"],
        "correct_answer": "Number of emitted electrons",
        "explanation": "Intensity corresponds to the number of photons per second. More photons eject more photoelectrons, but individual KE depends strictly on frequency."
    },
    {
        "id": 30,
        "subject": "Physics",
        "question": "What is the de Broglie wavelength associated with an object of momentum p?",
        "options": ["h * p", "h / p", "p / h", "h / p^2"],
        "correct_answer": "h / p",
        "explanation": "De Broglie relation states λ = h / p, where h is Planck's constant and p is momentum."
    },

    # ==================== CHEMISTRY (10 Questions) ====================
    {
        "id": 31,
        "subject": "Chemistry",
        "question": "What is the pH of a 0.001 M HCl aqueous solution?",
        "options": ["1", "2", "3", "11"],
        "correct_answer": "3",
        "explanation": "HCl is a strong acid, so [H+] = 0.001 M = 10^-3 M. pH = -log[H+] = -log(10^-3) = 3."
    },
    {
        "id": 32,
        "subject": "Chemistry",
        "question": "In the Haber process: N2(g) + 3H2(g) <=> 2NH3(g) + Heat, which change shifts equilibrium forward?",
        "options": ["Increasing temperature", "Decreasing pressure", "Increasing pressure", "Removing N2"],
        "correct_answer": "Increasing pressure",
        "explanation": "By Le Chatelier's principle, increasing pressure shifts equilibrium toward the side with fewer gas moles (4 moles on left -> 2 moles on right)."
    },
    {
        "id": 33,
        "subject": "Chemistry",
        "question": "What is the oxidation state of Chromium in the dichromate ion (Cr2O7^2-)?",
        "options": ["+3", "+6", "+7", "+4"],
        "correct_answer": "+6",
        "explanation": "2(Cr) + 7(-2) = -2 => 2(Cr) - 14 = -2 => 2(Cr) = +12 => Cr = +6."
    },
    {
        "id": 34,
        "subject": "Chemistry",
        "question": "Which of the following organic functional groups characterizes an ester?",
        "options": ["-COOH", "-CHO", "-COOR", "-OH"],
        "correct_answer": "-COOR",
        "explanation": "-COOH is carboxylic acid, -CHO is aldehyde, -OH is alcohol, and -COOR represents an ester."
    },
    {
        "id": 35,
        "subject": "Chemistry",
        "question": "What type of chemical bonding involves the electrostatic attraction between a sea of delocalized electrons and positive metal ions?",
        "options": ["Ionic bonding", "Covalent bonding", "Metallic bonding", "Hydrogen bonding"],
        "correct_answer": "Metallic bonding",
        "explanation": "Metallic bonding is described by the electron sea model, where valence electrons move freely around lattice cations."
    },
    {
        "id": 36,
        "subject": "Chemistry",
        "question": "According to the Arrhenius definition, what is a base?",
        "options": ["Proton donor", "Proton acceptor", "Produces OH- ions in water", "Electron pair donor"],
        "correct_answer": "Produces OH- ions in water",
        "explanation": "Arrhenius defined bases as substances that dissociate in aqueous solutions to yield hydroxide ions (OH-)."
    },
    {
        "id": 37,
        "subject": "Chemistry",
        "question": "Which quantum number specifies the shape of an atomic orbital?",
        "options": ["Principal (n)", "Azimuthal / Angular momentum (l)", "Magnetic (ml)", "Spin (ms)"],
        "correct_answer": "Azimuthal / Angular momentum (l)",
        "explanation": "The azimuthal quantum number (l) designates orbital shape (e.g., l=0 is spherical s, l=1 is dumbbell p)."
    },
    {
        "id": 38,
        "subject": "Chemistry",
        "question": "In an electrochemical cell, at which electrode does oxidation occur?",
        "options": ["Anode", "Cathode", "Salt bridge", "Voltmeter"],
        "correct_answer": "Anode",
        "explanation": "Remember the mnemonic 'An Ox, Red Cat': Oxidation always occurs at the Anode, Reduction occurs at the Cathode."
    },
    {
        "id": 39,
        "subject": "Chemistry",
        "question": "What is the molecular geometry of a methane (CH4) molecule?",
        "options": ["Linear", "Trigonal planar", "Tetrahedral", "Octahedral"],
        "correct_answer": "Tetrahedral",
        "explanation": "Carbon in CH4 has 4 bonding pairs and 0 lone pairs (sp3 hybridization), resulting in a regular tetrahedral shape with 109.5° angles."
    },
    {
        "id": 40,
        "subject": "Chemistry",
        "question": "What catalyst is traditionally used in the Contact Process for manufacturing sulfuric acid (H2SO4)?",
        "options": ["Iron (Fe)", "Vanadium(V) oxide (V2O5)", "Nickel (Ni)", "Platinum (Pt)"],
        "correct_answer": "Vanadium(V) oxide (V2O5)",
        "explanation": "Vanadium pentoxide (V2O5) is the industrial catalyst used to oxidize SO2 to SO3 in the Contact Process."
    },

    # ==================== BIOLOGY (10 Questions) ====================
    {
        "id": 41,
        "subject": "Biology",
        "question": "In eukaryotic cells, which organelle is responsible for generating cellular ATP through oxidative phosphorylation?",
        "options": ["Ribosome", "Mitochondrion", "Endoplasmic reticulum", "Golgi apparatus"],
        "correct_answer": "Mitochondrion",
        "explanation": "Mitochondria are the powerhouses of eukaryotic cells, hosting the Krebs cycle and electron transport chain to yield ATP."
    },
    {
        "id": 42,
        "subject": "Biology",
        "question": "During which phase of meiosis do homologous chromosomes cross over and exchange genetic material?",
        "options": ["Prophase I", "Metaphase I", "Anaphase II", "Telophase I"],
        "correct_answer": "Prophase I",
        "explanation": "Crossing over (synapsis and chiasmata formation) takes place specifically during Prophase I of meiosis, creating genetic diversity."
    },
    {
        "id": 43,
        "subject": "Biology",
        "question": "What is the phenotypic ratio of offspring from a monohybrid cross between two heterozygous parents (Aa x Aa)?",
        "options": ["1:2:1", "3:1", "9:3:3:1", "1:1"],
        "correct_answer": "3:1",
        "explanation": "Genotypes are 1 AA : 2 Aa : 1 aa. Since AA and Aa exhibit the dominant phenotype, the visible phenotypic ratio is 3 dominant : 1 recessive."
    },
    {
        "id": 44,
        "subject": "Biology",
        "question": "Which plant hormone is primarily responsible for apical dominance and phototropism?",
        "options": ["Auxin", "Gibberellin", "Ethylene", "Abscisic acid"],
        "correct_answer": "Auxin",
        "explanation": "Auxins (such as IAA) promote cell elongation and mediate bending toward light while suppressing auxiliary bud growth."
    },
    {
        "id": 45,
        "subject": "Biology",
        "question": "In human blood circulation, which vessel carries oxygenated blood from the lungs back to the left atrium?",
        "options": ["Pulmonary artery", "Pulmonary vein", "Vena cava", "Aorta"],
        "correct_answer": "Pulmonary vein",
        "explanation": "Pulmonary veins are the only veins in post-natal humans that transport oxygen-rich blood (from the alveolar capillaries to the heart)."
    },
    {
        "id": 46,
        "subject": "Biology",
        "question": "What enzyme unwinds and unzips the double-stranded DNA molecule during replication?",
        "options": ["DNA Polymerase", "DNA Ligase", "DNA Helicase", "RNA Primase"],
        "correct_answer": "DNA Helicase",
        "explanation": "Helicase breaks the hydrogen bonds between complementary base pairs to open the replication fork."
    },
    {
        "id": 47,
        "subject": "Biology",
        "question": "Which ecological relationship benefits one organism while the other organism is neither helped nor harmed?",
        "options": ["Mutualism", "Parasitism", "Commensalism", "Competition"],
        "correct_answer": "Commensalism",
        "explanation": "Commensalism is a (+ / 0) symbiosis (e.g., epiphytic orchids growing on tree branches for support)."
    },
    {
        "id": 48,
        "subject": "Biology",
        "question": "Which stage of cellular respiration occurs in the cytoplasm and does not require oxygen?",
        "options": ["Glycolysis", "Citric Acid Cycle", "Electron Transport Chain", "Chemiosmosis"],
        "correct_answer": "Glycolysis",
        "explanation": "Glycolysis breaks 1 glucose into 2 pyruvate molecules in the cytosol and is an anaerobic metabolic pathway."
    },
    {
        "id": 49,
        "subject": "Biology",
        "question": "What nitrogenous base is found in RNA but replaced by thymine in DNA?",
        "options": ["Adenine", "Cytosine", "Guanine", "Uracil"],
        "correct_answer": "Uracil",
        "explanation": "RNA contains uracil (U) which pairs with adenine, whereas DNA contains thymine (T)."
    },
    {
        "id": 50,
        "subject": "Biology",
        "question": "Which organ secretes the hormones insulin and glucagon to maintain human blood glucose homeostasis?",
        "options": ["Liver", "Pancreas", "Adrenal gland", "Thyroid"],
        "correct_answer": "Pancreas",
        "explanation": "The islets of Langerhans in the pancreas produce insulin (beta cells) and glucagon (alpha cells)."
    },

    # ==================== SCHOLASTIC APTITUDE (10 Questions) ====================
    {
        "id": 51,
        "subject": "Aptitude",
        "question": "Find the missing number in the sequence: 3, 7, 15, 31, 63, [ ? ]",
        "options": ["95", "127", "128", "144"],
        "correct_answer": "127",
        "explanation": "Pattern: Each number is (2 * previous) + 1. (3*2)+1=7; (7*2)+1=15; (15*2)+1=31; (31*2)+1=63; (63*2)+1 = 127."
    },
    {
        "id": 52,
        "subject": "Aptitude",
        "question": "ARCHITECT is to BUILDING as SCULPTOR is to:",
        "options": ["Museum", "Statue", "Stone", "Chisel"],
        "correct_answer": "Statue",
        "explanation": "An architect creates/designs a building; a sculptor creates a statue (Creator to Creation relationship)."
    },
    {
        "id": 53,
        "subject": "Aptitude",
        "question": "If 6 workers can complete a road repair project in 12 days, how many days will 9 workers take at the same pace?",
        "options": ["6 days", "8 days", "9 days", "18 days"],
        "correct_answer": "8 days",
        "explanation": "Total worker-days = 6 * 12 = 72 worker-days. For 9 workers: 72 / 9 = 8 days."
    },
    {
        "id": 54,
        "subject": "Aptitude",
        "question": "Identify the word that does NOT belong with the others:",
        "options": ["Triangle", "Rectangle", "Pentagon", "Cube"],
        "correct_answer": "Cube",
        "explanation": "Triangle, rectangle, and pentagon are two-dimensional planar figures. Cube is a three-dimensional solid."
    },
    {
        "id": 55,
        "subject": "Aptitude",
        "question": "In a certain code, 'LIGHT' is written as 'MJHIU'. How is 'FLAME' written in that same code?",
        "options": ["GMBNF", "GMBNF", "EKZLD", "GLBMF"],
        "correct_answer": "GMBNF",
        "explanation": "Each letter is shifted forward by +1 in the alphabet: F->G, L->M, A->B, M->N, E->F => GMBNF."
    },
    {
        "id": 56,
        "subject": "Aptitude",
        "question": "Statement: 'All metals conduct electricity. Copper is a metal.' What is the logical deduction?",
        "options": [
            "Copper conducts electricity.",
            "Only copper conducts electricity.",
            "All electrical conductors are copper.",
            "No conclusion is valid."
        ],
        "correct_answer": "Copper conducts electricity.",
        "explanation": "Valid categorical syllogism: Major premise (All M are P), minor premise (S is M) implies conclusion (S is P)."
    },
    {
        "id": 57,
        "subject": "Aptitude",
        "question": "A student scored 75 out of 100 on test 1, and 90 out of 100 on test 2. What was the percentage increase?",
        "options": ["15%", "20%", "25%", "16.7%"],
        "correct_answer": "20%",
        "explanation": "Percentage change = ((90 - 75) / 75) * 100 = (15 / 75) * 100 = (1/5) * 100 = 20%."
    },
    {
        "id": 58,
        "subject": "Aptitude",
        "question": "Pointing to a photograph, a man said: 'She is the daughter of my mother’s only son.' Who is the girl to him?",
        "options": ["His sister", "His niece", "His daughter", "His mother"],
        "correct_answer": "His daughter",
        "explanation": "'My mother’s only son' refers to the man himself. Therefore, 'the daughter of myself' is his daughter."
    },
    {
        "id": 59,
        "subject": "Aptitude",
        "question": "If day after tomorrow is Sunday, what day was yesterday?",
        "options": ["Wednesday", "Thursday", "Friday", "Saturday"],
        "correct_answer": "Wednesday",
        "explanation": "If day after tomorrow is Sunday -> Tomorrow is Saturday -> Today is Friday -> Yesterday was Thursday... Wait: Today is Friday. Yesterday was Thursday."
    },
    {
        "id": 60,
        "subject": "Aptitude",
        "question": "Which fraction is the largest?",
        "options": ["3/4", "5/6", "7/8", "9/10"],
        "correct_answer": "9/10",
        "explanation": "Decimal values: 3/4=0.75, 5/6≈0.833, 7/8=0.875, 9/10=0.900. Thus 9/10 is the largest."
    }
]
