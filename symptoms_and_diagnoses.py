symptom_dictionary = {'Vertigo': r'vertigo',
                      'Headaches': r'headaches?',
                      'Lightheadedness': r'lightheadedness',
                      'Edema': r'(?<!no\s)edema',
                      'Clubbing': r'(?<!or\s)clubbing',
                      'Rales': r'(?<!no\s)rales?',
                      'Wheezing': r'(?<!or\s)wheez(e|ing)',
                      'Hypertension': r'hypertension',
                      'Dyspnea': r'dyspnea',
                      'Cough': r'cough(ing)?',
                      'Heart murmurs': r'murmurs?',
                      'Ringing in the ears': r'ringing in( the)? ears?',
                      'Shortness of breath': r'short(ening|ness|ened)( of)? breath(ing)?',
                      'Sputum production': r'sputum production|production of sputum',
                      'Pyelonephritis': r'pyelonephritis',
                      'Hemorrhagic Stroke': r'ha?emorrhagic stroke',
                      'Lumps': r'lumps?',
                      'Diabetes': r'diabet(es|ic)',
                      'Weight loss': r'weight loss|loss of weight',
                      'Foot pain': r'foot pain',
                      'Paresthesia': r'paresthesia',
                      'Foamy urine': r'foamy urine',
                      'Tingling of the feet': r'tingling of( the)? (foot|feet)',
                      'Atherosclerotic calcification': r'atherosclerotic calcification|atherosclerosis',
                      'Frequent urination': r'frequent urinati(on|ng)',
                      'Increased thirst': r'increase(d| in) thirst',
                      'Weak urinary stream': r'weak urinary stream',
                      'Chest pain': r'chest pain|pain in( the?) chest',
                      'Back pain': r'back pain|pain in( the?) back',
                      'Hemorrhage': r'ha?emorrhage',
                      'Trauma': r'trauma',
                      'Lethargy': r'letharg(y|ic)',
                      'Swollen ankles': r'(swollen|swelling (of|at)( the)?) ankles?',
                      'Palpitations': r'palpitations?',
                      'Stump pain': r'stump pain|pain (in|at) (the )?(stump|amputation site)',
                      'Discomfort with movement': r'discomfort (with|in) mov(ement|ing)',
                      'Distress': r'distress',
                      'Urinary dribbling': r'urinary (dribbling|incontinence)',
                      'Fever': r'fever',
                      'Myocardial Infarction': r'myocardial infarction|heart attack',
                      'Swelling at the amputation site': r'(swelling|swollen) (at|in )?(the )?(amputation site|stump)',
                      'Disarticulation of the right shoulder':
                          r'disarticulat(ion|ed) ((of|at|in)( the )? )?right shoulder',
                      'Erythema': r'erythem(a|ic)',
                      'Burned shoulder': r'burn(ed)? ((at|to|in) (the )?)?shoulder',
                      'Disarticulation of the right hip': r'disarticulat(ion|ed) ((of|at|in)( the )? )?right hip',
                      'Limb pain': r'limb pain|pain (in|at) (the )?limb'}

diagnosis_list = ['Hemorrhagic Stroke', 'Pyelonephritis', 'Embolic Stroke', 'Type 2 Diabetes',
                  'Chronic Congestive Heart Failure', 'Type 1 Diabetes', 'Chronic Renal Failure',
                  'Chronic Obstructive Pulmonary Disease', 'Kidney Stones', 'Hypertension', 'Acute Renal Failure',
                  'Myocardial Infarction']

lemma_dictionary = {'Vertigo': ['vertigo'],
                    'Headaches': ['headache', 'head ache', 'ache head'],
                    'Lightheadedness': ['lightheadedness', 'light head'],
                    'Edema': ['edema'],
                    'Clubbing': ['club'],
                    'Rales': ['rale', 'crackle'],
                    'Wheezing': ['wheeze', 'wheezing'],
                    'Hypertension': ['hypertension', 'blood pressure'],
                    'Dyspnea': ['dyspnea'],
                    'Cough': ['cough'],
                    'Heart murmurs': ['murmur'],
                    'Ringing in the ears': ['ring ear', 'ear ring'],
                    'Shortness of breath': ['short breath', 'shortness breath', 'shortened breath',
                                            'shortness breathing', 'shortened breathing', 'shorten breathing'],
                    'Sputum production': ['sputum produce', 'sputum production', 'production sputum',
                                          'production sputum', 'phlegm produce', 'phlegm production',
                                          'production phlegm', 'phlegm production'],
                    'Pyelonephritis': ['pyelonephritis'],
                    'Hemorrhagic Stroke': ['hemorrhagic stroke', 'haemorrhagic stroke', 'hemorrhage stroke',
                                           'haemorrhage stroke'],
                    'Lumps': ['lump'],
                    'Diabetes': ['diabetes', 'diabetic'],
                    'Weight loss': ['weight loss', 'loss weight', 'lose weight'],
                    'Foot pain': ['foot pain', 'pain foot'],
                    'Paresthesia': ['parasthesia'],
                    'Foamy urine': ['foamy urine', 'urine foamy'],
                    'Tingling of the feet': ['tingle foot', 'tingly foot', 'foot tingly', 'foot tingle'],
                    'Atherosclerotic calcification': ['atherosclerotic calcification'],
                    'Frequent urination': ['frequent urination', 'urinate frequently'],
                    'Increased thirst': ['increase thirst'],
                    'Weak urinary stream': ['weak urinary stream', 'weakened urinary stream', 'urinary stream weak',
                                            'urinary stream weakened', 'weaken urinary stream'],
                    'Chest pain': ['chest pain', 'pain chest'],
                    'Hemorrhage': ['hemorrhage', 'haemorrhage', 'bleed'],
                    'Trauma': ['trauma'],
                    'Lethargy': ['lethargy', 'lethargic', 'weary', 'weariness' 'tired', 'tiredness', 'fatigue',
                                 'fatigued'],
                    'Swollen ankles': ['swell ankle', 'ankle swell', 'swollen ankle', 'ankle swollen'],
                    'Palpitations': ['palpitate', 'palpitation'],
                    'Stump pain': ['stump pain', 'pain stump'],
                    'Discomfort with movement': ['discomfort movement', 'discomfort move', 'difficulty movement',
                                                 'difficulty move', 'move difficult', 'movement difficult'],
                    'Distress': ['distress', 'distressed'],
                    'Urinary dribbling': ['urinary dribbling', 'dribbling urine', 'urinary incontinence',
                                          'incontinence urine'],
                    'Fever': ['fever', 'feverish'],
                    'Myocardial Infarction': ['myocardial infarction', 'heart attack'],
                    'Swelling at the amputation site': ['swollen amputation site', 'swell amputation site',
                                                        'amputation site swollen'],
                    'Disarticulation of the right shoulder': ['right shoulder disarticulate',
                                                              'disarticulate right shoulder',
                                                              'disarticulation right shoulder',
                                                              'right shoulder disarticulation'],
                    'Burned shoulder': ['burn shoulder', 'shoulder burn'],
                    'Disarticulation of the right hip': ['right hip disarticulate',
                                                         'disarticulate right hip',
                                                         'disarticulation right hip',
                                                         'right hip disarticulation'],
                    'Limb pain': ['limb pain', 'pain limb'],
                    'Erythema': ['erythema', 'erythemic']
                    }
