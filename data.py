import mido
import pandas as pd
import os
import numpy as np

def merge(time1, time2, hz1, hz2):
    i = 0
    j = 0
    ret = {"time": [],"hertz": []}
    while i < len(time1) and j < len(time2):
        if time2[j] < time1[i]:
            ret.time = time2[j]
            ret.hertz = hz2[j]
            j+=1
        else:
            ret.time = time1[i]
            ret.hertz = hz1[i]
            i+=1
    
    ret.time.extend(time1[i:])
    ret.time.extend(time2[j:])
    ret.hertz.extend(hz1[i:])
    ret.hertz.extend(hz2[j:])

    return ret



#tab: type jams
def tab2Sheet(tab):
    sheet = {}
    sheet.file_metadata = tab.file_metadata
    sheet.sandbox = tab.sandbox
    sheet.annotations = []
    ann = tab.annotations
    notes = merge(ann[0].data.time, ann[2].data.time, ann[0].data.value, ann[2].data.value)
    notes = merge(notes.time, ann[4].data.time, notes.hertz, ann[4].data.value)
    notes = merge(notes.time, ann[6].data.time, notes.hertz, ann[6].data.value)
    notes = merge(notes.time, ann[8].data.time, notes.hertz, ann[8].data.value)
    notes = merge(notes.time, ann[10].data.time, notes.hertz, ann[10].data.value)

    sheet.annotations.append({
        "annotation_metadata": tab.annotations[0].annotation_metadata,
        "namespace": "pitch_contour",
        "data": {
            "time": notes.time,
            "duration": [0] * len(notes.time),
            "value": notes.hertz
        },
        "sandbox": {},
        "time": ann[0].time,
        "duration": ann[0].duration
    })




    return sheet

def toTensor(jams):


class Sheet2TabDataset(Dataset):

    ## creates a dataset from given tabs and sheet music. If sheet music not provided,
    ## then creates the sheet music from the guitar tabs, and forms a new directory with the resulting sheet music in it
    ## new directory is formed in the root folder of this project
    ## number of tabs and sheets should be the same
    def __init__(self, tab_dir, tabs_file, sheet_dir=None, sheets_file=None):
        self.tab_dir = tab_dir 
        self.tab_labels = pd.read_csv(tabs_file)## TODO: labels for tabs (use pd most likely)
        self.sheet_dir = sheet_dir ## handle case where sheet dne
        self.sheet_labels = pd.read_csv(sheets_file) ## TODO: labels (?) for sheet

        if not self.sheet_dir:
            os.mkdir('sheets')
            project_root = os.path.dirname(os.path.dirname(__file__))
            output_path = os.path.join(project_root, 'sheets')
            self.sheet_labels = output_path
        if not self.sheet_labels:
            sheet_data = []
            for tab, row in self.tab_labels.iterrows():
                sheet_data.append(tab2Sheet(tab))
            self.sheet_labels = pd.DataFrame(sheet_data)

    def __len__(self):
        return len(self.tab_dir)
    
    def __getitem__(self, idx):
        tab_path = os.path.join(self.tab_dir, self.tab_labels.iloc([idx, 0]))
        tab_label = self.tab_labels.iloc[idx, 1]
        tab = #TODO

        sheet_path = os.path.join(self.sheet_dir.iloc, self.sheet_labels.iloc[idx, 1])
        sheet_label = self.tab_labels.iloc[idx, 1]

        sheet = #TODO

        sample = {"sheet music": sheet, "guitar tab": tab}
        return sample
#TODO: look into guitarset and lakh midi dataset
# https://guitarset.weebly.com/
# https://colinraffel.com/projects/lmd/