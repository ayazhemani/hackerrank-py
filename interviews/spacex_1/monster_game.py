import argparse, csv
from pprint import pprint


def main():
    parser = argparse.ArgumentParser(description='Print a Monster registry report.')
    # Accept 2 inputs: path to CSV file (known_monster_db) and monster_name
    monster_db_filename = None
    monster_name = None
    parser.add_argument('monster_db_filename', type=str,
                    help='a file path to the csv monster database')
    parser.add_argument('monster_name', type=str,
                    help='the monster name selected to display attributes')
    args = parser.parse_args()
    # Provide 3 outputs: stronger monsters, weaker monsters, evolution chart
    db = Database(args.monster_db_filename)

    #Find target monster
    target = None
    for monster_id in db.collection:
        monster = db.collection[monster_id]
        if monster.name.lower() == args.monster_name.lower():
            target = monster

    for strength in target.types:
        for monster_id in db.collection:
            monster = db.collection[monster_id]
            if strength in monster.weaknesses:
                target.strong.add(monster.name)

    for weakness in target.weaknesses:
        for monster_id in db.collection:
            monster = db.collection[monster_id]
            if weakness in monster.types:
                target.weak.add(monster.name)

    target.print()


class Monster():
    def __init__(self, Id=None, name=None, types=None, weaknesses=None, evolution=None):
        self.id = int(Id) if Id is not None else None
        self.name = name
        self.types = types
        self.weaknesses = weaknesses
        self.evolution = evolution

        self.evo_str=set()
        self.strong= set()
        self.weak = set()

    def print(self):
        id_output = f'{self.id:03d}'
        strong_output = '\n    '.join(self.strong) if len(self.strong) > 0 else "None"
        weak_output = '\n    '.join(self.weak) if len(self.weak) > 0 else "None"
        evolution_output = '\n    '.join(self.evo_str) if len(self.evo_str) > 0 else "None"
        evolution_output = evolution_output if self.evolution else "None"

        print("ID:", end='\n    ')
        print(id_output)
        print("Strong against:", end='\n    ')
        print(strong_output)
        print("Weak against:", end='\n    ')
        print(weak_output)
        print("Evolution:", end='\n    ')
        print(evolution_output, end='\n\n')

class Database():
    # First row of CSV contains column header mapping
    # All following rows contain monster data:
    #   * id, name, types, weaknesses, evolution (id reference)
    #   * types, weaknesses, evolution data can all contain multiple fields
    def __init__(self, filename=None):
        self.filename = filename
        self.collection = dict()
        dictionary = dict()

        csv_id_index = None
        #populate data into dictionary from csv
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for monster in reader:
                dictionary[int(monster['ID'])] = dict()
                dictionary[int(monster['ID'])]['name'] = monster['Name']
                dictionary[int(monster['ID'])]['type'] = monster['Types'].split(',')
                dictionary[int(monster['ID'])]['weak'] = monster['Weaknesses'].split(',')
                dictionary[int(monster['ID'])]['evolution'] = monster['Evolution'].split(',')

                for attrib in dictionary[int(monster['ID'])]:
                    if dictionary[int(monster['ID'])][attrib] == ['']:
                        dictionary[int(monster['ID'])][attrib] = None

                dictionary[int(monster['ID'])]['evolution'] = None if \
                    dictionary[int(monster['ID'])]['evolution'] is None else\
                    [int(x) for x in dictionary[int(monster['ID'])]['evolution'] ]

        #populate data into collection from dictionary
        for monster_id in dictionary:
            monster = dictionary[monster_id]
            temp_monster = Monster(monster_id, monster['name'], monster['type'], monster['weak'], monster['evolution'])
            self.collection[monster_id] = temp_monster

        #Get evolution mapping
        for monster_id in self.collection:
            monster = self.collection[monster_id]
            full_evo_maps = []
            evo_maps = [[monster]]
            while len(evo_maps) > 0 and evo_maps[0] is not None:
                for evo_map in evo_maps:
                    next_monster = evo_map[-1]
                    if (next_monster.evolution):
                        for this_evolution_id in next_monster.evolution:
                            this_evolution = self.collection[this_evolution_id]
                            temp_map = evo_map.copy()
                            temp_map.append(this_evolution)
                            evo_maps.append(temp_map)
                    else:
                        full_evo_maps.append(evo_map)
                    evo_maps.remove(evo_map)
            #Convert monster list to names
            for evomap in full_evo_maps:
                monster.evo_str.add(' > '.join([m.name for m in evomap]) )

    def print(self):
        #pprint(dictionary)
        for item in self.collection:
            pprint(self.collection[item].__dict__)


if __name__ == '__main__':
    main()
