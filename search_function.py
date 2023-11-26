from inflections import *
from itertools import product
from pandas.core.common import flatten

super_set = set(flatten(super_list))


def interval_checker(list_a, list_b, list_c):
    return any(a < b and not any((a < x < b) for x in list_c) for (a, b) in product(list_a, list_b))


def interval_three_checker(list_a, list_b, list_c, list_d):
    return any(a < b < c and not any((a < x < b) or (b < x < c) for x in list_d) for (a, b, c) in
               product(list_a, list_b, list_c))


def consecutive_checker(list_a, list_b):
    return any(a == b-1 for (a, b) in product(list_a, list_b))


def consecutive_interval_checker(list_a, list_b, list_c, list_d):
    return any((a == b-1) and interval_checker(list_b, list_c, list_d) for (a, b) in product(list_a, list_b))


def interval_consecutive_checker(list_a, list_b, list_c, list_d):
    return any((b == c-1) and interval_checker(list_a, list_b, list_d) for (b, c) in product(list_b, list_c))


class SymptomFinder:
    def __init__(self, symptom_name, keyword_list, external_function):
        self.symptom_name = symptom_name
        self.keyword_list = keyword_list
        self.external_function = external_function

    def symptom_checker(self, word_list):
        if set(word_list) & set(self.keyword_list):
            return self.external_function(word_list)
        return False


object_list = []


def vertigo_function(word_list):
    for word in word_list:
        if word in vertigo_list:
            return True
    return False


vertigo_object = SymptomFinder('Vertigo', set(vertigo_list), vertigo_function)
object_list.append(vertigo_object)


def headache_function(word_list):
    pre_ache_positions = []
    post_ache_positions = []
    other_positions = []
    head_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in headache_list:
            return True

        elif word_list[counter] in set(pre_ache_list).union(set(post_ache_list)):
            if word_list[counter] in pre_ache_list:
                pre_ache_positions.append(counter)
            if word_list[counter] in post_ache_list:
                post_ache_positions.append(counter)

        elif word_list[counter] == "head":
            head_positions.append(counter)

        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(pre_ache_positions, head_positions, other_positions):
        return True
    elif interval_checker(head_positions, post_ache_positions, other_positions):
        return True

    return False


headache_object = SymptomFinder('Headaches', set(headache_list + pre_ache_list + post_ache_list + ["head"]),
                                headache_function)
object_list.append(headache_object)


def lightheadedness_function(word_list):
    light_positions = []
    head_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in lightheadedness_list:
            return True
        elif word_list[counter] in light_list:
            light_positions.append(counter)
        elif word_list[counter] == "head":
            head_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(light_positions, head_positions, other_positions):
        return True
    elif interval_checker(head_positions, light_positions, other_positions):
        return True

    return False


lightheadedness_object = SymptomFinder('Lightheadedness', set(lightheadedness_list + light_list + ['head']),
                                       lightheadedness_function)
object_list.append(lightheadedness_object)


def edema_function(word_list):
    for word in word_list:
        if word in edema_list:
            return True
    return False


edema_object = SymptomFinder('Edema', set(edema_list), edema_function)
object_list.append(edema_object)


def clubbing_function(word_list):
    for word in word_list:
        if word in clubbing_list:
            return True
    return False


clubbing_object = SymptomFinder('Clubbing', set(clubbing_list), clubbing_function)
object_list.append(clubbing_object)


def rales_function(word_list):
    for word in word_list:
        if word in rale_list:
            return True
        elif word in crackle_list:
            return True
    return False


rales_object = SymptomFinder('Rales', set(rale_list), rales_function)
object_list.append(rales_object)


def wheezing_function(word_list):
    for word in word_list:
        if word in wheeze_list:
            return True
    return False


wheezing_object = SymptomFinder('Wheezing', set(wheeze_list), wheezing_function)
object_list.append(wheezing_object)


def hypertension_function(word_list):
    for word in word_list:
        if word in hypertension_list:
            return True
    return False


hypertension_object = SymptomFinder('Hypertension', set(hypertension_list), hypertension_function)
object_list.append(hypertension_object)


def dyspnea_function(word_list):
    for word in word_list:
        if word in dyspnea_list:
            return True
    return False


dyspnea_object = SymptomFinder('Dyspnea', set(dyspnea_list), dyspnea_function)
object_list.append(dyspnea_object)


def cough_function(word_list):
    for word in word_list:
        if word in cough_list:
            return True
    return False


cough_object = SymptomFinder('Cough', set(cough_list), cough_function)
object_list.append(cough_object)


def murmur_function(word_list):
    for word in word_list:
        if word in murmur_list:
            return True
    return False


murmur_object = SymptomFinder('Heart murmurs', set(murmur_list), murmur_function)
object_list.append(murmur_object)


def ringing_in_ears_function(word_list):
    pre_ringing_positions = []
    post_ringing_positions = []
    ear_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in set(pre_ringing_list).union(set(post_ringing_list)):
            if word_list[counter] in pre_ringing_list:
                pre_ringing_positions.append(counter)
            if word_list[counter] in post_ringing_list:
                post_ringing_positions.append(counter)

        elif word_list[counter] in ear_list:
            ear_positions.append(counter)

        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(pre_ringing_positions, ear_positions, other_positions):
        return True
    elif interval_checker(ear_positions, post_ringing_positions, other_positions):
        return True

    return False


ringing_ear_object = SymptomFinder('Ringing in the ears', set(pre_ringing_list + post_ringing_list + ear_list),
                                   ringing_in_ears_function)
object_list.append(ringing_ear_object)


def short_breath_function(word_list):
    breath_positions = []
    short_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in breath_list:
            breath_positions.append(counter)
        elif word_list[counter] in short_list:
            short_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(breath_positions, short_positions, other_positions):
        return True
    elif interval_checker(short_positions, breath_positions, other_positions):
        return True

    return False


short_breath_object = SymptomFinder('Shortness of breath', set(breath_list + short_list), short_breath_function)
object_list.append(short_breath_object)


def pyelonephritis_function(word_list):
    for word in word_list:
        if word in pyelonephritis_list:
            return True
    return False


pyelonephritis_object = SymptomFinder('Pyelonephritis', set(pyelonephritis_list), pyelonephritis_function)
object_list.append(pyelonephritis_object)


def sputum_production_function(word_list):
    pre_produce_positions = []
    sputum_positions = []
    post_produce_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in set(pre_produce_list).union(set(post_produce_list)):
            if word_list[counter] in pre_produce_list:
                pre_produce_positions.append(counter)
            if word_list[counter] in post_produce_list:
                post_produce_positions.append(counter)

        elif word_list[counter] in sputum_list:
            sputum_positions.append(counter)

        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(pre_produce_positions, sputum_positions, other_positions):
        return True
    elif interval_checker(sputum_positions, post_produce_positions, other_positions):
        return True

    return False


sputum_production_object = SymptomFinder('Sputum production', set(pre_produce_list + post_produce_list + sputum_list),
                                         sputum_production_function)
object_list.append(sputum_production_object)


def hemorrhagic_stroke_function(word_list):
    hemorrhagic_stroke_attributive_positions = []
    cerebral_hemorrhage_attributive_positions = []
    hemorrhagic_stroke_noun_positions = []
    cerebral_hemorrhage_noun_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in \
                set(hemorrhagic_stroke_attributive_list).union(set(cerebral_hemorrhage_attributive_list)):
            if word_list[counter] in hemorrhagic_stroke_attributive_list:
                hemorrhagic_stroke_attributive_positions.append(counter)
            if word_list[counter] in cerebral_hemorrhage_attributive_list:
                cerebral_hemorrhage_attributive_positions.append(counter)

        elif word_list[counter] in hemorrhagic_stroke_noun_list:
            hemorrhagic_stroke_noun_positions.append(counter)

        elif word_list[counter] in cerebral_hemorrhage_noun_list:
            cerebral_hemorrhage_noun_positions.append(counter)

    if consecutive_checker(hemorrhagic_stroke_attributive_positions, hemorrhagic_stroke_noun_positions):
        return True
    elif consecutive_checker(cerebral_hemorrhage_attributive_positions, cerebral_hemorrhage_noun_positions):
        return True

    return False


hemorrhagic_stroke_object = SymptomFinder('Hemorrhagic Stroke', set(hemorrhagic_stroke_attributive_list +
                                                                    cerebral_hemorrhage_attributive_list +
                                                                    hemorrhagic_stroke_noun_list +
                                                                    cerebral_hemorrhage_noun_list),
                                          hemorrhagic_stroke_function)
object_list.append(hemorrhagic_stroke_object)


def lump_function(word_list):
    for word in word_list:
        if word in lumps_list:
            return True
    return False


lump_object = SymptomFinder('Lumps', set(lumps_list), lump_function)
object_list.append(lump_object)


def diabetes_function(word_list):
    for word in word_list:
        if word in diabetes_list:
            return True
    return False


diabetes_object = SymptomFinder('Diabetes', set(diabetes_list), diabetes_function)
object_list.append(diabetes_object)


def weight_loss_function(word_list):
    pre_lose_positions = []
    post_lose_positions = []
    weight_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in set(pre_lose_list).union(set(post_lose_list)):
            if word_list[counter] in pre_lose_list:
                pre_lose_positions.append(counter)
            if word_list[counter] in post_lose_list:
                post_lose_positions.append(counter)

        elif word_list[counter] == "weight":
            weight_positions.append(counter)

        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(pre_lose_positions, weight_positions, other_positions):
        return True
    elif interval_checker(weight_positions, post_lose_positions, other_positions):
        return True

    return False


weight_loss_object = SymptomFinder('Weight loss', set(pre_lose_list + post_lose_list + ['weight']),
                                   weight_loss_function)
object_list.append(weight_loss_object)


def foot_pain_function(word_list):
    foot_positions = []
    pre_pain_positions = []
    post_pain_positions = []
    pre_hurt_positions = []
    post_hurt_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in foot_list:
            foot_positions.append(counter)

        elif word_list[counter] in set(pre_pain_list).union(set(post_pain_list)):
            if word_list[counter] in pre_pain_list:
                pre_pain_positions.append(counter)
            if word_list[counter] in post_pain_list:
                post_pain_positions.append(counter)

        elif word_list[counter] in set(pre_hurt_list).union(set(post_hurt_list)):
            if word_list[counter] in pre_hurt_list:
                pre_hurt_positions.append(counter)
            if word_list[counter] in post_hurt_list:
                post_hurt_positions.append(counter)

        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(pre_pain_positions, foot_positions, other_positions):
        return True
    elif interval_checker(foot_positions, post_pain_positions, other_positions):
        return True
    elif interval_checker(pre_hurt_positions, foot_positions, other_positions):
        return True
    elif interval_checker(foot_positions, post_hurt_positions, other_positions):
        return True

    return False


foot_pain_object = SymptomFinder('Foot pain', set(pre_pain_list + post_pain_list + foot_list), foot_pain_function)
object_list.append(foot_pain_object)


def foamy_urine_function(word_list):
    foamy_positions = []
    urine_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in foamy_list:
            foamy_positions.append(counter)
        elif word_list[counter] in urine_list:
            urine_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(foamy_positions, urine_positions, other_positions):
        return True
    elif interval_checker(urine_positions, foamy_positions, other_positions):
        return True

    return False


foamy_urine_object = SymptomFinder('Foamy urine', set(foamy_list + urine_list), foamy_urine_function)
object_list.append(foamy_urine_object)


def tingly_feet_function(word_list):
    foot_positions = []
    tingle_positions = []
    tingly_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in foot_list:
            foot_positions.append(counter)

        elif word_list[counter] in set(tingle_list).union(set(tingly_list)):
            if word_list[counter] in tingle_list:
                tingle_positions.append(counter)
            elif word_list[counter] in tingly_list:
                tingly_positions.append(counter)

        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(foot_positions, tingly_positions, other_positions):
        return True
    elif interval_checker(tingly_positions, foot_positions, other_positions):
        return True
    elif interval_checker(foot_positions, tingle_positions, other_positions):
        return True

    return False


tingly_feet_object = SymptomFinder('Tingling of the feet', set(foot_list + tingle_list + tingly_list),
                                   tingly_feet_function)
object_list.append(tingly_feet_object)


def atherosclerotic_calcification_function(word_list):
    consecutive_atherosclerotic_positions = []
    interval_atherosclerosis_positions = []
    calcification_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] == "calcification":
            calcification_positions.append(counter)

        elif word_list[counter] in set(consecutive_atherosclerotic_list).union(set(interval_atherosclerosis_list)):
            if word_list[counter] in consecutive_atherosclerotic_list:
                consecutive_atherosclerotic_positions.append(counter)
            if word_list[counter] in interval_atherosclerosis_list:
                interval_atherosclerosis_positions.append(counter)

        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(interval_atherosclerosis_positions, calcification_positions, other_positions):
        return True
    elif interval_checker(calcification_positions, interval_atherosclerosis_positions, other_positions):
        return True
    elif consecutive_checker(consecutive_atherosclerotic_positions, calcification_positions):
        return True

    return False


atherosclerotic_calcification_object = SymptomFinder('Atherosclerotic calcification', set(consecutive_atherosclerotic_list + interval_atherosclerosis_list + ["calcification"]), atherosclerotic_calcification_function)
object_list.append(atherosclerotic_calcification_object)


def frequent_urination_function(word_list):
    frequent_positions = []
    urination_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in frequent_list:
            frequent_positions.append(counter)
        elif word_list[counter] in urination_list:
            urination_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(frequent_positions, urination_positions, other_positions):
        return True
    elif interval_checker(urination_positions, frequent_positions, other_positions):
        return True

    return False


frequent_urination_object = SymptomFinder('Frequent urination', set(frequent_list + urination_list),
                                          frequent_urination_function)
object_list.append(frequent_urination_object)


def increased_thirst_function(word_list):
    for word in word_list:
        if word in thirst_list:
            return True
    return False


increased_thirst_object = SymptomFinder('Increased thirst', set(thirst_list), increased_thirst_function)
object_list.append(increased_thirst_object)


def weakened_urinary_stream_function(word_list):
    weak_positions = []
    urinary_positions = []
    stream_positions = []
    other_positions = []

    for counter in range(0, (len(word_list))):
        if word_list[counter] in weak_list:
            weak_positions.append(counter)
        elif word_list[counter] in urinary_list:
            urinary_positions.append(counter)
        elif word_list[counter] in stream_list:
            stream_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_three_checker(weak_positions, urinary_positions, stream_positions, other_positions):
        return True
    elif interval_three_checker(weak_positions, stream_positions, urinary_positions, other_positions):
        return True
    elif interval_three_checker(stream_positions, urinary_positions, weak_positions, other_positions):
        return True
    elif interval_three_checker(urinary_positions, stream_positions, weak_positions, other_positions):
        return True
    return False


weakened_urinary_stream_object = SymptomFinder('Weak urinary stream', set(weak_list + urinary_list + stream_list),
                                               weakened_urinary_stream_function)
object_list.append(weakened_urinary_stream_object)


def chest_pain_function(word_list):
    chest_positions = []
    pre_pain_positions = []
    post_pain_positions = []
    pre_hurt_positions = []
    post_hurt_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] == "chest":
            chest_positions.append(counter)
        elif word_list[counter] in set(pre_pain_list).union(set(post_pain_list)):
            if word_list[counter] in pre_pain_list:
                pre_pain_positions.append(counter)
            if word_list[counter] in post_pain_list:
                post_pain_positions.append(counter)
        elif word_list[counter] in set(pre_hurt_list).union(set(post_hurt_list)):
            if word_list[counter] in pre_hurt_list:
                pre_hurt_positions.append(counter)
            if word_list[counter] in post_hurt_list:
                post_hurt_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(pre_pain_positions, chest_positions, other_positions):
        return True
    elif interval_checker(chest_positions, post_pain_positions, other_positions):
        return True
    elif interval_checker(pre_hurt_positions, chest_positions, other_positions):
        return True
    elif interval_checker(chest_positions, post_hurt_positions, other_positions):
        return True
    return False


chest_pain_object = SymptomFinder('Chest pain', set(pre_pain_list + post_pain_list + pre_hurt_list + post_hurt_list +
                                                    ['chest']), chest_pain_function)
object_list.append(chest_pain_object)


def back_pain_function(word_list):
    back_positions = []
    pre_pain_positions = []
    post_pain_positions = []
    pre_hurt_positions = []
    post_hurt_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] == "back":
            back_positions.append(counter)
        elif word_list[counter] in set(pre_pain_list).union(set(post_pain_list)):
            if word_list[counter] in pre_pain_list:
                pre_pain_positions.append(counter)
            if word_list[counter] in post_pain_list:
                post_pain_positions.append(counter)
        elif word_list[counter] in set(pre_hurt_list).union(set(post_hurt_list)):
            if word_list[counter] in pre_hurt_list:
                pre_hurt_positions.append(counter)
            if word_list[counter] in post_hurt_list:
                post_hurt_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(pre_pain_positions, back_positions, other_positions):
        return True
    elif interval_checker(back_positions, post_pain_positions, other_positions):
        return True
    elif interval_checker(pre_hurt_positions, back_positions, other_positions):
        return True
    elif interval_checker(back_positions, post_hurt_positions, other_positions):
        return True
    return False


back_pain_object = SymptomFinder('Back pain', set(pre_pain_list + post_pain_list + pre_hurt_list + post_hurt_list +
                                                  ['back']), back_pain_function)
object_list.append(back_pain_object)


def hemorrhage_function(word_list):
    for word in word_list:
        if word in hemorrhage_list:
            return True
    return False


hemorrhage_object = SymptomFinder('Hemorrhage', set(hemorrhage_list), hemorrhage_function)
object_list.append(hemorrhage_object)


def trauma_function(word_list):
    for word in word_list:
        if word == "trauma":
            return True
    return False


trauma_object = SymptomFinder('Trauma', {'trauma'}, trauma_function)
object_list.append(trauma_object)


def lethargy_function(word_list):
    for word in word_list:
        if word in lethargy_list:
            return True
    return False


lethargy_object = SymptomFinder('Lethargy', set(lethargy_list), lethargy_function)
object_list.append(lethargy_object)


def swollen_ankles_function(word_list):
    swell_positions = []
    ankle_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in swell_list:
            swell_positions.append(counter)
        elif word_list[counter] in ankle_list:
            ankle_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(swell_positions, ankle_positions, other_positions):
        return True
    elif interval_checker(ankle_positions, swell_positions, other_positions):
        return True
    return False


swollen_ankles_object = SymptomFinder('Swollen ankles', set(swell_list + ankle_list), swollen_ankles_function)
object_list.append(swollen_ankles_object)


def palpitation_function(word_list):
    for word in word_list:
        if word in palpitation_list:
            return True
    return False


palpitation_object = SymptomFinder('Palpitations', set(palpitation_list), palpitation_function)
object_list.append(palpitation_object)


def distress_function(word_list):
    for word in word_list:
        if word in distress_list:
            return True
    return False


distress_object = SymptomFinder('Distress', set(distress_list), distress_function)
object_list.append(distress_object)


def stump_pain_function(word_list):
    stump_positions = []
    pre_pain_positions = []
    post_pain_positions = []
    pre_hurt_positions = []
    post_hurt_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] == "stump":
            stump_positions.append(counter)
        elif word_list[counter] in set(pre_pain_list).union(set(post_pain_list)):
            if word_list[counter] in pre_pain_list:
                pre_pain_positions.append(counter)
            if word_list[counter] in post_pain_list:
                post_pain_positions.append(counter)
        elif word_list[counter] in set(pre_hurt_list).union(set(post_hurt_list)):
            if word_list[counter] in pre_hurt_list:
                pre_hurt_positions.append(counter)
            if word_list[counter] in post_hurt_list:
                post_hurt_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(pre_pain_positions, stump_positions, other_positions):
        return True
    elif interval_checker(stump_positions, post_pain_positions, other_positions):
        return True
    elif interval_checker(pre_hurt_positions, stump_positions, other_positions):
        return True
    elif interval_checker(stump_positions, post_hurt_positions, other_positions):
        return True
    return False


stump_pain_object = SymptomFinder('Stump pain', set(['stump'] + pre_pain_list + pre_hurt_list +
                                                    post_pain_list + post_hurt_list), stump_pain_function)
object_list.append(stump_pain_object)


def limb_pain_function(word_list):
    limb_positions = []
    pre_pain_positions = []
    post_pain_positions = []
    pre_hurt_positions = []
    post_hurt_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in limb_list:
            limb_positions.append(counter)
        elif word_list[counter] in set(pre_pain_list).union(set(post_pain_list)):
            if word_list[counter] in pre_pain_list:
                pre_pain_positions.append(counter)
            if word_list[counter] in post_pain_list:
                post_pain_positions.append(counter)
        elif word_list[counter] in set(pre_hurt_list).union(set(post_hurt_list)):
            if word_list[counter] in pre_hurt_list:
                pre_hurt_positions.append(counter)
            if word_list[counter] in post_hurt_list:
                post_hurt_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(pre_pain_positions, limb_positions, other_positions):
        return True
    elif interval_checker(limb_positions, post_pain_positions, other_positions):
        return True
    elif interval_checker(pre_hurt_positions, limb_positions, other_positions):
        return True
    elif interval_checker(limb_positions, post_hurt_positions, other_positions):
        return True
    return False


limb_pain_object = SymptomFinder('Limb pain', set(limb_list + pre_pain_list + pre_hurt_list + post_pain_list +
                                                  post_hurt_list), limb_pain_function)
object_list.append(limb_pain_object)


def fever_function(word_list):
    for word in word_list:
        if word in fever_list:
            return True
    return False


fever_object = SymptomFinder('Fever', set(fever_list), fever_function)
object_list.append(fever_object)


def erythema_function(word_list):
    for word in word_list:
        if word in erythema_list:
            return True
    return False


erythema_object = SymptomFinder('Erythema', erythema_list, erythema_function)
object_list.append(erythema_object)


def discomfort_movement_function(word_list):
    discomfort_positions = []
    movement_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] in discomfort_list:
            discomfort_positions.append(counter)
        elif word_list[counter] in movement_list:
            movement_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(discomfort_positions, movement_positions, other_positions):
        return True
    elif interval_checker(movement_positions, discomfort_positions, other_positions):
        return True
    return False


discomfort_movement_object = SymptomFinder('Discomfort with movement', set(discomfort_list + movement_list),
                                           discomfort_movement_function)
object_list.append(discomfort_movement_object)


def urinary_dribbling_function(word_list):
    urinary_positions = []
    dribbling_positions = []
    other_positions = []
    local_urinary_list = urinary_list + ['urinating', 'urinate']

    for counter in range(0, len(word_list)):
        if word_list[counter] in local_urinary_list:
            urinary_positions.append(counter)
        elif word_list[counter] in dribbling_list:
            dribbling_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(urinary_positions, dribbling_positions, other_positions):
        return True
    elif interval_checker(dribbling_positions, urinary_positions, other_positions):
        return True
    return False


urinary_dribbling_object = SymptomFinder('Urinary dribbling', set(urinary_list + ['urinating', 'urinate'] +
                                                                  dribbling_list), urinary_dribbling_function)
object_list.append(urinary_dribbling_object)


def myocardial_infarction_function(word_list):
    for counter in range(0, len(word_list)):
        if counter < len(word_list) - 1:
            if word_list[counter] == "heart" and word_list[counter + 1] == "attack":
                return True
            elif word_list[counter] == "myocardial" and word_list[counter + 1] == "infarction":
                return True
            elif word_list[counter] == "cardiac" and word_list[counter + 1] == "arrest":
                return True
    return False


myocardial_infarction_object = SymptomFinder('Myocardial Infarction', {'heart', 'attack', 'myocardial', 'infarction', 'cardiac', 'arrest'}, myocardial_infarction_function)
object_list.append(myocardial_infarction_object)


def swelling_amputation_site_function(word_list):
    amputation_positions = []
    swelling_positions = []
    stump_positions = []
    other_positions = []

    for counter in range(0, len(word_list)):
        if word_list[counter] == "amputation":
            amputation_positions.append(counter)
        elif word_list[counter] in swell_list:
            swelling_positions.append(counter)
        elif word_list[counter] in stump_list:
            stump_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if consecutive_interval_checker(amputation_positions, stump_positions, swelling_positions, other_positions):
        return True
    elif consecutive_interval_checker(stump_positions, amputation_positions, swelling_positions, other_positions):
        return True
    elif interval_consecutive_checker(swelling_positions, amputation_positions, stump_positions, other_positions):
        return True
    elif interval_consecutive_checker(swelling_positions, stump_positions, amputation_positions, other_positions):
        return True

    return False


swelling_amputation_site_object = SymptomFinder('Swelling at the amputation site',
                                                set(['amputation'] + swell_list + stump_list),
                                                swelling_amputation_site_function)
object_list.append(swelling_amputation_site_object)


def disarticulation_right_shoulder(word_list):
    disarticulation_positions = []
    right_positions = []
    shoulder_positions = []
    other_positions = []
    for counter in range(0, len(word_list)):
        if word_list[counter] in disarticulation_list:
            disarticulation_positions.append(counter)
        elif word_list[counter] == "right":
            right_positions.append(counter)
        elif word_list[counter] == "shoulder":
            shoulder_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if consecutive_interval_checker(right_positions, shoulder_positions, disarticulation_positions, other_positions):
        return True
    elif interval_consecutive_checker(disarticulation_positions, right_positions, shoulder_positions, other_positions):
        return True
    return False


disarticulation_right_shoulder_object = SymptomFinder('Disarticulation of the right shoulder',
                                                      set(disarticulation_list + ["right", "shoulder"]),
                                                      disarticulation_right_shoulder)
object_list.append(disarticulation_right_shoulder_object)


def burn_shoulder_function(word_list):
    burn_positions = []
    shoulder_positions = []
    other_positions = []
    for counter in range(0, len(word_list)):
        if word_list[counter] in burn_list:
            burn_positions.append(counter)
        elif word_list[counter] in shoulder_list:
            shoulder_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if interval_checker(burn_positions, shoulder_positions, other_positions):
        return True
    elif interval_checker(shoulder_positions, burn_positions, other_positions):
        return True
    return False


burn_shoulder_object = SymptomFinder('Burned shoulder', set(burn_list + shoulder_list), burn_shoulder_function)
object_list.append(burn_shoulder_object)


def disarticulation_right_hip(word_list):
    disarticulation_positions = []
    right_positions = []
    hip_positions = []
    other_positions = []
    for counter in range(0, len(word_list)):
        if word_list[counter] in disarticulation_list:
            disarticulation_positions.append(counter)
        elif word_list[counter] == "right":
            right_positions.append(counter)
        elif word_list[counter] == "hip":
            hip_positions.append(counter)
        elif word_list[counter] in super_set:
            other_positions.append(counter)

    if consecutive_interval_checker(right_positions, hip_positions, disarticulation_positions, other_positions):
        return True
    elif interval_consecutive_checker(disarticulation_positions, right_positions, hip_positions, other_positions):
        return True
    return False


disarticulation_right_hip_object = SymptomFinder('Disarticulation of the right hip',
                                                 set(disarticulation_list + ["right", "hip"]),
                                                 disarticulation_right_hip)
object_list.append(disarticulation_right_hip_object)


def paresthesia_function(word_list):
    for word in word_list:
        if word == "paresthesia":
            return True
    return False


paresthesia_object = SymptomFinder('Paresthesia', {'paresthesia'}, paresthesia_function)
object_list.append(paresthesia_object)


def search_function(word_list):
    symptom_list = []
    for symptom_object in object_list:
        if symptom_object.symptom_checker(word_list):
            symptom_list.append(symptom_object.symptom_name)
    return set(symptom_list)

