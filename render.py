#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
from jinja2 import Environment, FileSystemLoader
import pandas as pd
from genXML_h import tewiki, writePage
from os import path

def getData(row):
    title = str(row['regional_name'])
    eng_name = str(row['name']).lower()
    print(eng_name)
    img_paths = []
    raga_img = 'wiki_ragas-master/raga_images_100' +  "/" + eng_name + '_kb2wiki.png'
    if path.exists(raga_img):
        img_paths.append(eng_name + '_kb2wiki.png')
    else:
        img_paths.append(eng_name + "_ar_kb2wiki.png")
        img_paths.append(eng_name + "_av_kb2wiki.png")

    row['alternates'] = row['alternates'].replace('[', '')
    row['alternates'] = row['alternates'].replace(']', '')
    row['alternates'] = row['alternates'].replace('"', '')
    row['alternates'] = row['alternates'].replace("'", '')
    row['alternates'] = row['alternates'].split(",")
    if row['alternates']:
        if len(row['alternates']) <= 2:
            row['alternates'] = None
    if row['janaka_melam']:
        row['janaka_melam'] = int(row['janaka_melam'])
    if row['melam_num']:
        row['melam_num'] = int(row['melam_num'])
    
    if row['chakra']:
        print("fobvieorbviot")
        if len(row['chakra']) < 2:
            row['chakra'] = None
    print(row['chakra'])
    print(len(row['chakra']))
    data = {
        'name': row['name'],
        'regional_name': row['regional_name'],
        'alternates': row['alternates'],
        'melam_num': str(row['melam_num']),
        'chakra': row['chakra'],
        'janya_of': row['janaka'],
        'janaka': row['janaka'],
        'janaka_melam': row['janaka_melam'],
        'melam_num': row['melam_num'],
        'category': row['category'],
        'aro': row['aro'],
        'ava': row['ava'],
        'aro_seq': row['aro_seq'],
        'ava_seq': row['ava_seq'],
        'is_vakra': row['is_vakra'],
        'img_paths': img_paths,
        'kritis': pd.eval(row['kritis']),
        'songs': pd.eval(row['songs']),
        'varnams': pd.eval(row['varnams']),
        'aro_swara_names': ', '.join(pd.eval(row['aro_swara_names']))[:-1],
        'ava_swara_names': ', '.join(pd.eval(row['ava_swara_names']))[2:],
        'one_swara_diff': pd.eval(row['one_swara_diff']),
        'source_num': int(row['source_num'])
	}
    # print(data)
    return data

def main():
    file_loader = FileSystemLoader('')
    env = Environment(loader=file_loader, newline_sequence='\n', keep_trailing_newline=True)
    template = env.get_template('ragas_new.j2')
    
    df = pd.read_csv(open('merged_100_final.csv', 'r'))
    df.fillna('', inplace=True)

    fobj = open('articles_ragas_4.xml', 'w')
    fobj.write(tewiki+'\n')
    
    count = 0
    for index, row in df.iterrows():
        title = str(row['regional_name'])
        text = template.render(getData(row))
        # print(text)
        writePage(title, text, fobj)
        print('\n', index, title)
        count+=1
    

    print(count)
    fobj.write('</mediawiki>')
    fobj.close()


if __name__ == '__main__':
	main()
