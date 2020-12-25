# Profile

def build_profile(first, last, **user_info):
    """   Build user profile """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('steve', 'drozdov', age=28, city='moscow', location='mititshi')
print(user_profile)
