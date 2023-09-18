import requests
import json


class GetPrograms:
    def get_programs(self):
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        response = requests.get(URL)
        return response.content

    def program_school(self):
        programs_list = []
        programs = json.loads(self.get_programs())
        for program in programs:
            programs_list.append(program["agency"])
        return programs_list


# programs = GetPrograms().get_programs()
# print(programs)

programs = GetPrograms()
program_schools = programs.program_school()

program_schools_set = set(program_schools)
for school in program_schools_set:
    print(school)
