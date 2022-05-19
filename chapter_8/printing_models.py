unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_designs = []

#while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print("I am working on " + current_design + " design now!")
#    completed_designs.append(current_design)
    
#print("\nThe following models're completed!")
#for c_d in completed_designs:
#    print(c_d)


def print_models(unprinted_designs, completed_designs):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("I am working on " + current_design + " design now!")
        completed_designs.append(current_design)
        
        
def show_completed_models(completed_designs):
    print("\nThe following models're completed!")
    for model in completed_designs:
        print(model)
        
print_models(unprinted_designs[:], completed_designs)
show_completed_models(completed_designs)
print(unprinted_designs)
