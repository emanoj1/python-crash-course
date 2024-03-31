# Move from 1 list to another using Functions

def printing_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_designs = unprinted_designs.pop()
        print(f"Printing design - {current_designs}")
        completed_models.append(current_designs)

def show_completed_designs(completed_models):
    print("\nThe following are printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 't-shirt', 'sticker']
completed_models = []

printing_models(unprinted_designs, completed_models)
show_completed_designs(completed_models)