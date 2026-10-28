from pyscript import document
def result_checker(e):
 club_members = ['Simon Malimbum', 'Lucas Blas', 'Dylan Cascalla', 'Matteo Ressurreccio', 'Peter Navarro', 'David Barretto', 'Qody Omengan', 'Andrew Barretto', 'Xander Espinosa', 'Lucas Flores', ' Adam Villarica', 'Gurvinder Virk', 'Joaquin Pascua', 'Bhavik Aku']
 f_name = document.getElementById('first_name').value
 l_name = document.getElementById('last_name').value
 candidate = f_name + ' ' + l_name
 member_checker = candidate.lower() in [member.lower() for member in club_members]
 messages = (f'Sorry {candidate}, your name is not on the list.', f'Congratulations {candidate}! You are now a part of the ICT club.')
 document.getElementById('output').innerHTML = messages[member_checker]