def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('vova', 'ivanov',
                             city='st. petersburg',
                             language='russian',
                             couple='dasha')
print(user_profile)

