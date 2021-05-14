import pandas as pd
import googletrans
from googletrans import Translator
import time

def translate_columns(df):
    translator = Translator(service_urls=['translate.googleapis.com'])

    trans_df = df.copy()
    trans_df.rename(columns=lambda x: translator.translate(x, src='ca', dest='en').text, inplace=True)

    trans_df.to_csv("translated.csv")

def translate_content(df):
    translations = {}

    for column in df.columns[4:]:
        # unique elements of the column
        unique_elements = df[column].unique().tolist()

        for element in unique_elements:
            # add translation to the dictionary
            translations[element] = translator.translate(element, src='ca', dest='en').text

            print(element, translations[element])
            time.sleep(0.2)

    with open("t.json", 'w') as outfile:
        json.dump(translations, outfile)

def replace_content(df):
    with open("t.json") as data:
        translations = json.load(data)

    df.replace(translations, inplace = True)
    df.to_csv("../../data/translated.csv")

if __name__ == '__main__':
    file_path = '../../data/2017_ebsib_bcn_enquesta_benestar_subjectiu_infancia_barcelona.csv'
    df = pd.read_csv(file_path, sep=';')

    # Did not run this
    # translate_columns(df)

    # Translate unique values and store them in a JSON file
    translate_content(df)

    # Traslate content and generate new csv file
    replace_content(df)

