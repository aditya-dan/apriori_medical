import spacy
import pyinflect

nlp = spacy.load('en_core_web_sm')

super_list = []

vertigo_token = nlp("vertigo")

vertigo_list = [vertigo_token[0]._.inflect('NN'), vertigo_token[0]._.inflect('NNS')]

# vertigo_list items are detected as they appear.

super_list.append(vertigo_list)

headache_token = nlp("headache")

headache_list = [headache_token[0]._.inflect('NN'), headache_token[0]._.inflect('NNS')]

# headache_list items are detected as they appear.

super_list.append(headache_list)

ache_token = nlp("ache")

pre_ache_list = [ache_token[0]._.inflect('NN'), ache_token[0]._.inflect('NNS'), ache_token[0]._.inflect('VBG')]

# pre_ache_list items appear before the word "head" with any number of non-included words between them.

super_list.append(pre_ache_list)

post_ache_list = [ache_token[0]._.inflect('NN'), ache_token[0]._.inflect('NNS'), ache_token[0]._.inflect('VBD'),
                  ache_token[0]._.inflect('VBG')]

# pre_ache_list items appear after the word "head" with any number of non-included words between them.

super_list.append(post_ache_list)

lightheadedness_list = ['lightheadedness', 'lightheaded', 'light-headedness', 'light-headed']

# lightheadedness_list items are detected as they appear.

super_list.append(lightheadedness_list)

light_list = ['light', 'lightness']

# light_list items appear before or after the word "head" with any number of non-included words between them.

super_list.append(light_list)

edema_list = ['edema', 'edemic', 'oedema', 'oedemic']

# edema_list items are detected as they appear.

super_list.append(edema_list)

clubbing_list = ['clubbing', 'clubbed', 'club']

# clubbing_list items are detected as they appear.

super_list.append(clubbing_list)

rale_token = nlp("rale")

rale_list = [rale_token[0]._.inflect('NN'), rale_token[0]._.inflect('NNS')]

# rale_list items are detected as they appear.

super_list.append(rale_list)

crackle_token = nlp("crackle")

crackle_list = [crackle_token[0]._.inflect('NN'), crackle_token[0]._.inflect('NNS'), crackle_token[0]._.inflect('VBG'),
                crackle_token[0]._.inflect('VBN')]

# crackle_list items are detected as they appear.

super_list.append(crackle_list)

wheeze_token = nlp("wheeze")

wheeze_list = [wheeze_token[0]._.inflect('NN'), wheeze_token[0]._.inflect('NNS'), wheeze_token[0]._.inflect('VBG'),
               wheeze_token[0]._.inflect('VBD')]

# wheeze_list items are detected as they appear.

super_list.append(wheeze_list)

hypertension_list = ['hypertension', 'high blood pressure']

# hypertension_list items are detected as they appear.

super_list.append(hypertension_list)

dyspnea_list = ['dyspnea', 'dyspneic', 'dyspneal', 'dyspnoea', 'dyspnoeic', 'dyspnoeal', 'breathless', 'breathlessness']

# dyspnea_list items are detected as they appear

super_list.append(dyspnea_list)

cough_token = nlp("cough")

cough_list = [cough_token[0]._.inflect('NN'), cough_token[0]._.inflect('NNS'), cough_token[0]._.inflect('VBG'),
              cough_token[0]._.inflect('VBD')]

# cough_list items are detected as they appear

super_list.append(cough_list)

murmur_list = ['murmur', 'murmurs', 'murmured', 'murmuring']

# murmur_list items are detected as they appear

super_list.append(murmur_list)

pre_ringing_list = ['ringing']

# pre_ringing_list items appear before inflections of the word "ear" with any number of non-included words between them.

super_list.append(pre_ringing_list)

post_ringing_list = ['ring', 'rings', 'ringing', 'rang', 'rung']

# post_ringing_list items appear after inflections of the word "ear" with any number of non-included words between them.

super_list.append(post_ringing_list)

ear_token = nlp("ear")

ear_list = [ear_token[0]._.inflect('NN'), ear_token[0]._.inflect('NNS')]

super_list.append(ear_list)

short_list = ['short', 'shortness', 'shortened', 'shortening']

super_list.append(short_list)

breath_token = nlp("breath")

breath_list = [breath_token[0]._.inflect('NN'), breath_token[0]._.inflect('VBG')]

super_list.append(breath_list)

pyelonephritis_list = ['pyelonephritis', 'pyelonephritic', 'pyelitis', 'pyelitic', 'pyelonephritides']

super_list.append(pyelonephritis_list)

produce_token = nlp("produce")

pre_produce_list = [produce_token[0]._.inflect('VB'), produce_token[0]._.inflect('VBD'),
                    produce_token[0]._.inflect('VBG'), produce_token[0]._.inflect('VBZ'), 'production']

# pre_produce_list items appear before sputum_list items with any number of non-included words between them.

super_list.append(pre_produce_list)

post_produce_list = [produce_token[0]._.inflect('VBD'), 'production']

# post_produce_list items appear after sputum_list items with any number of non-included words between them.

super_list.append(post_produce_list)

sputum_list = ['sputum', 'mucus', 'phlegm']

super_list.append(sputum_list)

hemorrhagic_stroke_attributive_list = ['hemorrhagic', 'haemorrhagic', 'intracerebral', 'cerebral']

super_list.append(hemorrhagic_stroke_attributive_list)

hemorrhagic_stroke_noun_list = ['stroke', 'apoplexy']

super_list.append(hemorrhagic_stroke_noun_list)

# hemorrhagic_stroke_attributive_list items appear immediately before hemorrhagic_stroke_noun_list items.

cerebral_hemorrhage_attributive_list = ['cerebral', 'intracerebral']

super_list.append(cerebral_hemorrhage_attributive_list)

cerebral_hemorrhage_noun_list = ['hemorrhage', 'haemorrhage']

# cerebral_hemorrhage_attributive_list items appear immediately before cerebral_hemorrhage_noun_list items.

super_list.append(cerebral_hemorrhage_noun_list)

lump_token = nlp("lump")

lumps_list = [lump_token[0]._.inflect('NN'), lump_token[0]._.inflect('NNS')]

# lumps_list items are detected as they appear.

super_list.append(lumps_list)

diabetes_list = ['diabetes', 'diabetic']

# diabetes_list items are detected as they appear.

super_list.append(diabetes_list)

lose_token = nlp("lose")

pre_lose_list = [lose_token[0]._.inflect('VB'), lose_token[0]._.inflect('VBG'), lose_token[0]._.inflect('VBD'), 'loss']

# pre_lose_list items appear before "weight" with any number of non-included words between them.

super_list.append(pre_lose_list)

post_lose_list = [lose_token[0]._.inflect('VBD'), 'loss']

# post_lose_list items appear after "weight" with any number of non-included words between them.

super_list.append(post_lose_list)

foot_token = nlp("foot")

foot_list = [foot_token[0]._.inflect('NN'), foot_token[0]._.inflect('NNS')]

super_list.append(foot_list)

pain_token = nlp("pain")

pre_pain_list = [pain_token[0]._.inflect('VB'), pain_token[0]._.inflect('VBG')]

# pre_pain_list items appear before foot_list items with any number of non-included words between them.

super_list.append(pre_pain_list)

post_pain_list = [pain_token[0]._.inflect('VB'), pain_token[0]._.inflect('VBD'), pain_token[0]._.inflect('VBG')]

# post_pain_list items appear after foot_list items with any number of non-included words between them.

super_list.append(post_pain_list)

hurt_token = nlp("hurt")

pre_hurt_list = [hurt_token[0]._.inflect('VB'), hurt_token[0]._.inflect('VBG')]

# pre_hurt_list items appear before foot_list items with any number of non-included words between them.

super_list.append(pre_hurt_list)

post_hurt_list = [hurt_token[0]._.inflect('VB'), hurt_token[0]._.inflect('VBD'), hurt_token[0]._.inflect('VBG')]

# post_hurt_list items appear before foot_list items with any number of non-included words between them.

super_list.append(post_hurt_list)

renal_failure_list = ['renal failure', 'kidney failure']

# renal_failure_list items are detected as they appear.

super_list.append(renal_failure_list)

foamy_token = nlp("foamy")

frothy_token = nlp("frothy")

foamy_list = [foamy_token[0]._.inflect('JJ'), foamy_token[0]._.inflect('JJR'), foamy_token[0]._.inflect('JJS'),
              frothy_token[0]._.inflect('JJ'), frothy_token[0]._.inflect('JJR'), frothy_token[0]._.inflect('JJS')]

super_list.append(foamy_list)

urine_list = ['urine', 'urination']

# foamy_list items appear before or after urine_list items with any number of non-included words between them.

super_list.append(urine_list)

tingly_token = nlp("tingly")

tingle_token = nlp("tingle")

tingly_list = [tingly_token[0]._.inflect('JJ'), tingly_token[0]._.inflect('JJR'), tingle_token[0]._.inflect('VBG')]

# tingly_list items appear before or after foot_list items with any number of non-included words between them.

super_list.append(tingly_list)

tingle_list = [tingle_token[0]._.inflect('VB'), tingle_token[0]._.inflect('VBD'), tingle_token[0]._.inflect('VBG'),
               tingle_token[0]._.inflect('VBZ')]

# tingle_list items appear after foot_list items with any number of non-included words between them.

super_list.append(tingle_list)

interval_atherosclerosis_list = ['atherosclerosis', 'arteries', 'artery', 'arterial', 'arteriosclerosis']

# interval_atherosclerosis_list items appear before or after "calcification" items with any number of non-included words between them.

super_list.append(interval_atherosclerosis_list)

consecutive_atherosclerotic_list = ['atherosclerotic', 'arterial']

# consecutive_atherosclerotic_list items appear immediately before "calcification".

super_list.append(consecutive_atherosclerotic_list)

frequent_list = ['frequent', 'frequently']

urination_list = ['urinating', 'urination', 'urinate', 'urinated']

super_list.append(urination_list)

thirst_list = ['thirst', 'thirsty', 'dehydrated', 'dehydration']

super_list.append(thirst_list)

weak_list = ['weak', 'weakened', 'weakness']

urinary_list = ['urinary', 'urine', 'urination']

super_list.append(urinary_list)

stream_list = ['stream', 'flow']

super_list.append(stream_list)

bleed_token = nlp("bleed")
hemorrhage_token = nlp("hemorrhage")
haemorrhage_token = nlp("haemorrhage")

hemorrhage_list = [hemorrhage_token[0]._.inflect('VB'), hemorrhage_token[0]._.inflect('VBD'),
                   hemorrhage_token[0]._.inflect('VBG'), hemorrhage_token[0]._.inflect('VBZ'),
                   haemorrhage_token[0]._.inflect('VB'), haemorrhage_token[0]._.inflect('VBD'),
                   haemorrhage_token[0]._.inflect('VBG'), haemorrhage_token[0]._.inflect('VBZ'),
                   bleed_token[0]._.inflect('VB'), bleed_token[0]._.inflect('VBZ'), bleed_token[0]._.inflect('VBG'),
                   bleed_token[0]._.inflect('VBN')]

super_list.append(hemorrhage_list)

lethargy_list = ['lethargy', 'lethargic', 'tired', 'tiredness', 'fatigue', 'fatigued', 'weary', 'weariness']

super_list.append(lethargy_list)

swell_list = ['swell', 'swelling', 'swollen', 'swelled']

super_list.append(swell_list)

ankle_list = ['ankle', 'ankles']

super_list.append(ankle_list)

palpitate_token = nlp("palpitate")

palpitation_token = nlp("palpitation")

palpitation_list = [palpitate_token[0]._.inflect('VB'), palpitate_token[0]._.inflect('VBD'),
                    palpitate_token[0]._.inflect('VBG'), palpitate_token[0]._.inflect('VBZ'),
                    palpitation_token[0]._.inflect('NN'), palpitation_token[0]._.inflect('NNS')]

super_list.append(palpitation_list)

distress_list = ['distress', 'distressed']

super_list.append(distress_list)

limb_list = ['limb', 'leg', 'arm', 'limbs', 'legs', 'arms']

super_list.append(limb_list)

fever_list = ['fever', 'feverish']

super_list.append(fever_list)

erythema_list = ['erythema', 'erythemic', 'erythematous']

super_list.append(erythema_list)

movement_list = ['moving', 'movement', 'motion', 'walking']

super_list.append(movement_list)

discomfort_list = ['discomfort', 'difficulty', 'difficult']

super_list.append(discomfort_list)

dribbling_list = ['dribbling', 'incontinence', 'dribble']

super_list.append(dribbling_list)

stump_list = ['site', 'stump']

super_list.append(stump_list)

disarticulate_token = nlp("disarticulate")

disarticulation_list = ['disarticulation', disarticulate_token[0]._.inflect('VB'),
                        disarticulate_token[0]._.inflect('VBG'), disarticulate_token[0]._.inflect('VBN')]

super_list.append(disarticulation_list)

burn_list = ['burn', 'burnt', 'bunred', 'burning', 'burns']

super_list.append(burn_list)

shoulder_list = ['shoulder', 'shoulders']

super_list.append(shoulder_list)

super_list.append(['amputation', 'head', 'trauma', 'hip', 'paresthesia'])

