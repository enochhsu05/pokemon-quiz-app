import sys
import pokeapi

data_to_pass_back = pokeapi.get_bst_from_pokemon(pokeapi.api_call("pokemon", "charizard"))
input = sys.argv[1]
output = data_to_pass_back
print(output)
sys.stdout.flush()
