#
# Created on Sun Oct 09 2022
#
# The MIT License (MIT)
# Copyright (c) 2022 Rohit Geddam, Arun Kumar, Teja Varma, Kiron Jayesh, Shandler Mason
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from base.models import Profile


WEIGHTS = {
    "gender": 0.4,
    "diet": 0.3,
    "degree": 0.1,
    "course": 0.1,
    "country": 0.1,
}


def similarity_score(gender, degree, diet, country, course):
    """Calculate the similarity score"""
    score = (
        WEIGHTS["gender"] * gender
        + WEIGHTS["diet"] * diet
        + WEIGHTS["degree"] * degree
        + WEIGHTS["country"] * country
        + WEIGHTS["course"] * course
    )

    return score


def matchings(current_user):
    """Generate matches using Manhattan Distance Algorithm"""
    user_profile = Profile.objects.get(user=current_user)
    all_profiles = Profile.objects.exclude(user=current_user)

    match_list = []
    matches = []

    for profile in all_profiles:

        gender = (
            1
            if user_profile.preference_gender == profile.gender
            or user_profile.preference_gender == profile.NO_PREF
            else 0
        )
        degree = (
            1
            if user_profile.preference_degree == profile.degree
            or user_profile.preference_degree == profile.NO_PREF
            else 0
        )
        diet = (
            1
            if user_profile.preference_diet == profile.diet
            or user_profile.preference_diet == profile.NO_PREF
            else 0
        )
        country = (
            1
            if user_profile.preference_country == profile.country
            or user_profile.preference_country == profile.NO_PREF
            else 0
        )
        course = (
            1
            if user_profile.preference_course == profile.course
            or user_profile.preference_course == profile.NO_PREF
            else 0
        )

        score = similarity_score(gender, degree, diet, country, course)

        if score > 0.5:
            match_list.append((profile, score))

    match_list.sort(key=lambda x: x[1], reverse=True)

    for m in match_list:
        matches.append(m[0])

    return matches
