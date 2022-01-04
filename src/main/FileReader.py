# In this file, write methods that read in the csv file and convert them to usable data formats
import pandas as pd

def pandas_csv_cols(path, fields):
    file = pd.read_csv(path, usecols = fields, on_bad_lines='skip', sep=';')
    return file

def pandas_csv_sbi(path):
    kvk = 'KvkNr'
    fields = ['KvkNr', 'SbiCode']
    file = pd.read_csv(path, usecols = fields, on_bad_lines='skip', encoding='cp1252', sep =';')
    return file

# Initialize paths
base_path = "C:/Users/gebruiker/Documents/Uni/Year 3/Project 3-1/Data/" #EDIT THIS TO YOUR PATH
filenames = ["AGB_instellingen", "AGB_persoon", "Algemene_info_zorginstelling", "Bezoekadres_instellingen", "BIG_AGB_Linktable_person", 
"BIG_persoon", "JMV", "KWAL_instellingen", "KWAL_persoon", "SBI_instellingen"]
extension = ".csv"

i = 0
path_list = []
for name in filenames:
    temppath = base_path + name + extension
    path_list.insert(i, temppath)
    i += 1

# Read csv to DataFrame

#TODO: get first 2 digits, link to caretype, 7 digit codes = 0+code
fields = ['KvkNr', 'AGB_Nummer_ond']
agb_inst = pandas_csv_cols(path_list[0], fields)
fields = ['KvkNr', 'AGB_Nummer_pers']
agb_persoon = pandas_csv_cols(path_list[1], fields)

fields = ['KvkNr', 'Rechtsvorm', 'WerkzamepersonenFulltime', 'WerkzamepersonenParttime', 'number_of_establishments']
algemene_info_inst = pandas_csv_cols(path_list[2], fields)

# Note: left out individual columns for specific street information, most likely will just use postcode/plaats
fields = ['KvkNr', 'PostcodecijferFysiek', 'PlaatsFysiek', 'volledigAdresFysiek']
bezoekadres_inst = pandas_csv_cols(path_list[3], fields)

fields = ['BIG_Nummer_pers', 'AGB_Nummer_pers']
big_agb_link = pandas_csv_cols(path_list[4], fields)

fields = ['KvkNr', 'BIGnr', 'DatumaanvangBIG', 'specialisatie', 'Beroep', 'Geslacht']
big_persoon = pandas_csv_cols(path_list[5], fields)

fields = ['TraderegisterNumber', 'variabel', 'waarde']
jmv = pandas_csv_cols(path_list[6], fields)

# Can most likely categorize the qualificaties by kwal_codes, have not found an easy file for this
fields = ['KvkNr', 'Kwal_code_ond', 'Kwal_Datumaanvang_ond', 'Kwalificatie_ond']
kwal_inst = pandas_csv_cols(path_list[7], fields)
fields = ['KvkNr', 'AGB_Nummer_pers', 'kwalificatie_aanvang_pers', 'kwalificatie_code_pers', 'kwalificatie']
kwal_persoon = pandas_csv_cols(path_list[8], fields)

#TODO: Just like AGB, need to create a file with the SBI Code meanings
sbi_inst = pandas_csv_sbi(path_list[9])
