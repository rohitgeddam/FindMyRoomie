def check_ncsu_email(email):
    parts = email.split("@")
    if parts[-1] != "ncsu.edu":
        return False
    return True
