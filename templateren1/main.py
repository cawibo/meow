#Input: Den första raden innehåller ett heltal N, antalet kommandon.Därefter följer N kommandon.Det finns tre olika kommandon:

#Output: Ditt program ska skriva ut resultatet av alla render-kommandon.

import sys, json, string

contexts = {}
templates = {}

n = int(sys.stdin.readline())
for _ in range(n):
	command, id, rows = sys.stdin.readline().split()

	if command == "load_context":
		contexts[id] = json.loads("".join([sys.stdin.readline() for _ in range(int(rows))]))

	if command == "load_template":

		template = []
		for _ in range((int(rows))):
			line = sys.stdin.readline()
			line = line.replace("{{ put ", "$")
			line = line.replace(" }}", "")
			template.append(line)

		templates[id] = "".join(template)

	if command == "render":
		print(templates[id])
		ctx_id = rows

		template = templates[id]
		context = contexts[ctx_id]

		print(string.Template(template).substitute(context))



		

print(contexts)