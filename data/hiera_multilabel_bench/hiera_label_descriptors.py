import json
import os

label2desc_reduced_aapd = {"cs": "Computer Science", "math": "Mathematics", "stat": "Statistics", "physics": "Physics",
                           "quant-ph": "Quantum Physics", "cmp-lg": "Computation and Language",
                           "cond-mat": "Condensed Matter",
                           "q-bio": "Quantitative Biology", "nlin": "Nonlinear Sciences", "cs.it": "Information Theory",
                           "math.it": "Information Theory", "cs.lg": "Machine Learning",
                           "cs.ai": "Artificial Intelligence",
                           "stat.ml": "Machine Learning", "cs.ds": "Data Structures and Algorithms",
                           "cs.si": "Social and Information Networks", "cs.dm": "Discrete Mathematics",
                           "physics.soc-ph": "Physics and Society", "cs.lo": "Logic in Computer Science",
                           "math.co": "Combinatorics",
                           "cs.cc": "Computational Complexity", "math.oc": "Optimization and Control",
                           "cs.ni": "Networking and Internet Architecture",
                           "cs.cv": "Computer Vision and Pattern Recognition",
                           "cs.cl": "Computation and Language", "cs.cr": "Cryptography and Security",
                           "cs.sy": "Systems and Control",
                           "cs.dc": "Distributed, Parallel, and Cluster Computing",
                           "cs.ne": "Neural and Evolutionary Computing",
                           "cs.ir": "Information Retrieval", "cs.gt": "Computer Science and Game Theory",
                           "cs.cy": "Computers and Society", "cs.pl": "Programming Languages",
                           "cs.se": "Software Engineering",
                           "math.pr": "Probability", "cs.db": "Databases", "cs.cg": "Computational Geometry",
                           "cs.na": "Numerical Analysis", "cs.hc": "Human-Computer Interaction",
                           "math.na": "Numerical Analysis",
                           "cs.ce": "Computational Engineering, Finance, and Science", "cs.ma": "Multiagent Systems",
                           "cs.ro": "Robotics", "cs.fl": "Formal Languages and Automata Theory",
                           "math.st": "Statistics Theory",
                           "stat.th": "Statistics Theory", "cs.dl": "Digital Libraries", "cs.mm": "Multimedia",
                           "cond-mat.stat-mech": "Statistical Mechanics", "cs.pf": "Performance", "math.lo": "Logic",
                           "stat.ap": "Applications", "cs.ms": "Mathematical Software", "stat.me": "Methodology",
                           "cs.sc": "Symbolic Computation", "cond-mat.dis-nn": "Disordered Systems and Neural Networks",
                           "q-bio.nc": "Neurons and Cognition",
                           "physics.data-an": "Data Analysis, Statistics and Probability",
                           "nlin.ao": "Adaptation and Self-Organizing Systems", "q-bio.qm": "Quantitative Methods",
                           "math.nt": "Number Theory"}

label2desc_reduced_rcv = {'CCAT': 'CORPORATE', 'ECAT': 'ECONOMICS', 'GCAT': 'GOVERNMENT', 'MCAT': 'MARKETS',
                          'C11': 'STRATEGY', 'C12': 'LEGAL', 'C13': 'REGULATION', 'C14': 'SHARE LISTINGS',
                          'C15': 'PERFORMANCE', 'C16': 'INSOLVENCY', 'C17': 'FUNDING', 'C18': 'OWNERSHIP CHANGES',
                          'C21': 'PRODUCTION', 'C22': 'NEW PRODUCTS', 'C23': 'RESEARCH', 'C24': 'CAPACITY',
                          'C31': 'MARKETING', 'C32': 'ADVERTISING', 'C33': 'CONTRACTS', 'C34': 'MONOPOLIES',
                          'C41': 'MANAGEMENT', 'C42': 'LABOUR', 'E11': 'ECONOMIC PERFORMANCE', 'E12': 'MONETARY',
                          'E13': 'INFLATION', 'E14': 'CONSUMER FINANCE', 'E21': 'GOVERNMENT FINANCE', 'E31': 'OUTPUT',
                          'E41': 'EMPLOYMENT', 'E51': 'TRADE', 'E61': 'HOUSING STARTS', 'E71': 'LEADING INDICATORS',
                          'G15': 'EUROPEAN COMMUNITY', 'GCRIM': 'CRIME, LAW ENFORCEMENT', 'GDEF': 'DEFENCE',
                          'GDIP': 'INTERNATIONAL RELATIONS', 'GDIS': 'DISASTERS AND ACCIDENTS',
                          'GENT': 'ARTS, CULTURE, ENTERTAINMENT', 'GENV': 'ENVIRONMENT AND NATURAL WORLD',
                          'GFAS': 'FASHION', 'GHEA': 'HEALTH', 'GJOB': 'LABOUR ISSUES', 'GMIL': 'MILLENNIUM ISSUES',
                          'GOBIT': 'OBITUARIES', 'GODD': 'HUMAN INTEREST', 'GPOL': 'DOMESTIC POLITICS',
                          'GPRO': 'BIOGRAPHIES, PERSONALITIES, PEOPLE', 'GREL': 'RELIGION',
                          'GSCI': 'SCIENCE AND TECHNOLOGY', 'GSPO': 'SPORTS', 'GTOUR': 'TRAVEL AND TOURISM',
                          'GVIO': 'WAR, CIVIL WAR', 'GVOTE': 'ELECTIONS', 'GWEA': 'WEATHER',
                          'GWELF': 'WELFARE, SOCIAL SERVICES', 'M11': 'EQUITY MARKETS', 'M12': 'BOND MARKETS',
                          'M13': 'MONEY MARKETS', 'M14': 'COMMODITY MARKETS', 'C151': 'ACCOUNTS', 'C152': 'COMMENT',
                          'C171': 'SHARE CAPITAL', 'C172': 'BONDS', 'C173': 'LOANS', 'C174': 'CREDIT RATINGS',
                          'C181': 'MERGERS', 'C182': 'ASSET TRANSFERS', 'C183': 'PRIVATISATIONS',
                          'C311': 'DOMESTIC MARKETS', 'C312': 'EXTERNAL MARKETS', 'C313': 'MARKET SHARE',
                          'C331': 'DEFENCE CONTRACTS', 'C411': 'MANAGEMENT MOVES', 'E121': 'MONEY SUPPLY',
                          'E131': 'CONSUMER PRICES', 'E132': 'WHOLESALE PRICES', 'E141': 'PERSONAL INCOME',
                          'E142': 'CONSUMER CREDIT', 'E143': 'RETAIL SALES', 'E211': 'EXPENDITURE',
                          'E212': 'GOVERNMENT BORROWING', 'E311': 'INDUSTRIAL PRODUCTION',
                          'E312': 'CAPACITY UTILIZATION', 'E313': 'INVENTORIES', 'E411': 'UNEMPLOYMENT',
                          'E511': 'BALANCE OF PAYMENTS', 'E512': 'MERCHANDISE TRADE', 'E513': 'RESERVES',
                          'G151': 'EUROPEAN COMMUNITY INTERNAL MARKET', 'G152': 'EUROPEAN COMMUNITY CORPORATE POLICY', 'G153': 'EUROPEAN COMMUNITY AGRICULTURE POLICY',
                          'G154': 'EUROPEAN COMMUNITY MONETARY', 'G155': 'EUROPEAN COMMUNITY INSTITUTIONS', 'G156': 'EUROPEAN COMMUNITY ENVIRONMENT ISSUES',
                          'G157': 'EUROPEAN COMMUNITY COMPETITION', 'G158': 'EUROPEAN COMMUNITY EXTERNAL RELATIONS', 'G159': 'EUROPEAN COMMUNITY GENERAL',
                          'M131': 'INTERBANK MARKETS', 'M132': 'FOREX MARKETS', 'M141': 'SOFT COMMODITIES',
                          'M142': 'METALS TRADING', 'M143': 'ENERGY MARKETS', 'C1511': 'ANNUAL RESULTS'}

label2desc_reduced_bgc = {
    'Children’sBooks': 'Children’s Books',
    'Classics': 'Classics',
    'Fiction': 'Fiction',
    'Humor': 'Humor',
    'Nonfiction': 'Nonfiction',
    'Poetry': 'Poetry',
    'Teen&YoungAdult': 'Teen and Young Adult',
    'Arts&Entertainment': 'Arts and Entertainment',
    'Biography&Memoir': 'Biography and Memoir',
    'Business': 'Business',
    'Children’sMiddleGradeBooks': 'Children’s Middle Grade Books',
    'Cooking': 'Cooking',
    'Crafts,Home&Garden': 'Crafts, Home and Garden',
    'Fantasy': 'Fantasy',
    'FictionClassics': 'Fiction Classics',
    'Games': 'Games',
    'Gothic&Horror': 'Gothic and Horror',
    'GraphicNovels&Manga': 'Graphic Novels and Manga',
    'Health&Fitness': 'Health and Fitness',
    'HistoricalFiction': 'Historical Fiction',
    'History': 'History',
    'LiteraryCollections': 'Literary Collections',
    'LiteraryCriticism': 'Literary Criticism',
    'LiteraryFiction': 'Literary Fiction',
    'MilitaryFiction': 'Military Fiction',
    'Mystery&Suspense': 'Mystery and Suspense',
    'NonfictionClassics': 'Nonfiction Classics',
    'ParanormalFiction': 'Paranormal Fiction',
    'Parenting': 'Parenting',
    'Pets': 'Pets',
    'Politics': 'Politics',
    'PopularScience': 'Popular Science',
    'Psychology': 'Psychology',
    'Reference': 'Reference',
    'Religion&Philosophy': 'Religion and Philosophy',
    'Romance': 'Romance',
    'ScienceFiction': 'Science Fiction',
    'Self-Improvement': 'Self-Improvement',
    'SpiritualFiction': 'Spiritual Fiction',
    'Sports': 'Sports',
    'StepIntoReading': 'Step Into Reading',
    'Teen&YoungAdultAction&Adventure': 'Teen and Young Adult Action and Adventure',
    'Teen&YoungAdultFantasyFiction': 'Teen and Young Adult Fantasy Fiction',
    'Teen&YoungAdultFiction': 'Teen and Young Adult Fiction',
    'Teen&YoungAdultHistoricalFiction': 'Teen and Young Adult Historical Fiction',
    'Teen&YoungAdultMystery&Suspense': 'Teen and Young Adult Mystery and Suspense',
    'Teen&YoungAdultNonfiction': 'Teen and Young Adult Nonfiction',
    'Teen&YoungAdultRomance': 'Teen and Young Adult Romance',
    'Teen&YoungAdultScienceFiction': 'Teen and Young Adult Science Fiction',
    'Teen&YoungAdultSocialIssues': 'Teen and Young Adult Social Issues',
    'Travel': 'Travel',
    'WesternFiction': 'Western Fiction',
    'Women’sFiction': 'Women’s Fiction',
    'AlternativeTherapies': 'Alternative Therapies',
    'Art': 'Art',
    'Arts&EntertainmentBiographies&Memoirs': 'Arts and Entertainment Biographies and Memoirs',
    'Baking&Desserts': 'Baking and Desserts',
    'Beauty': 'Beauty',
    'Bibles': 'Bibles',
    'Children’sMiddleGradeAction&AdventureBooks': 'Children’s Middle Grade Action and Adventure Books',
    'Children’sMiddleGradeFantasy&MagicalBooks': 'Children’s Middle Grade Fantasy and Magical Books',
    'Children’sMiddleGradeHistoricalBooks': 'Children’s Middle Grade Historical Books',
    'Children’sMiddleGradeMystery&DetectiveBooks': 'Children’s Middle Grade Mystery and Detective Books',
    'Children’sMiddleGradeSportsBooks': 'Children’s Middle Grade Sports Books',
    'ContemporaryFantasy': 'Contemporary Fantasy',
    'ContemporaryRomance': 'Contemporary Romance',
    'CookingMethods': 'Cooking Methods',
    'CozyMysteries': 'Cozy Mysteries',
    'Crafts&Hobbies': 'Crafts and Hobbies',
    'CrimeMysteries': 'Crime Mysteries',
    'CyberPunk': 'Cyber Punk',
    'Design': 'Design',
    'Diet&Nutrition': 'Diet and Nutrition',
    'DomesticPolitics': 'Domestic Politics',
    'Economics': 'Economics',
    'EpicFantasy': 'Epic Fantasy',
    'Erotica': 'Erotica',
    'EspionageMysteries': 'Espionage Mysteries',
    'Exercise': 'Exercise',
    'FairyTales': 'Fairy Tales',
    'Film': 'Film',
    'FoodMemoir&Travel': 'Food Memoir and Travel',
    'Health&Reference': 'Health and Reference',
    'HistoricalFigureBiographies&Memoirs': 'Historical Figure Biographies and Memoirs',
    'HistoricalRomance': 'Historical Romance',
    'Home&Garden': 'Home and Garden',
    'Inspiration&Motivation': 'Inspiration and Motivation',
    'Language': 'Language',
    'LiteraryFigureBiographies&Memoirs': 'Literary Figure Biographies and Memoirs',
    'Management': 'Management',
    'Marketing': 'Marketing',
    'MilitaryHistory': 'Military History',
    'MilitaryScienceFiction': 'Military Science Fiction',
    'Music': 'Music',
    'NewAdultRomance': 'New Adult Romance',
    'NoirMysteries': 'Noir Mysteries',
    'ParanormalRomance': 'Paranormal Romance',
    'PerformingArts': 'Performing Arts',
    'PersonalFinance': 'Personal Finance',
    'PersonalGrowth': 'Personal Growth',
    'Philosophy': 'Philosophy',
    'Photography': 'Photography',
    'PoliticalFigureBiographies&Memoirs': 'Political Figure Biographies and Memoirs',
    'RegencyRomance': 'Regency Romance',
    'Regional&EthnicCooking': 'Regional and Ethnic Cooking',
    'Religion': 'Religion',
    'Science': 'Science',
    'SpaceOpera': 'Space Opera',
    'SpecialtyTravel': 'Specialty Travel',
    'Suspense&Thriller': 'Suspense and Thriller',
    'SuspenseRomance': 'Suspense Romance',
    'Technology': 'Technology',
    'TestPreparation': 'Test Preparation',
    'Travel:Africa': 'Travel: Africa',
    'Travel:Asia': 'Travel: Asia',
    'Travel:Australia&Oceania': 'Travel: Australia and Oceania',
    'Travel:Caribbean&Mexico': 'Travel: Caribbean and Mexico',
    'Travel:Central&SouthAmerica': 'Travel: Central and South America',
    'Travel:Europe': 'Travel: Europe',
    'Travel:MiddleEast': 'Travel: Middle East',
    'Travel:USA&Canada': 'Travel: USA and Canada',
    'TravelWriting': 'Travel Writing',
    'U.S.History': 'U.S. History',
    'UrbanFantasy': 'Urban Fantasy',
    'Weddings': 'Weddings',
    'WesternRomance': 'Western Romance',
    'Wine&Beverage': 'Wine and Beverage',
    'WorldHistory': 'World History',
    'WorldPolitics': 'World Politics',
    'Writing': 'Writing',
    '1950–PresentMilitaryHistory': '1950–Present Military History',
    '19thCenturyU.S.History': '19th Century U.S. History',
    '20thCenturyU.S.History': '20th Century U.S. History',
    '21stCenturyU.S.History': '21st Century U.S. History',
    'AfricanWorldHistory': 'African World History',
    'AncientWorldHistory': 'Ancient World History',
    'AsianWorldHistory': 'Asian World History',
    'CivilWarPeriod': 'Civil War Period',
    'Colonial/RevolutionaryPeriod': 'Colonial/Revolutionary Period',
    'EuropeanWorldHistory': 'European World History',
    'LatinAmericanWorldHistory': 'Latin American World History',
    'MiddleEasternWorldHistory': 'Middle Eastern World History',
    'NativeAmericanHistory': 'Native American History',
    'NorthAmericanWorldHistory': 'North American World History',
    'WorldWarIIMilitaryHistory': 'World War II Military History',
    'WorldWarIMilitaryHistory': 'World War I Military History'
}